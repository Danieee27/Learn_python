from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Store.models import Product
from django.http import JsonResponse

# Create your views here.
def Cart_summary(request):
    cart = Cart(request)
    #get the products in the cart
    cart_products = cart.get_prods()
    return render(request, 'Cart_summary.html', {'cart_products': cart_products})

def Cart_add(request):
    #get the cart
    cart = Cart(request)
   #check for POST
    if request.POST.get('action') == 'post':
        #get the product 
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #SAVE TO SESSION
        cart.add(product=product, quantity = product_qty)

        cart_quantity = cart.__len__()
        #return JsonResponse
        response = JsonResponse({'qty': cart_quantity}, )
        return response
    

def Cart_delete(request):
    pass

def Cart_update(request):
    pass
