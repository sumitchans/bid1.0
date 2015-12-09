"""Djngo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from bid.views import *
from Djngo import settings
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello),
     url(r'^hello/$', hello),
    url(r'^Addforbid/$',Addforbid),
    url(r'^Sinup/(\w+)$',Sinup),
     url(r'^UserLogin/$',UserLogin),
     url(r'^Login/$',Login),
     url(r'^LoginUser/$',LoginUser),
       url(r'^Logout/$',Logout),
       url(r'^AddItemInfo/$',AddItemInfo),
       url(r'^Confirm/$',AddItemInfo,{'Confirm':True}), 
    url(r'^Reset/$',AddItemInfo,{'Delete':True}),
       url(r'^ConfirmItem/$',ConfirmItem),
       url(r'^RunningBid/$',RunningBid),
       url(r'^BidOnItem/(\d+)$',BidOnItem),
       url(r'^BidOnUserItem/(\d+)$',BidOnItem,{'UsersItem':True}), 
       url(r'^AddBidOnItem/(\d+)$',AddBidOnItem),
       url(r'^BiddingHistory/$',BiddingHistory),
        url(r'^Exit/(\d+)$',Exit),      
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
