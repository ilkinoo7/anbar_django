from fileinput import filename
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from . models import Brands , Clients, Expenses , Orders , Products , Ishciler, Senedler

from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User, auth

from django.db.models import Q

# Create your views here.

# USER_SYS START.
# request.user.id
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Bu istifadeci artiq movcuddur')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('login_user')


        else:
            messages.info(request, 'Parollar uygundur')
            return redirect(register)
            

    else:
        return render(request, 'main/registration.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('order')
        else:
            messages.info(request, 'Login ve ya parol yanlishdir')
            return redirect('login_user')
    else:
        return render(request, 'main/login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('order')

def home(request):
    return render(request,'main/order.html')




# USER_SYS END.



# BRAND START.

def brand(request):
    info = Brands.objects.filter(user_id=request.user.id).all()
    say = Brands.objects.filter(user_id=request.user.id).count()
    return render(request,'main/brand.html',{'data':info,'say':say})

def addbrand(request):
   
    x = request.POST['brend']
    
    image = request.FILES['foto']
    fs = FileSystemStorage()
    filename = fs.save(image.name,image)
    uploaded_file_url = fs.url(filename)
    yoxla = Brands.objects.filter(brend=x).count()
    if yoxla>0:
        messages.warning(request, 'Bu brend artiq movcuddur!')
    else:
        daxilet = Brands(brend = x,image = uploaded_file_url,user_id = request.user.id)
        daxilet.save()
        messages.success(request,'Brend ugurla elave edildi')
 
    return HttpResponseRedirect(reverse('brand'))


def silbrand(request, id):
    info = Brands.objects.all()
    say = Brands.objects.count()
    return render(request,'main/brand.html',{'data':info,'say':say,'sil_id':id})

def delete(request, id):
    info = Brands.objects.all()
    say = Brands.objects.count()
    sil = Brands.objects.get(id=id)
    sil.delete()
    return HttpResponseRedirect(reverse('brand'),{'data':info,'say':say})

def redaktebrand(request, id):
    editdata = Brands.objects.get(id=id)
    info = Brands.objects.filter(user_id=request.user.id).all()
    say = Brands.objects.filter(user_id=request.user.id).count()
    return render(request,'main/brand.html',{'data':info,'say':say,'editdata':editdata})


def edit(request):

    x = request.POST['brend']
    id = request.POST['id']
    filepath = request.FILES.get('filepath', False)
    
    if 'foto' in request.FILES:
        image = request.FILES['foto']
        fs = FileSystemStorage()
        filename = fs.save(image.name,image)
        uploaded_file_url = fs.url(filename)
    else:
        uploaded_file_url = request.POST['bfoto']

    yoxla = Brands.objects.filter(brend=x).count()
    if yoxla<0:
        messages.warning(request, 'Bu brend artiq movcuddur!')
    else:
        editdata = Brands.objects.get(id=id)
        editdata.brend = x
        editdata.image = uploaded_file_url
        editdata.save()
        messages.success(request,'Brend ugurla yenilendi')
 
    return HttpResponseRedirect(reverse('brand'))



def axtar(request):
    x = request.POST['sorgu']
    my_brands=Brands.objects.filter(Q(brend__contains=x) | Q(data_brend__contains=x))
    template=loader.get_template('main/brand.html')
    return HttpResponse(template.render({'data':my_brands},request))


# BRAND END.

# CLIENT START.


def client(request):
    info = Clients.objects.filter(user_id=request.user.id).all()
    say = Clients.objects.filter(user_id=request.user.id).count()

  
    return render(request,'main/client.html',{'clientdata':info,'say':say,'sil_id':id})


def axtar_client(request):
    x = request.POST['sorgu']
    my_clients=Clients.objects.filter(Q(ad__contains=x) | Q(soyad__contains=x) | Q(shirket__contains=x))
    template=loader.get_template('main/client.html')
    return HttpResponse(template.render({'clientdata':my_clients},request))


def addclient(request):
    
    ad = request.POST['ad']
    soyad = request.POST['soyad']
    tel = request.POST['tel']
    email = request.POST['email']
    shirket = request.POST['shirket']

    imageclient = request.FILES['foto']
    fs = FileSystemStorage()
    filename = fs.save(imageclient.name,imageclient)
    uploaded_file_url = fs.url(filename)

    yoxla = Clients.objects.filter(ad=ad).count()
    if yoxla>0:
        messages.warning(request, 'Bu klient artiq movcuddur!')
    else:
        daxilet = Clients(ad = ad, soyad = soyad, tel = tel, email = email, shirket = shirket,imageclient = uploaded_file_url,user_id = request.user.id)
        daxilet.save()
        messages.success(request,'Klient ugurla elave edildi')
 
    return HttpResponseRedirect(reverse('client'))


def silclient(request, id):
    info = Clients.objects.all()
    say = Clients.objects.count()
    return render(request,'main/client.html',{'clientdata':info,'say':say,'sil_id':id})

def deleteclient(request, id):
    info = Clients.objects.all()
    say = Clients.objects.count()
    sil = Clients.objects.get(id=id)
    sil.delete()
    return HttpResponseRedirect(reverse('client'),{'clientdata':info,'sayclient':say})

def redakteclient(request, id):
    editdata = Clients.objects.get(id=id)
    info = Clients.objects.filter(user_id=request.user.id).all()
    say = Clients.objects.filter(user_id=request.user.id).count()
    return render(request,'main/client.html',{'clientdata':info,'sayclient':say,'editdata':editdata})

def editclient(request):

    ad = request.POST['ad']
    soyad = request.POST['soyad']
    tel = request.POST['tel']
    email = request.POST['email']
    shirket = request.POST['shirket']
    id = request.POST['id']
    
    if 'foto' in request.FILES:
        imageclient = request.FILES['foto']
        fs = FileSystemStorage()
        filename = fs.save(imageclient.name,imageclient)
        uploaded_file_url = fs.url(filename)
    else:
        uploaded_file_url = request.POST['cfoto']

    yoxla = Clients.objects.filter(ad=ad).count()
    if yoxla>0:
        messages.warning(request, 'Bu klient artiq movcuddur!')
    else:
        editdata = Clients.objects.get(id=id)
        editdata.ad = ad
        editdata.soyad = soyad
        editdata.tel = tel
        editdata.email = email
        editdata.shirket = shirket
        editdata.imageclient = uploaded_file_url
        editdata.save()
        messages.success(request,'Klient ugurla yenilendi')
 
    return HttpResponseRedirect(reverse('client')) 

# CLIENT END.

# ORDER START.

def order(request):

    sifarish=Orders.objects.filter(user_id=request.user.id).all().select_related().order_by('-id')
    myclients=Clients.objects.filter(user_id=request.user.id).all()
    mehsul = Products.objects.filter(user_id=request.user.id).all().select_related()
    bsay = Orders.objects.filter(user_id=request.user.id).all().count()
    sayklient = Clients.objects.filter(user_id=request.user.id).all().count()
    saybrend = Brands.objects.filter(user_id=request.user.id).all().count()
    saymehsul = Products.objects.filter(user_id=request.user.id).values_list('miqdar').count()
    cesid = Products.objects.filter(user_id=request.user.id).values_list('mehsul').distinct().count()
    mehsulsayi = Products.objects.filter(user_id=request.user.id).values_list('miqdar', flat=True)
    mehsuldepo = sum(mehsulsayi)
    mehsulal = Products.objects.filter(user_id=request.user.id).values_list("alis",flat=True)
    alisdepo = sum(mehsulal)
    mehsulsat = Products.objects.filter(user_id=request.user.id).values_list("satis",flat=True)
    satisdepo = sum(mehsulsat)


    clients = Clients.objects.filter(user_id=request.user.id).all()
    products = Products.objects.filter(user_id=request.user.id).all()
    info = Orders.objects.filter(user_id=request.user.id).all()
    say = Orders.objects.filter(user_id=request.user.id).count()
    
    mehsulselect = Products.objects.filter(user_id=request.user.id).all()
    qazancmehsul = 0
    for x in mehsulselect:
        qazancmehsul = ((x.satis - x.alis) *  x.miqdar) + qazancmehsul 
    # cari qazanc
    cariqaz = 0
    for y in sifarish:
        
        if y.tesdiq == 1 :
            cariqaz = (int(y.product_id.satis) * int(y.pmiqdar)) - (int(y.product_id.alis) * int(y.pmiqdar)) + cariqaz
        

    
    template=loader.get_template('main/order.html')
    data = {'sifarish': sifarish,"myclients":myclients,"mehsul":mehsul,"bsay":bsay,"sayklient":sayklient
    ,"saybrend":saybrend,"saymehsul":saymehsul,"cesid":cesid,"mehsuldepo":mehsuldepo,"alisdepo":alisdepo,
    "satisdepo":satisdepo,"qazanc":qazancmehsul,"cariqaz":cariqaz,'orderdata':info,'clients':clients,'products':products,'sayorder':say,'sil_id':id}
    return HttpResponse(template.render(data,request))

    
    #clients = Clients.objects.all()
    #products = Products.objects.all()
    #info = Orders.objects.all()
    #say = Orders.objects.count()
    
    #return render(request,'main/order.html',{'orderdata':info,'clients':clients,'products':products,'sayorder':say,'sil_id':id})


"""def axtar_order(request):
    x = request.POST['sorgu']
    my_clients=Clients.objects.filter(Q(ad__contains=x) | Q(soyad__contains=x) | Q(shirket__contains=x))
    template=loader.get_template('main/client.html')
    return HttpResponse(template.render({'clientdata':my_clients},request))"""

def addorder(request):
    
    client_id = request.POST['client_id']
    product_id = request.POST['product_id']
    pmiqdar = request.POST['pmiqdar']

    
    product = Products.objects.filter(user_id=request.user.id).get(id=product_id)
    client = Clients.objects.filter(user_id=request.user.id).get(id=client_id)
    daxilet = Orders(client_id = client,product_id = product,pmiqdar = pmiqdar,user_id=request.user.id,tesdiq = 0)
    daxilet.save()
    messages.success(request,'Sifariş ugurla elave edildi')
 
    return HttpResponseRedirect(reverse('order'))


def silorder(request, id):
    info = Orders.objects.all()
    say = Orders.objects.count()
    return render(request,'main/order.html',{'orderdata':info,'sayorder':say,'sil_id':id})

def deleteorder(request, id):
    info = Orders.objects.all()
    say = Orders.objects.count()
    sil = Orders.objects.get(id=id)
    sil.delete()
    return HttpResponseRedirect(reverse('order'),{'orderdata':info,'sayorder':say})

def tesdiqorder(request):

    pid = int(request.POST['pid'])
    oid = int(request.POST['oid'])
    pmiqdar = int(request.POST['pmiqdar'])
    miqdar = int(request.POST['miqdar'])

    order = Orders.objects.get(id=oid)
    product = Products.objects.get(id=pid)

    if pmiqdar <= miqdar:
        netice = miqdar - pmiqdar
        product.miqdar = netice
        product.save()
        order.tesdiq = 1
        order.save()

        messages.success(request,'Uğurla təsdiqləndi')
    else:
        messages.warning(request,'Sifarişi təsdiq etmek üçün anbarda kifayət qədər məhsul yoxdur!')

    return HttpResponseRedirect(reverse('order'))



def legvetorder(request, id):

    if request.method == 'GET':
        order = Orders.objects.get(id=id)
        product = Products.objects.get(id= order.product_id_id)
        omiq = order.pmiqdar
        pmiq = product.miqdar
        netice = int(pmiq) + int(omiq)
        
        product.miqdar = netice
        order.tesdiq = 0
        order.save()
        product.save()
   
    messages.warning(request,'Ugurla legv edildi')

    return HttpResponseRedirect(reverse('order'))


def redakteorder(request, id):
    editdata = Orders.objects.get(id=id)
    info = Orders.objects.filter(user_id=request.user.id).all()
    say = Orders.objects.filter(user_id=request.user.id).count()

    clients = Clients.objects.filter(user_id=request.user.id).all()
    products = Products.objects.filter(user_id=request.user.id).all()
    return render(request,'main/order.html',{'orderdata':info,'clients':clients,'products':products,'sayorder':say,'editdata':editdata})

def editorder(request):

    pmiqdar = request.POST['pmqidar']
    id = request.POST['id']

    client_id = request.POST['client_id']
    product_id = request.POST['product_id']

    yoxla = Orders.objects.filter(pmiqdar=pmiqdar).count()
    if yoxla>0:
        messages.warning(request, 'Bu sifariş artiq movcuddur!')
    else:
        editdata = Orders.objects.get(id=id)
        editdata.pmiqdar = pmiqdar
        editdata.client_id = client_id
        editdata.product_id = product_id
        editdata.save()
        messages.success(request,'Sifariş ugurla yenilendi')
 
    return HttpResponseRedirect(reverse('order'))

# ORDER END.

# PRODUCT START.


def product(request):
    brands = Brands.objects.filter(user_id=request.user.id).all()
    info = Products.objects.filter(user_id=request.user.id).all()
    say = Products.objects.filter(user_id=request.user.id).count()
    return render(request,'main/product.html',{'productdata':info,'brands':brands,'say':say,'sil_id':id})


def axtar_product(request):
    x = request.POST['sorgu']
    my_products=Products.objects.filter(Q(mehsul__contains=x))
    template=loader.get_template('main/product.html')
    return HttpResponse(template.render({'productdata':my_products},request))


def addproduct(request):

    brand_id = request.POST['brand_id']
    mehsul = request.POST['mehsul']
    alis = request.POST['alis']
    satis = request.POST['satis']
    miqdar = request.POST['miqdar']

    imageproduct = request.FILES['foto']
    fs = FileSystemStorage()
    filename = fs.save(imageproduct.name,imageproduct)
    uploaded_file_url = fs.url(filename)
    
    yoxla = Products.objects.filter(mehsul=mehsul).count()
    if yoxla>0:
        messages.warning(request, 'Bu məhsul artiq movcuddur!')
    else:
        brand = Brands.objects.get(id=brand_id)
        daxilet = Products(brand_id = brand, mehsul = mehsul, alis = alis, satis = satis, miqdar = miqdar,imageproduct = uploaded_file_url,user_id=request.user.id)
        daxilet.save()
        messages.success(request,'Məhsul ugurla elave edildi')
 
    return HttpResponseRedirect(reverse('product'))


def silproduct(request, id):
    info = Products.objects.all()
    say = Products.objects.count()
    return render(request,'main/product.html',{'productdata':info,'say':say,'sil_id':id})

def deleteproduct(request, id):
    info = Products.objects.all()
    say = Products.objects.count()
    sil = Products.objects.get(id=id)
    sil.delete()
    return HttpResponseRedirect(reverse('product'),{'productdata':info,'sayproduct':say})

def redakteproduct(request, id):
    editdata = Products.objects.get(id=id)
    info = Products.objects.filter(user_id=request.user.id).all()
    say = Products.objects.filter(user_id=request.user.id).count()
    brands = Brands.objects.filter(user_id=request.user.id).all()
    return render(request,'main/product.html',{'productdata':info,'sayproduct':say,'editdata':editdata,'brands':brands})

def editproduct(request):

    brand_id = request.POST['brand_id']
    mehsul = request.POST['mehsul']
    alis = request.POST['alis']
    satis = request.POST['satis']
    miqdar = request.POST['miqdar']
    id = request.POST['id']

    if 'foto' in request.FILES:
        imageproduct = request.FILES['foto']
        fs = FileSystemStorage()
        filename = fs.save(imageproduct.name,imageproduct)
        uploaded_file_url = fs.url(filename)
    else:
        uploaded_file_url = request.POST['pfoto']

    yoxla = Products.objects.filter(mehsul=mehsul).count()
    if yoxla>0:
        messages.warning(request, 'Bu məhsul artiq movcuddur!')
    else:
        editdata = Products.objects.get(id=id)
        r = Brands.objects.get(id=brand_id)
        
        editdata.mehsul = mehsul
        editdata.alis = alis
        editdata.satis = satis
        editdata.miqdar = miqdar
        editdata.brand_id = r
        editdata.imageproduct = uploaded_file_url
        editdata.save()
        messages.success(request,'Məhsul ugurla yenilendi')
 
    return HttpResponseRedirect(reverse('product')) 

# PRODUCT END.


# EXPENSES START.


def expenses(request):
    info = Expenses.objects.filter(user_id=request.user.id).all()
    say = Expenses.objects.filter(user_id=request.user.id).count()
    return render(request,'main/expenses.html',{'expensesdata':info,'say':say,'sil_id':id})


def axtar_expenses(request):
    x = request.POST['sorgu']
    my_expenses=Expenses.objects.filter(Q(xerc__contains=x))
    template=loader.get_template('main/expenses.html')
    return HttpResponse(template.render({'expensesdata':my_expenses},request))

def addexpenses(request):
    
    xerc = request.POST['xerc']
    
    
    yoxla = Expenses.objects.filter(xerc=xerc).count()
    if yoxla>0:
        messages.warning(request, 'Bu məhsul artiq movcuddur!')
    else:
        daxilet = Expenses(xerc = xerc,user_id=request.user.id)
        daxilet.save()
        messages.success(request,'Məhsul ugurla elave edildi')
 
    return HttpResponseRedirect(reverse('expenses'))


def silexpenses(request, id):
    info = Expenses.objects.all()
    say = Expenses.objects.count()
    return render(request,'main/expenses.html',{'expensesdata':info,'say':say,'sil_id':id})

def deleteexpenses(request, id):
    info = Expenses.objects.all()
    say = Expenses.objects.count()
    sil = Expenses.objects.get(id=id)
    sil.delete()
    return HttpResponseRedirect(reverse('expenses'),{'expensesdata':info,'sayexpenses':say})

def redakteexpenses(request, id):
    editdata = Expenses.objects.get(id=id)
    info = Expenses.objects.filter(user_id=request.user.id).all()
    say = Expenses.objects.filter(user_id=request.user.id).count()
    return render(request,'main/expenses.html',{'expensesdata':info,'sayxpenses':say,'editdata':editdata})

def editexpenses(request):

    
    xerc = request.POST['xerc']
    id = request.POST['id']

    yoxla = Expenses.objects.filter(xerc=xerc).count()
    if yoxla>0:
        messages.warning(request, 'Bu məhsul artiq movcuddur!')
    else:
        editdata = Expenses.objects.get(id=id)
        editdata.xerc = xerc
        editdata.save()
        messages.success(request,'Məhsul ugurla yenilendi')
 
    return HttpResponseRedirect(reverse('expenses')) 

# EXPENSES END.


# STAFF START.


def staff(request):
    staff = Ishciler.objects.filter(user_id=request.user.id).order_by('-id')
    say = Ishciler.objects.filter(user_id=request.user.id).count()
    template=loader.get_template('main/staff.html')
    data={'staff':staff,'say':say}
    return HttpResponse(template.render(data,request))

def addstaff(request):
    ad = request.POST['ad']
    soyad = request.POST['soyad']
    telefon = request.POST['telefon']
    ev_tel=  request.POST['ev_tel']
    unvan = request.POST['unvan']
    email = request.POST['email']
    vezife = request.POST['vezife']
    
    daxilet = Ishciler(ad=ad,soyad=soyad,telefon=telefon,ev_tel=ev_tel,unvan=unvan,email=email,vezife=vezife,user_id=request.user.id)
        
    daxilet.save()
    return HttpResponseRedirect(reverse('staff'))

def editstaff(request,id):
    staff = Ishciler.objects.filter(user_id=request.user.id).order_by('-id')
    say = Ishciler.objects.filter(user_id=request.user.id).count()
    editstaff = Ishciler.objects.get(id=id)
    template=loader.get_template('main/staff.html')
    data={'staff':staff,'say':say,"editstaff":editstaff}
    return HttpResponse(template.render(data,request))

def updatestaff(request,id):
    ad = request.POST['ad']
    soyad = request.POST['soyad']
    telefon = request.POST['telefon']
    ev_tel=  request.POST['ev_tel']
    unvan = request.POST['unvan']
    email = request.POST['email']
    vezife = request.POST['vezife']


    savestaff = Ishciler.objects.get(id=id)
    savestaff.ad=ad
    savestaff.soyad=soyad
    savestaff.telefon=telefon
    savestaff.ev_tel=ev_tel
    savestaff.unvan=unvan
    savestaff.email=email
    savestaff.vezife=vezife
    savestaff.save()
    return HttpResponseRedirect(reverse('staff'))

def deleteconstaff(request,id):
    staff = Ishciler.objects.filter(user_id=request.user.id).order_by('-id')
    say = Ishciler.objects.filter(user_id=request.user.id).count()
    deletest = Ishciler.objects.get(id=id)
    template=loader.get_template('main/staff.html')
    data={'staff':staff,'say':say,"deletest":deletest}
    return HttpResponse(template.render(data,request))

def deletestaff(request,id):
    
    staff=Ishciler.objects.get(id=id)
    staff.delete()
    return HttpResponseRedirect(reverse('staff'))

# STAFF END.

# Senedler

def senedler(request,id):
    staff = Ishciler.objects.all()
    senedler = Senedler.objects.all().order_by('-id')
    say = Senedler.objects.all().count()
    sened_id = Senedler.objects.filter(ishci_id=id).select_related()
    template=loader.get_template('main/senedler.html')
    data={'senedler':senedler,'say':say,"staff":staff,"sened_id":sened_id}
    return HttpResponse(template.render(data,request))

def addsenedler(request):
    if request.method=='POST' and request.FILES['foto']:
        foto=request.FILES['foto']
        fs = FileSystemStorage()
        filename=fs.save(foto.name,foto)
        uploaded_file_url=fs.url(filename)
        isci_id = request.POST['isci_id']
        basliq = request.POST['basliqs']
        qeyd = request.POST['qeyds']
        r = Ishciler.objects.get(id = isci_id)
        
        daxilet = Senedler(ishci_id=r, basliq=basliq,skan=uploaded_file_url,qeyd=qeyd)
            
        daxilet.save()
    return HttpResponseRedirect(reverse('senedler',kwargs={'id': isci_id}))

def deletesenedler(request,id):
    deletesen = Senedler.objects.get(id=id)
    deletesen.delete()
    messages.success(request,'Ugurla Silindi')
    return HttpResponseRedirect(reverse('senedler'))


#PROFILE START

@login_required

def profile(request):
     
    editdata = User.objects.filter(id=request.user.id)

    return render(request,'main/profile.html',{'editdata':editdata})


def updateprofile(request,id):
    

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    newpassconf = request.POST['newpassconf']

    user = User.objects.get(id=id)
    user.first_name = first_name
    user.last_name = last_name
    user.username = username
    user.email = email
    
    
    if user.check_password(password) and newpassconf != '' and request.POST['newpass'] != '':
        
        
        if request.POST['newpass']==newpassconf:
            user.set_password(request.POST['newpass'])
        else:
            messages.warning(request,'Parollar uygun deyil')
        
    
    user.save()
    

    return HttpResponseRedirect(reverse('profile'))









# def profile(request,id):
#     info = User.objects.all()
#     say = User.objects.count()
#     editdata = User.objects.get(id=request.user.id)

#     return render(request,'main/profile.html',{'profiledata':info,'say':say,'editdata':editdata})



# def profile(request):
     
#     editdata = User.objects.filter(id=request.user.id)

#     return render(request,'main/profile.html',{'editdata':editdata})



# def updateprofile(request):

#     user = User.objects.get(id=request.user.id)
    
#     first_name = request.POST['first_name']
#     last_name = request.POST['last_name']
#     username = request.POST['username']
#     email = request.POST['email']
#     password = request.POST['password']
#     newpassconf = request.POST['newpassconf']

#     user.first_name = first_name
#     user.last_name = last_name
#     user.username = username
#     user.email = email
#     user.password = password



#     if user.check_password(password) and newpassconf != '' and request.POST['newpass'] != '':
        
        
#         if request.POST['newpass']==newpassconf:
#             user.set_password(request.POST['newpass'])
#         else:
#             messages.warning(request,'Parollar uygun deyil')
   

#     user.save()
    

#     return HttpResponseRedirect(reverse('profile'))      




 

#PROFILE END

























