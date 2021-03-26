from django.conf.urls import url
from django.urls import path
from .views import order_history,history_details,view_order_details,get_orders,delivered


app_name='orders'



urlpatterns = [
    path("order-history", order_history, name="order_history"),
    path("orders-history/<int:pk>/details", history_details,name='history_detail'),
    path("user-orders/<int:pk>/details", view_order_details,name='order_detail'),
    path("user-orders/<int:pk>/deliver", delivered,name='delivered'),
    path("admin-orders", get_orders,name='get_orders'),
]
