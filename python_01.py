import importlib
import pkgutil
import django

from django import views


# django_db = importlib.import_module('django.db')
# print(django_db)
# print(dir(django_db))

# for _, module_name, ispkg in pkgutil.iter_modules(django.__path__):
#     full_name = f'django.{module_name}'
#     module = importlib.import_module(full_name)
#     print(f"✅ Loaded: {full_name}")

print(dir(views))
print(help(views))