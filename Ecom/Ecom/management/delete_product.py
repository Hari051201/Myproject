from django.core.management.base import BaseCommand
from Ecom import Product

class Command(BaseCommand):
    help = 'Delete a product by its ID'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='Product ID to delete')

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            self.stdout.write(self.style.SUCCESS(f'Product {product_id} deleted successfully'))
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Product {product_id} does not exist'))
