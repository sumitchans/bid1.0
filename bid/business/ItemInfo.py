'''
Created on Oct 4, 2015

@author: sumit
'''
from Djngo.settings import BASE_DIR
from bid.models import *
from datetime import datetime
from itertools import count
from collections import namedtuple
from django.db.models import Max
from bid.business.Registration import UserInformation
from warnings import catch_warnings
from string import upper
from bid.ConstantsInfo import ConstantsInfo
class AddItem1(object):
    itcount=count(0)    
    def addItem(self,itname,ittype,itdesc,itprice,ituserid,itclosingdate,itclosingtime,itpic,source,destination):
        dict={}
        '''
        self.itcount=self.itcount.next()
        
        #self.itcount=self.itcount.next()
        dict['itemname']=itname
        dict['itemtype']=ittype
        dict['itemdesc']=itdesc
        dict['source']=source
        dict['destination']=destination
        dict['itemimg']=itpic
            #dict['itpics']=itpic
        #fl=open(BASE_DIR+'/static/img/'+str(ituserid)+str(self.itcount)+".jpg",'wb+')
        #fl.write(itpic.read())
        #dict['itemimgpath']=str(ituserid)+str(self.itcount)+".jpg"
        dict['item_price']=itprice
        '''
        enddate=str(itclosingdate)+" "+str(itclosingtime)
        item_info=self.ConfirmValue(itname, ittype, itdesc,itpic, itprice, enddate, ituserid, source, destination,bid_confirm=None)
        dict['item_id']=item_info.id
        dict['item_name']=item_info.item_name
        dict['item_type']=item_info.item_type
        dict['item_info']=item_info.item_info
        dict['imgpath']=item_info.item_img_path
        dict['item_location']=item_info.item_location
        dict['item_destination']=item_info.item_destination
        dict['end_date']=item_info.bid_close_time
        dict['bid_start_price']=item_info.bid_start_price
        return dict
    
    def ConfirmValue(self,itname,ittype,itdesc,imgpath,itprice,enddate,ituserid,source,destination,bid_confirm=None):
            us=User_Info.objects.get(user_name=ituserid)
            dt=str(datetime.now().strftime('%d/%m/%Y %H:%M'))
            iteminfo=Item_Info(item_name=itname,item_type=ittype,item_info=itdesc,item_img_path=imgpath
                          ,item_location=upper(source),item_destination=upper(destination),user_id=us,
                              bid_start_time=dt,bid_close_time=enddate,bid_start_price=itprice,is_confirm=False)
            iteminfo.save()
            return iteminfo
    
    def ConfirmItem(self,item_id,confirm=None,delete=None):
        item=Item_Info.objects.filter(id=item_id)
        if confirm is not None:
           item.update(is_confirm=True)
        if delete is not None:
            item.delete()       
            
        
             
    def item_info(self,userid,start_date=None,end_date=None,itemtype=None,item_location=None):
        item_list=Item_Info.objects.all().filter(user_id=userid).filter(is_confirm=True).order_by('bid_start_time')
        if start_date is not None:
            item_list=item_list.objects.get(bid_start_time=start_date)
        if end_date is not None:
            item_list=item_list.objects.get(bid_close_time=end_date).order_by('bid_close_time')
        if itemtype is not None:
            item_list=item_list.objects.get(item_type=itemtype)
        if item_location is not None:
            item_list=item_list.objects.get(item_location=item_location)    
        return  item_list
    
    def running_bid(self,userid,location,start_date=None,end_date=None,itemtype=None):
        running_bid_info=[]
        today=str(datetime.now().strftime('%d/%m/%y %H:%M'))
        bid_info=namedtuple('bid_info','id item_name item_type imgpath item_start_price item_max_price source destination bid_start_date bid_end_date')
        item_list=Item_Info.objects.all().filter(item_location=upper(location)).filter(bid_start_time__lte=today).filter(bid_close_time__gte=today).exclude(user_id=userid).order_by('bid_start_time')
        if start_date is not None:
            item_list=item_list.objects.get(bid_start_time__contains=start_date)
        if end_date is not None:
            item_list=item_list.objects.get(bid_close_time__cotains=end_date)
        if itemtype is not None:
            item_list=item_list.objects.get(item_type=itemtype) 
        for item in item_list:
            id=item.id
            itnm=item.item_name
            ittype=item.item_type
            bidstartdate=item.bid_start_time
            bidclosedate=item.bid_close_time
            bidstartprice=item.bid_start_price
            imgpath=item.item_img_path
            source=item.item_location
            destination=item.item_destination
            itmax=item.bidding_info_set.values('bid_price').filter(item_id=item.id).aggregate(Max('bid_price')).values()[0]
            maxprice=None
            if itmax is not None:
                maxprice=itmax
            else:
                maxprice='bid not started'
            ip=bid_info(id,itnm,ittype,imgpath,bidstartprice,maxprice,source,destination,bidstartdate,bidclosedate)
            running_bid_info.append(ip)
        return running_bid_info

