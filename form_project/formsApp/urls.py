from django.urls import path
from .views import HomePageView,ContactFormPageView

urlpatterns = [
    path('contactform/',ContactFormPageView, name='contactform'),
    path('', HomePageView, name='home'),
]
