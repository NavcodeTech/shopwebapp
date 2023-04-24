from django.shortcuts import render,redirect
from elshopapp.models import Product,Categories,Filter_Price,color,Brand,Order,OrderItem,Contact,Profile,AddressMod
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
import uuid

from datetime import datetime,date
from django.core.mail import send_mail

client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))

def BASE(request):
    return render(request,'Main/base.html')

def HOME(request):
    product=Product.objects.filter(status='Publish')
    context={
        'product':product
    }

    return render(request,'Main/index.html',context)

def PRODUCT(request):
    product = Product.objects.filter(status='Publish')
    brand=Brand.objects.all()
    categories=Categories.objects.all()
    filter = Filter_Price.objects.all()
    col = color.objects.all()
    catid=request.GET.get('categories')
    fid = request.GET.get('filter')
    cid = request.GET.get('color')
    bid = request.GET.get('brand')
    ATOZID=request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    LTOHID = request.GET.get('LTOH')
    HTOLID = request.GET.get('HTOL')
    NPRODID = request.GET.get('nprod')
    OPRODID = request.GET.get('oprod')


    if catid:
        product = Product.objects.filter(categories=catid,status='Publish')
    elif fid:
        product = Product.objects.filter(filter_price=fid,status='Publish')
    elif cid:
        product = Product.objects.filter(color=cid, status='Publish')
    elif bid:
        product = Product.objects.filter(brand=bid, status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif LTOHID:
        product = Product.objects.filter(status='Publish').order_by('price')
    elif HTOLID:
        product = Product.objects.filter(status='Publish').order_by('-price')
    elif NPRODID:
        product = Product.objects.filter(status='Publish',condition='New')
    elif OPRODID:
        product = Product.objects.filter(status='Publish',condition='Old')
    else:
        product = Product.objects.filter(status='Publish')

    context = {
        'product': product,
        'categories':categories,
        'filter':filter,
        'col':col,
        'brand':brand
    }
    return render(request,'Main/product.html',context)

def SEARCH(request):
    query=request.GET.get('query')
    product=Product.objects.filter(name__icontains=query)
    context={
        'product':product
    }
    return render(request,'Main/search.html',context)
def PRODUCT_DETAIL(request,id):
    prod=Product.objects.filter(id = id).first()
    context={
        'prod':prod
    }


    return render(request,'Main/product_detail.html',context)

def HandleRegister(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        customer=User.objects.create_user(username,email,pass1)
        customer.first_name=first_name
        customer.last_name=last_name

        customer.save()
        data = Profile(user=customer, first_name=first_name, last_name=last_name, email=email)
        data.save()
        return redirect('signin')

    return render(request,'Registration/register.html')


def Signin(request):
    print("chk")
    print(request.POST)
    alld=User.objects.get(username='newprof')
    print(alld.password)
    user=User.objects.filter(username=request.POST.get('username'))
    print(user)
    if request.method=='POST':
        print("hk")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, " ", password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')


    context={
        'user':user
    }
    return render(request,'Registration/login.html',context)

def LogoutHandle(request):
    logout(request)

    return redirect('home')

def About(request):
    return render(request,'Main/about.html')

def Forget(request):
    if request.method=="POST":
        username=request.POST.get('username')
        userobj=User.objects.get(username=username)
        print(userobj)
        if userobj is None:
            return redirect('f_password')
        else:
            print("sending..")
            token=str(uuid.uuid4())
            profobj=Profile.objects.get(email=userobj.email)
            profobj.token=token
            profobj.save()
            subject='Elshop-Forget Password link'
            message=f'Hi, click on the link to reset our password http://127.0.0.1:8000/sigin/password_change/{token}/'
            recipient_list=[userobj.email]
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            return redirect('m_password')


    return render(request,'Registration/forget.html')

def ResetMessage(request):
    return render(request,'Registration/password_reset_mess.html')

def false_message(request):
    return render(request,'Registration/false_user_mess.html')

def ChangePassword(request,token):
    context={}
    userobj=Profile.objects.get(token=token)
    print(userobj)
    if userobj is None:
        return redirect('/sigin/false_user_mess/')
    else:
        print("chk")
        if request.method=="POST":
            password=request.POST.get('password')
            print(password)
            userobj=User.objects.get(email=userobj.email)
            userobj.password=password
            userobj.save()
            print(userobj)
            context={
                'userobj':userobj
            }
            return redirect('signin')

        return render(request, 'Registration/password_change.html', context)



@login_required(login_url="/signin/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/signin/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/signin/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/signin/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/signin/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/signin/")
def cart_detail(request):
    return render(request, 'Cart/cart_details.html')

@login_required(login_url="/signin/")
def CHECKOUT(request):
    amount=request.POST.get("amount")
    print(amount)
    amount_int=int(amount)
    print(type(amount_int))
    payment=client.order.create({
        "amount":amount_int,
        "currency":"INR",
        "payment_capture":'1'
    })
    addobj = AddressMod.objects.get(user=request.user)
    print(addobj.country)
    order_id=payment['id']
    print("check",order_id)
    context1={
        'order_id':order_id,
        'payment':payment,
        'addobj':addobj

    }


    return render(request,'Cart/checkout.html',context1)

@login_required(login_url="/signin/")
def PLACE(request):
    if request.method=='POST':
        print("chk")
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        state=request.POST.get('state')
        payment=request.POST.get('payment')
        order_id=request.POST.get('order_id')
        country = request.POST.get('country')
        address= request.POST.get('address')
        city=request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        postcode = request.POST.get('postcode')
        amount=request.POST.get('amount')
        print(order_id)
        context2={
            'order_id':order_id
        }
        print("place=",context2)
        order=Order(
            user=user,
            first_name=first_name,
            last_name=last_name,

            email=email,
            phone=phone,
            postcode=postcode,
            city=city,
            country=country,
            state=state,
            address=address,
            payment_id=order_id,
            amount=amount,
        )
        order.save()
        for i in cart:
            p=int(cart[i]['price'])
            total=p*cart[i]['quantity']
            item=OrderItem(
                user=user,
                order=order,
                image=cart[i]['image'],
                product=cart[i]['name'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                total=total
            )
            item.save()

        return render(request, 'Cart/placeorder.html',context2)

    return render(request,'Cart/placeorder.html')

@csrf_exempt
def Success(request):
    if request.method=="POST":
        a=request.POST
        print(a)
        order_id=""
        for key,val in a.items():
            if key=='razorpay_order_id':
                print("chk")
                order_id=val
                break

        print("id",order_id)
        user1=Order.objects.filter(payment_id=order_id).first()
        #print(user1)
        user1.paid=True
        user1.save()
        cart = Cart(request)
        cart.clear()
    return render(request,'Cart/thank.html')

@login_required(login_url="/signin/")
def my_order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(id=uid)
    order=OrderItem.objects.filter(user=user)
    context={
        'order':order
    }

    return render(request,'Main/myorder.html',context)

def CONTACT(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        subject=request.POST.get('subject')
        details=Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        subject=subject
        message=message
        email_from=settings.EMAIL_HOST_USER
        try:
            send_mail(
                subject,
                message,
                email_from,
                ["ernaveen2708@gmail.com"],

            )
            details.save()
        except:
              return redirect('contact')


        return redirect('home')

    return render(request,'Main/contact.html')

@login_required(login_url="/signin/")
def UserProfile(request):

    uid=request.session.get('_auth_user_id')
    prof=User.objects.get(id=uid)
    print(prof.first_name)
    ghj=Profile.objects.get(user=prof)
    add=AddressMod.objects.get(user=prof)

    context={
        'ghj':ghj,
        'add':add

    }


    if request.method=="POST":
        if 'account' in request.POST:

            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            dob=request.POST.get('birthday')
            genderf=request.POST.get('id_gender_f')
            genderm = request.POST.get('id_gender_m')
            print(genderf," ",genderm)
            if genderf:
                gender=genderf
            if genderm:
                gender=genderm
            email=request.POST.get('email')
            print(first_name," ",gender)
            Profile.objects.filter(user=prof).update(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                dob=dob,
                gender=gender,
                email=email

            )
            print("form ",dob,type(dob))
            ghj = Profile.objects.get(user=prof)
            context = {
                'ghj': ghj,

            }
            return render(request, 'Registration/user_profile.html', context)
        if 'address' in request.POST:
            print("address")
            country=request.POST.get('Country')
            state=request.POST.get('State')
            city=request.POST.get('City')
            phone=request.POST.get('phone')
            area=request.POST.get('area')
            zipcode=request.POST.get('postcode')
            uid = request.session.get('_auth_user_id')
            prof = User.objects.get(id=uid)
            AddressMod.objects.filter(user=prof).update(
                user=request.user,
                country=country,
                state=state,
                city=city,
                zipcode=zipcode,
                phone=phone,
                area=area
            )
            ghj = Profile.objects.get(user=prof)
            add = AddressMod.objects.get(user=prof)

            context = {
                'ghj': ghj,
                'add': add

            }




    return render(request, 'Registration/user_profile.html', context)

