from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from todo_list import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
]
