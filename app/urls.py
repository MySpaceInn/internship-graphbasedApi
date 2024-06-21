from django.urls import path, include
from rest_framework import routers
from app.views.record_views import RecordViewSet



# It is used for url configuration. it routes the url based on key of url_viewset. it transfer key in url in router
url_viewset= {
    'roster': RecordViewSet,
    'business': RecordViewSet,
    'staff': RecordViewSet,
    'allowance': RecordViewSet,
    'leave': RecordViewSet,
}


router=routers.DefaultRouter()
for url, viewset in url_viewset.items():
    router.register(url, viewset, basename=url)

urlpatterns = [
    path('',include(router.urls)),

]
