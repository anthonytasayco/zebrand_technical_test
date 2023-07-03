import logging
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from apps.users.models import User
from .models import Product

logger = logging.getLogger(__name__)


def send_email_admin_product_update(product_id: int, differences: dict):
    try:
        product_instance = Product.objects.get(id=product_id)
        recipient_list = User.objects.filter(Q(is_superuser=True) | Q(is_staff=True))
        message = f'Following product have been updated: {product_instance.name}  |  differences: {differences}'
    except Product.DoesNotExist:
        logger.error('Product does not exist: {}'.format(product_id))
    try:
        send_mail(
            subject='Notification for Product update information',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False
        )
    except Exception as e:
        print(e, 'EXCEPTION!')
        logger.error('Failed to send email: {}'.format(e))
