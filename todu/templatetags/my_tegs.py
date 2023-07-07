from django import template

register = template.Library()

from ..models import CategoriyModel


@register.simple_tag
def get_categori(order_valiu=None):
    if not order_valiu:
        return CategoriyModel.objects.all()
    else:
        return CategoriyModel.objects.all().order_by(order_valiu)


@register.inclusion_tag('layauts/cat_navbar.html')
def category():
    object = CategoriyModel.objects.all()

    return {
        'cats': object
    }
