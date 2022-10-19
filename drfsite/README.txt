python -m pip install --upgrade pip
pip install django
django-admin startproject drfsite
cd drfsite
python manage.py startapp blog
pip install psycopg2
python manage.py makemigrations
python manage.py migrate


python manage.py shell
from blog.models import Post
#post запрос
Post(title = 'title5', content = 'lorem ipsum')
u1 = _
u1.save()
#get запрос
Post.objects.all()
#u1.pk == u1.id
#посмотреть sql запрос
from django.db import connection
connection.queries
Post.objects.all()[0]
Post.objects.all()[0].title
for post in Post.objects.all():
    print(post.title)

Post.objects.filter(pk=3)
#больше или равно
Post.objects.filter(pk__gte=3)
#меньше или равно
Post.objects.filter(pk__lte=3)
#всех кроме
Post.objects.exclude(pk=5)
#найти уникальную запись
Post.objects.get(pk=5)
#сортировка
Post.objects.filter(pk__gte=3).order_by('title')
#изменение записи-put запрос
post5 = Post.objects.get(pk=5)
post5.title = 'Title 5'
post5.title
post5.save()
#удаление-delete запрос
Post.objects.get(pk=5).delete()
exit()
