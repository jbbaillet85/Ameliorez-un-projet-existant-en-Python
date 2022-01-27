from django.urls import path

from homepage.views import homepage, mentions_legales, error_404_view_handler, error_500_view_handler, error_403_view_handler, error_400_view_handler

urlpatterns = [
    path('', homepage, name='homepage'),
    path('mentions_legales', mentions_legales, name='mentions_legales'),
]
