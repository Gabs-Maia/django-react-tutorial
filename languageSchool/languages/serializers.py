from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('id', 'language_name', 'language_family', 'region_origin', 'sentences', 'words')
        