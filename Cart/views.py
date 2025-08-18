from django.shortcuts import render, get_object_or_404
from .cart import Cart
from Store.models import Product
from django.http import JsonResponse

# Create your views here.
def Cart_summary(request):
    return render(request, 'Cart_summary.html', {})

def Cart_add(request):
    #get the cart
    cart = Cart(request)
   #check for POST
    if request.POST.get('action') == 'post':
        #get the product 
        product_id = int(request.POST.get('product_id'))
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #SAVE TO SESSION
        cart.add(product=product)

        cart_quantity = cart.__len__()
        #return JsonResponse
        response = JsonResponse({'qty': cart_quantity}, {'price': Product.price})
        return response
    

def Cart_delete(request):
    pass

def Cart_update(request):
    pass
