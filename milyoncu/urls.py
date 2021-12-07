from django.conf.urls import url
from milyoncu.views import *
from milyoncu.api import ProductAddView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^sweatbands/', SweatbandsView.as_view(), name='sweatbands'),

    url(r'^headbands/', HeadbandsView.as_view(), name='headbands'),

    url(r'^bandanas/', BandanasView.as_view(), name='bandanas'),

    url(r'^balloons/', BalloonsView.as_view(), name='balloons'),

    url(r'^tablecovers/', TableCoversView.as_view(), name='tablecovers'),

    url(r'^coasters/', CoastersView.as_view(), name='coasters'),

    url(r'^cart/', CartView.as_view(), name='cart'),

    url(r'^(?P<id>[0-9]+)/delete$', Delete.as_view(), name='delete'),

    url(r'^post/new/', post_new, name='post_new'),

    url(r'^allproducts/', AllProducts.as_view(), name='allproducts'),

    url(r'^api/v1/add', ProductAddView.as_view(), name='allproducts'),

    url(r'^(?P<slug>[\w-]+)/', Preview.as_view(), name='preview'),


]

