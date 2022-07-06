from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('quantity-change/', views.cart, name="quantity-change"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('my-shop/', views.shop_my, name="my-shop"),
    path('add-product/', views.product_add, name="add-product"),
    path('product/<int:product_id>', views.product_page, name="product"),
    path('add-to-cart', views.add_to_cart, name="add-to-cart"),
]