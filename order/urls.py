"""
URL configuration for Hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from order import views


urlpatterns = [
    path('', views.index,name='index'),
    path('hotel_login', views.hotel_login,name='hotel_login'),
    path('sunil_login', views.sunil_login,name='sunil_login'),
    path('marketing_employee', views.marketing_employee,name='marketing_employee'),
    path('hotel', views.hotel,name='hotel'),
    path('marketing_employee_login', views.marketing_employee_login,name='marketing_employee_login'),
    path('chef_login', views.chef_login,name='chef_login'),
    path('chef_dashboard', views.chef_dashboard,name='chef_dashboard'),
    path('waiter_login', views.waiter_login,name='waiter_login'),
    path('hotel_dashboard', views.hotel_dashboard,name='hotel_dashboard'),
    path('waiter_dashboard', views.waiter_dashboard,name='waiter_dashboard'),
    path('employee', views.employee,name='employee'),
    path('dish_category',views.dish_category , name='dish_category'),
    path('dish',views.dish,name='dish'),
    path('table',views.table,name='table'),
    path('waiter_add_order/<int:id>/',views.waiter_add_order,name='waiter_add_order'),
    path('dish_filter',views.dish_filter,name='dish_filter'),
    path('filter_by_category',views.filter_by_category,name='filter_by_category'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('view_order/<int:id>',views.view_order,name='view_order'),
    path('complate_view_order/<int:id>',views.complate_view_order,name='complate_view_order'),
    path('running_table',views.running_table,name='running_table'),
    path('complate_order',views.complate_order,name='complate_order'),
    path('place_order/<int:id>',views.place_order,name='place_order'),
    path('remove_cart',views.remove_cart,name='remove_cart'),
    path('remove_cart_waiter',views.remove_cart_waiter,name='remove_cart_waiter'),
    path('merge_card/<int:table_id>/<int:hotel_id>',views.merge_card,name='merge_card'),
    
    path('test',views.test,name='test'),
   
]
