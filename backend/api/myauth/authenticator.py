from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class PhoneNumberBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None, device_id=None, **kwargs):
        try:
            user = User.objects.get(phone_number=phone_number, device_id=device_id)
            print(user)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
