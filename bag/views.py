from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity', 1))  
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')  
    bag = request.session.get('bag', {})

    if item_id in bag:
        if isinstance(bag[item_id], int):
            bag[item_id] = {'items_by_size': {}}
    else:
        bag[item_id] = {'items_by_size': {}}

    if size in bag[item_id]['items_by_size']:
        bag[item_id]['items_by_size'][size] += quantity
        messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
    else:
        bag[item_id]['items_by_size'][size] = quantity
        messages.success(request, f'Added size {size.upper()} {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


from django.contrib import messages
from django.shortcuts import get_object_or_404

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')  
    bag = request.session.get('bag', {})

    if item_id in bag and size in bag[item_id]['items_by_size']:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


from django.contrib import messages

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST['product_size'] 
        bag = request.session.get('bag', {})

        if item_id in bag and size in bag[item_id]['items_by_size']:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
