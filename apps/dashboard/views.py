from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_dashboard(request):
    return HttpResponse("Soy la Pagina del Dashboard")