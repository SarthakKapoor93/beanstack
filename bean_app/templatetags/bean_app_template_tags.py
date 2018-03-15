from django import template

register = template.Library()


@register.simple_tag
def get_stars(rating, colour):
    s = ""
    for star in range(0, int(rating)):
        s += '<span class="glyphicon glyphicon-star" style="color: ' + colour + '; font-size: 20px;"></span>'
    return s
