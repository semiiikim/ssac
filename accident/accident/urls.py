"""accident URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import HomeView, UserCreateView, UserCreateDoneView

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),  # accounts/login
    path('accounts/register/', UserCreateView.as_view(), name = "register"),  
    path('accounts/register/done/', UserCreateDoneView.as_view(), name = "register_done"),   

    path('accyear/', include('accyear.urls')),
    path('acctype/', include('acctype.urls')),
    path('accranking/', include('accranking.urls')),
    
]
