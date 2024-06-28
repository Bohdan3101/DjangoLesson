from app_blog import views
from django.urls import path

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
