from django.apps import AppConfig


class ChryblkConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chryblk"

    def ready(self):
        import chryblk.signals