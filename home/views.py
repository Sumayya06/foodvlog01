from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core. paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def home1(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:
        prodt=products.objects.all().filter(available=True)
    cat=categ.objects.all()
    paginator=Paginator(prodt,4)
    # page num veran
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'pr':prodt,'ct':cat,'pg':pro})

def prodDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,'search.html',{'qr':query,'pr':prod})

# def login(request):

#     # if request.method=="GET":
#     #     username=request.GET['username']
#     #     password=request.GET['password']
#     #     user=auth.authenticate(username=username,password=password)
#     #     if user is not None:
#     #         auth.login(request,user)
#     #         return redirect('/')
#     #     else:
#     #         messages.info(request,'invalid details')
#     #         return redirect('login')
#     # else:
#         return render(request,'login.html')
        
# def register(request):
#     if request.method=="GET":
#         first_name=request.GET['first_name']
#         last_name = request.GET['last_name']
#         username = request.GET['username']
#         password1 = request.GET['password1']
#         password2 = request.GET['password2']
#         email = request.GET['email']
#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username already taken")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"email already taken")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
#                 user.save()
#                 print("USER CREATED")

#         else:
#             print("password not match")
#             return redirect('register')
#         return redirect('/')
#     else:
#         return render(request,'register.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')

    # the above things are created for displaying the link for each category 