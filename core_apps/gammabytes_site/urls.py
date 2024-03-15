from django.urls import path
from .views import website_page, contact_form
from django.conf import settings
from django.conf.urls.static import static

# {% url 'pharmafriend:homepage' %}

app_name = 'gammabytes_site'

urlpatterns = [
    path('', website_page, name='website_page'),
    path('contact/', contact_form, name='contact_form'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)