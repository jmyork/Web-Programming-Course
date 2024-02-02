from . import views
from django.urls import path

urlpatterns=[
    path("",views.index,{
        "name":"York"
        }),
    
    path('smith',views.smith),
    path('greet',views.greet,{
        'name':"Jhon"
    }),
    path('<str:name>',views.greet,name="Greet")
]