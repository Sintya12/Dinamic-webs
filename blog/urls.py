from django.conf.urls import url
from .views import (
    DaftarBlog,
    DetailBlog,
    BuatBlog,
    EditBlog,
    HapusBlog,
    DaftarPenggunaBlog,
)
from . import views

urlpatterns = [
    url(r'^postingan/(?P<pk>\d+)/hapus/$', HapusBlog.as_view(), name='hapus'),
    url(r'^postingan/(?P<pk>\d+)/edit/$', EditBlog.as_view(), name='edit'),
    url(r'^postingan/baru/', BuatBlog.as_view(), name='buat'),
    url(r'^postingan/(?P<pk>\d+)/$', DetailBlog.as_view(), name='detail'),
    url(r'^pengguna-post/(?P<user>.*)/$', DaftarPenggunaBlog.as_view(), name='pengguna'),
    url(r'^$', DaftarBlog.as_view(), name='home'),
    url(r'^about/$', views.about, name='about'),
]
