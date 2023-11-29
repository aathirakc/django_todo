
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home,name='home'),
    path('add/', views.add,name='add'),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('update/<int:id>/', views.update,name='update'),
    path('cbvhome/',views.list_view.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.detail_view.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.update_view.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.delete_view.as_view(),name='cbvdelete'),


]
