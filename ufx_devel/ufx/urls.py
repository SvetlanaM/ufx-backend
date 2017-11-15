from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from records.views import RecordCreateAPIView
from rest_framework_swagger.views import get_swagger_view
from django.views.generic.base import RedirectView

schema_view = get_swagger_view(title='UFX API')

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='admin'), name='index'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/v1.0/records/$', RecordCreateAPIView.as_view(), name='create-record'),
    url(r'^api/v1.0/docs/$', schema_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
