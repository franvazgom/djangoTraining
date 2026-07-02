from django import template
from pages.models import Page

register = template.Library()

# Restrarlo en la librería de templates


@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
