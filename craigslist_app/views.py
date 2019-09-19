import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
# Create your views here.

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    return render(request, 'craigslist_app/new_search.html')