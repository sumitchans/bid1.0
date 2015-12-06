
from django.http import HttpResponseRedirect
import os
import sys
from Djngo.settings import BASE_DIR 
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render_to_response
sys.path.append(os.path.join(BASE_DIR,'bid/business'))
from business.Registration import UserRegister,UserInformation
from business.ItemInfo import *
from django.contrib.auth.models import *
# Create your views here.
from django.http import HttpResponse
from django.template.context_processors import request
from django.template.loader import get_template 
from django.template import Context,Template
from django import template
from bid.main_template_tag import GetStaticFile
from django.contrib import auth
from bid.form import FileUpload
from django.template.context import RequestContext
from bid.ConstantsInfo import ConstantsInfo

def hello(request):
    c={'page_title':ConstantsInfo.main_page}
    return render_to_response(template_name=ConstantsInfo.tem_MainPage,context=c, context_instance=RequestContext(request))
 
def Addforbid(request,Message=None):
    if "username" in request.session:
        return HttpResponseRedirect("/UserLogin/")
    else:
        user_loggedin=False
        UserData=None
        if Message is None:
            UserData=False
        else:
            UserData=True            
        c={'page_title':ConstantsInfo.add_item}
        #return HttpResponse(tem.render(c))
        return render_to_response(template_name=ConstantsInfo.tem_AddforBid,context=c, context_instance=RequestContext(request))
def Sinup(request,UserType):
    p=None
    if UserType=='User':
        if request.method=='POST':
            _name=request.POST["name"]
            _username=request.POST["user_name"]
            _password=request.POST["pwd"]
            _cpassword=request.POST["cpwd"]
            _city=request.POST["address"]
            p= UserRegister().registration(_name, _username,_password,_cpassword, _city)   
    else:
        if request.method=='POST':
            _name=request.POST["name"]
            _username=request.POST["user_name"]
            _password=request.POST["pwd"]
            _cpassword=request.POST["cpwd"]
            _city=request.POST["address"]
            _transortname=request.POST['transport_name']
            _transportreg=request.POST['registration_number']
            p=UserRegister().registration(name=_name, username=_username, password=_password, cpassword=_cpassword,address=_city, transport_name=_transortname, transport_registration_number=_transportreg)
    if p is not None:
            request.session["username"]=_username
            request.session["usertype"]=UserType
            request.session.modified=True
            return HttpResponseRedirect('/UserLogin/')
        
def UserLogin(request):
    username=request.session["username"]
    usertype=request.session["usertype"]
    UserInfo=UserInformation(username,usertype)
    tem=None
    c={}
    c['user_loggedin']=True
    c['UserType']=usertype
    if usertype=="User":
        return render_to_response(template_name=ConstantsInfo.tem_AddforBid, context=c, context_instance=RequestContext(request))
    else:
        c['Item_Info']=AddItem1().running_bid(username,UserInfo.address)
        return render_to_response(template_name=ConstantsInfo.tem_RunningBid,context=c,context_instance=RequestContext(request))


def Login(request):
    if request.method=='POST':
        user_name=request.POST["username"]
        pwd=request.POST["pwd"]
        user=auth.authenticate(username=user_name,password=pwd)
        if user is not None:
            request.session["username"]=user_name
            auth.login(request, user)
            usertype=user.groups.get().__str__()
            request.session["usertype"]=usertype
            request.session.modified=True
            return HttpResponseRedirect('/UserLogin/')
        else:
            return HttpResponse(Addforbid(request,Message=True))
           
def Logout(request):
    auth.logout(request)  
    return HttpResponseRedirect("/hello/")     

