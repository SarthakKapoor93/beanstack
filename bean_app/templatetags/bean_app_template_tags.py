from django import template

register = template.Library()


@register.simple_tag
def get_stars(rating):
    s = ""
    for star in range(0, int(rating)):
        s += '<span class="glyphicon glyphicon-star-empty" style="color: white;"></span>'
    return s