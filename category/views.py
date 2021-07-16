from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from core .models import  Category,Item



def category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    display_mode = 'P'
    items=Item.objects.filter(category=category, label=display_mode).order_by('-id', 'title')
    return render(request,'category/item.html',{'categories':category,'items':items})
