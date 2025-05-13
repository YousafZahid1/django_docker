from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class IonAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Hardcoded user data
        user_data = {
            'id': 1002854,
            'ion_username': '2027yzahid',
            'display_name': 'Yousaf Zahid',
            'full_name': 'Yousaf Zahid',
            'first_name': 'Yousaf',
            'last_name': 'Zahid',
            'email': '2027yzahid@tjhsst.edu',
        }
        
        # Get or create the user
        user, created = User.objects.get_or_create(
            username=user_data['ion_username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
            }
        )
        
        if created:
            user.set_unusable_password()
            user.save()
            
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None 