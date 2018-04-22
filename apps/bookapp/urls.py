from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^log_in$', views.log_in), 
    url(r'^dashboard$', views.dashboard),  
    url(r'^add$', views.add),
    url(r'^add_book$', views.add_book),
    url(r'^book/(?P<id>\d+)$', views.book),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^logout$', views.log_out),
]