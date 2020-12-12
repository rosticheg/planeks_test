import string
import csv
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task
from .models import Schema
from django.conf import settings

from random import choice
from string import ascii_uppercase
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


@shared_task
def create_csv_file(data):
    logger.error('STARTTTTTT')

    logger.error('DATA' + str(data))
    schema_id = data['current_schema']
    rows_number = int(data['rows_number'])

    schema = Schema.objects.get(id=schema_id)
    file_name = str(schema.file_name)
        
    titles = []
    titles = data['titles']

    rows = []
    for i in range(rows_number):
        one_row = []
        for j in range(len(titles)):
            one_row.append(''.join(choice(ascii_uppercase) for k in range(12)))
        rows.append(one_row)



    with open(settings.MEDIA_URL + file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(titles)
        for row in rows:
            writer.writerow(row)

    schema.status = True
    schema.save()

    logger.error('STOPPPPPPP')



