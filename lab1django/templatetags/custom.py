from django import template

register = template.Library()


@register.filter
def add_emoji(value,char):
    return value + char
@register.filter
def is_bestseller(value):
    rating = int(value)
    if rating > 5:
        return str(rating) + '😎'
    else:
        return str(rating)+'😔'
@register.simple_tag
def book_mood(rating):
    try:
        rating = float(rating)
    except (TypeError, ValueError):
        return "🤷 Рейтинг неизвестен"

    if rating >= 4.5:
        return "🔥 Эту книгу точно стоит прочитать"
    elif rating >= 3:
        return "👍 Нормальная книга"
    else:
        return "😴 Можно пропустить"