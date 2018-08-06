import os
from django.core.management import execute_from_command_line
import manage
# load config
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_mini_v18.settings")


# run server here:
command = 'runserver'
argv = [manage.__file__, command]
execute_from_command_line(argv)











