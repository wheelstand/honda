# Honda Wheelstand Project

Django app that provides a content management system for the wheelstand project. Provides API to the front-end via the djangorestframework 

### Prerequisites

```
Django==1.8.6
Pillow==3.4.2
django-admin-tools==0.8.0
django-colorfield==0.1.10
djangorestframework==3.5.3
pilkit==1.1.13
wsgiref==0.1.2
django-admin-bootstrapped==2.5.7
django-model-utils==2.6
django-rest-multiple-models==1.8.1
django-sortedm2m==1.3.2
psycopg2==2.6.2
```

### Installing

Add to settings.py

```
INSTALLED_APPS = (
	'django_admin_bootstrapped',
    'wheelstand',
    'colorfield',
    'rest_framework',
    'drf_multiple_model',
    'sortedm2m',
)
```
Then makemigrations and migrate


### To Do

* Add Fabric file for deployment
* Add auto-generated static file for api
