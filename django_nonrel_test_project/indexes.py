#use this to automatically register all database indexes in project
from dbindexer import autodiscover
autodiscover()

#use this to load module.py in installed apps

# def autodiscover():
#     from autoload import autodiscover as auto_discover
#     auto_discover('module_name_here')