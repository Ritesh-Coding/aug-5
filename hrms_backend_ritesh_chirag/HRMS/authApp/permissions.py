from rest_framework import permissions

#create by chirag

class IsAdminOrSelf(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    return request.user.is_staff or obj == request.user