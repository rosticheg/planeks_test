from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "csv_gen/index.html")


@login_required
def dashboard(request):
    return render(request, 'csv_gen/dashboard.html', {'section': 'dashboard'})




