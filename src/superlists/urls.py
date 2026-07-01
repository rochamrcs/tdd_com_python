from django.urls import include, path
from src.lists import views as list_views  

urlpatterns = [
    path("", list_views.home_page, name="home"),
    path("lists/", include("lists.urls")),  
]
