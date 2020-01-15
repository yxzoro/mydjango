
# ----------------------更多Django详情,请参考 = https://docs.djangoproject.com/en/1.9/ref/models------------------------- # 
# ----------------------更多Django详情,请参考 = http://djangobook.py3k.cn/2.0/chapter03/--------------------------------- # 

# -----------------------------------其实CRUD中，复杂的查询是最重点------------------------------------------------------ #
# 如果2张表之间需要用到了join，则这2张表应该有一定的外键关系？否则不会需要用到毫无关系的2张表的join?
# ----------------------****其实仅使用一个【ForeignKey】足够处理所有关系(1-1/1-m/m-m)了！-------------------------------- #

# ----------------------------------------------------------------------------------------------------------------------- #
**Field options：
	null =  True 数据库字段值是否可null值
	blank = True 数据库字段值是否可空
	db_column = 'field name' 可指定字段名字
	db_index = True 字段加入索引
	db_tablespace 
	default = 'default value' 默认值
	primary_key = False 指定主键
	unique = True 值唯一
	validators = [] 指定字段值的验证函数 A list of validators to run for this field.


# ----------------------------------------------------------------------------------------------------------------------- #
**Field types：
	AutoField 主键使用的自增长唯一的数字类型
	BigIntegerField  -9223372036854775808 to 9223372036854775807
	IntegerField   -2147483648 to 2147483647
	SmallIntegerField  -32768 to 32767
	PositiveIntegerField   0 to 2147483647 
	PositiveSmallIntegerField  0 to 32767
	FloatField 	
	BinaryField 二进制类型
	BooleanField  True/False
	NullBooleanField   True/False/null
	CharField  必须指定max_length长度
	DateField   auto_now=False  Automatically set the field to now every time the object is saved.
				auto_now_add=False  Automatically set the field to now when the object is first created. 
	DateTimeField  (auto_now=False, auto_now_add=False) 同上
	DurationField  A field for storing periods of time - modeled in Python by timedelta. 
	EmailField  A CharField that checks that the value is a valid email address. It uses EmailValidator to validate the input.
	FileField  (upload_to=None, max_length=100, **options)  A file-upload field.  文件上传时使用
	FilePathField (path=None, match=None, recursive=False, max_length=100, **options) A CharField whose choices are limited to the filenames in a certain directory on the filesystem
	ImageField (upload_to=None, height_field=None, width_field=None, max_length=100, **options)
	GenericIPAddressField (protocol='both', unpack_ipv4=False, **options) An IPv4 or IPv6 address
	TextField   A large text field
	TimeField (auto_now=False, auto_now_add=False, **options) A time, represented in Python by a datetime.time instance
	URLField  
	UUIDField 

*****Relationship fields：
	ForeignKey (othermodel, on_delete, **options)  A many-to-one relationship. othermodel+on_delete必须指定
				on_delete=models.CASCADE/models.SET_NULL/models.DO_NOTHING
	ManyToManyField (othermodel, **options)  A many-to-many relationship.
	OneToOneField (othermodel, on_delete, parent_link=False, **options)  A one-to-one relationship.


# ----------------------------------------------------------------------------------------------------------------------- #
****Field API reference(讲解Field类的属性和函数，重点==>>django内部机制会依次调用的函数讲解)
	>>>参阅 = https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-api-reference
    >>>自定义 Field类 = https://docs.djangoproject.com/en/1.9/howto/custom-model-fields/                #[TODO]

****Lookup API reference(讲解Lookup类的属性和函数，重点==>>django内部机制会依次调用的函数讲解)
	# the class Lookup is for building the WHERE clause of a database query => because complex SELECT is import.
	>>>参阅 = https://docs.djangoproject.com/en/1.9/ref/models/lookups/
    >>>自定义 Lookup类 = https://docs.djangoproject.com/en/1.9/howto/custom-lookups/


# ----------------------------------------------------------------------------------------------------------------------- #
*****Meta options：
	db_table = 'music_album'  The name of the database table to use for the model:
	default_related_name    The default is <model_name>_set.
	managed = True   If False, no database table creation or deletion operations will be performed for this model.you manage it youself.
	ordering = ['pub_date']/ordering = ['-pub_date']  正反排序
	unique_together = ("driver", "restaurant")  Sets of field names that, taken together, must be unique
		# 注意： unique_together = (("driver", "restaurant"), )  ！=  unique_together = ("driver", "restaurant")
	index_together = ["pub_date", "deadline"]  Sets of field names that, taken together, are indexed


# ----------------------------------------------------------------------------------------------------------------------- #
******# API that lets you create, retrieve, update and delete [CRUD] Model objects in Python ==>>
1 Creating objects:
>>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()  # To create and save an object in a single step, use the [ create() ] method.
To save changes[ UPDATE ] to an object that’s already in the database, u can also use save():
>>> b5.name = 'New name'
>>> b5.save()

