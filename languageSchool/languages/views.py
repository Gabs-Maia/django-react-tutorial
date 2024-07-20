from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LanguageSerializer
from .models import Language


class LanguageView(viewsets.ModelViewSet):
   serializer_class = LanguageSerializer
   queryset = Language.objects.all()


class WordsViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_queryset(self):
        return Language.objects.values_list('words', flat=True)