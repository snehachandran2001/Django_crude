from . import views
from django.urls import path

urlpatterns=[

    path('',views.table,name='table'),
    path('input/',views.input,name='form'),
    path('remove/<int:id>/',views.remove,name='remove'),
    path('update/<int:id>/',views.update,name='update')
    ]