2 Saving ForeignKey and ManyToManyField fields:
>>> from blog.models import Entry
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog
>>> entry.save()

3 use the add() method on the field to add a record to a ManyToManyField relation:
>>> from blog.models import Author
>>> joe = Author.objects.create(name="Joe")
>>> entry.authors.add(joe)
>>> entry.authors.add(john, paul, george, ringo)

# ----------------------------------------------------------------------------------------------------------------------- #
Retrieving objects:
# You get a QuerySet by using your model’s Manager. Each model has at least one Manager, 
# and it’s called objects by default. Access it directly via the model class, not instance, see below:
>>> Blog.objects
<django.db.models.manager.Manager object at ...>
>>> b = Blog(name='Foo', tagline='Bar')
>>> b.objects
Traceback:
AttributeError: "Manager isn't accessible via Blog instances."

Retrieving all objects:
	all_entries = Entry.objects.all()

Retrieving specific objects with filters:
	Entry.objects.filter(pub_date__year=2006)
	Entry.objects.filter(headline__startswith='What').exclude(pub_date__gte=datetime.date.today()).filter(pub_date__gte=datetime(2005, 1, 30))

## just querying a QuerySet doesn’t really hit database ,Django will actually run the query in DB until the QuerySet is [evaluated].

Retrieving a single object with get():
	one_entry = Entry.objects.get(pk=1)

Limiting QuerySets:
	Entry.objects.all()[5:10]
	Entry.objects.all()[:10:2]  # 0 to 10, step = 2
	Entry.objects.order_by('headline')[0]

# ----------------------------------------------------------------------------------------------------------------------- #
Field lookups: (field__lookuptype=value)
	Entry.objects.filter(pub_date__lte='2006-01-01')
	Entry.objects.get(headline__exact="Cat bites dog")
	Blog.objects.get(name__iexact="beatles blog")  # A case-insensitive match.
	Entry.objects.get(headline__contains='Lennon')
	Entry.objects.get(headline__startswith='Lennon')

*****Lookups that span relationships:
# To span a relationship, just use the field name of related fields across models, separated by double underscores, 
>>> Entry.objects.filter(blog__name='Beatles Blog')
# It works backwards, too. To refer to a “reverse” relationship, just use the lowercase name of the model.
>>> Blog.objects.filter(entry__headline__contains='Lennon')
>>> Blog.objects.filter(entry__authors__name__isnull=True)  # a little different from below:
>>> Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)

**Spanning multi-valued relationships:
# finding blogs that have an entry which has [both] "Lennon" in the headline and was published in 2008. 
>>> Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)  # 2个条件是 并且 的关系
# find blogs that have an entry with "Lennon" in the headline [as well as] an entry that was published in 2008.
>>> Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)  # 2个条件是  的关系 ??  #[TODO]


# construct filters that compare the value of the model field beyond just a constant but also Fields in self/related Model.
*****Filters can reference fields on the self/related model ==>> use F():
# Instances of F() act as a reference to a model field within a query.
>>> from django.db.models import F
>>> Entry.objects.filter(comments__gt=F('pingbacks'))  # comments & pingbacks in the same Model
>>> Entry.objects.filter(comments__gt=F('pingbacks') * 2)
>>> Entry.objects.filter(rating__lt=F('comments') + F('pingbacks'))
>>> Entry.objects.filter(authors__name=F('blog__name'))  # blog__name in related Model
>>> from datetime import timedelta
>>> Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))


**The pk lookup shortcut:
>>> Blog.objects.get(id__exact=14) 
>>> Blog.objects.get(id=14) 
>>> Blog.objects.get(pk=14) 
>>> Blog.objects.filter(pk__in=[1,4,7])  # Get blogs entries with id 1, 4 and 7
>>> Blog.objects.filter(pk__gt=14)  # Get all blog entries with id > 14
>>> Entry.objects.filter(blog__id__exact=3) 
>>> Entry.objects.filter(blog__id=3)        
>>> Entry.objects.filter(blog__pk=3)        


**Escaping percent signs and underscores in LIKE statements:
#(in SQL, the '%' signifies a multiple-character wildcard and the '__' signifies a single-character wildcard.) 	
>>> Entry.objects.filter(headline__contains='%')
>>> Entry.objects.filter(headline__contains='__')
# Both percentage signs and underscores are handled for you automatically in Django.

# ----------------------------------------------------------------------------------------------------------------------- #
**Caching and QuerySets: (django use a cache mechanism for QuerySet)  [不是理解地非常清楚]                        #[TODO]
# QuerySet contains a cache to minimize database access. Understanding it will help you to write the most efficient code.
# Django hit database until QuerySet is evaluated[求值], Django saves the QuerySet’s cache then.
>>>参阅：https://docs.djangoproject.com/en/1.9/ref/models/querysets/#queryset-api-reference


