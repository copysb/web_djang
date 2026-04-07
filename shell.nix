let
  pkgs = import (fetchTarball ("channel:nixpkgs-unstable")) { };

  python = pkgs.python312;

  lsprotocol_2023_0_1 = python.pkgs.buildPythonPackage rec {
    pname = "lsprotocol";
    version = "2023.0.1";

    pyproject = true;

    src = python.pkgs.fetchPypi {
      inherit pname version;
      sha256 = "cc5c15130d2403c18b734304339e51242d3018a05c4f7d0f198ad6e0cd21861d";
    };

    build-system = with python.pkgs; [
      flit-core
    ];

    dependencies = with python.pkgs; [
      attrs
      cattrs
    ];

    doCheck = false;
  };

  pygls_1_3_1 = python.pkgs.buildPythonPackage rec {
    pname = "pygls";
    version = "1.3.1";

    pyproject = true;

    src = python.pkgs.fetchPypi {
      inherit pname version;
      sha256 = "140edceefa0da0e9b3c533547c892a42a7d2fd9217ae848c330c53d266a55018";
    };

    build-system = with python.pkgs; [
      poetry-core
    ];

    dependencies = with python.pkgs; [
      lsprotocol_2023_0_1
      typeguard
      cattrs
      attrs
    ];

    doCheck = false;
  };

  django-template-lsp = python.pkgs.buildPythonPackage rec {
    pname = "django_template_lsp";
    version = "1.2.2";

    pyproject = true;

    src = python.pkgs.fetchPypi {
      inherit pname version;
      sha256 = "15dccbb33dc7ef4cb84e1673bf0583d5452bb29b8cb246563b8c5ba4e1415c83";
    };

    build-system = with python.pkgs; [
      setuptools
      wheel
    ];

    dependencies = with python.pkgs; [
      pygls_1_3_1
      jedi
      django
    ];

    doCheck = false;

    pythonImportsCheck = [
      "djlsp"
    ];
  };

  pythonEnv = python.withPackages (ps: [
    ps.django
    ps.django-stubs
    ps.mypy
    ps.jedi

    pygls_1_3_1
    lsprotocol_2023_0_1
    django-template-lsp
  ]);
in
pkgs.mkShell {
  strictDeps = true;

  nativeBuildInputs = [
    pythonEnv

    pkgs.pyright
    pkgs.ty
    pkgs.ruff
    pkgs.vscode
  ];

  buildInputs = [ ];

  shellHook = ''
      export DJANGO_SETTINGS_MODULE=django_labs.settings
      export PYTHONPATH=$PWD:$PYTHONPATH

      rm -rf .venv
      mkdir -p .venv/bin

      PYTHON_ENV="$(which python3)"

      cat > .venv/bin/python <<EOF
    #!/usr/bin/env sh
    export DJANGO_SETTINGS_MODULE=django_labs.settings
    export PYTHONPATH="$PWD:\$PYTHONPATH"
    exec "$PYTHON_ENV" "\$@"
    EOF

      chmod +x .venv/bin/python

      cat > .venv/bin/python3 <<EOF
    #!/usr/bin/env sh
    export DJANGO_SETTINGS_MODULE=django_labs.settings
    export PYTHONPATH="$PWD:\$PYTHONPATH"
    exec "$PYTHON_ENV" "\$@"
    EOF

      chmod +x .venv/bin/python3

      echo "Django Python shell ready"
      python --version
      django-admin --version

      echo "python3 = $(which python3)"
      echo ".venv python check:"
      ./.venv/bin/python3 -c "import django; print(django.get_version())"
  '';
}
