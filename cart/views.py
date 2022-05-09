from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from home.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_details(request,tot=0,count=0,cart_items=None):
    try:
        ct=cartlist.objects.get(user=request.user)
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.qty)
            count+=i.qty
    except ObjectDoesNotExist:
        return HttpResponse("oops...Your cart is empty")

    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})



def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id


# addin item to a cart
def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request),user=request.user)
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.qty < c_items.prodt.stock:
            c_items.qty += 1
        c_items.save()
    except items.DoesNotExist:
            c_items=items.objects.create(prodt=prod,qty=1,cart=ct)
            c_items.save()
    return redirect('cartDetails')


#  removing a item from cart
def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    if c_items.qty>1:
        c_items.qty-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')


def delete_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    c_items.delete()
    return redirect('cartDetails')
