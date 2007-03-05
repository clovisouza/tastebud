from django.conf.urls.defaults import *
import settings
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['views'])

urlpatterns = patterns('',
    # Example:
    # (r'^stds/', include('stds.foo.urls')),
    (r'^$', 'blog.views.blog_latest'),
    (r'^blog/(?P<slug>.*)/$', 'blog.views.blog_entry'),
    (r'^blog_archive/$', 'blog.views.blog_archive'),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
