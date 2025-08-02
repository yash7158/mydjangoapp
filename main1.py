import os, sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import path

def add_numbers(a: int, b: int) -> int:
    return a + b

def add_view(request):
    try:
        a = int(request.GET.get('a', '0'))
        b = int(request.GET.get('b', '0'))
    except ValueError:
        return HttpResponseBadRequest('invalid')
    return JsonResponse({'result': add_numbers(a, b)})

urlpatterns = [path('add/', add_view)]

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='x',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
        MIDDLEWARE=[],
        INSTALLED_APPS=['django.contrib.contenttypes', 'django.contrib.auth'],
    )

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '__main__')
    execute_from_command_line(sys.argv)
