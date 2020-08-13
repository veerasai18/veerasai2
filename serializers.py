from rest_framework_json_api import serializers
from user_activity.models import Members, Activity


class MembersSerializer(serializer.HyperlinkedModelSerializer):
    class Meta:
        model = Members
        fields = ('id', 'real_name', 'tz')


class ActivitySerializer(serializer.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('start_name', 'end_name')