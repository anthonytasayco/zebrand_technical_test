import logging
from django.db.models import Q
from django.conf import settings
from django.core.mail import EmailMessage
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
        e_mail = u'{0}<{1}>'.format(
            "Notifications", settings.DEFAULT_FROM_EMAIL)
        msg = EmailMessage(
            'Notification for Product update information',
            message,
            e_mail,
            recipient_list,
        )
        msg.content_subtype = "html"
        msg.send()
    except Exception as e:
        logger.error('Failed to send email: {}'.format(e))
