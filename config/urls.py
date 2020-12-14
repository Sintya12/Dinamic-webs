from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from akun import views as akun_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='akun/password_reset_complete.html'
        ),
        name='password_reset_complete'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='akun/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    url(r'^password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='akun/password_reset_done.html'
        ),
        name='password_reset_done'),
    url(r'^password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='akun/password_reset.html'
        ),
        name='password_reset'),
    url(r'^logout/',
        auth_views.LogoutView.as_view(
            template_name='akun/logout.html'
        ),
        name='logout'),
    url(r'^login/',
        auth_views.LoginView.as_view(
            template_name='akun/login.html'
        ),
        name='login'),
    url(r'^profil/(?P<user>.*)/',
        akun_views.profil,
        name='profil'),
    url(r'^register/',
        akun_views.register,
        name='register'),
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
