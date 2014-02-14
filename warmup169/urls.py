from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warmup169.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/add', 'warmup169.main.views.add'),
    url(r'^users/login', 'warmup169.main.views.login'),
    url(r'^TESTAPI/resetFixture', 'warmup169.main.views.TESTAPI_resetFixture'),
    url(r'^TESTAPI/unitTests', 'warmup169.main.views.TESTAPI_test'),
)
