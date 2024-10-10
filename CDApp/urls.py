from django.urls import path
from .views import HomePageView, AboutPageView, FooterPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'Home'),
    path('about/', AboutPageView.as_view(), name = 'About'),
    path('footer/', FooterPageView.as_view(), name = 'Footer')
]
