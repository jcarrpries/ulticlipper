from .base import *
import os

ENV_NAME = os.environ.get("ENV_NAME")

if ENV_NAME == 'prod':
    from .prod import *
elif ENV_NAME == 'ci':
    from .ci import *
else:
    from .dev import *
