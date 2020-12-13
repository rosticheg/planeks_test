import string
import csv
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task
from .models import Schema
from django.conf import settings
from mimesis import Generic


@shared_task
def create_csv_file(data):

    schema_id = data['current_schema']
    rows_number = int(data['rows_number'])
    separ = data['separ']

    schema = Schema.objects.get(id=schema_id)
    file_name = str(schema.file_name)
        
    titles = []
    titles = data['titles']
    types = []
    types = data['types']

    rows = []
    for i in range(rows_number):
        one_row = []
        for j in range(len(titles)):
            one_row.append(_generate_fake_news(types[j]))
        rows.append([separ.join(one_row)])

    with open(settings.MEDIA_URL + file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow([separ.join(titles)])
        for row in rows:
            writer.writerow(row)

    schema.status = True
    schema.save()


def _generate_fake_news(typ):
    g = Generic('en')

    fake = ''
    if typ == '1':
        fake = g.person.full_name() 
    elif typ == '2':
        fake = g.person.occupation() 
    elif typ == '3':
        fake = g.person.email() 
    elif typ == '4':
        fake = g.internet.home_page()
    elif typ == '5':
        fake = g.person.telephone()
    elif typ == '6':
        fake = g.business.company()
    elif typ == '7':
        fake = g.text.title()
    elif typ == '8':
        fake = g.numbers.integer_number()
    elif typ == '9':
        fake = g.address.address() 
    elif typ == '10':
        fake = g.datetime.datetime()
    else:
        fake = '----'

    return fake





