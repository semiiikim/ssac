from django.urls import path, include

from .views import HomeView, AccRankingCountView, AccRankingDeathView, AccRankingInjuryView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('acccount/<str:key1>/<str:key2>', AccRankingCountView.as_view(), name='ranking-count'),
    path('deathcount/<str:key1>/<str:key2>', AccRankingDeathView.as_view(), name='ranking-death'),
    path('injurycount/<str:key1>/<str:key2>', AccRankingInjuryView.as_view(), name='ranking-injury'),
    
]