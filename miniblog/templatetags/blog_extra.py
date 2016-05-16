#-*- coding: utf-8 -*-

from django import template
from django.forms.extras import widgets


register = template.Library()

@register.filter
def lower(text):
    return text.lower()

@register.filter
def upper(text):
    return text.upper()

@register.filter
def splitUrl(url, index=-1):
    if url[-1:] == '/':
        url = url[:-1]
        
    url_list = url.split('/')
    try:
        return url_list[index]
    except IndexError:
        return url_list[-1:] if url_list[-1:] != [] else ''

@register.filter
def get_date(time):
    return str(time.day) + "." + str(time.month) + "." + str(time.year)

@register.filter
def content_split(content):
    return content[0:200] + " ..."
