from user_activity.models import Members,Activity
from user_activity.serializers import MembersSerializer,ActivitySerializer
from rest_framework import viewsets


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.object.all()
    serializer_class = MembersSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.object.all()
    serializer_class = ActivitySerializer