# ----------------------------------------------------------------------------------------------------------------------- #
*****Complex lookups with Q objects ==>> Q():
# If you need to execute more complex queries in filter().etc(for example, queries with OR/NOT statements), you can use Q objects.	
Q(question__startswith='Who') & Q(question__startswith='What')  # AND
Q(question__startswith='Who') | Q(question__startswith='What')  # OR 
Q(question__startswith='Who') | ~Q(pub_date__year=2005)         # OR + NOT

>>> from django.db.models import Q
>>> Poll.objects.filter(Q(name='test') | ~Q(age=24))
>>> Poll.objects.get(Q(question__startswith='Who'), Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)))

# if a Q object is provided mixed with keyword argument in AND, Q() must precede the definition of any keyword arguments.  
>>> Poll.objects.filter(Q(name='test') | ~Q(age=24), question__startswith='Who')  # 顺序不能写反, Q()在前

# ----------------------------------------------------------------------------------------------------------------------- #
**Deleting objects：
# the delete() methods of individual object instances will [not necessarily be called] during the process.
>>> e.delete()    # instance delete, not recommended, but better use delete() in class delete.
(1, {'weblog.Entry': 1})
>>> Entry.objects.filter(pub_date__year=2005).delete()    # better use class delete
(5, {'webapp.Entry': 5})
# When Django deletes an object, by default it emulates the behavior of the SQL constraint [ ON DELETE CASCADE ],
# – in other words, any objects which had Foreignkeys[1To1/1ToN] pointing at the object to be deleted will be deleted along with it. 

# delete() is the only method that of but not inside Manager ,it's inside QuerySet for you to safely delete all,
# If you do want to delete all the objects, then you have to explicitly request a complete query set:
>>> Entry.objects.all().delete()  # Entry.objects.delete() is invalid


**Copying model instances:
# there is no built-in method for copying model instances, but you can just set pk to None to copy it.
>>> blog = Blog(name='My blog', tagline='Blogging is easy')
>>> blog.save() # blog.pk == 1
# u can only set PrimaryKey first time you save it, u will create a new object if u change PrimaryKey of an existed object.
>>> blog.pk = None  
>>> blog.save() # blog.pk == 2


*****Updating multiple objects at once:  # update() != save() when update(), things like 'auto_now' in DateField only triggered in save()
>>> Entry.objects.filter(pub_date__year=2007).update(headline='Everything is the same')
# To update ForeignKey fields, set the new value to be the new model instance you want to point to.
>>> b = Blog.objects.get(pk=1)
>>> Entry.objects.filter(name='Emily').update(blog=b)

# The only restriction on the QuerySet being updated is that it can only access one database table ==>> the model’s main table
# You can filter based on related fields, but you can only update columns in the [model’s main table]. Example:
>>> b = Blog.objects.get(pk=1)
>>> Entry.objects.select_related().filter(blog=b).update(headline='Everything is the same')

# update can also use F expressions to update one field based on the value of another field
>>> Entry.objects.all().update(pingbacks=F('pingbacks') + 1)
# u can’t introduce joins when you use F() objects in an update – u can only reference [fields local to the model] being updated.
# THIS WILL RAISE A FieldError:
>>> Entry.objects.update(headline=F('blog__name'))  # ×××× it's ERROR


# ----------------------------------------------------------------------------------------------------------------------- #
*****Related objects ==>> Django has convenient API to access the [related object(s)]
*****One-to-many relationships:
# Forward: 
>>> e = Entry.objects.get(id=2)
>>> e.blog  # Returns the related Blog object.	
>>> e.blog = some_blog_instance
>>> e.save()
# If a ForeignKey field has null=True set (it allows NULL values), you can assign None to remove the relation. Example:
>>> e = Entry.objects.get(id=2)
>>> e.blog = None
>>> e.save()  # ="UPDATE blog_entry SET blog_id = NULL ;"

# Backward: ====>> 'Modelname_set'
>>> b = Blog.objects.get(id=1)
>>> b.entry_set.all()  # Returns all Entry objects related to Blog.
# b.entry_set is a RelatedManager who is subclass of the default Manager that returns QuerySets.
>>> b.entry_set(manager='MyManager').all()  
>>> b.entry_set(manager='MyManager').my_own_manager_method()
# can also use your own Manager where u defines in Models alongsides 'objects = models.Manager()', +'MyManager = OwnManager()'
>>> b.entry_set.filter(headline__contains='Lennon')
>>> b.entry_set.count()

****Additional methods to handle related objects in [ForeignKey]:
# the ForeignKey's RelatedManager has additional methods used to handle the set of related objects. 
>>> add(obj1, obj2, ...)
>>> b = Blog.objects.get(id=1)
>>> b.entry_set = [e1, e2]  # e1 and e2 can be full Entry instances, or integer primary key values.
# Adds the specified model objects to the related object set.
>>> create(**kwargs)
# Creates a new object, saves it and puts it in the related object set. Returns the newly created object.
>>> remove(obj1, obj2, ...)
# Removes the specified model objects from the related object set.
>>> clear()
# Removes all objects from the related object set.
>>> set(objs)
# Replace the set of related objects.

