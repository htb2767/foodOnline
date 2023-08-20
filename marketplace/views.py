from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from vendor.models import Vendor
from menu.models import Category,FoodItem
from django.db.models import Prefetch
from .models import Cart
from .context_processors import get_cart_counter,get_cart_amount
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D  # ``D`` is a shortcut for ``Distance``
from django.contrib.gis.db.models.functions import Distance
# Create your views here.
def marketplace(request):
    vendors=Vendor.objects.filter(is_approved=True,user__is_active=True)
    vendor_count=vendors.count()
    context={
        'vendors':vendors,
        'vendor_count':vendor_count,
    }
    return render(request,'marketplace/listings.html',context)
def vendor_detail(request,vendor_slug):
    vendor=get_object_or_404(Vendor,vendor_slug=vendor_slug)
    categories=Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
        'fooditems',
        queryset=FoodItem.objects.filter(is_available=True)
        )
    )
    if request.user.is_authenticated:
        cart_items=Cart.objects.filter(user=request.user)
    else:
        cart_items=None

    context={
        'vendor':vendor,
        'categories':categories,
        'cart_items':cart_items,
    }
    return render(request,'marketplace/vendor_detail.html',context)
def add_to_cart(request,food_id=None):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            #check if the food item exist
            try:
                fooditem=FoodItem.objects.get(id=food_id)
                #check if the user has already added food to the cart
                try:
                    checkcart=Cart.objects.get(user=request.user,fooditem=fooditem)
                    #Increase the cart quantity
                    checkcart.quantity+=1
                    checkcart.save()
                    return JsonResponse({'status':'Success','message':'Increase the cart quantity','cart_counter':get_cart_counter(request),'qty':checkcart.quantity,'cart_amount':get_cart_amount(request)})
                except:
                    checkcart=Cart.objects.create(user=request.user,fooditem=fooditem,quantity=1)
                    return JsonResponse({'status':'Success','message':'Added the food the cart','cart_counter':get_cart_counter(request),'qty':checkcart.quantity,'cart_amount':get_cart_amount(request)})

                    
            except:
                return JsonResponse({'status':'Failed','message':'This food does not exist'})
        else:
            return JsonResponse({'status':'Failed','message':'Invalid Request'})

    else:

        return JsonResponse({'status':'login_required','message':'Please log in to continue'})
def decrease_cart(request,food_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            #check if the food item exist
            try:
                fooditem=FoodItem.objects.get(id=food_id)
                #check if the user has already added food to the cart
                try:
                    checkcart=Cart.objects.get(user=request.user,fooditem=fooditem)
                    #Decrease the cart quantity
                    if checkcart.quantity>1:
                        checkcart.quantity-=1
                        checkcart.save()
                    else:
                        checkcart.delete()
                        checkcart.quantity=0
                    return JsonResponse({'status':'Success','cart_counter':get_cart_counter(request),'qty':checkcart.quantity,'cart_amount':get_cart_amount(request)})
                except:
                    
                    return JsonResponse({'status':'Failed','message':'You do not have this item in your cart'})

                    
            except:
                return JsonResponse({'status':'Failed','message':'This food does not exist'})
        else:
            return JsonResponse({'status':'Failed','message':'Invalid Request'})

    else:

        return JsonResponse({'status':'login_required','message':'Please log in to continue'})
@login_required(login_url='login')
def cart(request):
    cart_items=Cart.objects.filter(user=request.user).order_by('created_at')
    context={
        'cart_items':cart_items,
    }
    return render(request,'marketplace/cart.html',context)
def delete_cart(request,cart_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            try:
                #check if cart items exist
                cart_item=Cart.objects.get(user=request.user,id=cart_id)
                if cart_item:
                    cart_item.delete()
                    return JsonResponse({'status':'Sucesss','message':'Cart item has been deleted','cart_counter':get_cart_counter(request),'cart_amount':get_cart_amount(request)})
            except:
                return JsonResponse({'status':'Failed','message':'Cart item does not exist'})
        else:
            return JsonResponse({'status':'Failed','message':'Invalid Request'})


def search(request):
    if not 'address' in request.GET:
        return redirect('marketplace')
    else:
        address = request.GET['address']
        latitude = request.GET['lat']
        longtitude = request.GET['lng']
        radius = request.GET['radius']
        keyword = request.GET['keyword']

        # get vendor ids that has the food item the user is looking for
        fetch_vendors_by_fooditems = FoodItem.objects.filter(food_title__icontains=keyword, is_available=True).values_list('vendor', flat=True)
        
        vendors = Vendor.objects.filter(Q(id__in=fetch_vendors_by_fooditems) | Q(vendor_name__icontains=keyword, is_approved=True, user__is_active=True))
        if latitude and longtitude and radius:
            pnt = GEOSGeometry("POINT(%s %s)" % (longtitude,latitude))
            vendors=Vendor.objects.filter(Q(id__in=fetch_vendors_by_fooditems) | Q(vendor_name__icontains=keyword, is_approved=True, user__is_active=True),
            user_profile__location__distance_lte=(pnt, D(mi=radius))).annotate(distance=Distance("user_profile__location",pnt)).order_by("distance")
            for v in vendors:
                v.miles=round(v.distance.mi,1)
            
        vendor_count = vendors.count()
        context = {
            'vendors': vendors,
            'vendor_count': vendor_count,
            'source_location':address,
            
        }


        return render(request, 'marketplace/listings.html', context)

