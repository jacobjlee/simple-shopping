from rest_framework import permissions


class IsUserOrAdmin(permissions.BasePermission):
    """유저나 관리자를 허용하는 커스텀 퍼미션입니다"""

    def has_object_permission(self, request, view, obj):
        """커스텀 퍼미션을 위한 베이스 퍼미션 오버라이딩 함수"""
        return obj.user == request.user or request.user.is_staff

