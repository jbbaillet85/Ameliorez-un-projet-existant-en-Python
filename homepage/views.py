from django.shortcuts import render
from homepage.forms import SearchForm
from products.algoSubtitution import AlgoSubtitution
from django.utils.translation import gettext_lazy as _
# Create your views here.


def homepage(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        search_product = request.POST.get("search_product")
        print(f"keyword: {search_product}")
        if form.is_valid():
            products = AlgoSubtitution(search_product)
            print(f"products: {products}")
            context = {'search_product': search_product,
                       'products': products.result_search}
            return render(request, "result_products.html", context)
    else:
        form = SearchForm()
    return render(request, "homepage.html", {'form_search': form})


def mentions_legales(request):
    context = {'form_search': SearchForm()}
    return render(request, "mentions_legales.html", context)

VIEW_ERRORS = {
    404: {'title': _("404 - Page non trouvée"),
          'content': _("A 404 la page demandée est indisponible ou le serveur n'arrive pas à la trouver."), },
    500: {'title': _("500 Serveur Erreure"),
          'content': _("A 500  le serveur est temporairement indisponible ou en maintenance"), },
    403: {'title': _("Permission refusée"),
          'content': _("A 403 Vous n'êtes pas autoriser à accéder à cette page"), },
    400: {'title': _("Mauvaise requête"),
          'content': _("A 400 la requête a été mal formulée"), }, }

def error_view_handler(request, exception, status):
    return render(request, template_name='errors.html', status=status,
                  context={'error': exception, 'status': status,
                           'title': VIEW_ERRORS[status]['title'],
                           'content': VIEW_ERRORS[status]['content']})
    
def error_404_view_handler(request, exception=None):
    return error_view_handler(request, exception, 404)

def error_500_view_handler(request, exception=None):
    return error_view_handler(request, exception, 500)

def error_403_view_handler(request, exception=None):
    return error_view_handler(request, exception, 403)

def error_400_view_handler(request, exception=None):
    return error_view_handler(request, exception, 400)