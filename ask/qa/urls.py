from django.urls import path
from . import views

urlpatterns = [                                                                 
    path('login/', admin.site.urls),
	path('', views.test, name='qa_list'),
	path('login/', views.test, name='login'),
	path('signup/', views.test, name='signup'),
	path('question/<int:id>/', views.test, name='question'),
	path('ask/', views.test, name='ask'),
	path('popular/', views.test, name='popular'),
	path('new/', views.test, name='new'),                                            
]                 
