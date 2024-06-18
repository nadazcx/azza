
from django.urls import path,include, re_path
from .views import signup, login, logout,getId

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('getId/', getId, name='getId'),
]
