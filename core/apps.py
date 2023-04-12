from django.apps import AppConfig


class ManageUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    def ready(self):
        import signals