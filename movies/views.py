from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Actor, Movie
from movies.serializers import ActorSerializer, MovieSerializer


class MovieListAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieItemAPIView(APIView):
    def get_object(self, movie_id):
        try:
            return Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, movie_id):
        movie = self.get_object(movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, movie_id):
        movie = self.get_object(movie_id)
        serializer = MovieSerializer(movie, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, movie_id):
        movie = self.get_object(movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorListAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorItemAPIView(APIView):
    def get_object(self, actor_id):
        try:
            return Actor.objects.get(pk=actor_id)
        except Actor.DoesNotExist:
            raise Http404

    def get(self, request, actor_id):
        actor = self.get_object(actor_id)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def put(self, request, actor_id):
        actor = self.get_object(actor_id)
        serializer = ActorSerializer(actor, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, actor_id):
        actor = self.get_object(actor_id)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
