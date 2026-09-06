from rest_framework.permissions import BasePermission


class IsRecruiterOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        return (
            request.user.is_authenticated
            and request.user.profile.role == 'recruiter'
            and obj.recruiter == request.user
        )