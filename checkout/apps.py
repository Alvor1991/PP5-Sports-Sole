from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the checkout application, which handles
    order processing and payment integration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
