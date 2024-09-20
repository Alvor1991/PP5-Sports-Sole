from django.shortcuts import render, redirect

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity', 1))  # default to 1 if not provided
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    # Initialize the product in the bag if it doesn't exist
    if item_id not in bag:
        bag[item_id] = {'items_by_size': {}}

    # Update the quantity for the specified size
    if size in bag[item_id]['items_by_size']:
        bag[item_id]['items_by_size'][size] += quantity
    else:
        bag[item_id]['items_by_size'][size] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

