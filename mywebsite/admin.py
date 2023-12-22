from django.contrib import admin
from django.db.models import get_models, get_app
from django.contrib.admin.sites import AlreadyRegistered

#Any number of arguments can be passed on to the auto_register which 
#will be taken as a list with the help of *args
#get_app gets the app object with the help of app name provided
#get_models gets the list of models in the specific app
def auto_register(*apps):
    for app_name in apps:
        app = get_app(app_name)
        for model in get_models(app):
            try:
                admin.site.register(model)
            except AlreadyRegistered:
                pass

auto_register('mywebsite')


# Register your models here.
