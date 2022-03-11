
from django.urls import reverse, resolve

from spaceUser.views import register, identification, spaceUser, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


class TestSpaceUserUrls:
    def test_register_url(self):
        """
        Testing if the 'register' route maps to register
        """

        url = reverse('register')
        assert resolve(url).view_name == 'register'
        assert resolve(url).func, register

    def test_identification_url(self):
        """
        Testing if the 'identification' route maps to login
        """

        url = reverse('login')
        assert resolve(url).view_name == 'login'
        assert resolve(url).func, identification

    def test_spaceUser_url(self):
        """
        Testing if the 'spaceUser' route maps to spaceUser
        """

        url = reverse('spaceUser')
        assert resolve(url).view_name == 'spaceUser'
        assert resolve(url).func, spaceUser

    def test_logout_url(self):
        """
        Testing if the 'spaceUser' route maps to spaceUser
        """

        url = reverse('logout')
        assert resolve(url).view_name == 'logout'
        assert resolve(url).func, logout

    def test_reset_passord_url(self):
        """
        Testing if the 'spaceUser' route maps to reset password
        """

        url = reverse('password_reset')
        assert resolve(url).view_name == 'password_reset'
        assert resolve(url).func, PasswordResetView

        url = reverse('password_reset_done')
        assert resolve(url).view_name == 'password_reset_done'
        assert resolve(url).func, PasswordResetDoneView

        url = reverse('password_reset_complete')
        assert resolve(url).view_name == 'password_reset_complete'
        assert resolve(url).func, PasswordResetCompleteView