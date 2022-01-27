"""pureBeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from homepage.views import error_400_view_handler, error_403_view_handler, error_404_view_handler, error_500_view_handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homepage.urls")),
    path("homepage/", include("homepage.urls")),
    path("spaceUser/", include("spaceUser.urls")),
    path("products/", include("products.urls")),
]

handler404 = 'homepage.views.error_404_view_handler'
handler500 = 'homepage.views.error_500_view_handler'
handler403 = 'homepage.views.error_403_view_handler'
handler400 = 'homepage.views.error_400_view_handler'
