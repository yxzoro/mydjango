# setup db:
# manager.py  check/sqlall appName/syncdb/makemigrations/migrate

# setup db from here:
import os
from django.core.management import execute_from_command_line
import manage
import time

# load config
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# run db commands here:
commands = ['check', 'makemigrations', 'migrate']
for command in commands:
    print('=> %s' % command)
    argv = [manage.__file__, command]
    execute_from_command_line(argv)
    print('\n')
    time.sleep(3)


