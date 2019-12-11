from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import models
import json

# Create your views here.
""" def index(request):
    return HttpResponse("Project 3: TODO") """

def menu(request):
    context = {

        "regular_pizza": zip(models.Pizza.objects.filter(tipe="RP", size="S"), models.Pizza.objects.filter(tipe="RP", size="L")),
        "sicilian_pizza": zip(models.Pizza.objects.filter(tipe="SP", size="S"), models.Pizza.objects.filter(tipe="SP", size="L")),
        "toppings": models.Topping.objects.all(),
        "subs": zip(models.Pizza.objects.filter(tipe="Sub", size="S"), models.Pizza.objects.filter(tipe="Sub", size="L")),
        "pasta": models.Pizza.objects.filter(tipe="Pasta"),
        "salad": models.Pizza.objects.filter(tipe="Salad"),
        "dinnerplatters": zip(models.Pizza.objects.filter(tipe="DP", size="S"), models.Pizza.objects.filter(tipe="DP", size="L"))
    }
    
    if (request.user.get_username()):
        return render(request, "orders/menu.html", context)
    else:
        return redirect('/login',  {"message": "You need to be logged."})

def registration(request):
    context = {
        "client": models.Client.objects.all(),
        "client2": User.objects.all()
    }
    if request.method == 'POST':
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
        user.first_name = request.POST.get('name')
        user.last_name = request.POST.get('lastname')
        user.save()
        
        post = models.Client()
        post.username = request.POST.get('username')
        post.password = request.POST.get('password')
        post.firstname = request.POST.get('name')
        post.lastname = request.POST.get('lastname')
        post.email = request.POST.get("email")
        post.save()

        return render(request, "orders/register.html", context)

    else:
        return render(request, "orders/register.html", context)



def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return redirect('/menu')

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html",  {"message": 'Welcome to the webpage. If you have an account, login. Else click on Register.'})

def logout_view(request):
    logout(request)
    return redirect('/login')

def cart(request):
    
    Carrito = models.Carrito.objects.filter(userID = request.user.get_username())
    suma = 0
    productos = []
    for car in Carrito:
        print(car.productID)
        p = models.Pizza.objects.get(id=car.productID)
        productos.append(p)
        suma += p.price
    context = {
        "Cart": zip(productos, Carrito),
        "Cart2": Carrito,
        "precio": round(suma, 2)
    }


    return render(request, "orders/carrito.html", context)


def accept(request):
    cart = models.Carrito.objects.filter(userID = request.user.get_username())
    for i in cart:
        o = models.Order(productID=i.productID, topings=i.topings, userID=i.userID)
        o.save()
    models.Carrito.objects.filter(userID = request.user.get_username()).delete()
    return render(request, "orders/confirmedOrder.html")


def AddtoCart(request):
    print("entre add to cart")
    lista = request.POST["lista"]
    Pid = request.POST["productID"] 
    print(lista)
    topping = lista
    print(topping)
    c = models.Carrito(productID = Pid, userID = request.user.get_username(), topings = topping)
    c.save()

    Carrito = models.Carrito.objects.filter(userID = request.user.get_username())

    suma = 0    
    productos = []
    for car in Carrito:
        print(car.productID)
        p = models.Pizza.objects.get(id=car.productID)
        productos.append(p)
        suma += p.price
    
    print(models.Carrito.objects.all())
    return render(request, "orders/carrito.html", {"Cart": zip(productos,Carrito), "Cart2": Carrito, "precio" : round(suma, 2)})


def selectTopping(request, product):
    
    product = models.Pizza.objects.get(id=product)
    print(product.product[0])
    
    if product.product == "1 topping" or product.product == "2 toppings" or product.product == "3 toppings ":
        context = {
        "product": product,
        "toppings": models.Topping.objects.all(),
        "limit": int(product.product[0])
        }
        return render(request, "orders/topping.html", context)
    else:
        c = models.Carrito(productID = product.id, userID = request.user.get_username(), topings = "")
        c.save()
        Carrito = models.Carrito.objects.filter(userID = request.user.get_username())
        
        suma = 0
        productos = []
        for car in Carrito:
            print(car.productID)
            p = models.Pizza.objects.get(id=car.productID)
            productos.append(p)
            suma += p.price
        return render(request, "orders/carrito.html", {"Cart": zip(productos, Carrito), "Cart2": Carrito, "precio" : round(suma,2) })

def viewOrders(request):

    orders = models.Order.objects.all()
    clients = models.Client.objects.all()
    # names_prod = []
    lista = []

    for client in clients:
        byclient = models.Order.objects.filter(userID=client.username)
        if (byclient):
            lista.append(byclient)
    print("LISTA")
    print(lista)
    completa = []
    for lis in lista:
        names_prod = []
        for order in lis:
            name = models.Pizza.objects.get(id=order.productID)
            print(name)
            names_prod.append(name)
        completa.append(names_prod)
    print("nombres completos")
    print(completa)
    print("FIN")
    # print("Estoy aqui")
    lista_completa = zip(completa, lista)
    users = []
    for e1,e2 in lista_completa:
        users.append(e2[0].userID)
    print('USERS')
    print(json.dumps(users))
    # print(jsonify(users))
            # print("hola")
            # print(e.topings)
            # print("chao")
    context = {
        "Orders": orders,
        "Complete": zip(completa, lista),
        "byClient": json.dumps(users),
        "completa": completa,
        "lista": lista
    }
    if request.user.is_staff:
        return render(request, "orders/orders.html", context)
    else:
        return checkStatus(request)

def checkStatus(request):
    if request.user.is_staff:
        uID = request.POST["userID"]
        print(uID)
        orders = models.Order.objects.filter(userID=uID)
        for ord in orders:
            if (ord.status) :
                ord.status = False
            else:
                ord.status = True
            ord.save()
        return viewOrders(request)
    else:
        orders = models.Order.objects.filter(userID=request.user.get_username())
        names_prod = []
        for order in orders:
            name = models.Pizza.objects.get(id=order.productID)
            names_prod.append(name)
        print(orders)
        print(names_prod)

        context = {
            "Orders": zip(names_prod,orders)
        }
        return render(request, "orders/status.html", context)
    


