from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        
        if isinstance(item_data, int):
            # Handle legacy case where quantity is stored as an int
            price = Decimal(product.price)
            quantity = item_data
            subtotal = price * quantity
            total += subtotal
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'price': price,
                'subtotal': subtotal,
            })
        else:
            # Handle new case with items by size
            for size, size_data in item_data['items_by_size'].items():
                price = Decimal(size_data['price'])  # Get price from session
                quantity = size_data['quantity']
                subtotal = price * quantity
                total += subtotal
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'price': price,
                    'subtotal': subtotal,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
