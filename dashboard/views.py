from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')