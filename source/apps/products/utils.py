from .models import Product


def update_product_view_counter(product_slug: str) -> int:
    product = Product.objects.get(slug=product_slug)
    product.times_visited += 1
    product.save()
    return product.times_visited


def get_changed_product_fields(old, new) -> dict:
    fields_to_compare = ['is_active', 'sku', 'name', 'price', 'brand']
    differences = {}
    fields_types = {f.name: f.get_internal_type() for f in Product._meta.get_fields()}
    for field in fields_to_compare:
        if fields_types.get(field) == 'DecimalField':
            old_value = str(old.price)
            new_value = str(new.price)
        else:
            old_value = getattr(old, field)
            new_value = getattr(new, field)
        if old_value != new_value:
            differences[field] = {
                'old': old_value,
                'new': new_value
            }
    return differences
