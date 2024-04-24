from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.reg),
    path('', views.main),
    path('reg/registrate', views.registrate),
    path('reg/authorize', views.authorize, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('like/<str:pk>', views.like),
    path('create/', views.create),
    path('create/create_post', views.create_post),
    path('update/<str:pk>/', views.update),
    path('update/update_post/<str:pk>', views.update_post),
]
