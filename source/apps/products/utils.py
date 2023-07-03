from .models import Product


def update_product_view_counter(product_slug: str) -> int:
    product = Product.objects.get(slug=product_slug)
    product.times_visited =+ 1
    product.save()
    return product.times_visited
