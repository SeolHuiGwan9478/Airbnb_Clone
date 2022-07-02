from os import stat
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer, RoomSerializer
# Create your views here

class RoomsView(APIView):
    # GET
    def get(self,request):
        paginator = PageNumberPagination()
        paginator.page_size = 20
        rooms = Room.objects.all()
        results = paginator.paginate_queryset(rooms, request)
        serializer = RoomSerializer(results, many=True).data
        return paginator.get_paginated_response(data=serializer)
    #POST
    def post(self,request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            room_serializer = RoomSerializer(room)
            return Response(data=room_serializer, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RoomView(APIView):
    def get_room(self,pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            return None

    def get(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            serializer = RoomSerializer(room).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            serializer = RoomSerializer(instance=room, data=request.data, partial=True)
            if serializer.is_valid():
                room = serializer.save()
                return Response(room, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request, pk):
        room = self.get_room(pk)
        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            room.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def room_search(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    rooms = Room.objects.filter()
    results = paginator.paginate_queryset(rooms)
    serializers = RoomSerializer(results, many=True).data
    return paginator.get_paginated_response(results)