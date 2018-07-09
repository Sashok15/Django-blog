from django.contrib.auth.models import Permission, User, Group


def add_editor_perms_to_group():
    # one time use
    group = Group.objects.get(name='author')
    add_perm = Permission.objects.get('custom_can_add_article')
    change_perm = Permission.objects.get('custom_can_add_article')
    delete_perm = Permission.objects.get(name='custom_can_delete_article')
    group.permissions.add(add_perm, change_perm, delete_perm)
    return group


def grant_editor_status(user_object):
    group = Group.objects.get(name='author')
    user_object.groups.add(group)
    return User.objects.get(id=user_object.id)


def revoke_editor_status(user_object):
    group = Group.objects.get(name='author')
    user_object.groups.remove(group)
    return User.objects.get(id=user_object.id)