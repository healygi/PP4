"""
ASGI config for healyhealth project.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healyhealth.settings')

application = get_asgi_application()
