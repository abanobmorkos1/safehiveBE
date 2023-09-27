from reporting.models import SafehiveDetails
from rest_framework import serializers

class Hiveserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SafehiveDetails
        fields = ['address', 'incident' ,'emergency']