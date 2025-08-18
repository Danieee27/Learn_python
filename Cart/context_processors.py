from .cart import Cart

#context processor so cart can work on all pages
def cart(request):
    return{"cart": Cart(request)}