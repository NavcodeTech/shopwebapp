"""elshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('search/',views.SEARCH,name='name'),
    path('contact/',views.CONTACT,name='contact'),
    path('products/<str:id>',views.PRODUCT_DETAIL,name='product_detail'),
    path('',views.HOME,name='home'),
    path('products/', views.PRODUCT, name='products'),
    path('about/', views.About, name='about'),

    path('register/',views.HandleRegister,name='register'),
    path('signin/', views.Signin, name='signin'),
    path('logout/', views.LogoutHandle, name='logout'),
    path('profile/',views.UserProfile,name='profile'),
    path('sigin/forget/',views.Forget,name='f_password'),
    path('sigin/password_change/<token>/',views.ChangePassword,name='c_password'),
    path('sigin/password_reset_mess/',views.ResetMessage,name='m_password'),
    path('sigin/false_user_mess/',views.false_message,name='false_message'),


    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/checkout',views.CHECKOUT,name='checkout'),
    path('cart/checkout/placeorder',views.PLACE,name='placeorder'),
    path('success',views.Success,name='success'),

    path('my_order',views.my_order,name="my_order"),




]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
