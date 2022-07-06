from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
import json
# from decimal import *

def store(request):
    products = Product.objects.all()
    p = Paginator(products, 9)
    page = request.GET.get('page')
    shops = p.get_page(page)
    context = {
        'shops': shops
    }
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    #     cartItems = order.get_cart_items
    # else:
    #     try:
    #         cart = json.loads(request.COOKIES['cart'])
    #     except:
    #         cart = {}
    #     print('Cart:', cart)
    #     items = []
    #     order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    #     cartItems = order['get_cart_items']

    #     for i in cart:
    #         cartItems += cart[i]["quantity"]

    #         product = Product.objects.get(id=i)
    #         total = (product.price * cart[i]["quantity"])

    #         order['get_cart_total'] += total
    #         order['get_cart_items'] += cart[i]["quantity"]

    #         item = {
    #             'product':{
    #                 'id':product.id,
    #                 'name':product.name,
    #                 'price':product.price,
    #                 'imageURL':product.imageURL,
    #                 },
    #             'quantity': cart[i]["quantity"],
    #             'get_total': total
    #             }
    #         items.append(item)
    # context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
    
def contact_us(request):
    context = {}
    return render(request, 'store/contact-us.html', context)

def shop_my(request):
    context = {}
    return render(request, 'store/shop-my.html', context)

def product_add(request):
    context = {}
    product = Product.objects.create(
        name = request.POST["name"],
        desc = request.POST["desc"],
        price = request.POST["price"]
        )
    product.save()
    return render(request, 'store/shop-my.html', context)

def product_page(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product':product}

    return render(request, 'store/product-page.html', context)

def add_to_cart(request):
    request.session["cart-product"] = request.POST['cart-item']
    product = Product.objects.get(id=request.session["cart-product"])

    cart = []
    item = {
    'product':{
    'id':product.id,
    'name':product.name,
    'price':product.price,
    'desc':product.desc,
    'digital':product.digital}}
    # 'quantity': cart[i]["quantity"],
    # 'get_total': total
    # }
    cart.append(item)
    print(cart)

    return render(request, 'store/cart.html')
