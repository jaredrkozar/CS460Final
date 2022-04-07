from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


'''#superuser info
#name: admin
#pw: password'''
#models = apps.get_models()

#for model in models:
 #   admin.site.register(model)

group = Group.objects.get(name='doctors')
group2 = Group.objects.get(name='nurses')
group3 = Group.objects.get(name='billing')

content_type = ContentType.objects.get(app_label='staff', model='patient')
permission = Permission.objects.get(codename='doctor', content_type=content_type)
permission2 = Permission.objects.get(codename='nurse', content_type=content_type)
permission3 = Permission.objects.get(codename='billing', content_type=content_type)
permission4 = Permission.objects.get(codename='medical professional', content_type=content_type)

group.permissions.add(permission)
group2.permissions.add(permission2)
group3.permissions.add(permission3)
group.permissions.add(permission4)
group2.permissions.add(permission4)


#doctor1 = User.objects.create_user('doctor1', 'email@email.com', 'pw')
#doctor2 = User.objects.create_user('doctor2', 'email@email.com', 'pw')
#nurse1 = User.objects.create_user('nurse1', 'email@email.com', 'pw')
#nurse2 = User.objects.create_user('nurse2', 'email@email.com', 'pw')
#billing1 = User.objects.create_user('billing1', 'email@email.com', 'pw')
#billing2 = User.objects.create_user('billing2', 'email@email.com', 'pw')
#registration1 = User.objects.create_user('registration1', 'email@email.com', 'pw')
#registration2 = User.objects.create_user('registration2', 'email@email.com', 'pw')
#a
