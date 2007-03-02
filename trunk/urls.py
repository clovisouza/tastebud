from django.conf.urls.defaults import *
MODULE_NAME = 'tastebud'

urlpatterns = patterns('',
    # Example:
    # (r'^stds/', include('stds.foo.urls')),
    (r'$^', '%s.blog.views.index' % MODULE_NAME),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
