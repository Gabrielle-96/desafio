"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from erros import views
from django.contrib.auth.views import LoginView, LogoutView

handler404 = views.handler404;

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path(
    #     'accounts/login/',
    #     LoginView.as_view(
    #         template_name='core/auth.html'
    #     ),
    #     name='authenticate'
    # ),
    # path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('mensagensAleatorias/', include('mensagensAleatorias.urls')),
    path('mensagens/', include('mensagens.urls')),
]
