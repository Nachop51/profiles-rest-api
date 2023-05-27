from django.urls import path, include # Import path from django.urls
from rest_framework.routers import DefaultRouter
from profiles_api import views # Import our views from profiles_api/views.py


router = DefaultRouter() # Create a router object
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset') # Register our viewset with the router

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
