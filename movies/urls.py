from django.urls import path
from . import views

urlpatterns =[
    path('popular_movies/',views.popularMovies,name="popular_movies")
]