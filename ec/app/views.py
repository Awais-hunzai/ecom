from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from . models import Product,Customer,Cart,OrderPlaced
from django.db.models import Count,Q
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"app/home.html",locals())
    
def about(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"app/about.html",locals())
    
def contact(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"app/contact.html",locals())
    
class CategoryView(View):
    def get(self,request,val):
        totalitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,"app/category.html",locals())
    

class ProductDetail(View):
    def get(self, request, pk):
        # Retrieve a single product based on its primary key
        product =  Product.objects.get(pk=pk)
       
        totalitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, "app/productdetails.html", locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/customerregistration.html',locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully")
            return render(request, 'app/customerregistration.html',  {'form': form})
        else:
            messages.warning(request, "Invalid Input Data")
            return render(request, 'app/customerregistration.html', {'form': form})
        
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html',locals())
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()

            # Process the form data if needed
            messages.success(request, "Profile updated successfully!")
        else:
            # Handle form validation errors
            messages.error(request, "Invalid form data, please correct it.")
        
        return render(request, 'app/profile.html', {'form': form})  # Pass form as context data
    

def address(request):
    # Assuming you have some logic to retrieve address information here
    addresses = Customer.objects.filter(user=request.user)
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())

from django.shortcuts import redirect, get_object_or_404
from .models import Product, Cart

def add_to_cart(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('prod_id')
        # Get the product by ID or return 404 if not found
        product = get_object_or_404(Product, id=product_id)
        # Add the product to the user's cart
        Cart.objects.create(user=user, product=product)
        return redirect("/cart")
    else:
        # Handle unauthenticated users here, such as redirecting to a login page
        return redirect("/login")  # Adjust the URL as per your project setup



def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        try:
            value = p.quantity * p.product.price
        except AttributeError:
            # If discounted_price attribute is not available, use regular price
            value = p.quantity * p.product.price
        amount += value
    totalamount = amount + 40
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,'app/addtocart.html',locals())

class checkout(View):
    def get(self, request):
        totalitem = 0
        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
           value = p.quantity * p.product.price
           famount = famount + value
        totalamount = famount + 40
        return render(request, 'app/checkout.html', locals())
def orders(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        order_placed=OrderPlaced.objects.filter(user=request.user)
        return render(request, 'app/orders.html',locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        user = request.user
        try:
            cart_item = get_object_or_404(Cart, product_id=prod_id, user=user)
            cart_item.quantity += 1
            cart_item.save()

            # Recalculate amount and totalamount for the cart
            cart = Cart.objects.filter(user=user)
            amount = 0
            for p in cart:
                value = p.quantity * p.product.price
                amount += value
            totalamount = amount + 40

            data = { 
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'}, status=404)
    
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        user = request.user
        try:
            cart_item = get_object_or_404(Cart, product_id=prod_id, user=user)
            cart_item.quantity -= 1
            cart_item.save()

            # Recalculate amount and totalamount for the cart
            cart = Cart.objects.filter(user=user)
            amount = 0
            for p in cart:
                value = p.quantity * p.product.price
                amount += value
            totalamount = amount + 40

            data = { 
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'}, status=404)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        user = request.user
        try:
            cart_item = get_object_or_404(Cart, product_id=prod_id, user=user)
            cart_item.quantity += 1
            cart_item.delete()

            # Recalculate amount and totalamount for the cart
            cart = Cart.objects.filter(user=user)
            amount = 0
            for p in cart:
                value = p.quantity * p.product.price
                amount += value
            totalamount = amount + 40

            data = { 
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'}, status=404)
        
def search(request):
    query = request.GET['search']
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request,"app/search.html",locals())