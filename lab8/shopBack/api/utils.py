

def get_default_category():
    from .models import ProductCategory
    result, _ = ProductCategory.objects.get_or_create(name="default")
    return result
