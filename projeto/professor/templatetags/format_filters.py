from django import template

register = template.Library()

@register.filter
def formata_telefone(value):
    """
    Formata telefone no padrão (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
    """
    if not value:
        return ""
    
    value = ''.join(filter(str.isdigit, str(value)))  # remove não dígitos

    if len(value) == 11:
        return f"({value[:2]}) {value[2:7]}-{value[7:]}"
    elif len(value) == 10:
        return f"({value[:2]}) {value[2:6]}-{value[6:]}"
    else:
        return value  # retorna sem formatação se diferente
