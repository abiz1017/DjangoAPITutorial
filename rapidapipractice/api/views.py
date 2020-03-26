from django.shortcuts import render
from rest_framework import viewsets
From .serializers import UserSerializer, GroupSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view or edit users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint to edit or view groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

