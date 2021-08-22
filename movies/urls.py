from django.urls import path

from movies import views

urlpatterns = [
    path("movies/", views.MovieListAPIView.as_view()),
    path("movies/<int:movie_id>/", views.MovieItemAPIView.as_view()),
]