# The API works just as the same as one-to-many relationship above.
*****Many-to-many relationships:
>>> e = Entry.objects.get(id=3)
>>> e.authors.all()  # Returns all Author objects for this Entry.
>>> e.authors.count()
>>> e.authors.filter(name__contains='John')
>>> a = Author.objects.get(id=5)

# Backward: ====>> 'Modelname_set'
>>> a.entry_set.all()  # Returns all Entry objects for this Author.

# The API works just as the same as one-to-many relationship above.
****One-to-one relationships:
ed = EntryDetail.objects.get(id=2)
ed.entry  # Returns the related Entry object.
e = Entry.objects.get(id=2)

# Backward: ====>> just use'Modelname', not 'Modelname_set' in One-to-one relationships. Because it's really not a "QuerySet" here.
e.entrydetail  # it's just a related EntryDetail object here.


# ----------------------------------------------------------------------------------------------------------------------- #
Manager API reference: 
# Manager返回的就是一个QuerySet类, 详细介绍 Manager 的一些好用的函数,
filter(**kwargs)
# Returns a new QuerySet containing objects that match the given lookup parameters.
exclude(**kwargs)
# Returns a new QuerySet containing objects that do not match the given lookup parameters.

annotate(*args, **kwargs)  
# Annotates each object in the QuerySet with the provided list of query expressions.
# 参阅 = https://docs.djangoproject.com/en/1.9/ref/models/querysets/#annotate
>>> from django.db.models import Count
>>> q = Blog.objects.annotate(Count('entry'))
# The name of the first blog
>>> q[0].name
'Blogasaurus'
# The number of entries on the first blog
>>> q[0].entry__count
42
>>> q = Blog.objects.annotate(number_of_entries=Count('entry'))
# The number of entries on the first blog, using the name provided
>>> q[0].number_of_entries
42

order_by(*fields)  # order_by() may has some problem with distinct() ?
# By default, results returned by a QuerySet are ordered by the ordering tuple given by the ordering option in the model’s Meta. 
# You can override this on a per-QuerySet basis by using the order_by method.
>>> Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
>>> Entry.objects.order_by('blog__name', 'headline')
>>> Entry.objects.order_by('blog') 
>>> Entry.objects.order_by('blog_id')  # dirrenent from above
>>> Entry.objects.order_by(Coalesce('summary', 'headline').desc())
>>> Entry.objects.order_by(Lower('headline').desc())
>>> Entry.objects.order_by('headline').order_by('pub_date')  # order_by() call will clear any previous ordering => pub_date not headline.

reverse()
# Use the reverse() method to reverse the order in which a queryset’s elements are returned. 
# reverse() should only be called on a QuerySet which has a defined ordering, otherwise no effect.

distinct(*fields)  # distinct() may has some problem with order_by() ?
# Returns a new QuerySet that uses SELECT DISTINCT in its SQL query. This eliminates duplicate rows from the query results.
>>> Author.objects.distinct()
# ****Only On PostgreSQL only, you can pass positional arguments (*fields) to specify fields for DISTINCT.
# >>> Entry.objects.order_by('pub_date').distinct('pub_date')
# >>> Entry.objects.order_by('blog').distinct('blog')
# >>> Entry.objects.order_by('author', 'pub_date').distinct('author', 'pub_date')
# >>> Entry.objects.order_by('blog__name', 'mod_date').distinct('blog__name', 'mod_date')
# >>> Entry.objects.order_by('author', 'pub_date').distinct('author')

values(*fields)  #  a model object ====>> a dic
# Returns a QuerySet that returns key-value dictionaries, rather than model instances, when used as an iterable.
# -------------------------------------------------------------------------------------------------- #
#  In Essence, a Model object == a key-value dictionary. they just store DATA in "key=>value" format.
# -------------------------------------------------------------------------------------------------- #
>>> Blog.objects.filter(name__startswith='Beatles').values()
[{'id': 1, 'name': 'Beatles Blog'}, ...]
>>> Entry.objects.values()
[{'blog_id': 1, 'headline': 'First Entry', ...}, ...]
>>> Entry.objects.values('blog','name')
[{'blog': 1, 'name':'Emily'}, ...]
>>> Entry.objects.values('blog_id')
[{'blog_id': 1}, ...]
# You can also refer to fields on related models with reverse relations through OneToOneField/ForeignKey/ManyToManyField attributes
>>> Blog.objects.values('name', 'entry__headline')  # ==> there may be many related rows for one row in ForeignKey/ManyToManyField
[{'name': 'My blog', 'entry__headline': 'An entry'},{'name': 'My blog', 'entry__headline': 'Another entry'}, ...]

