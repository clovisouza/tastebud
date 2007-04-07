from django.conf.urls.defaults import *
import settings
blog = __import__("%s.blog" % settings.MODULE_NAME,globals(),locals(),['views'])
rss = __import__("%s.blog.rss" % settings.MODULE_NAME,globals(),locals(),['*'])


feeds = {
    'blog': rss.BlogFeed,
}
urlpatterns = patterns('',
    # Example:
    # (r'^stds/', include('stds.foo.urls')),
    (r'^$', 'blog.views.front_page'),
    (r'^blog/(?P<slug>.*)/$', 'blog.views.blog_entry'),
    (r'^blog_archive/$', 'blog.views.blog_archive'),
    (r'^category/(?P<slug>.*)/$', 'blog.views.category_listing'),
    #(r'^comments/', include('django.contrib.comments.urls.comments')),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',{'feed_dict': feeds}),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    
    # For development only
    (r'^tastebud_media/(.*)$', 'django.views.static.serve', {'document_root': '/Users/cmcavoy/projects/testbud/public/tastebud_media'}),
    (r'^stds_media/(.*)$', 'django.views.static.serve', {'document_root': '/Users/cmcavoy/projects/testbud/public/stds_media'}),
    (r'^media_root/(.*)$', 'django.views.static.serve', {'document_root': '/Users/cmcavoy/projects/testbud/public/media_root'}),
    (r'^images/(.*)$', 'django.views.static.serve', {'document_root': '/Users/cmcavoy/projects/testbud/public/media_root/images'}),
    
    
)
