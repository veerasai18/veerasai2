from django.urls import include,path
from rest_framework import routers
from user_activity import views

router = routers.DefaultRouter()
router.register(r'members', views.MembersViewSet)
router.register(r'activity', views.ActivityViewSetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]