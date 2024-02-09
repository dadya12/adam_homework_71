from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from webapp.models import Publication
from api_v1.serializers import PublicationModelSerializer
from django.views.decorators.csrf import ensure_csrf_cookie
from api_v1.permission import IsAuthorPermission


@ensure_csrf_cookie
def get_token(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])

class PubViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationModelSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return [IsAuthorPermission()]

class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()
        return Response({'status': 'ok'})
