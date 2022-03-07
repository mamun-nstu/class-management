from core.utils import UserJWT
from django.contrib.auth.models import User


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        auth_cookie = request.COOKIES.get('auth_token', '')
        request.app_user = UserJWT.get_user(auth_cookie)
        if request.app_user.is_admin:
            request.user = request.auth = User.objects.get(
                username=request.app_user.user.username
            )
        return self.get_response(request)
