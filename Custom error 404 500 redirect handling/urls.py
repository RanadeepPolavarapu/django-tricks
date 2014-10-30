from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic.base import TemplateView

from myproject import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myproject.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

)

# You have to declare handler404 and etc.
# See: https://docs.djangoproject.com/en/dev/ref/urls/#handler400
handler404 = views.page_not_found_custom
handler500 = views.page_error_found_custom
