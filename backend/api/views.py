from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, MailListSerializer, MessageSerializer, ClientSerializer
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MaillistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MailLists to be viewed or edited.
    """
    queryset = Maillist.objects.all()
    serializer_class = MailListSerializer
    permission_classes = [permissions.IsAuthenticated]  

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Messages to be viewed or edited.
    """
    queryset = Message.objects.all().filter(status=True).order_by('-id')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

