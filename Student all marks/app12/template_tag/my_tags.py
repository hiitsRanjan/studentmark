from django.template import Library

register = Library()

@register.simple_tag()

def doTotal(marks):
    return sum(marks)