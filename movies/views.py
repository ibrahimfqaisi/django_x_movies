from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Movie


class MoviesListView(ListView):
    template_name = "movies/movies-list.html"
    model = Movie


class MoviesDetailView(DetailView):
    template_name = "movies/movies-detail.html"
    model = Movie


class MoviesCreateView(CreateView):
    template_name = "movies/movies-create.html"
    model = Movie
    fields = ["title" ,"purchaser" ,"description" ]


class MoviesUpdateView(UpdateView):
    template_name = "movies/movies-update.html"
    model = Movie
    fields = ["title" ,"purchaser" ,"description" ]


class MoviesDeleteView(DeleteView):
    template_name = "movies/movies-delete.html"
    model = Movie
    success_url = reverse_lazy("movies_list")