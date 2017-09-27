#Creacion de objetos
>>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()

 #guardar cambios en los objetos
>>> b5.name = 'New name'
>>> b5.save()

# este proceso imporca la importacion de las clases y su objetivo principal es el de asignar llave foranea y almacenar el id del campo creado para la llamaforanea
>>> from blog.models import Blog, Entry, Author
>>> ed = Entry.objects.get(pk=1)
>>>  cheese_blog1 = Blog.objects.create(name="Cheddar Talk")
>>> cheese_blog1.save()
>>> cheese_blog1= Blog.objects.get(id=5)
>>> cheese_blog1 = Blog.objects.get(name="Cheddar Talk")

>>> Author.objects.filter(
...    headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
...  ).filter(
...    pub_date__gte=datetime(2005, 1, 30)

#Recuperacion de objetos
>>> Blog.objects.filter(
...    headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
...  ).filter(
...    pub_date__gte=datetime(2005, 1, 30)
... )

#filtrado de quierYSets unicos
>>> q1 = Author.objects.filter(headline__startswith="What")
>>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
>>> q3 = q1.filter(pub_date__gte=datetime.date.today())

>>> q4 = Blog.objects.filter(headline__startswith="What")
>>> q5 = q4.exclude(pub_date__gte=datetime.date.today())
>>> q6 = q4.filter(pub_date__gte=datetime.date.today())

>>> qfilter(headline__startswith="What")
>>> q = q.filter(pub_date__lte=datetime.date.to = Entry.objects.day())
>>> q = q.exclude(body_text__icontains="food")
>>> print(q)

#Limitacion de querysets
>>> Author.objects.all()[:5]
>>> Blog.objects.all()[:5]
>>> Author.objects.all()[5:10]
>>> Blog.objects.all()[5:10]
>>> Author.objects.all()[:10:2]
>>> Blog.objects.all()[:10:2]
>>> Author.objects.order_by('headline')[0]
>>> Blog.objects.order_by('headline')[0]
>>> Author.objects.order_by('headline')[0:1].get()
>>> Blog.objects.order_by('headline')[0:1].get()

#Busqueda de campo
>>> Author.objects.filter(pub_date__lte='2006-01-01')
>>> Blog.objects.filter(pub_date__lte='2006-01-01')
>>> Author.objects.filter(blog_id=4)
>>> Blog.objects.filter(blog_id=4)
>>> Author.objects.get(headline__exact="Cat bites dog")
>>> Blog.objects.get(headline__exact="Cat bites dog")
>>> Blog.objects.get(id__exact=14)  # Explicit form
>>> Blog.objects.get(id=14)         # __exact is implied
>>> Blog.objects.get(name__iexact="beatles blog")

>>> Blog.objects.get(id__exact=14)  # Explicit form
>>> Blog.objects.get(id=14)         # __exact is implied
>>> Blog.objects.get(name__iexact="beatles blog")
>>> Author.objects.get(headline__contains='Lennon')
>>> Blog.objects.get(headline__contains='Lennon')
>>> Author.objects.filter(blog__name='Beatles Blog')
>>> Blog.objects.filter(blog__name='Beatles Blog')
>>> Blog.objects.filter(entry__headline__contains='Lennon')
>>> Blog.objects.filter(entry__authors__name='Lennon')
>>> Blog.objects.filter(entry__authors__name__isnull=True)
>>> Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)

#intercambiando relaciones de valores multiples
>>>Blog.objects.filter(entry__headline__contains='Lennon', >>>entry__pub_date__year=2008)
>>>Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)


>>> from django.db.models import F
>>> Author.objects.filter(n_comments__gt=F('n_pingbacks'))
>>> Blog.objects.filter(n_comments__gt=F('n_pingbacks'))
>>> Author.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
>>> Blog.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
>>> Author.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
>>> Blog.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))
>>> Author.objects.filter(authors__name=F('blog__name'))
>>> Blog.objects.filter(authors__name=F('blog__name'))
>>> from datetime import timedelta
>>> Author.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))
>>> Blog.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))
>>> F('somefield').bitand(16)

#El acceso directo de busqueda de pk
>>> Blog.objects.get(id__exact=14) # Explicit form
>>> Blog.objects.get(id=14) # __exact is implied
>>> Blog.objects.get(pk=14) # pk implies id__exact
# Get blogs entries with id 1, 4 and 7
>>> Blog.objects.filter(pk__in=[1,4,7])

# Get all blog entries with id > 14
>>> Blog.objects.filter(pk__gt=14)
>>> Author.objects.filter(blog__id__exact=3) # Explicit form
>>> Blog.objects.filter(blog__id__exact=3)
>>> Author.objects.filter(blog__id=3)        # __exact is implied
>>> Blog.objects.filter(blog__id=3)
>>> Author.objects.filter(blog__pk=3)        # __pk implies
>>> Blog.objects.filter(blog__pk=3) __id__exact
>>> Author.objects.filter(headline__contains='%')
>>> Blog.objects.filter(headline__contains='%')

#almacenamiento en cache y query sets
>>> queryset = Author.objects.all()
>>> queryset = Blog.objects.all()
>>> print([p.headline for p in queryset]) # Evaluate the query set.
>>> print([p.pub_date for p in queryset]) # Re-use the cache from the evalua


#cuando querysets no se almacenan en cache
>>> queryset = Author.objects.all()
>>> queryset = Blog.objects.all()
>>> print(queryset[5]) # Queries the database
>>> print(queryset[5]) # Queries the database again
>>> queryset = Author.objects.all()
>>> queryset = Blog.objects.all()
>>> [Author for Author in queryset] # Queries the database
>>> [Blog for Blog in queryset] # Queries the database
>>> print(queryset[5]) # Uses cache
>>> print(queryset[5]) # Uses cache
>>> [entry for entry in queryset]
>>> bool(queryset)
>>> Author in queryset
>>> Blog in queryset
>>> list(queryset)


#utilizar un gestor inverso personalizado
from django.db import models
class Entry(models.Model):
    #...
    objects = models.Manager()  # Default Manager
    entries = EntryManager()    # Custom Manager

b = Blog.objects.get(id=1)
b.entry_set(manager='entries').all()
b.entry_set(manager='entries').is_published()
b = Blog.objects.get(id=1)
b.entry_set.set([e1, e2])


# consulta sobre objetos relacionados
Entry.objects.filter(blog=b) # Query using object instance
Entry.objects.filter(blog=b.id) # Query using id from instance
Entry.objects.filter(blog=5) # Query using id directly


---------------------##Referencia https://docs.djangoproject.com/en/1.11/topics/db/queries/ ## ----------------------------------------
