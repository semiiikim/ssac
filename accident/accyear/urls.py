from django.contrib import admin
from django.urls import path, include

from .views import HomeView, TotalView, SearchView,YearDetailView

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('total/', TotalView.as_view(), name='total'),
    path('search/<str:key>',SearchView.as_view(), name='search'),
    path('detail/<str:key>',YearDetailView.as_view(), name='detail'),


] 