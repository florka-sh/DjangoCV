from django.apps import AppConfig


class CvAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cv_app'
    def ready(self):
    	import cv_app.signal
    	
