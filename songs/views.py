from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from .models import Song
from .serializers.common import SongSerializer
from utils.decorators import handle_exceptions
from utils.permisssions import IsOwnerOrReadOnly

# Create your views here.



class SongListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @handle_exceptions
    def get(self, request):
        songs = Song.objects.all()
        serialized_songs = SongSerializer(songs, many=True)
        print(serialized_songs.data)
        return Response(serialized_songs.data)

    @handle_exceptions
    def post(self, request):
            request.data['owner'] = request.user.id
            song_to_create = SongSerializer(data=request.data)
            if song_to_create.is_valid():
               song_to_create.save()
               return Response(song_to_create.data, 201)
            
            print('Validation error:', song_to_create.errors)
            return Response(song_to_create.errors, 400)
        

        


class SongRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsOwnerOrReadOnly]


    @handle_exceptions
    def get(self, request, pk):
        song = Song.objects.get(pk=pk)
        serialized_song = SongSerializer(song)
        return Response(serialized_song.data)
        
       
    @handle_exceptions
    def put(self, request, pk):
        song_to_update = Song.objects.get(pk=pk)
        self.check_object_permissions(request, song_to_update)
        serialized_song = SongSerializer(song_to_update, data=request.data, partial=True)
        if serialized_song.is_valid():
            serialized_song.save()
            return Response(serialized_song.data)
        return Response(serialized_song.errors, 400)
           
        


    @handle_exceptions
    def delete(self, request, pk):
        song_to_delete = Song.objects.get(pk=pk)
        self.check_object_permissions(request, song_to_delete)
        song_to_delete.delete()
        return Response({ 'message': 'Song deleted'}, 204)
        

