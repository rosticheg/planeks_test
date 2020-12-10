import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def create_csv_file(optional_param):
    pass