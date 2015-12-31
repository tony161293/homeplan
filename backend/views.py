from django.shortcuts import HttpResponseRedirect
from django.template import RequestContext
from backend.forms import *
from django.conf import settings
from backend.models import *
from django.shortcuts import render_to_response
# import pdb


def add_category(request):
    categories = Category.objects.all()
    form = CategoryForm()
    context = RequestContext(request, {'form': form, 'category': categories,
                                       'MEDIA_URL': settings.MEDIA_URL})
    # pdb.set_trace()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = CategoryForm.save(form)
            category_parent = form.cleaned_data['category_parent']
            category_image = form.cleaned_data['category_image']
            category.category_image = category_image
            category.category_parent = category_parent
            category.save()
    else:
        categories = Category.objects.all()
        form = CategoryForm()
        context = RequestContext(request,
                                 {'form': form, 'category': categories,
                                  'MEDIA_URL': settings.MEDIA_URL})
    return render_to_response('backend/index.html', context_instance=context)


def remove_category(request, id):
    Category.objects.get(id=id).delete()
    return HttpResponseRedirect('/backend/')


def add_brand(request):
    brands = Brand.objects.all()
    form = BrandForm()
    context = RequestContext(request, {'form': form, 'brand': brands,
                                       'MEDIA_URL': settings.MEDIA_URL})
    # pdb.set_trace()
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            brand = BrandForm.save(form)
            brand.save()
    else:
        brands = Brand.objects.all()
        form = BrandForm()
        context = RequestContext(request,
                                 {'form': form, 'brand': brands,
                                  'MEDIA_URL': settings.MEDIA_URL})
    return render_to_response('backend/brand.html', context_instance=context)


def remove_brand(request, id):
    Brand.objects.get(id=id).delete()
    return HttpResponseRedirect('/backend/brand')


def add_group(request):
    groups = Group.objects.all()
    form = GroupForm()
    context = RequestContext(request, {'form': form, 'group': groups,
                                       'MEDIA_URL': settings.MEDIA_URL})
    # pdb.set_trace()
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = GroupForm.save(form)
            group.save()
    else:
        group = Group.objects.all()
        form = GroupForm()
        context = RequestContext(request,
                                 {'form': form, 'group': groups,
                                  'MEDIA_URL': settings.MEDIA_URL})
    return render_to_response('backend/group.html', context_instance=context)


def remove_group(request, id):
    Group.objects.get(id=id).delete()
    return HttpResponseRedirect('/backend/group')


def add_product(request):
    products = Product.objects.all()
    form = ProductForm()
    context = RequestContext(request, {'form': form, 'product': products,
                                       'MEDIA_URL': settings.MEDIA_URL})
    # pdb.set_trace()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = ProductForm.save(form)
            product.save()
    else:
        product = Product.objects.all()
        form = ProductForm()
        context = RequestContext(request,
                                 {'form': form, 'product': products,
                                  'MEDIA_URL': settings.MEDIA_URL})
    return render_to_response('backend/product.html', context_instance=context)


def remove_product(request, id):
    Product.objects.get(id=id).delete()
    return HttpResponseRedirect('/backend/product')


def add_supplier(request):
    suppliers = Supplier.objects.all()
    form = SupplierForm()
    context = RequestContext(request, {'form': form, 'supplier': suppliers,
                                       'MEDIA_URL': settings.MEDIA_URL})
    # pdb.set_trace()
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            supplier = SupplierForm.save(form)
            supplier.save()
    else:
        supplier = Supplier.objects.all()
        form = SupplierForm()
        context = RequestContext(request,
                                 {'form': form, 'supplier': suppliers,
                                  'MEDIA_URL': settings.MEDIA_URL})
    return render_to_response('backend/supplier.html',
                              context_instance=context)


def remove_supplier(request, id):
    Supplier.objects.get(id=id).delete()
    return HttpResponseRedirect('/backend/supplier')


def add_vendor(request):
    vendors = Vendor.objects.all()
    form = VendorForm()
    context = RequestContext(request, {'form': form, 'vendor': vendors,
                                       'MEDIA_URL': settings.MEDIA_URL})
    # pdb.set_trace()
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = VendorForm.save(form)
            vendor.save()
    else:
        vendors = Vendor.objects.all()
        form = VendorForm()
        context = RequestContext(request,
                                 {'form': form, 'vendor': vendors,
                                  'MEDIA_URL': settings.MEDIA_URL})
    return render_to_response('backend/vendordetails.html',
                              context_instance=context)


def remove_vendordetail(request, id):
    Vendor.objects.get(id=id).delete()
    return HttpResponseRedirect('/backend/vendordetails')


def add_vendor_order(request):
    vendor_orders = VendorOrder.objects.all()
    form = VendorOrderForm()
    context = RequestContext(request, {'form': form, 'vendor': vendor_orders,
                                       'MEDIA_URL': settings.MEDIA_URL})
    if request.method == 'POST':
        form = VendorOrderForm(request.POST, request.FILES)
        if form.is_valid():
            vendor_orders = VendorOrderForm.save(form)
            vendor_orders.save()
    else:
        vendor_orders = VendorOrder.objects.all()
        form = VendorOrderForm()
        context = RequestContext(request,
                                 {'form': form, 'vendor': vendor_orders,
                                  'MEDIA_URL': settings.MEDIA_URL})
    return render_to_response('backend/vendororder.html',
                              context_instance=context)


def remove_vendororder(request, id):
    VendorOrder.objects.get(id=id).delete()
    return HttpResponseRedirect('/backend/vendororder')


def usercontact(request):
    context = RequestContext(request)
    return render_to_response('backend/usercontact.html', context)
