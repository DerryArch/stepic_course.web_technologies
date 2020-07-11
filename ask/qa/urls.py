from django.conf.urls import url
from . import views

urlpatterns = [
    url('login/', views.test, name='login'),
    url('signup/', views.test, name='signup'),
    url('question/', views.test, name='question'),
    url('question/<int:id>/', views.test),
    url('ask/', views.test, name='ask'),
    url('popular/', views.test, name='popular'),
    url('new/', views.test, name='new'),

    url('^$', views.test, name='index'),
]
