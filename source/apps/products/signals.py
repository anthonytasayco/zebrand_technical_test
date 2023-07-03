import logging
from django.dispatch import receiver
from django import dispatch
from django.db.models.signals import pre_save, post_save
from .models import Product
from .utils import update_product_view_counter

logger = logging.getLogger(__name__)

viewed_product = dispatch.Signal()


@receiver(viewed_product)
def increment_product_view_counter(sender, user, product_slug: str, **kwargs):
    if user.is_anonymous:
        view_count = update_product_view_counter(product_slug)
        logger.info('product: {}, times visited: {}'.format(product_slug, view_count))
