from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.add_category, name="add_category"),
    url(r'^brand$', views.add_brand, name="add_brand"),
    url(r'^group$', views.add_group, name="add_group"),
    url(r'^product$', views.add_product, name="add_product"),
    url(r'^supplier$', views.add_supplier, name="add_supplier"),
    url(r'^category_remove/(?P<id>\d+)$', views.remove_category,
        name="remove_category"),
    url(r'^brand_remove/(?P<id>\d+)$', views.remove_brand,
        name="remove_brand"),
    url(r'^group_remove/(?P<id>\d+)$', views.remove_group,
        name="remove_group"),
    url(r'^product_remove/(?P<id>\d+)$', views.remove_product,
        name="remove_product"),
    url(r'^supplier_remove/(?P<id>\d+)$', views.remove_supplier,
        name="remove_supplier"),
]
