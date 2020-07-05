from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.showHTML,name="showHTML"),
    path("search",views.search,name="search"),
    path("showMd/<str:title>",views.showMd,name='showMd'),
    path("randomPage",views.randomPage,name="randomPage"),
    path("createPage",views.createPage,name="createPage"),
    path("savePage",views.savePage,name="savePage"),
    path("edit",views.edit,name="edit"),
    path("wiki/edit/<str:title>",views.editPage,name="editPage")
   
    

]
