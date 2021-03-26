from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages


from core.models import Order,OrderItem


@user_passes_test(lambda u: u.is_superuser)
def get_orders(request):
    orders=Order.objects.filter(ordered=True,being_delivered=False)
    context={
        'orders':orders
    }

    return render(request,'orders/admin_orders.html',context)

@user_passes_test(lambda u: u.is_superuser)
def delivered(request,pk):
    order=get_object_or_404(Order,pk=pk)
    try:
        if order:
            order.being_delivered=True
            order.save()
            messages.success(request,'订单状态标记为已交付')
        else:
            messages.error(request,'订单已经送达')
    except ObjectDoesNotExist:
        print('this does not exist')
    

    return render(request,'orders/admin_orders.html')


@user_passes_test(lambda u: u.is_superuser)
def view_order_details(request,pk):
    order=get_object_or_404(Order,pk=pk)
    context={
        'order':order
    }
    return render(request,'orders/details.html',context)




def order_history(request):
    orders=Order.objects.filter(user=request.user)
    context={
        'orders':orders
    }
    return render(request,'orders/history.html',context)

def history_details(request,pk):
    order=get_object_or_404(Order,pk=pk)
    context={
        'order':order
    }

    return render(request, 'orders/history_detail.html',context)