
from django.urls import path

from . import views

urlpatterns = [

    # path('',views.demo,name='demo'),
    path('',views.about,name='index'),
    path('add/',views.operation,name='operation'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('thanks/',views.thanks,name='thanks'),
]