from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.app_user.is_student


class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.app_user.is_instructor


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.app_user.is_admin
