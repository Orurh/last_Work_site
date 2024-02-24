from django import template
import members.views as views

register = template.Library()

@register.simple_tag()
def get_categories():
    return views.categors

@register.inclusion_tag('members/list_positions.html')
def show_position(pos_selected=0):
    position = views.categors
    return {'position': position, 'pos_selected': pos_selected}