from django.test import Client
from django.urls import reverse, resolve

from spaceUser.views import password_reset, password_reset_done, password_reset_confirm, password_reset_succes

client = Client()
list_name_url = ['password_reset', 'password_reset_done', 'password_reset_confirm', 'password_reset_succes']

def test_spaceUser_reset_passord_url():
    """
        Testing if the 'identification' route maps to login
    """
    for name_url in list_name_url:
        url = reverse(name_url)
        assert resolve(url).view_name == name_url
        assert resolve(url).func, name_url
    
# def test_spaceUser_reset_password_view():
#     """
#     """
#     for name_url in list_name_url:
#         print(name_url)
#         response = client.get(reverse(name_url))
#         print(response)
#         assert response.url == f'/spaceUser/{name_url}'
#         print(response.url)
#         assert response.status_code == 200
#         print(response.status_code)