
from django import template
from django.template.loader import get_template

register = template.Library()


@register.filter
def bootstrap(element):
    """
    Django form render with bootstrap
    """

    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        add_input_classes(element)
    else:
        for field in element.visible_fields():
            add_input_classes(field)

    template = get_template('bootstrap/form.html')
    context = {'form': element}

    return template.render(context)


def add_input_classes(field):
    """
    依照不同的 field widget 加上相對應的 class attribute
    """

    field_classes = field.field.widget.attrs.get('class', '')

    if 'form-control' not in field_classes:
        field_classes = f'{field_classes} form-control'

    field.field.widget.attrs['class'] = field_classes.strip()