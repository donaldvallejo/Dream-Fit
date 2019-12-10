from django.urls import path
from wiki.views import SignUpView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup')
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)