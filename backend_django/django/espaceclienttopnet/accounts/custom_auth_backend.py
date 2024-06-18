from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, cin=None,email=None, password=None,name=None,**kwargs):
        user_model = get_user_model()
        
        try:
            # Try to find a user matching the email or username
            user = user_model.objects.get(Q(email=email) | Q(cin=cin)|Q(name=name))
            
            # Check the password
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            # Run the default password hasher to prevent timing attacks
            user_model().set_password(password)