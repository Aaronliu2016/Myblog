from django.urls import re_path, path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Post
from . import views

info_dict = {
    'queryset': Post.objects.all(),
    'data_field': 'created_time',
}
Sitemaps = {
    'blog': GenericSitemap(info_dict, priority=0.6)
}


urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    re_path(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    re_path(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    path('sitemap.xml', sitemap, {'sitemaps': Sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
