from django.urls import path,re_path

from . import views

urlpatterns=[
    path('index',views.index,name='index'),
    path('article/<int:id>/',views.article,name='article'),
]