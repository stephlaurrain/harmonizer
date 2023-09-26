# -*-coding:utf-8 -*

import os
from os import path
import inspect
from datetime import datetime
import json

from string import Template
#mes libs
import utils.str_utils as str_utils
import utils.file_utils as file_utils
import utils.img_utils as img_utils
from utils.urls import Urls
from utils.mydecorators import _error_decorator

import re   
class Engine:
        
        def __init__(self, trace, log, jsprms):
                self.trace = trace
                self.log = log
                self.jsprms = jsprms                                
                self.root_app = os.getcwd()

        @_error_decorator()
        def get_mins_from_note(self):
                self.trace(inspect.stack()[0])
                note = input('note : (c d e f g a b) : ')                
                alteration = input('alteration : (n # b) : ')
                code_mode = input('mode : (io dor ph lyd mx aeo loc) : ')
                base = self.jsprms.prms['modes']['musical']
                print(base)
                cpt = 0
               
                for b in base:
                        if b['code'] == code_mode:
                                break
                        cpt += 1
                        if cpt == 7: 
                                cpt = 0
                print(cpt)
                print(self.jsprms.prms['modes']['musical'][cpt]['mode'])
                

                 
        