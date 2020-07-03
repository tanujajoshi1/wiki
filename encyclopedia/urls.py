from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.showHTML,name="showHTML"),
    path("search",views.search,name="search"),
    path("showHTML/<str:title>",views.showHTML,name='showHTML')
]
