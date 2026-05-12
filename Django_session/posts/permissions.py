from rest_framework.permissions import BasePermission
from django.utils import timezone

class MycustomPermissionIstime(BasePermission):
	def has_permission(self, request, view):
		current = timezone.localtime().hour ## 현재 시간
		if current >= 22 or current < 7:
			return False
		return True
	
class MycustomPermissionIsOwner(BasePermission):
	
	def has_object_permission(self, request, view, obj):
		if request.method in ['GET','HEAD',"OPTIONS"]:
			return True
		return obj.writer == request.user
		