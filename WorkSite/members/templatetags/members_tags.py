from django import template
import members.views as views
from members.models import Positions

register = template.Library()


@register.inclusion_tag('members/list_positions.html')
def show_position(pos_selected=0):
    position = Positions.objects.all()
    return {'position': position, 'pos_selected': pos_selected}