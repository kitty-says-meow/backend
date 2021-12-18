import os

import django

django.setup()

from django.conf import settings
from django.core.management import call_command

print(f'Current path: {os.path.abspath(".")}')

print('Django settings:')
for attr in ['ALLOWED_HOSTS', 'BASE_DIR', 'STATICFILES_DIRS']:
    print('', attr, getattr(settings, attr, 'FAIL!'), sep='\t')

print('Collecting static files...')
call_command('collectstatic', interactive=False)

print('Applying migrations...')
call_command('migrate', interactive=False)

# Create django DATA_DIR
os.makedirs(getattr(settings, 'DATA_DIR'), exist_ok=True)

print('Setup completed!')
