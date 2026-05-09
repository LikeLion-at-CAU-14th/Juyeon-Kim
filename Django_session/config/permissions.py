from rest_framework.permissions import IsAuthenticatedOrReadOnly
from datetime import datetime

class MycustomPermissionIstime(IsAuthenticatedOrReadOnly):
	def has_permission(self, request, view):
		current = datetime.now().hour ## 현재 시간
		if current >= 22 or current <= 7:
			return False
		return True
	
class MycustomPermissionIsOwner(IsAuthenticatedOrReadOnly):
	def has_object_permission(self, request, view, obj):
		if request.method in ['GET']:
			return True
		if obj.author == request.user:
			return True