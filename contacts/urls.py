from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('repeatName/', views.repeatName, name="repeatName"),
    path('contact/<int:id>/update/', views.update, name="update"),
    path('contact/<int:id>/delete/', views.delete, name="delete"),
    path('contact/<int:id>/delete/delete/', views.confirm_delete, name="delete"),
    path('delete/<int:id>/delete/', views.confirm_delete, name="delete"),
    path('contact/<int:id>/', views.contact, name="contact"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec")
]