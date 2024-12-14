from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import UrlAlias


# Create your views here.
def redirect_to_url(request, alias):
    # Look up the alias in the database
    url_alias = get_object_or_404(UrlAlias, alias=alias)

    # Redirect to the original URL
    return redirect(url_alias.url)
