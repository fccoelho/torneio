from django.conf.urls import patterns, include, url
from teste.views import pagina_inicial
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', pagina_inicial, name='inicial'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
