from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('home-admin/',views.home_admin,name='home_admin'),
    path('home-base/',views.home_base,name='home_base'),
    path('logout/',views.user_logout,name='logout'),
    path('success/',views.success,name='success'),
    path('success-admin/',views.success_admin,name='success_admin'),
    path('modify-permission/<int:candidate_id>/',views.modify_candidate,name='modify_permission'),
    path('candidate/<int:candidate_id>/delete', views.delete_candidate, name='delete')
    

]
