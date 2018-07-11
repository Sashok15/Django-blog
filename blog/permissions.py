def has_perm_or_is_author(user_object, instance=None, permission=None):
    if user_object.is_superuser:
        return True
    elif instance is not None:
        if user_object.id == instance.author.id:
            return True
        return user_object.has_perm(permission)
