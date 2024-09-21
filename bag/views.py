from django.shortcuts import render, redirect, reverse, HttpResponse

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')  # Size should always be present for your case
    bag = request.session.get('bag', {})

    # Check if the item already exists in the bag
    if item_id in bag:
        # Ensure that bag[item_id] is always a dictionary with 'items_by_size'
        if isinstance(bag[item_id], int):
            # If it was mistakenly stored as an int, convert it to the correct structure
            bag[item_id] = {'items_by_size': {}}
    else:
        # Initialize the product in the bag as a dictionary with 'items_by_size'
        bag[item_id] = {'items_by_size': {}}

    # Update the quantity for the specified size
    if size in bag[item_id]['items_by_size']:
        bag[item_id]['items_by_size'][size] += quantity
    else:
        bag[item_id]['items_by_size'][size] = quantity

    # Save the updated bag in the session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')  # Size is always expected
    bag = request.session.get('bag', {})

    if item_id in bag and size in bag[item_id]['items_by_size']:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = request.POST['product_size']  # Size is always expected
        bag = request.session.get('bag', {})

        if item_id in bag and size in bag[item_id]['items_by_size']:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

