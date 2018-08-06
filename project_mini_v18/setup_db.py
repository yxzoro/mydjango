# setup db from cmd:
# manager.py  check/sqlall appName/syncdb/makemigrations/migrate


# setup db from here:
import os
from django.core.management import execute_from_command_line
import manage
# load config
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_mini_v18.settings")


# run commands here:
commands = ['check', 'makemigrations', 'migrate']  # run command in order

for command in commands:
    argv = [manage.__file__, command]
    execute_from_command_line(argv)













