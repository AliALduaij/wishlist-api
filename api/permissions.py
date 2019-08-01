from rest_framework.permissions import BasePermission


class staff_owner(BasePermission):
	message = "staff and owner only can access"

	def has_object_permission(self, request, view, obj):
		if request.user==obj.added_by or request.user.is_staff:
			return True
		else:
			return False