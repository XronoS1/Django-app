from django.apps import AppConfig


class MarketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'market'
    default = False

    def ready(self):
        import market.signals
