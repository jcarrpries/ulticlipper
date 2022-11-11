from .base import *
import os

environment_name = os.environ.get("ENV_NAME")

if environment_name == 'prod':
    from .prod import *
elif environment_name == 'ci':
    from .ci import *
else:
    from .dev import *
