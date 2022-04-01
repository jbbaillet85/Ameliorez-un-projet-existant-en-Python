from django.urls import path

from products.views import get_results_products, get_choice_substitution
from products.views import get_description_product, get_favorites, DeleteView

urlpatterns = [
    path("result_products", get_results_products, name="result_products"),
    path("choice_subtitution", get_choice_substitution, name="choice_subtitution"), # noqa
    path("description_product", get_description_product, name="description_product"), # noqa
    path("favorites", get_favorites, name="favorites"),
    path(
        "delete_favorite",
        DeleteView.as_view(template_name="delete_favorite"),
        name="delete_favorite",
    ),
]
