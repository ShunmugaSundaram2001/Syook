from django.urls import path
from . import views

app_name = 'logistic_system'

urlpatterns = [
    path('items/', views.ItemListCreateView.as_view(), name='item-list'),
    path('items/<int:pk>/', views.ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),
    path('customers/', views.CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('vehicles/', views.DeliveryVehicleListCreateView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', views.DeliveryVehicleRetrieveUpdateDestroyView.as_view(), name='vehicle-detail'),
    path('orders/', views.OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
]
