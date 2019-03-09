from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from asset import views

urlpatterns = [
	path('add-asset',views.addAsset,name='addAsset'),
	path('add-task',views.addTask,name='addTask'),
	path('add-worker',views.addWorker,name='addWorker'),
	path('',views.assetAll,name='assetAll'),
	path('assets/all',views.assetAll,name='assetAll'),
	path('allocate-task',views.allocateTask,name='allocateTask'),
	path('get-tasks-for-worker',views.getTasksForWorker,name='getTasksForWorker'),
	path('get-tasks-for-worker/<workerId>',views.getTasksForWorker,name='getTasksForWorker'),
	path('get-tasks-for-worker&workerId=<workerId>',views.getTasksForWorker,name='getTasksForWorker'),
]