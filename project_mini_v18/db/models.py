from django.db import models

# --------------------db commands to create database tables:------------------ #
# manager.py  check/sqlall appName/syncdb/makemigrations/migrate

# ----------------define your [fields + methods] for Model-------------------- #

# if you need to operate db in other file:
# from db.models import Apple


class Apple_manager(models.Manager):                
    def get_SuZhou_apples(self):                    
        SuZhou_apples = self.filter(city="SuZhou")  
        return SuZhou_apples                        

    def get_two_apples(self):
        apples = self.all()[0:2]
        return apples
        

class Apple(models.Model):
    Name = models.CharField(max_length=50)        
    xing = models.CharField(max_length=50)        
    age = models.IntegerField()
    figure = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)

    apple_manager = Apple_manager()               
    objects = models.Manager()                    
    
    def get_full_name(self):                       
        full_name = self.xing + self.name          
        return full_name

    def is_young(self):
        return True if self.age <=28 else False