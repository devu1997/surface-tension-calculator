from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from asset import views

urlpatterns = [
	path('',views.getSurfaceTension,name='getSurfaceTension'),
	path('solid',views.addSolid,name='addSolid'),
	path('liquid',views.addLiquid,name='addLiquid'),
	path('solid/all',views.solidAll,name='solidAll'),
	path('liquid/all',views.liquidAll,name='liquidAll'),
]
