from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Schema
from .tasks import create_csv_file
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


@login_required
def new_schema(request):
    return render(request, 'csv_gen/new_schema.html')


@login_required
def generate(request):
    create_csv_file.delay()
    if request.method == 'POST':
        data = request.POST

        f_dict = {}
        schema_name = ''
        for i in range(len(data)):
            for key in data:
                if key == 'schema_name':
                    schema_name = data[key]
                if key == "order"+str(i):
                    f_dict[i] = data[key]


        for key in f_dict:
            logger.error('DICT = ' + str(key) + "____" + f_dict[key])        

#        for key in data:
#            logger.error('DATA = ' + str(key))

#            if key == 'schema_name':
#                 schema = Schema(title=data[key], user=request.user)
#                 schema.save()
                

        logger.error('GENERATE = ' + str(data))

    return render(request, 'csv_gen/generate.html')



def del_scheme(request, s_id):
    try:
        scheme = Schema.objects.get(id=s_id)
        scheme.delete()
        return HttpResponseRedirect("/dashboard")
    except Schema.DoesNotExist:
        return HttpResponseNotFound("<h2>Schema not found</h2>")



