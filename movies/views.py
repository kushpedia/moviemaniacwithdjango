from django.shortcuts import render
import requests
API_KEY = 'ff6552b3b190a00faa2c2a1991ee9557'
# Create your views here.
def popularMovies(request):
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=ff6552b3b190a00faa2c2a1991ee9557'
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmZjY1NTJiM2IxOTBhMDBmYWEyYzJhMTk5MWVlOTU1NyIsInN1YiI6IjY1YzNiODk2M2ZlNzk3MDE4M2ZmMWRhNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ce7M-5R3xeAW8U23Nre1MGHLg7tRG3MpJbNh1aTtS24"
    }

    response = requests.get(url, headers=headers)
    data = response.text
    context ={
        'data' : data
    }
        

    return render(request, 'movies/popular_movies.html', context)