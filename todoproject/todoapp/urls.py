from .import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classview/',views.TaskListview.as_view(),name='classview'),
    path('classdetailview/<int:pk>/',views.TaskDetailview.as_view(),name='classdetailview'),
    path('classviewupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='classviewupdate'),
    path('classviewdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='classviewdelete'),
]
