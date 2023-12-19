from django import template

register = template.Library()


@register.filter
def get_enrolled(obj):
    return obj.iterrows()
