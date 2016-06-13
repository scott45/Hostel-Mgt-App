from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from Gyobera import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.home, name='home',),
                       url(r'^Gyobera/', views.index, name='index',),
                       url(r'^about/', views.about, name='about'),
                       url(r'^add_classification/$', views.add_classification, name='add_classification'),
                       url(r'^book/$', views.book, name='book'),
                       url(r'^classification/(?P<classification_name_slug>\w+)/$', views.classification,
                           name='classification'),
                       url(r'^classification/(?P<classification_name_slug>\w+)/add_list/$', views.add_list,
                           name='add_list'),
                       url(r'^booking/', views.booking, name='booking'),
                       url(r'^contact/', views.contact, name='contact'),
                       url(r'^gallery/', views.gallery, name='gallery'),
                       url(r'^student/$', views.student, name='student'),
                       url(r'^registry/$', views.registry, name='registry'),
                       url(r'^rooms/$', views.rooms, name='rooms'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^restricted/', views.restricted, name='restricted'),
                       url(r'^payment/$', views.payment, name='payment'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^goto/$', views.track_url, name='goto'),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
