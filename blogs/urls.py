from django.urls import path
from . import views


urlpatterns = [

    path('',views.index,name="index"),
    path('loader/',views.loader_fn,name="loader"),

    path('new',views.new,name="new"),
]
