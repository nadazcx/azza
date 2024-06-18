# gestionMail/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EmailViewSet,getId

router = DefaultRouter()
router.register(r'emails', EmailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/accept/', EmailViewSet.as_view({'post': 'accept_email'}), name='email-accept'),
    path('<int:pk>/refuse/', EmailViewSet.as_view({'post': 'refuse_email'}), name='email-refuse'),
    path('getId/', getId, name='getId'),
]
