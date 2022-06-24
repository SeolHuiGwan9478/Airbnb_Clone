from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import ReadUserSerializer, RelatedUserSerializer
from .models import User
# Create your views here.
class MeView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response(RelatedUserSerializer(request.user).data)
    
    def put(self, request):
        pass

@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(ReadUserSerializer(user).data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
