from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile """

    def has_object_permission(self, req, view, obj):
        """ Check user is trying to edit their own profile """
        if req.method in permissions.SAFE_METHODS: # SAFE_METHODS -> GET
            return True

        return obj.id == req.user.id
