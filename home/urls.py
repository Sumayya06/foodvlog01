from django.urls import path
from . import views

urlpatterns=[
    path('',views.home1,name='hm'),
    path('<slug:c_slug>/',views.home1,name='prodt_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='details'),
    path('search',views.searching,name='search'),
    # path('register',views.register,name='register'),
    # path('login',views.login,name='login'),
    # path('logout',views.logout,name='logout'),
   
]