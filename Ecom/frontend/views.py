from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Product, Brand, Category, Order, Coupon, Report, Setting
from django.contrib.auth.decorators import login_required
from django.utils import timezone
def delete_product_view(request, product_id):



  def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Deleting the product
    product.delete()

    # Redirect to a product list or another page after deletion
    return redirect('product_list')
    
    
    # Deleting the product
    product.delete()

    # Redirect to a product list or another page after deletion
    return redirect('product_list')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Ensure 'home' URL exists
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def brand_list_view(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {'brands': brands})

def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def coupon_list_view(request):
    coupons = Coupon.objects.all()
    return render(request, 'coupons_list.html', {'coupons': coupons})

def report_list_view(request):
    reports = Report.objects.all()
    return render(request, 'reports_list.html', {'reports': reports})

def setting_view(request):
    settings = Setting.objects.all()  # Fixed typo here
    return render(request, 'settings_list.html', {'settings': settings})

def checkout(request):
    cart = Order.objects.filter(user=request.user, ordered_date__isnull=True)  # Assuming these are the items in the user's cart
    total = sum(item.product.price * item.quantity for item in cart)

    coupon_code = request.POST.get('coupon', None)
    discount = 0
    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code)
            discount = coupon.discount
        except Coupon.DoesNotExist:
            discount = 0
    
    total_after_discount = total - discount

    if request.method == 'POST':
        # Logic for processing payment, saving the order, etc.
        for order_item in cart:
            order_item.ordered_date = timezone.now()
            order_item.save()
        return redirect('order_success')

    context = {
        'cart': cart,
        'total': total,
        'discount': discount,
        'total_after_discount': total_after_discount
    }

    return render(request, 'checkout.html', context)