values_list(*fields, flat=False)  
# This is similar to values() except that instead of returning dictionaries, it returns tuples when iterated over. 
>>> Entry.objects.values_list('id', 'headline')
[(1, 'First entry'), ...]
>>> Entry.objects.values_list('id').order_by('id')
[(1,), (2,), (3,), ...]
>>> Entry.objects.values_list('id', flat=True).order_by('id')  # pass flat=True/False only when only one Field specified
[1, 2, 3, ...]
>>> Author.objects.values_list('name', 'entry__headline')  # querying across a ManyToManyField:
[('Noam Chomsky', 'Impressions of Gaza'),           # ==> there may be many related rows for one row in ForeignKey/ManyToManyField
 ('George Orwell', 'Why Socialists in Fun'),
 ('George Orwell', 'In Defence of English'),
 ('Don Quixote', None)]  # this Author has no entry
>>> Entry.objects.values_list('authors')
[('Noam Chomsky',), ('George Orwell',), (None,)]  # this Entry has no author

all()
# Returns a copy of the current QuerySet (or QuerySet subclass). 

select_related(*fields)
# Returns a QuerySet that will "follow" foreign-key relationships, Pre-select-cache related-object data when it executes its query.
>>> e = Entry.objects.select_related('blog').get(id=5)  # Hits the database.
>>> b = e.blog  # Don't hit the database again, because e.blog has been prepopulated in the previous query.

prefetch_related(*lookups)   [参阅 = https://docs.djangoproject.com/en/1.9/ref/models/querysets/#prefetch-related]  #[TODO]
# This has a similar purpose to select_related(), in that both are designed to stop the deluge of database queries 
# that is caused by accessing related objects, but the strategy is quite different.
>>> Pizza.objects.all().prefetch_related('toppings')
>>> Restaurant.objects.prefetch_related('pizzas__toppings')
>>> Restaurant.objects.select_related('best_pizza').prefetch_related('best_pizza__toppings')

extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)           #[TODO]
# a hook for injecting specific clauses into the SQL generated by a QuerySet. express a complex WHERE clause.

defer(*fields)
# tell Django not to retrieve some Fields from the database, passing the names of the noneed fields.
>>> Entry.objects.defer("headline", "body")

only(*fields)
# opposite of defer(). only retrieve some Fields from the database.
>>> Person.objects.only("name")

using(alias)
# This method is for controlling which database the QuerySet will be evaluated against.
>>> Entry.objects.all()  # queries the database with the 'default' DB.
>>> Entry.objects.using('backup')  # queries the database with the 'backup' DB

select_for_update(nowait=False)  # if nowait=True, This will make the transaction non-blocking.  ## depend on different Databases
# Returns a queryset that will lock rows until the end of the transaction, generating a SELECT ... FOR UPDATE SQL statement on supported databases.

*****raw(raw_query, params=None, translations=None)
# Takes a raw SQL, executes it, returns a django.db.models.query.RawQuerySet just like normal QuerySet providing object instances.
# --------------------------------------------- #
#  better to use raw SQL if ORM become complex!!
# --------------------------------------------- #

get(**kwargs)
# Returns the one object matching the given lookup parameters
>>> Entry.objects.get(id='foo')  # will raise MultipleObjectsReturned/DoesNotExist Exception if >1 or =0

create(**kwargs)
# A convenient method for creating an object and saving it all in one step. Thus:
>>> p = Person.objects.create(first_name="Bruce", last_name="Springsteen")  # same as below:
>>> p = Person(first_name="Bruce", last_name="Springsteen")
>>> p.save(force_insert=True)

get_or_create(defaults=None, **kwargs)
# looking up an object with the given kwargs(may be empty if your model has defaults for all fields),creating one if necessary.
>>> Person.objects.get_or_create(first_name='John',last_name='Lennon',defaults={'birthday': date(1940, 10, 9)})
# it's just encapsulate some code below, same as :
>>> try:
>>>     obj = Person.objects.get(first_name='John', last_name='Lennon')
>>> except Person.DoesNotExist:
>>>     obj = Person(first_name='John', last_name='Lennon', birthday=date(1940, 10, 9))
>>>     obj.save()

update_or_create(defaults=None, **kwargs)
# updating an object with the given kwargs, creating a new one if necessary. defaults is a field-value dictionary to update the object.
>>> Person.objects.update_or_create(first_name='John', last_name='Lennon', defaults=updated_values)
# it's just encapsulate some code below, same as :
>>> try:
>>>     obj = Person.objects.get(first_name='John', last_name='Lennon')
>>>     for key, value in updated_values.iteritems():
>>>         setattr(obj, key, value)
>>>     obj.save()
>>> except Person.DoesNotExist:
>>>     updated_values.update({'first_name': 'John', 'last_name': 'Lennon'})
>>>     obj = Person(**updated_values)
>>>     obj.save()

