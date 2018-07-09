def has_perm_or_is_author(user_object, permission, instance=None):
    if instance is not None:
        if user_object.id == instance.author.id:
            return True
        return user_object.has_perm(permission)


