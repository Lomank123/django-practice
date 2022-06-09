import logging

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from accounts.models import UserProfile
from accounts.views import AccountsSignupView


user_model = get_user_model()
logger = logging.getLogger('main.middleware.custom')

new_sign_up = Signal()  # Custom signal


@receiver(post_save, sender=user_model)
def create_profile(sender, instance, created, **kwargs):
    """
    Simple receiver which will create and attach UserProfile instance after CustomUser has been created.
    """

    if created:
        UserProfile.objects.create(user=instance)
        logger.info("UserProfile created!")


@receiver(post_save, sender=user_model)
def update_profile(sender, instance, created, **kwargs):
    """
    Receiver to update UserProfile when CustomUser isntance has been updated.
    """

    if not created:
        instance.profile.save()
        logger.info("UserProfile updated!")


@receiver(new_sign_up, sender=AccountsSignupView)
def notify_new_sign_up(sender, new_user, **kwargs):
    logger.warning(f"New sign up! It is {new_user.username}")
