'''
Created on Oct 3, 2015

@author: sumit
'''
from django import forms
class FileUpload(forms.Form):
    file=forms.FileField()
    
    