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

handler404 = error_404_view_handler
handler500 = error_500_view_handler
handler403 = error_403_view_handler
handler400 = error_400_view_handler
