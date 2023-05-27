from django.urls import path # Import path from django.urls
from profiles_api import views # Import our views from profiles_api/views.py


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
