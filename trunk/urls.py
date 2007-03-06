from django.conf.urls.defaults import *
import settings
blog = __import__("%s.blog.models" % settings.MODULE_NAME,globals(),locals(),['views'])

urlpatterns = patterns('',
    # Example:
    # (r'^stds/', include('stds.foo.urls')),
    (r'^$', 'blog.views.blog_latest'),
    (r'^blog/(?P<slug>.*)/$', 'blog.views.blog_entry'),
    (r'^blog_archive/$', 'blog.views.blog_archive'),
    (r'^category/(?P<slug>.*)/$', 'blog.views.category_listing'),
    (r'^comments/', include('django.contrib.comments.urls.comments')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    
    # For development only
    (r'^testbud_media/(.*)$', 'django.views.static.serve', {'document_root': '/Users/cmcavoy/projects/testbud/public/testbud_media'}),
    
)
