from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from inventory.models import ProductGroup, Product
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed initial data for the project'

    def handle(self, *args, **kwargs):
        # 1. Create Admin
        if not CustomUser.objects.filter(username='admin').exists():
            CustomUser.objects.create_superuser(
                username='admin',
                password='Admin@123',
                email='admin@skygate.com',
                full_name='System Admin',
                role='Admin'
            )
            self.stdout.write(self.style.SUCCESS('Created Admin: admin / Admin@123'))

        # 2. Create Sample User
        if not CustomUser.objects.filter(username='user1').exists():
            CustomUser.objects.create_user(
                username='user1',
                password='User@123',
                email='user1@example.com',
                full_name='Regular User',
                role='User'
            )
            self.stdout.write(self.style.SUCCESS('Created User: user1 / User@123'))

        # 3. Create Product Groups
        laptop_group, _ = ProductGroup.objects.get_or_create(
            group_code='LAP01',
            defaults={'group_name': 'Laptop', 'description': 'Các loại máy tính xách tay'}
        )
        phone_group, _ = ProductGroup.objects.get_or_create(
            group_code='PHN01',
            defaults={'group_name': 'Điện thoại', 'description': 'Các loại điện thoại di động'}
        )
        self.stdout.write(self.style.SUCCESS('Created Product Groups'))

        # 4. Create Products
        if not Product.objects.filter(product_code='L001').exists():
            Product.objects.create(
                product_code='L001',
                product_name='MacBook Pro M3',
                product_group=laptop_group,
                price=45000000,
                quantity=10,
                description='Chip M3 cực mạnh'
            )
            Product.objects.create(
                product_code='L002',
                product_name='Dell XPS 13',
                product_group=laptop_group,
                price=35000000,
                quantity=5,
                description='Siêu mỏng nhẹ'
            )
            Product.objects.create(
                product_code='P001',
                product_name='iPhone 15 Pro',
                product_group=phone_group,
                price=28000000,
                quantity=20,
                description='Titanium design'
            )
            self.stdout.write(self.style.SUCCESS('Created Sample Products'))
