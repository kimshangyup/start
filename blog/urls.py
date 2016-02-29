from django.conf.urls import url, patterns

urlpatterns = patterns('blog.views',
    url(r'^$', 'index'),
)
