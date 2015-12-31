from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^categories/$', views.CategoryList.as_view()),

    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),

    url(r'^brands/$', views.BrandList.as_view()),

    url(r'^brands/(?P<pk>[0-9]+)/$', views.BrandDetail.as_view()),

    url(r'^groups/$', views.GroupList.as_view()),

    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view()),

    url(r'^products/$', views.ProductList.as_view()),

    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),

    url(r'^suppliers/$', views.SupplierList.as_view()),

    url(r'^suppliers/(?P<pk>[0-9]+)/$', views.SupplierDetail.as_view()),

    url(r'^vendordetails/$', views.VendorList.as_view()),

    url(r'^vendordetails/(?P<pk>[0-9]+)/$', views.VendorDetail.as_view()),

    url(r'^vendororders/$', views.VendorOrderList.as_view()),

    url(r'^vendororders/(?P<pk>[0-9]+)/$', views.VendorOrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
