from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from webapp.models import Publication
from api_v1.serializers import PublicationModelSerializer
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])

class PubViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationModelSerializer
