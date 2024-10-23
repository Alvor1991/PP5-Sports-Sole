from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Wishlist
from .forms import UserProfileForm
from checkout.models import Order
from products.models import Product

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Fetch the user's orders and wishlist items, regardless of request method
    orders = profile.orders.all()
    wishlist_items = Wishlist.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist_items': wishlist_items,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ View to display the user's past order details """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """ Add a product to the user's wishlist """
    product = get_object_or_404(Product, id=product_id)

    # Check if the product is already in the user's wishlist
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    if created:
        # Adding 'wishlist' tag to the success message
        messages.success(
            request,
            f"{product.name} has been added to your wishlist!",
            extra_tags='wishlist'
        )
    else:
        messages.info(
            request,
            f"{product.name} is already in your wishlist.",
            extra_tags='wishlist'
        )

    return redirect('product_detail', product_id=product_id)


@login_required
def remove_from_wishlist(request, product_id):
    """ Remove a product from the user's wishlist """
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)
    
    if wishlist_item.exists():
        wishlist_item.delete()
        messages.success(request, f"{product.name} has been removed from your wishlist.", extra_tags='wishlist')
    else:
        messages.error(request, f"{product.name} was not found in your wishlist.", extra_tags='wishlist')

    return redirect('profile')
