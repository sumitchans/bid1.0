from django.db import models,connection
#from django.template.defaultfilters import default
from datetime import datetime
# Create your models here.


class User_Info(models.Model):
    user_name=models.CharField(max_length=255,primary_key=True)
    name=models.CharField(max_length=255)
    mobile_number=models.CharField(max_length=13,blank=True)
    email_id=models.CharField(max_length=255,blank=True)
    address=models.CharField(max_length=255)
    
class Transporter_Info(models.Model):
    user_name=models.CharField(max_length=255,primary_key=True)
    owner_name=models.CharField(max_length=255)
    Mobile_no=models.CharField(max_length=13,blank=True)
    email_id=models.CharField(max_length=255,blank=True)
    transport_name=models.CharField(max_length=255)
    registration_number=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
            
class Item_Info(models.Model):
    item_name=models.CharField(max_length=255)
    item_type=models.CharField(max_length=255)
    item_info=models.CharField(max_length=255)
    item_img_path=models.ImageField(upload_to='item')
    item_location=models.CharField(max_length=255)
    item_destination=models.CharField(max_length=255)
    user_id=models.ForeignKey(User_Info)
    bid_start_time=models.CharField(max_length=20)
    bid_close_time=models.CharField(max_length=20)
    bid_start_price=models.DecimalField(max_digits=60,decimal_places=2)
    is_confirm=models.BooleanField(default=False)
class Bidding_Info(models.Model):
    item_id=models.ForeignKey(Item_Info)
    bid_price=models.DecimalField(max_digits=60,decimal_places=2);
    bid_person_id=models.ForeignKey(Transporter_Info)
    bidding_date=models.CharField(max_length=20);
    is_Exit=models.BooleanField(default=False) 
    
    




    
        
    
    
     
    
    
'''
Created on Oct 17, 2015

@author: sumit
'''
