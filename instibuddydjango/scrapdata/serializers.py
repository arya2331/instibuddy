from rest_framework import serializers
from .models import Scrapcode

class ScrapcodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Scrapcode
        fields=('prof_Name','email','phone_number','expertise','department')
