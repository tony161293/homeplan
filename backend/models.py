from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=300)
    category_code = models.CharField(max_length=100)
    category_parent = models.ForeignKey('self', blank=True, null=True)
    category_image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_code = models.CharField(max_length=100)
    brand_image = models.ImageField(upload_to='brand')

    def __str__(self):
        return self.brand_name


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_priority = models.IntegerField(default=0)

    def __str__(self):
        return self.group_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_brand = models.ForeignKey(Brand, blank=True, null=True)
    product_category = models.ForeignKey(Category, blank=True, null=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_feature = models.ForeignKey(Group, blank=True, null=True)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.product_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    supplier_person = models.CharField(max_length=100)
    supplier_title = models.CharField(max_length=100)
    supplier_paddress = models.TextField()
    supplier_saddress = models.TextField()
    supplier_city = models.CharField(max_length=100)
    supplier_state = models.CharField(max_length=100)
    supplier_pin = models.IntegerField(default=0)
    supplier_country = models.CharField(max_length=100)
    supplier_phone = models.IntegerField(default=0)
    supplier_fax = models.IntegerField(default=0)
    supplier_email = models.EmailField()
    supplier_url = models.URLField()
    supplier_notes = models.TextField()
    supplier_image = models.ImageField(upload_to='supplier')

    def __str__(self):
        return self.supplier_name


# Vendor order details class
class Vendor(models.Model):
    sales_order_id = models.IntegerField(default=0)
    order_date = models.DateTimeField()
    project_id = models.IntegerField()
    product_id = models.IntegerField()
    product_quality = models.CharField(max_length=400)
    remarks = models.TextField()

    def __str__(self):
        return self.sales_order_id


class VendorOrder(models.Model):
    order_id = models.IntegerField(default=0)
    order_date = models.DateTimeField()
    project_id = models.IntegerField(default=0)

    def __str__(self):
        return self.order_id
