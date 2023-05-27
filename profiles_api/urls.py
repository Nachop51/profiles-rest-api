from django.urls import path, include # Import path from django.urls
from rest_framework.routers import DefaultRouter
from profiles_api import views # Import our views from profiles_api/views.py


router = DefaultRouter() # Create a router object
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset') # Register our viewset with the router
router.register('profile', views.UserProfileViewSet) # Register our viewset with the router

# Router is used to register our viewsets with the Django REST framework
# while the path function is used to register our APIView with the Django REST framework
# include is used to include the urls from the router in our urlpatterns

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()), # Add login url
    path('', include(router.urls)), # Include the router urls in our urlpatterns
]
