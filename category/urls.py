from django.urls import path

from .views import category


app_name='categories'

urlpatterns = [
    path('items/<int:pk>/list', category,name='category_list')
]
