from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile """

    def has_object_permission(self, req, view, obj):
        """ Check user is trying to edit their own profile """
        if req.method in permissions.SAFE_METHODS: # SAFE_METHODS -> GET
            return True

        return obj.id == req.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """ Allow users to update their own status """

    def has_object_permission(self, req, view, obj):
        """ Check the user is trying to update their own status """
        if req.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == req.user.id