
from django import template
from django.template.loader import get_template

register = template.Library()


@register.filter
def coreui(element):
    """
    Django form render with coreui
    """

    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        add_input_classes(element)

        template = get_template('coreui/field.html')
        context = {'field': element}
    else:
        has_management = getattr(element, 'management_form', None)
        if not has_management:
            for field in element.visible_fields():
                add_input_classes(field)

            template = get_template('coreui/form.html')
            context = {'form': element}

    return template.render(context)


def add_input_classes(field):
    """
    依照不同的 field widget 加上相對應的 class attribute
    """

    classes = field.field.widget.attrs.get('class', '')

    classes = f'{classes} form-control'
    classes = f'{classes} is-invalid' if field.errors else classes

    field.field.widget.attrs['class'] = classes.strip()


@register.filter
def is_input_prepend_icon(field):
    return 'input_prepend_icon' in field.field.widget.attrs


@register.filter
def is_input_group(field):
    return is_input_prepend_icon(field)


@register.filter
def is_input_group_prepend(field):
    return is_input_prepend_icon(field)
