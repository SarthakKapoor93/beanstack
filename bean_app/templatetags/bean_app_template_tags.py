from django import template
from beanstack.settings import MEDIA_ROOT
from pathlib import Path

register = template.Library()


@register.simple_tag
def get_stars(rating, colour):
    s = ""
    for star in range(0, int(rating)):
        s += '<span class="glyphicon glyphicon-star" style="color: ' + colour + '; font-size: 20px;"></span>'
    return s


@register.filter(name='image_exists')
def image_exists(image_name):
    return Path(MEDIA_ROOT + '/' + image_name + '.jpeg').exists()

