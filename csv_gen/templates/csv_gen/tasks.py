import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task
import logging
import csv
import uuid


# Get an instance of a logger
logger = logging.getLogger(__name__)

@shared_task
def create_csv_file(data):
    logger.error('STARTTTTTT')
    filename = str(uuid.uuid4()) + ".csv"
    

    logger.error('POST' + str(data))
    data = [
        ['Name', 'Height'],
        ['Keys', '176cm'],
        ['HongPing', '160cm'],
        ['WenChao', '176cm']
    ]
    with open(r'csv_gen\static\users_files\%s' % filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        for row in data:
            writer.writerow(row)

    logger.error('STOPPPPPPP')



