from django.conf.urls import patterns, include, url
from teste.views import pagina_inicial, EstrategiaCreate, EstrategiaUpdate, EstrategiaDelete
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', pagina_inicial, name='inicial'),
    url(r'estrategia/add/$', EstrategiaCreate.as_view(), name='estrategia_add'),
    url(r'estrategia/(?P<pk>\d+)/$', EstrategiaUpdate.as_view(), name='estrategia_update'),
    url(r'estrategia/(?P<pk>\d+)/delete/$', EstrategiaDelete.as_view(), name='estrategia_delete'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
