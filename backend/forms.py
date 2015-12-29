from django import forms
from backend.models import *


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['category_parent'].required = False

    category_parent = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label='None')
    category_image = forms.ImageField()

    class Meta:
        model = Category
        fields = ('category_name', 'category_code',)


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ('brand_name', 'brand_code', 'brand_image',)


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('group_name', 'group_priority',)


class ProductForm(forms.ModelForm):

    product_brand = forms.ModelChoiceField(
        queryset=Brand.objects.all())
    product_category = forms.ModelChoiceField(
        queryset=Category.objects.all())
    product_feature = forms.ModelChoiceField(
        queryset=Group.objects.all())

    class Meta:
        model = Product
        fields = ('product_name', 'product_description',
                  'product_price', 'product_image',)


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('supplier_name', 'supplier_person', 'supplier_title',
                  'supplier_paddress', 'supplier_saddress', 'supplier_city',
                  'supplier_state', 'supplier_pin', 'supplier_country',
                  'supplier_phone', 'supplier_fax', 'supplier_email',
                  'supplier_url', 'supplier_notes', 'supplier_image',)
