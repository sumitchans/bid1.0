import sys
import os
from Djngo.settings import BASE_DIR
from bid.data.UserInfo import UserRegistration
#sys.path.append(os.path.join(BASE_DIR,'bid/data'))
#sys.path.append(os.path.join(os.path.dirname(__file__),'data'))
from bid.models import *
from django.contrib.auth import *
#from bid.UserInfo import UserRegistration
import re

import re
#from email.utils import parseaddr
class UserRegister(object):
    def registration(self,name,username,password,cpassword,address,transport_name=None,transport_registration_number=None):
        _name=name
        _username=username
        _mobile=''
        _email=''
        if self.isMobile(username):
            _mobile=username
        else:
            _email=username
        _city=address
        _transportname=transport_name
        _transportregnumber=transport_registration_number
        if _transportname is None and _transportregnumber is None:
             usertype=UserRegistration().userRegistration(_username,password,_name,_mobile,_email,_city)
             return usertype
        else:
            usertype=UserRegistration().transportRegistration(username=_username, pwd=password, fname=_name,
                    mobile=_mobile, email=_email, add=_city, transportname=_transportname, transportregnum=_transportregnumber)
            return usertype
    
    def isMobile(self,user):
        username=str(user)
        if username.isdigit():
            if (len(username)==10) and int(username[0])>=7 and int(username[0])<=9:
                return 1
        else:
            return 0
       
        

class UserInformation:
    User_Name=None
    Mobileno=None
    Name=None
    address=None
    email=None
    transport_name=None
    
    def __init__(self,username,usertype):
        if usertype=="User":
            ui=User_Info.objects.get(user_name=username)
            self.User_Name=ui.user_name
            self.Mobileno=ui.mobile_number
            self.Name=ui.name
            self.address=ui.address
            self.email=ui.email_id
        else:
            ti=Transporter_Info.objects.get(user_name=username)
            self.User_Name=ti.user_name
            self.Mobileno=ti.Mobile_no
            self.Name=ti.owner_name
            self.address=ti.address
            self.email=ti.email_id
            self.transport_name=ti.transport_name
  

        