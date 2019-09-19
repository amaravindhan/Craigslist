from django.urls import path

from . import views

app_name = "craigslist_app"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('search/', views.new_search, name = 'new_search')
]