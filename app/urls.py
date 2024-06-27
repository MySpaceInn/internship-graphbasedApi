from django.urls import path, include
from rest_framework import routers
from .views.record_views import RecordViewSet
from .views.register_view import RegisterView

# Define the URL configuration for viewsets
url_viewset = {
    'roster': RecordViewSet,
    'business': RecordViewSet,
    'staff': RecordViewSet,
    'allowance': RecordViewSet,
    'leave': RecordViewSet,
}

router = routers.DefaultRouter()
for url, viewset in url_viewset.items():
    router.register(url, viewset, basename=url)

# Define urlpatterns including both viewsets and APIViews
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
