from Store.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get("session_key")
#if user is new, no session key yet.
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        #make sure cart is available on all pages
        self.cart = cart
    

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)


    #Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = { "price": str(product.price),
            
            self.cart[product_id] = int(product_qty)

        #update session 
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart) #convert dictionary to string
            carty = carty.replace("'", '"')
            current_user.update(old_cart = carty)

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)


    #Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = { "price": str(product.price),
            
            self.cart[product_id] = int(product_qty)

        #update session 
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart) #convert dictionary to string
            carty = carty.replace("'", '"')
            current_user.update(old_cart = carty)

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        mycart = self.cart

        #update dictionary-cart
        mycart[product_id] = product_qty
        self.session.modified = True

        #Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart) #convert dictionary to string
            carty = carty.replace("'", '"')
            current_user.update(old_cart = carty)


        thing = self.cart
        return thing
       
    def delete(self, product):
        #{'4': 3}, where 4 is the product id and 3 is the quantity
        product_id = str(product)
        #delete from dictionary-cart
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

        #Deal with logged in user
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            carty = str(self.cart) #convert dictionary to string
            carty = carty.replace("'", '"')
            current_user.update(old_cart = carty)


    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        #start counting at 0
        total = 0
        for key, value in quantities.items():
            #convert string key to integer so we can do maths
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price * value)

        return total