bulk_create(objs, batch_size=None)
# This method inserts the provided list of objects into the database in one step.
>>> Entry.objects.bulk_create([
...     Entry(headline="Django 1.0 Released"),
...     Entry(headline="Django 1.1 Announced"),
...     Entry(headline="Breaking: Django is awesome")
... ])
# But The model’s save() method will not be called in this method !! 	
# It does not work with many-to-many relationships.

count()
# Returns number of objects in the database matching the QuerySet. The count() method never raises exceptions.
>>> Entry.objects.count()  # Returns the total number of entries in the database.
>>> Entry.objects.filter(headline__contains='Lennon').count()  # Returns the number of entries whose headline contains 'Lennon'

in_bulk(id_list)
# Takes a list of primary-key id and returns a dictionary mapping each id to an instance of the object with the given ID.
>>> Blog.objects.in_bulk([1])
{1: <Blog: Beatles Blog>}
>>> Blog.objects.in_bulk([1, 2])
{1: <Blog: Beatles Blog>, 2: <Blog: Cheddar Talk>}
>>> Blog.objects.in_bulk([])
{}

iterator()
# Evaluates the QuerySet (by performing the query) and returns an iterator(see PEP 234) over the results. 

latest(field_name=None)
# Returns the latest object in the table, by date, using the field_name provided as the date field.
>>> Entry.objects.latest('pub_date')

earliest(field_name=None)
# Works otherwise like latest() except the direction is changed.

first()
# Returns the first object matched by the queryset, or None if there is no matching object. 
>>> p = Article.objects.order_by('title', 'pub_date').first()
# it's just encapsulate some code below, same as :
>>> try:
>>>     p = Article.objects.order_by('title', 'pub_date')[0]
>>> except IndexError:
>>>     p = None

last()
# Works like first(), but returns the last object in the queryset.

aggregate(*args, **kwargs)  # SQL的聚合函数功能 = https://docs.djangoproject.com/en/1.9/topics/db/aggregation/
# Returns a dictionary of aggregate values (averages, sums, etc.) calculated over the QuerySet. 
# Each argument to aggregate() specifies a value that will be included in the dictionary that is returned.
>>> from django.db.models import Count
>>> q = Blog.objects.aggregate(Count('entry'))
{'entry__count': 16}
>>> q = Blog.objects.aggregate(number_of_entries=Count('entry'))
{'number_of_entries': 16}

exists()
# Returns True if the QuerySet contains any results, and False if not. 

as_manager()  # classmethod
# Class method that returns an instance of Manager with a copy of the QuerySet’s methods. 

update(**kwargs) 
# Performs an SQL update query for the specified fields, and returns the number of rows matched
>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False)
>>> Entry.objects.filter(pub_date__year=2010).update(comments_on=False, headline='This is old')
# ****the only restriction on the QuerySet that is updated is that it can only update columns in the model’s main table, 
# not on related models. You can’t do this, for example:
>>> Entry.objects.update(blog__name='foo') # ×××× it Won't work!
# the most efficient way is to call update() if u just update a record and don’t do anything with the model object
>>> Entry.objects.filter(id=10).update(comments_on=False)  # update() don't not call save(), Note that!!
# better than :
>>> e = Entry.objects.get(id=10)
>>> e.comments_on = False
>>> e.save()

delete()
# Performs an SQL delete query on all rows in the QuerySet and returns the number of objects deleted and 
# a dictionary with the number of deletions per object type.
>>> b = Blog.objects.get(pk=1)
>>> Entry.objects.filter(blog=b).delete()  # Delete all the entries belonging to this Blog.
(4, {'weblog.Entry': 2, 'weblog.Entry_authors': 2})
>>> blogs = Blog.objects.all()
>>> blogs.delete()  # This will delete all Blogs and all of their Entry objects.
(5, {'weblog.Blog': 1, 'weblog.Entry': 2, 'weblog.Entry_authors': 2})
# ------------------------------------------------------------------------------------------------- #
#  You can't call delete()/update()/filter() on a QuerySet that has had a slice taken. Note that!!
# ------------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------------------------------- #
*****Field lookups
# Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods.
exact
# Exact match. If the value provided for comparison is None, it will be interpreted as an SQL NULL (see isnull for more details).
>>> Entry.objects.get(id__exact=14)
>>> Entry.objects.get(id__exact=None)
iexact
# Case-insensitive exact match.
>>> Blog.objects.get(name__iexact='beatles blog')
>>> Blog.objects.get(name__iexact=None)
contains
# Case-sensitive containment test.
>>> Entry.objects.get(headline__contains='Lennon')
icontains
# Case-insensitive containment test.
>>> Entry.objects.get(headline__icontains='Lennon')
in
# In a given list.
>>> Entry.objects.filter(id__in=[1, 3, 4])
gt
# Greater than.
>>> Entry.objects.filter(id__gt=4)
gte
# Greater than or equal to.
lt
# Less than.
lte
# Less than or equal to.
startswith
# Case-sensitive starts-with.
>>> Entry.objects.filter(headline__startswith='Will')
istartswith
# Case-insensitive starts-with.
>>> Entry.objects.filter(headline__istartswith='will')
endswith
# Case-sensitive ends-with.
>>> Entry.objects.filter(headline__endswith='cats')
iendswith
# Case-insensitive ends-with.
>>> Entry.objects.filter(headline__iendswith='will')
range
# Range test (inclusive). between and. u can use range anywhere you can use BETWEEN in SQL — for dates, numbers and even characters.
>>> import datetime
>>> start_date = datetime.date(2005, 1, 1)
>>> end_date = datetime.date(2005, 3, 31)
>>> Entry.objects.filter(pub_date__range=(start_date, end_date))
isnull
# Takes either True or False, which correspond to SQL queries of IS NULL and IS NOT NULL, respectively.
>>> Entry.objects.filter(pub_date__isnull=True)
search
# A boolean full-text search, taking advantage of full-text indexing. This is like contains but is significantly faster due to full-text indexing.
>>> Entry.objects.filter(headline__search="+Django -jazz Python")
# SQL equivalent:
# SELECT ... WHERE MATCH(tablename, headline) AGAINST (+Django -jazz Python IN BOOLEAN MODE);
# Note this is only available in [MySQL] and requires direct manipulation of the database to add the full-text index. 