class ItemBidInfo:
    def item_info(self,item_id):
        iteminfo=namedtuple('iteminfo','id item_name item_type item_img_path item_desc bid_start_time bid_close_time bid_start_price source destination')
        item=Item_Info.objects.get(id=item_id)
        user_name=UserInformation(item.user_id_id,"User").Name
        it=iteminfo(item.id,item.item_name,item.item_type,item.item_img_path,item.item_info,item.bid_start_time,item.bid_close_time,item.bid_start_price,item.item_location,item.item_destination)
        return it
    def item_bid_info(self,item_id,usertype):
        bidinfolist=[] 
        bid_info=Bidding_Info.objects.filter(item_id=item_id).order_by('-bid_price')[:10]
        if usertype=="User":
            bid_info_tuple=namedtuple('bid_info_tuple','bidder_name mobileno transportname bid_date bid_price')
            for item in bid_info:
                bidder_info=UserInformation(item.bid_person_id_id,ConstantsInfo.transporter)
                bidder_name=bidder_info.Name
                bidder_transportname=bidder_info.transport_name
                bidder_mobileno=bidder_info.Mobileno
                bid_date=item.bidding_date
                bid_price=item.bid_price
                bi=bid_info_tuple(bidder_name,bidder_mobileno,bidder_transportname,bid_date,bid_price)
                bidinfolist.append(bi)
        else:
            bid_info_tuple=namedtuple('bid_info_tuple','bidder_name transportname bid_date bid_price')
            for item in bid_info:
                bidder_info=UserInformation(item.bid_person_id_id,ConstantsInfo.transporter)
                bidder_name=bidder_info.Name
                bidder_transportname=bidder_info.transport_name
                bid_date=item.bidding_date
                bid_price=item.bid_price
                bi=bid_info_tuple(bidder_name,bidder_transportname,bid_date,bid_price)
                bidinfolist.append(bi)    
        return bidinfolist
    def bidonitem(self,item_id,user_id,Amount):
        bid_item=Bidding_Info.objects.all().filter(item_id=item_id).filter(bid_person_id=user_id)
        today=str(datetime.now().strftime('%d/%m/%Y %H:%M'))
        if bid_item.count()!=0:
            bid_item.update(bid_price=Amount,bidding_date=today)
        else:
            bid_item=Bidding_Info(item_id=Item_Info.objects.all().get(id=item_id),bid_price=Amount,bidding_date=today,bid_person_id=Transporter_Info.objects.all().get(user_name=user_id))
            bid_item.save()
            
    def bidding_history(self,userid,source=None,destination=None,itemtype=None):
        bidding_history=[]
        item_list=None
        #item_info_tuple=namedtuple('item_info_tupe','item_name')
        today=str(datetime.now().strftime('%d/%m/%Y %H:%M'))
        bid_info=namedtuple('bid_info','id item_name item_type imgpath item_start_price  your_price your_bid_date bid_start_date bid_end_date')
        bi=Bidding_Info.objects.all().filter(bid_person_id=userid).filter(is_Exit=False).order_by('-bidding_date')
        if source is not None or destination is not None or itemtype is not None:
            item_list=Item_Info.objects.all()            
            if source is not None:
                item_list=item_list.objects.get(item_location=source)
            if destination is not None:
                item_list=item_list.objects.get(item_destination=destination)
            if itemtype is not None:
                item_list=item_list.objects.get(item_type=itemtype) 
        
        for bit in bi:
            item=bit.item_id 
            item_name=item.item_name
            itemtype=item.item_type
            itemprice=item.bid_start_price
            itimgath=item.item_img_path
            bidstartdate=item.bid_start_time
            bidclose=item.bid_close_time
            yourprice=bit.bid_price
            biddate=bit.bidding_date
            bif=bid_info(bit.item_id_id,item.item_name,itemtype,itimgath,itemprice,yourprice,biddate,bidstartdate,bidclose)
            bidding_history.append(bif)
        return bidding_history
    
    def ExitBid(self,item_id,userid):
        bi=Bidding_Info.objects.filter(item_id=item_id).filter(bid_person_id=userid).update(is_Exit=True)

    
    
            
        
        
        
        
    
           
        