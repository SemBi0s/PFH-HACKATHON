from django.apps import AppConfig
from django.conf import settings
import os


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    PWD = os.path.dirname(os.path.realpath(__file__))
    TEMPLATE_DIRS = (

        os.path.join(PWD, 'templates'),
    )
