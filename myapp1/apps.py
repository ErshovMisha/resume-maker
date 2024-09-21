from django.apps import AppConfig


class Myapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp1'
    def ready(self):
        import myapp1.signals  # Імпорт сигналів