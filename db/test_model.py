import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db.settings")


from db.models  import Apple

print Apple.objects.filter()



