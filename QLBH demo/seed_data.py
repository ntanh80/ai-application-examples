import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.users.models import CustomUser
from apps.product_groups.models import ProductGroup
from apps.products.models import Product

def seed():
    # 1. Create Admin
    if not CustomUser.objects.filter(username='admin').exists():
        CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='Admin@123',
            full_name='System Administrator',
            role='Admin'
        )
        print("Admin created: admin / Admin@123")
    else:
        print("Admin already exists.")

    # 2. Create Sample User
    if not CustomUser.objects.filter(username='user1').exists():
        CustomUser.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='User@123',
            full_name='Demo User',
            role='User'
        )
        print("User created: user1 / User@123")

    # 3. Create Product Groups
    g1, _ = ProductGroup.objects.get_or_create(group_code='DT', group_name='Điện thoại', description='Các loại điện thoại thông minh')
    g2, _ = ProductGroup.objects.get_or_create(group_code='LT', group_name='Laptop', description='Máy tính xách tay văn phòng và gaming')
    print("Product groups created.")

    # 4. Create Products
    Product.objects.get_or_create(
        product_code='IP15',
        product_name='iPhone 15 Pro Max',
        product_group=g1,
        price=32000000,
        quantity=50,
        description='Siêu phẩm mới nhất từ Apple'
    )
    Product.objects.get_or_create(
        product_code='S24',
        product_name='Samsung Galaxy S24 Ultra',
        product_group=g1,
        price=28000000,
        quantity=30,
        description='Đỉnh cao công nghệ AI'
    )
    Product.objects.get_or_create(
        product_code='MACM3',
        product_name='MacBook Pro M3',
        product_group=g2,
        price=45000000,
        quantity=15,
        description='Hiệu năng vượt trội cho đồ họa'
    )
    print("Products created.")

    # 5. Create Purchase Invoices
    from apps.purchase_invoices.models import PurchaseInvoice, PurchaseInvoiceDetail
    from apps.sales_invoices.models import SalesInvoice, SalesInvoiceDetail
    
    p1 = Product.objects.get(product_code='IP15')
    p2 = Product.objects.get(product_code='S24')
    p3 = Product.objects.get(product_code='MACM3')

    # Purchase Invoice 1
    inv_p1, created = PurchaseInvoice.objects.get_or_create(
        invoice_number='PN001',
        defaults={'supplier_name': 'Apple Vietnam', 'note': 'Nhập hàng đợt 1'}
    )
    if created:
        PurchaseInvoiceDetail.objects.create(invoice=inv_p1, product=p1, quantity=10, unit_price=28000000, amount=280000000)
        PurchaseInvoiceDetail.objects.create(invoice=inv_p1, product=p3, quantity=5, unit_price=40000000, amount=200000000)
        inv_p1.total_amount = 480000000
        inv_p1.save()
        print("Purchase invoice PN001 created.")

    # Purchase Invoice 2
    inv_p2, created = PurchaseInvoice.objects.get_or_create(
        invoice_number='PN002',
        defaults={'supplier_name': 'Samsung Store', 'note': 'Nhập hàng bổ sung'}
    )
    if created:
        PurchaseInvoiceDetail.objects.create(invoice=inv_p2, product=p2, quantity=20, unit_price=24000000, amount=480000000)
        inv_p2.total_amount = 480000000
        inv_p2.save()
        print("Purchase invoice PN002 created.")

    # 6. Create Sales Invoices
    admin_user = CustomUser.objects.get(username='admin')
    
    inv_s1, created = SalesInvoice.objects.get_or_create(
        invoice_number='PX001',
        defaults={'customer_name': 'Nguyễn Văn A', 'note': 'Khách quen', 'staff': admin_user}
    )
    if created:
        SalesInvoiceDetail.objects.create(invoice=inv_s1, product=p1, quantity=2, unit_price=32000000, amount=64000000)
        inv_s1.total_amount = 64000000
        inv_s1.save()
        print("Sales invoice PX001 created.")

    inv_s2, created = SalesInvoice.objects.get_or_create(
        invoice_number='PX002',
        defaults={'customer_name': 'Trần Thị B', 'note': 'Bán lẻ', 'staff': admin_user}
    )
    if created:
        SalesInvoiceDetail.objects.create(invoice=inv_s2, product=p3, quantity=1, unit_price=45000000, amount=45000000)
        inv_s2.total_amount = 45000000
        inv_s2.save()
        print("Sales invoice PX002 created.")

if __name__ == '__main__':
    seed()
