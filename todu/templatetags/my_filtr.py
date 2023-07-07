from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# @register.filter
# def to_upper(v):
#     return v.upper()

@register.filter()
def leng(v):
    if len(v) > 7:
        s = v[:12]
        return f"{s}..."

# @register.filter
# def first_word(v, number):
#     s = ''
#     for i, q in enumerate(v, 1):
#         if q.isalpha() and i <= int(number):
#             s += q.upper()
#         else:
#             s += q
#     return s

# @register.filter
# def del_word(v):
#     s = f'<del>{v}</del>'
#     return mark_safe(s)
