'''
Created on Oct 2, 2015

@author: sumit
'''
from bid.models import User_Info,Transporter_Info
from django.contrib.auth.models import *
from bid.ConstantsInfo import ConstantsInfo
class UserRegistration(object):  
    def userRegistration(self,username,pwd,fname,mobile,email,add):
        ui=User_Info(user_name=username,name=fname,mobile_number=mobile,email_id=email,address=add)
        ui.save()
        user=User.objects.create_user(username, email,pwd)
        user.is_staff=True
        user.first_name=fname
        user.is_active=True
        user.is_superuser=False
        user.save()
        grp=Group.objects.get(id=ConstantsInfo.user_id);
        grp.user_set.add(user) 
        return ConstantsInfo.user_id
    def transportRegistration(self,username,pwd,fname,mobile,email,add,transportname,transportregnum):
        ti=Transporter_Info(user_name=username,owner_name=fname,Mobile_no=mobile,email_id=email,address=add,transport_name=transportname,registration_number=transportregnum)
        ti.save()
        user=User.objects.create_user(username,email,pwd)
        Group.objects.get(id=ConstantsInfo.transporter_id).user_set.add(user)
        return ConstantsInfo.transporter_id

    
    