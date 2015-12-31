from backend.models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryList(APIView):
    def get(self, request, format=None):
        cateogries = Category.objects.all()
        serializer = CategorySerializer(cateogries, many=True)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cateogry = self.get_object(pk)
        serializer = CategorySerializer(cateogry)
        return Response(serializer.data)


class BrandList(APIView):
    def get(self, request, format=None):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)


class BrandDetail(APIView):
    def get_object(self, pk):
        try:
            return Brand.objects.get(id=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)


class GroupList(APIView):
    def get(self, request, format=None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)


class GroupDetail(APIView):
    def get_object(self, pk):
        try:
            return Group.objects.get(id=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class SupplierList(APIView):
    def get(self, request, format=None):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)


class SupplierDetail(APIView):
    def get_object(self, pk):
        try:
            return Supplier.objects.get(id=pk)
        except Supplier.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        supplier = self.get_object(pk)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)


class VendorList(APIView):
    def get(self, request, format=None):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)


class VendorDetail(APIView):
    def get_object(self, pk):
        try:
            return Vendor.objects.get(id=pk)
        except Vendor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)


class VendorOrderList(APIView):
    def get(self, request, format=None):
        vendororders = VendorOrder.objects.all()
        serializer = VendorOrderSerializer(vendororders, many=True)
        return Response(serializer.data)


class VendorOrderDetail(APIView):
    def get_object(self, pk):
        try:
            return VendorOrder.objects.get(id=pk)
        except VendorOrder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vendororder = self.get_object(pk)
        serializer = VendorOrderSerializer(vendororder)
        return Response(serializer.data)
