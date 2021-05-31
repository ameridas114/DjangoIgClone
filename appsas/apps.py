from django.apps import AppConfig


class AppsasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appsas'

    def ready(self):
        from .signals import create_profile, save_profile
# class LibraryConfig(AppConfig):
#     name = 'library'

