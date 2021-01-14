from django.urls import path, include

from .views import HomeView, AccCountView, DeathCountView, InjuryCountView


urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('acccount/<str:key>/<str:key2>', AccCountView.as_view(), name='acccount'),
    path('deathcount/<str:key>/<str:key2>', DeathCountView.as_view(), name='deathcount'),
    path('injurycount/<str:key>/<str:key2>', InjuryCountView.as_view(), name='injurycount'),
    
]