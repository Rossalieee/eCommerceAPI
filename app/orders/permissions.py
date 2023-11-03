from rest_framework import permissions
from users.enums import UserRole


class HasCustomerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role == UserRole.CUSTOMER


class HasSellerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role == UserRole.SELLER


class IsSellerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        return user.is_authenticated and user.role == UserRole.SELLER

