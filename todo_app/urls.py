from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from todo_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
]    
