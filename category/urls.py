from django.urls import path

from .views import category, Top_Items

app_name='categories'

urlpatterns = [
    path('items/<int:pk>/list', category ,name='category_list'),
    path('top-items',Top_Items ,name='top-items')
]
