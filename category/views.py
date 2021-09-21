from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from core .models import  Category,Item,OrderItem
from itertools import chain
from django.db.models import Count



def category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    display_mode = 'P'
    items=Item.objects.filter(category=category, label=display_mode).order_by('-id', 'title')
    return render(request,'category/item.html',{'categories':category,'items':items})
# def Top_Items(request):
#
#     # orderitem = OrderItem.objects.filter(ordered=1)
#
#     # orderitem = Item.objects.filter(F('orderitem__quantity') == 2, orderitem__ordered=1)
#     orderitem = Item.objects.filter(orderitem__ordered = 1).aggregate(Sum('id', field="quantity * item_id"))
#     print(orderitem)
#     return render(request, 'category/item.html', {'items': orderitem})
def Top_Items(request):
    display_mode = 'S'
    items_S_id = Item.objects.filter(label=display_mode).order_by('-id', 'title')

    quantity_item_id = OrderItem.objects.filter(ordered=True).values('item_id').annotate(
        total_quantity=Count('quantity')).order_by('-total_quantity').values_list('item_id')[0:200]
    item_id_list = []
    exclude_id_list = [_.id for _ in items_S_id]

    for i in quantity_item_id:
        item_id_list.append(i[0])
    for i in exclude_id_list:
        if i in item_id_list:
            item_id_list.remove(i)

    objects = Item.objects.in_bulk(item_id_list)
    items = [objects[id] for id in item_id_list]

    # quantity_item_id2 = OrderItem.objects.filter(ordered=True).values('item_id','item__title').annotate(
    #     total_quantity=Count('quantity')).order_by('-total_quantity')[0:200]
    # f = open('11-09-2021.txt', 'w')
    # for x in quantity_item_id2: f.write(u'%s\n' % x)
    # f.close()
    # with open('11-09-2021.txt', 'w') as f:
    #     f.writelines(str(quantity_item_id2))

    # print(objects)
    # print(items)
    return render(request, 'category/item.html', {'items': items})