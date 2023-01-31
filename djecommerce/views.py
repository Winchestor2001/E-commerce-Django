from django.shortcuts import render
from store.models import Product
from store.models import ReviewRating


def home_page(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    context = {
        'products': products,
        
    }
    return render(request, 'home.html', context)