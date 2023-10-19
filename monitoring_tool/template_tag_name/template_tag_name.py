# code for user group template from stack overflow and django documentation:
# https://stackoverflow.com/questions/34571880/how-to-check-in-template-if-user-belongs-to-a-group
# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/

from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()