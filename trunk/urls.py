from django.conf.urls.defaults import *
import settings
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['views'])

urlpatterns = patterns('',
    # Example:
    # (r'^stds/', include('stds.foo.urls')),
    (r'$^', 'blog.views.index'),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
