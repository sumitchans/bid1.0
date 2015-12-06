'''
Created on Sep 26, 2015

@author: sumit
'''
import logging
from cookielib import logger
class GetStaticFile(object):
    
    
    '''
    classdocs
    '''


    def __init__(self, params):
        logger = logging.getLogger(__name__)
        '''
        Constructor
        '''
    @staticmethod 
    def get_static_file_data(path):
        css=None
        fh=None
        try:
            fh=open(path,'r')
            css=fh.read()
        except IOError:
            logger.error("File not Found")
        else:
            fh.close()   
        return css;
    
        
        
        