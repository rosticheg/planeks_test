from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Schema
from .tasks import create_csv_file
import logging
import uuid



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


@login_required
def new_schema(request):
    return render(request, 'csv_gen/new_schema.html')


@login_required
def generate(request):
 
    if request.method == 'POST':
        data = request.POST

        f_dict = {}
        schema_name = ''
        for i in range(len(data)):
            for key in data:
                if key == 'schema_name':
                    schema_name = data[key]


    file_name = str(uuid.uuid4()) + ".csv"
    schema = Schema(title=schema_name, user=request.user, file_name=file_name)
    schema.save()

    logger.error('SCHEMA = ' + str(schema.id))

    context = {
        'schemes': Schema.objects.filter(user=request.user),
        'current_schema': schema.id
    }    

    data = {
        'current_schema': schema.id,
        'rows_number': 10,
        'titles': ['name', 'job', 'city']
    }
    create_csv_file.delay(data)

    return render(request, 'csv_gen/generate_csv.html', context)


def generate_csv(request):
    if request.method == 'POST':
        data = request.POST
        create_csv_file.delay(data)

    return render(request, 'csv_gen/generate.html')


def del_scheme(request, s_id):
    try:
        scheme = Schema.objects.get(id=s_id)
        scheme.delete()
        return HttpResponseRedirect("/dashboard")
    except Schema.DoesNotExist:
        return HttpResponseNotFound("<h2>Schema not found</h2>")


def check_scheme(request):
    context = {}
    if request.method == 'GET':
        s_id = request.GET.get("id")
        scheme = Schema.objects.get(id=s_id)
        context = {
            'scheme': scheme
        }    
    return render(request, 'csv_gen/check_scheme.html', context)


