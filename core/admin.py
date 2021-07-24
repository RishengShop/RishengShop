from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile, Category

from django.contrib.auth.models import User

# def make_refund_accepted(modeladmin, request, queryset):
#     queryset.update(refund_requested=False, refund_granted=True)

def make_being_delivered(modeladmin, request, queryset):
    queryset.update(being_delivered=True, refund_granted=True)

# make_refund_accepted.short_description = 'Update orders to refund granted'
make_being_delivered.short_description = '更新订单为已配送'

class ItemAdmin(admin.ModelAdmin):
    list_display = ['get_title',
                    'get_id',
                    'get_price',
                    'get_discount_price',
                    'get_category_name'
                    ]
    list_filter = ('label',)
    search_fields = ['title', 'id',]

    def get_title(self, obj):
        return obj.title
    get_title.short_description = u'商品'

    def get_id(self, obj):
        return obj.id
    get_id.short_description = u'编号'

    def get_price(self, obj):
        return obj.price
    get_price.short_description = u'价格'

    def get_discount_price(self, obj):
        return obj.discount_price
    get_discount_price.short_description = u'折扣价'

    def get_category_name(self, obj):

        return Category.objects.filter(id = obj.category_id)[0]
    get_category_name.short_description = u'类别'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon',
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon',
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']

    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_being_delivered, ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['get_category_name',
                    'get_category_count'
                    ]


    def get_category_name(self, obj):
        return obj.name

    get_category_name.short_description = u'类别'

    def get_category_count(self, obj):
        return len(Item.objects.filter(category_id = obj.id))

    get_category_count.short_description = u'数量'

class OrderItemAdmin(admin.ModelAdmin):

    list_display = [
        'get_user_id',
        'get_user_name',
        'get_item_name',
        'get_item_price',
        'get_item_discount_price',
        'get_quantity'
    ]

    list_filter = [
        'order__being_delivered',
        'item_id__category',
    ]



    search_fields = ['item__title','user__username', 'user__id']

    def get_user_id(self, obj):
        return User.objects.filter(id = obj.user_id)[0].id

    get_user_id.short_description = '账号'

    def get_user_name(self, obj):
        return User.objects.filter(id = obj.user_id)[0].username

    get_user_name.short_description = u'姓名'

    def get_item_price(self, obj):

        return Item.objects.filter(id = obj.item_id)[0].price

    get_item_price.short_description = u'价格'

    def get_item_name(self, obj):
        return obj.item

    get_item_name.short_description = u'商品'

    def get_item_discount_price(self, obj):
        return Item.objects.filter(id = obj.item_id)[0].discount_price

    get_item_discount_price.short_description = u'折扣价'

    def get_quantity(self, obj):
        return obj.quantity

    get_quantity.short_description = u'数量'


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(Payment)
# admin.site.register(Coupon)
# admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
# admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
