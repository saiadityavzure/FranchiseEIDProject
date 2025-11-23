from django.apps import AppConfig


class FimsCoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fims_core"

    def ready(self):
        from . import signals
