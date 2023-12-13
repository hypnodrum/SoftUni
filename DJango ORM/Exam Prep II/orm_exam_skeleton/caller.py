import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Profile, Product, Order

#from populate_db import populate_model_with_data

# populate_model_with_data(Profile)
# populate_model_with_data(Product)
# populate_model_with_data(Order)


def get_profiles(search_string=None):

    query_name = (Q(full_name__icontains=search_string)
                  |
                  Q(phone_number__icontains=search_string)
                  |
                  Q(email__icontains=search_string))

    if search_string is None:
        return ""

    profile = Profile.objects.filter(query_name).order_by('full_name')

    result = [f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}" for p in profile]
    return "\n".join(result)


def get_loyal_profiles():

    profile = Profile.objects.get_regular_customers()

    result = [f"Profile: {p.full_name}, orders: {p.orders.count()}" for p in profile]

    return "\n".join(result)


def get_last_sold_products():

    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ""

    return f"Last sold products: {', '.join([p.name for p in last_order.products.all()])}"


def get_top_products():
    top_products = Product.objects.annotate(
        num_orders= Count('order')
    ).filter(num_orders__gt=0).order_by('-num_orders', 'name')[:5]

    if not top_products:
        return ""

    result = [f"{tp.name}, sold {tp.num_orders} times" for tp in top_products]
    return f"Top products:\n" + '\n'.join(result)


def apply_discounts():
    discount_orders = Order.objects.annotate(
        products_count = Count('products')
    ).filter(products_count__gt=2, is_completed=False).update(
        total_price=F('total_price') * 0.90)

    return f"Discount applied to {discount_orders} orders."


def complete_order():
    oldest_order = Order.objects.prefetch_related('products').filter(is_completed=False).order_by('creation_date').first()

    if not oldest_order:
        return ""

    for product in oldest_order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False
        product.save()

    oldest_order.is_completed = True
    oldest_order.save()

    return "Order has been completed!"
