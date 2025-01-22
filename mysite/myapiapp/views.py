from django.contrib.auth.models import Group
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import GroupSerializer
from rest_framework.generics import ListCreateAPIView
@api_view()
def hello_world_view(request: Request):
    return Response({"message": "Hello, World!"})

class GroupsListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # def get(self, request: Request):
    #     groups = Group.objects.all()
    #     serialized = GroupSerializer(groups, many=True)
    #     return Response({"groups": serialized.data})