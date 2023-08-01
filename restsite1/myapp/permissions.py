from rest_framework import permissions


class HasGroupPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """

    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, "required_groups", {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])

        # Return True if the user has all the required groups or is staff.
        # return all([is_in_group(request.user, group_name) if group_name != "__all__" else True for group_name in
        #             required_groups]) or (request.user and request.user.is_staff)
        for i in request.user.groups.values_list('name', flat=True):
            if i in required_groups_mapping.get(request.method, []):
                return True
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return False


class HasURLPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        import re
        re.match()
        return '/admin/' in request.path