def AddItemInfo(request,Confirm=None,Delete=None):
    _userid=request.session['username']
    usertype=request.session['usertype']
    if Confirm is None and Delete is None:
        if request.method=='POST':
            _itnm=request.POST["item_name"]
            _ittype=request.POST['item_type']
            _itdesc=request.POST['item_desc']
            _itimg=request.FILES['image']
            _itprice=request.POST['item_price']
            _itsource=request.POST['source_location']
            _itdestination=request.POST['destination']
            _itclosingdate=request.POST['closing_date']
            _itclosingtime=request.POST['closing_time']
            
            AddItemsInfo=AddItem1().addItem(itname=_itnm,ittype=_ittype,itdesc=_itdesc,itprice=_itprice,ituserid=_userid,
                                       itclosingdate=_itclosingdate,itclosingtime=_itclosingtime,itpic=_itimg,source=_itsource,destination=_itdestination)
            request.session['AddItem']=AddItemsInfo['item_id']
            request.session.modified=True
            c={'AddItemsInfo':AddItemsInfo,'user_loggedin':True,'page_title':ConstantsInfo.confirm_item}
            c['UserName']=UserInformation(username=_userid,usertype=usertype).Name
            c['UserType']=usertype 
            return render_to_response(template_name=ConstantsInfo.tem_ConfirmItemAddition,context=c,context_instance=RequestContext(request))
        
    else:
        if Confirm is not None:
            item_id=request.session['AddItem'] 
        #AddItem1().ConfirmValue(itname=ad['itemname'], ittype=ad['itemtype'], itdesc=ad['itemdesc'], imgpath=ad['itemimgpath'], itprice=ad['item_price'], enddate=ad['end_date'],ituserid=_userid,source=ad['source'],destination=ad['destination'])          
            AddItem1().ConfirmItem(item_id,confirm=True)
            return HttpResponseRedirect('/ConfirmItem/')
        else:
            item_id=request.session['AddItem']
            AddItem1().ConfirmItem(item_id,delete=True)
            return HttpResponseRedirect('/Addforbid/')
            
        
        
def ConfirmItem(request):
    username=request.session['username']
    _userid=request.session['username']
    Item_list=AddItem1().item_info(username)
    usertype=request.session['usertype']
    c={'Item_Info':Item_list,'user_loggedin':True,'page_title':'Added items list'}
    c['UserName']=UserInformation(username=username,usertype=usertype).Name 
    c['UserType']=usertype
    return render_to_response(template_name=ConstantsInfo.tem_AddItemHistory, context=c, context_instance=RequestContext(request))
def RunningBid(request,Message=None):
    userid=None
    running_bid=None
    name=None
    login_js=None
    login_css=None
    if 'username' not in request.session:
        user_loggedin=False  
    else:
        user_loggedin=True
        userid=request.session['username'] 
        usertype=request.session['usertype']   
        place=UserInformation(userid,usertype).address
        name=UserInformation(username=userid,usertype=usertype).Name
        running_bid=AddItem1().running_bid(userid=userid,location=place)
    c={'Item_Info':running_bid,'user_loggedin':True,'page_title':'Running Bid'}
    c['UserName']=name
    c['user_loggedin']=user_loggedin
    c['UserType']=usertype
    c['login_css']=login_css
    return render_to_response(template_name=ConstantsInfo.tem_RunningBid, context=c, context_instance=RequestContext(request))
def BidOnItem(request,item_id,UpdateBid=None):
    user_id=request.session['username']
    usertype=request.session['usertype']
    bidinfo=ItemBidInfo()
    item_info=bidinfo.item_info(item_id)
    item_bid_info=bidinfo.item_bid_info(item_id,usertype)
    c={'user_loggedin':True}
    if UpdateBid==True:
        if request.method=='POST':
            Amount=request.POST['amount']
            ItemBidInfo().bidonitem(item_id=item_id,user_id=user_id,Amount=Amount)
            return HttpResponseRedirect('/BidOnItem/%s' % item_id)      
    c['UserName']=UserInformation(username=user_id,usertype=usertype).Name     
    c['item_id']=item_id    
    c['ItemInfo']=item_info
    c['Item_Bid_Info']=item_bid_info
    c['page_title']='bid on item'
    c['UserType']=usertype
    return render_to_response(template_name=ConstantsInfo.tem_BidOnItem, context=c, context_instance=RequestContext(request))

def AddBidOnItem(request,item_id):
    user_id=request.session['username']
    if request.method=='POST':
        Amount=request.POST['amount']
        ItemBidInfo().bidonitem(item_id=item_id,user_id=user_id,Amount=Amount)
        return HttpResponseRedirect('/BidOnItem/%s' % item_id)
    
def BiddingHistory(request):
    userid=request.session['username']
    usertype=request.session['usertype']
    c={'user_loggedin':True}
    c['Item_Info']=ItemBidInfo().bidding_history(userid)
    c['page_title']='bidding history'
    c['UserType']=usertype
    c['UserName']=UserInformation(username=userid,usertype=usertype).Name  
    return render_to_response(template_name=ConstantsInfo.tem_BiddingHistory, context=c, context_instance=RequestContext(request))

def Exit(request,item_id):
    userid=request.session['username']
    usertype=request.session['usertype']
    c={'user_loggedin':True}
    ItemBidInfo().ExitBid(item_id,userid)
    return HttpResponseRedirect('/BiddingHistory/')
    
    
    
    
    
    
    
    
    
    

     
     
     
     
     
    
    

