from django.apps import AppConfig
from api.inference import models

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        models.load_all_models()
