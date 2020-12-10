from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Schema
from django.views.generic import TemplateView, ListView
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


@login_required
def index(request):
    return render(request, "csv_gen/index.html")


@login_required
def dashboard(request):
    context = {
        'schemes': Schema.objects.filter(user=request.user)
    }    
    return render(request, 'csv_gen/dashboard.html', context)


