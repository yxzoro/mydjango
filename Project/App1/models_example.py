#encoding=utf-8
from django.db import models            ## ****please refer: https://docs.djangoproject.com/en/1.9/topics/db/models/ **** ##

# Create your models here.

# 1--------define your [fields + methods] for Model------------- #

class Apple_manager(models.Manager):                ## Table level 's operation need to be defined in your own Manager here,
    def get_SuZhou_apples(self):                    ## Never rewrite Django's Manager, create your own Manager inherit of it 
        SuZhou_apples = self.filter(city="SuZhou")  ## here's self == original Manager, use any Method of Django's  Manager 
        return SuZhou_apples                        

    def get_two_apples(self):
        apples = self.all()[0:2]
        return apples
        

class Apple(models.Model):
    Name = models.CharField(max_length=50)         ## filed is colume in DB
    xing = models.CharField(max_length=50)         ## more Fields: docs.djangoproject.com/en/1.9/ref/models/fields/#model-field-types
    age = models.IntegerField()
    figure = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)

    apple_manager = Apple_manager()                  ## like objects = Manager(), register your own Manager here
    objects = models.Manager()                     ## must add this ,otherwise objects missing
    
    def get_full_name(self):                       ## define Row level's method here, method on a single Object/Row 
        full_name = self.xing + self.name          ## ****Remember: Never Rewrite Django's Method, Add Your Own Method****
        return full_name

    def is_young(self):
        return True if self.age <=28 else False


# 2--------(ForeignKey)ManyToOneField/OneToOneFiled + ManyToManyField------------- #

class Manufacturer(models.Model):
    pass

class Car(models.Model):                                                             
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)         ## ForeignKey==ManyToOneField
    # manufacturer = models.OneToOneField(Manufacturer, on_delete=models.CASCADE)    ## 1To1 relationship makes two tables as one table
    # manufacturer = models.ManyToManyField(Manufacturer, on_delete=models.CASCADE)  ## django create Intermediate Table for ManyToMany


# --------------------------------------------------------------------------------- #
## if u need your own Intermediate Table to store ManyToMany relationship(not recommend, use Django's enough) :

## because only way to create the relationship is to create instance of the Intermediate model, then add relationed Object youself,
## and it becomes a little complex now... 
## so i like using Django's ManyToManyField/IntermediateTable, only to store [ IDs ] for Relationed Tables

# class Person(models.Model):
#     name = models.CharField(max_length=128)

# class Group(models.Model):                                           
#     name = models.CharField(max_length=128)                          
#     members = models.ManyToManyField(Person, through='Membership')   ## use through='Membership' to create your Intermediate Table
                                                                       ## so can store more fields than only IDs in Intermediate Table 
# class Membership(models.Model):                                      
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)     
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()                                 
#     invite_reason = models.CharField(max_length=64)
# --------------------------------------------------------------------------------- #


# 3---------------------------Model Metadata--------------------------------------- #
# Give your model metadata by using an inner class Meta, like so:

# Model metadata is for [ anything that's not a field but about table ], such as ordering options (ordering), 
# table name (db_table), or human-readable singular and plural names (verbose_name and verbose_name_plural).

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:                               ## specify some action for your Model in Meta Class
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"


################################################################################################
# 4---------------------------Execute Raw SQL------------------------------------- #        
## if u want to write Raw SQL for complex Multi-Table operations(&& i like raw SQL so much!!) :
'''
it’s important to note that the Django database layer is merely an interface to your database. 
You can access your database via other tools, programming languages or database frameworks.
'''
from django.db import connection
cursor = connection.cursor()
cursor.execute("""
       SELECT DISTINCT first_name
       FROM people_person
       WHERE last_name = %s""", ['Lennon'])
result = cursor.fetchone()  # cursor.fetchall()
# result is querySet

Book.objects.raw('..SQL..')  ## raw() method to use raw SQL

Q()  ## Q() object, like an F object, encapsulates a SQL expression in a Python object. 
# In general, Q() objects make it possible to define and reuse conditions. This permits the 
# construction of complex database queries using | (OR) and & (AND) operators; in particular, 
# it is not otherwise possible to use OR in QuerySets.


# 5-----------------------------Model Python API---------------------------------- #    
# operate DB models in Python code:

from app.models import Publisher

# create
p = Publisher(name='xx')
p.save()
p = Publisher.objects.create(name='yy')

# delete
p.delete()
Publisher.objects.all().delete()

# update
p.update(name='zz')
Publisher.objects.all().update(country='USA')

# select
Publisher.objects.all()
Publisher.objects.filter(name='vv')
Publisher.objects.filter(name__contains="x")

# get object by ForeignKey 
b = Book.objects.get(name='The Django Book')
b.publisher  
b.publisher.name  # = 'Oreilly'
# get object by reverse ForeignKey                    ##  ****django create " modelname_set " as reverse foreignkey automaticaly****
p = Publisher.objects.get(name='Oreilly')
p.book_set.all()  # [<Book: The Django Book>, <Book: Dive Into Python>...]

# example:
# b = Book.objects.get(id=50)
# b.authors.all()
# [<Author: Adrian Holovaty>, <Author: Jacob Kaplan-Moss>]
# b.authors.filter(first_name='Adrian')
# [<Author: Adrian Holovaty>]
# b.authors.filter(first_name='Adam')
# []
# a = Author.objects.get(first_name='Adrian', last_name='Holovaty')
# a.book_set.all()
# [<Book: The Django Book>, <Book: Adrian's Other Book>]


# more methods

Publisher.objects.order_by("name")
Publisher.objects.filter(country="U.S.A.").order_by("-name")
Publisher.objects.order_by('name')[0:2]



# 6----------------------------change DB schema---------------------------------- #    
## Django only create new tables for you, not change DB schema/DB structure when you change Models definition...
## So you can only Change Your Database's Table Structure Youself By SQL when you want to change Models definition...


#--------------------------------------深入理解掌握Django Model--------------------------------------------#

# 1----------------------------阅读django官网文档note[先看完N之后再整理]---------------------------------- #    

# 2----------------------------使用Pycharm Debug Django源码去深入理解框架运行机制------------------------- #    

# 3----------------------------通过练习写SPA小程序[重点后台DB设计+开发]来熟悉Model层的使用-------------- #    




