"""
WSGI config for BooksCrawlerV2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from crawlerCroe.booksCom.mainRunner import BooksCom
from crawlerCroe.queuePool import QueuePoolService

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BooksCrawlerV2.settings")

application = get_wsgi_application()

queuePoolService = QueuePoolService()
queuePoolService.start()