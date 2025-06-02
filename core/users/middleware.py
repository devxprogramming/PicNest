from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()



class UpdateLastLoginMiddleware:
    """
    Middleware to update the last login time of 
    authenticated users on each request.
    """

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            if (not request.user.last_active or (timezone.now() - request.user.last_active).seconds > 300):
                request.user.update_last_active()
        return response