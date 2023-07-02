import sys
from .base import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
SECRET_KEY = env('DJANGO_SECRET_KEY', default='%g_70dtk@k2@fr6(Ajbnbji8-0-ceg4i1id*blkotm(0gwlk+')
