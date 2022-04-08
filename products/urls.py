from django.urls import path
from products.models import Favorites
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from products.views import get_results_products, get_choice_substitution
from products.views import get_description_product, get_favorites

urlpatterns = [
    path("result_products", get_results_products, name="result_products"),
    path("choice_subtitution", get_choice_substitution, name="choice_subtitution"), # noqa
    path("description_product", get_description_product, name="description_product"), # noqa
    path("favorites", get_favorites, name="favorites"),
]
