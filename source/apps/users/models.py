from django.contrib.auth.models import AbstractUser
from apps.base.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser, TimeStampedModel):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
