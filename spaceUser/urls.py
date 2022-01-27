from django.urls import path

from spaceUser.views import identification, register, spaceUser, logout_user, password_reset, password_reset_done, password_reset_confirm, password_reset_succes

urlpatterns = [
    path('register', register, name='register'),
    path('login', identification, name='login'),
    path('logout', logout_user, name='logout'),
    path('spaceUser', spaceUser, name='spaceUser'),
    path('password_reset', password_reset, name='password_reset'),
    path('password_reset_done', password_reset_done, name='password_reset_done'),
    path('password_reset_confirm', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_succes', password_reset_succes, name='password_reset_succes')
]
