import logging
from django.dispatch import receiver
from django import dispatch
from django.db.models.signals import pre_save, post_save
from .models import Product
from .utils import update_product_view_counter, get_changed_product_fields
from .tasks import send_email_admin_product_update

logger = logging.getLogger(__name__)

viewed_product = dispatch.Signal()


@receiver(viewed_product)
def increment_product_view_counter(sender, user, product_slug: str, **kwargs):
    if user.is_anonymous:
        view_count = update_product_view_counter(product_slug)
        logger.info('product: {}, times visited: {}'.format(product_slug, view_count))


@receiver(pre_save, sender=Product)
def send_notification_product_update(sender, instance, **kwargs):
    if instance.id:
        new_instance = instance
        logger.info('send notification for product: {}'.format(new_instance.id))
        previous = Product.objects.get(id=new_instance.id)
        differences = get_changed_product_fields(previous, new_instance)
        send_email_admin_product_update(instance.id, differences)
