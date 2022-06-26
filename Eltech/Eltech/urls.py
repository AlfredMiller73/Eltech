#"""
#Definition of urls for DjangoWebProject1.
#"""

"""
Definition of urls for New.
"""

from datetime import datetime
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    #path('install/', views.install, name='install'),
    path('reviews/', views.reviews, name='reviews'),
    path('video/', views.video, name='video'),
    path('prices/', views.prices, name='prices'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<parametr>/', views.blogpost, name='blogpost'),
    path('newpost/', views.newpost, name='newpost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


#from datetime import datetime
#from Eltech import urls
#from django.conf.urls import url
#import django.contrib.auth.views
#import app.forms
#import app.views
#from django.contrib.auth.views import LoginView
#from django.contrib.auth import views as auth_views
## Uncomment the next lines to enable the admin:
#from django.conf.urls import include
#from django.contrib import admin
#admin.autodiscover()

#from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.urls import path

#urlpatterns = [
#    # Examples:
#    url(r'^$', app.views.home, name='home'),
#    url(r'^about$', app.views.about, name='about'),
#    url(r'^catalog$', app.views.catalog, name='catalog'),
#    url(r'^install$', app.views.install, name='install'),
#    url(r'^reviews$', app.views.reviews, name='reviews'),
#    url(r'^prices$', app.views.prices, name='prices'),
#    url(r'^contact$', app.views.contact, name='contact'),
#    url(r'^registration$', app.views.registration, name='registration'),
#    url(r'^blog$', app.views.blog, name='blog'),
#    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
#    url(r'^newpost$', app.views.newpost, name='newpost'),
#    url(r'^login/$',
#        django.contrib.auth.views.LoginView.as_view(),
#        {
#            'template_name': 'app/login.html',
#            'authentication_form': app.forms.BootstrapAuthenticationForm,
#            'extra_context':
#            {
#                'title': 'Вход',
#                'year': datetime.now().year,
#            }
#        },
#        name='login'),
#    url(r'^logout$',
#        django.contrib.auth.views.LogoutView.as_view(),
#        {
#            'next_page': '/',
#        },
#        name='logout'),

#    # Uncomment the admin/doc line below to enable admin documentation:
#    # path('admin/doc/', include('django.contrib.admindocs.urls')),
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    # Uncomment the next line to enable the admin:
#    url(r'^admin/', admin.site.urls),
#    #path('admin/', admin_site.urls),
#]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()