# ------------------------u can use regex in lookup [重点掌握]-------------------------------------- #
******regex  # u can just use Python's re module for regex ! 
# Case-sensitive regular expression match.
# The regular expression syntax is that of the database backend in use. In the case of SQLite, 
# which has no built in regular expression support, this feature is provided by a (Python) user-defined REGEXP function, 
# and the regular expression syntax is therefore that of Python’s [re module].
>>> Entry.objects.get(title__regex=r'^(An?|The) +')
# SQL equivalents:
# SELECT ... WHERE title REGEXP BINARY '^(An?|The) +'; -- MySQL
# SELECT ... WHERE REGEXP_LIKE(title, '^(An?|The) +', 'c'); -- Oracle
# SELECT ... WHERE title ~ '^(An?|The) +'; -- PostgreSQL
# SELECT ... WHERE title REGEXP '^(An?|The) +'; -- SQLite
# Using raw strings (e.g., r'foo' instead of 'foo') for passing in the regular expression syntax is recommended.
*****iregex
# Case-insensitive regular expression match.
>>> Entry.objects.get(title__iregex=r'^(an?|the) +')
# SQL equivalents:
# SELECT ... WHERE title REGEXP '^(an?|the) +'; -- MySQL
# SELECT ... WHERE REGEXP_LIKE(title, '^(an?|the) +', 'i'); -- Oracle
# SELECT ... WHERE title ~* '^(an?|the) +'; -- PostgreSQL
# SELECT ... WHERE title REGEXP '(?i)^(an?|the) +'; -- SQLite
# --------------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------------------------------- #
**Aggregation functions [参阅聚合函数 = https://docs.djangoproject.com/en/1.9/topics/db/aggregation/]
# All aggregates have the following 3 parameters in common:
# expression  # A string that references a field on the model, or a query expression.
# output_field  # An optional argument that represents the model field of the return value
# **extra  # Keyword arguments that can provide extra context for the SQL generated by the aggregate.
Avg
# class Avg(expression, output_field=FloatField(), **extra)
# Returns the mean value of the given expression, which must be numeric unless you specify a different output_field.
# Default alias: <field>__avg
# Return type: float (or the type of whatever output_field is specified)
Count
# class Count(expression, distinct=False, **extra)
# Returns the number of objects that are related through the provided expression.
# Default alias: <field>__count
# Return type: int
Max
# class Max(expression, output_field=None, **extra)
# Returns the maximum value of the given expression.
# Default alias: <field>__max
# Return type: same as input field, or output_field if supplied
Min
# class Min(expression, output_field=None, **extra)
# Returns the minimum value of the given expression.
# Default alias: <field>__min
# Return type: same as input field, or output_field if supplied
StdDev
# class StdDev(expression, sample=False, **extra)
# Returns the standard deviation of the data in the provided expression.
# Default alias: <field>__stddev
# Return type: float
Sum
# class Sum(expression, output_field=None, **extra)
# Computes the sum of all values of the given expression.
# Default alias: <field>__sum
# Return type: same as input field, or output_field if supplied
Variance
# class Variance(expression, sample=False, **extra)
# Returns the variance of the data in the provided expression.
# Default alias: <field>__variance
# Return type: float


# ----------------------------------------------------------------------------------------------------------------------- #
******Instance methods： [讲解Model类的CRUD函数，重点==>>django内部机制会依次调用的函数讲解]
>>>参考 = https://docs.djangoproject.com/en/1.9/ref/models/instances/
>>> Model.from_db()  # the process that load fields values from db to python model object 
>>> Model.refresh_from_db()
>>> Model.full_clean()
>>> Model.clean()
>>> Model.validate_unique()  # use some 'if' to validate if fileds values satisfy the requirements or raise ValidationException


# ----------------------------------------------------------------------------------------------------------------------- #
**What happens when save()? When you save an object, Django performs the following steps:
# 1.Emit a pre-save signal. The signal django.db.models.signals.pre_save is sent, allowing any functions listening for that signal to take some customized action.
# 2.Pre-process the data. Each field on the object is asked to perform any automated data modification that the field may need to perform.
# Most fields do no pre-processing — the field data is kept as-is. Pre-processing is only used on fields that have special behavior. For example, if your model 
# has a DateField with auto_now=True, the pre-save phase will alter the data in the object to ensure that the date field contains the current date stamp. 
# 3.Prepare the data for the database. Each field is asked to provide its current value in a data type that can be written to the database.
# Most fields require no data preparation. Simple data types, such as integers and strings, are ‘ready to write’ as a Python object. However, more complex data types often require some modification.
# For example, DateField fields use a Python datetime object to store data. Databases don’t store datetime objects, so the field value must be converted into an ISO-compliant date string for insertion into the database.
# 4.Insert the data into the database. The pre-processed, prepared data is then composed into an SQL statement for insertion into the database.
# 5.Emit a post-save signal. The signal django.db.models.signals.post_save is sent, allowing any functions listening for that signal to take some customized action.

**How Model.save() knows to UPDATE or INSERT:
# save()
>>> b3 = Blog(id=3, name='Not Cheddar', tagline='Anything but cheese.')
>>> b3.save()  # create a new blog with id=3 if not a blog(id=3) exists!
# update()
>>> b4 = Blog(id=3, name='lichard reaman', tagline='Anything but coco.')
>>> b4.save()  # update the previous blog with id=3 because bolg(id=3) already exists!
# so, it's apparent that Model.save() use id(primarykey) if or not exists to create or update!

# ----------------------------------------------------------------------------------------------------------------------- #
****Accessing related objects
>>>参考= https://docs.djangoproject.com/en/1.9/ref/models/relations/

# ----------------------------------------------------------------------------------------------------------------------- #
****Pickling objects：[序列化成字符串来存储对象(对象里的DATA其实就是k-v属性值 == {})]
# When you pickle a model, its current state is pickled. When you unpickle it, it’ll contain the model instance 
# at the moment it was pickled, rather than the data that’s currently in the database.

# ----------------------------------------------------------------------------------------------------------------------- #
*****Calling custom QuerySet methods from custom Manager:
>>>class PersonQuerySet(models.QuerySet):  # your custom QuerySet
>>>    def authors(self):
>>>        return self.filter(role='A')
>>>    def editors(self):
>>>        return self.filter(role='E')
>>>class PersonManager(models.Manager):  # your custom Manager
>>>    def get_queryset(self):
>>>        return PersonQuerySet(self.model, using=self._db)
>>>    def authors(self):
>>>		  return self.get_queryset().authors()
>>>    def editors(self):
>>>       return self.get_queryset().editors()
>>>class Person(models.Model):
>>>    first_name = models.CharField(max_length=50)
>>>    last_name = models.CharField(max_length=50)
>>>    role = models.CharField(max_length=50)
>>>    people = PersonManager()
>>># directly call your custom methods: 
>>>Person.people.authors()
>>>Person.people.editors()


# ---------------------------------------execute raw SQL-------------------------------------------#
****Manager.raw()  # perform raw SQL queries and return model instances
# This method takes a raw SQL query, executes it, and returns a [django.db.models.query.RawQuerySet] instance. 
# This RawQuerySet instance can be iterated over just like a normal QuerySet to provide object instances.

*****Executing raw SQL directly:  # i like to write raw SQL using this method if ORM beccome complex!!
# Sometimes even [Manager.raw()] isn’t quite enough: you might need to perform queries that don’t map cleanly to models, 
# or directly execute UPDATE, INSERT, or DELETE queries.
>>>from django.db import connection
>>>def my_custom_sql(self):
>>>    cursor = connection.cursor()
>>>    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
>>>    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
>>>    row = cursor.fetchone()
>>>    return row
# -------------------------------------------------------------------------------------------------#


# ----------------------------------------------------------------------------------------------------------------------- #
****Managing database transactions:  # u just need to write [decorator] in Transaction like in dajngo Cache mechanism
>>>参考==https://docs.djangoproject.com/en/1.9/topics/db/transactions/


# ----------------------------------------------------------------------------------------------------------------------- #
****Multiple databases
>>>参考==https://docs.djangoproject.com/en/1.9/topics/db/multi-db/	


# ----------------------------------------------------------------------------------------------------------------------- #
****Aggregation[聚合函数]
>>>参考==https://docs.djangoproject.com/en/1.9/topics/db/aggregation/


# ----------------------------------------------------------------------------------------------------------------------- #
