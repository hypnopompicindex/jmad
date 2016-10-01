from django.conf.urls import url
from django.contrib import admin
from solos.views import index, SoloDetailView

urlpatterns = [
    url(r'^$', index),
    url(r'^solos/(?P<pk>\d+)/$', SoloDetailView.as_view()),
    url(r'^admin/', admin.site.urls),
]
