import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

@shared_task
def create_csv_file():
    logger.error('STARTTTTTT')
    pass



