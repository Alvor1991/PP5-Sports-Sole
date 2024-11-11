from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration for the profiles app, which handles user profile
    management and related functionality.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
