# results/templatetags/gpa_extras.py

from django import template

register = template.Library()

@register.filter
def get_gpa(marks):
    if marks >= 80:
        return 4.00
    elif marks >= 75:
        return 3.75
    elif marks >= 70:
        return 3.50
    elif marks >= 65:
        return 3.25
    elif marks >= 60:
        return 3.00
    elif marks >= 55:
        return 2.75
    elif marks >= 50:
        return 2.50
    elif marks >= 45:
        return 2.25
    elif marks >= 40:
        return 2.00
    else:
        return 0.00
