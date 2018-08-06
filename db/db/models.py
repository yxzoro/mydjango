from django.db import models

class Apple(models.Model):
    Name = models.CharField(max_length=50)
    xing = models.CharField(max_length=50)
    age = models.IntegerField()
    figure = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)

    class Meta:
        app_label = 'db'

    def get_full_name(self):
        full_name = self.xing + self.name
        return full_name

    def is_young(self):
        return True if self.age <=28 else False

