from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    price = float(product.discounted_price) if product.discounted_price else float(product.price)  # Convert Decimal to float
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if item_id not in bag:
        bag[item_id] = {'items_by_size': {}}

    if size in bag[item_id]['items_by_size']:
        bag[item_id]['items_by_size'][size]['quantity'] += quantity
        bag[item_id]['items_by_size'][size]['price'] = price
        messages.success(
            request,
            f'Updated size {size.upper()} {product.name} quantity to '
            f'{bag[item_id]["items_by_size"][size]["quantity"]}'
        )
    else:
        bag[item_id]['items_by_size'][size] = {'quantity': quantity, 'price': price}
        messages.success(
            request,
            f'Added size {size.upper()} {product.name} to your bag'
        )

    request.session['bag'] = bag  # Save the updated bag in session
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')  # All products have sizes
    bag = request.session.get('bag', {})

    # Check if the item and size exist in the bag
    if item_id in bag and size in bag[item_id]['items_by_size']:
        if quantity > 0:
            # Update the quantity for the specific size while keeping the price
            bag[item_id]['items_by_size'][size]['quantity'] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to '
                f'{bag[item_id]["items_by_size"][size]["quantity"]}'
            )
        else:
            # If quantity is 0, remove the size from the bag
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
            )

    # Save the updated bag in session
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


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

            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
            )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {str(e)}')
        return HttpResponse(status=500)

