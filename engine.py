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
import pdb

class Engine:
        
        def __init__(self, trace, log, jsprms):
                self.trace = trace
                self.log = log
                self.jsprms = jsprms                                
                self.root_app = os.getcwd()
                self.modes = self.jsprms.prms['modes']['musical']
                self.notes = self.jsprms.prms['notes']

        @_error_decorator()
        def get_mode_idx(self, code_mode):
                # print(modes)                
                for idx_mode, mode in enumerate(self.modes):
                        if mode['code'] == code_mode:
                                # print(idx_mode)
                                # print(self.jsprms.prms['modes']['musical'][idx_mode]['mode'])
                                return idx_mode                        

        @_error_decorator()
        def get_note_idx(self, code_note):
                # idx_note = 0
                for idx_note, note in enumerate(self.notes):                
                        if note['code'] == code_note:
                                # print(idx_note)
                                # print(self.jsprms.prms['notes'][idx_note]['code'])
                                return idx_note
                
        @_error_decorator()
        def get_note_input(self):
                lnotes = ''
                for n in self.notes :
                        lnotes += f"{n['code']} "                
                return input(f'note : ({lnotes}) : ')   

        @_error_decorator()
        def get_mode_input(self):
                lmodes = ''
                for m in self.modes :
                        lmodes += f"{m['code']} "                
                return input(f'mode : ({lmodes}) : ')   
        

        @_error_decorator()
        def get_modes_by(self, code_note, code_mode, tone='none'):
                self.trace(inspect.stack()[0])
                
                idx_mode = self.get_mode_idx(code_mode)
                idx_note = self.get_note_idx(code_note)
                idx = idx_mode
                idx_c = idx_note
                for i in range(0, len(self.modes)):           
                        #print(f'@@@@@@@@@@@@@ idx_c={idx_c} idx={idx}')                                    
                        if tone == 'none' or (tone in ['min', 'max'] and self.modes[idx]['tone'] == tone):
                                print('#######################')
                                print(f"{self.notes[idx_c]['code']} {self.modes[idx]['mode']}")
                        # print(modes[idx]['semiton'])
                        # print(notes[idx_c]['code'])
                        # pdb.set_trace()
                        idx_c += self.modes[idx]['semiton']
                        # print(f'{idx_c} = idx_c')                        
                        if idx_c >= len(self.notes):
                                idx_c-= len(self.notes)
                                # print(f'idx_c = {idx_c}')
                        
                        
                        # input()
                        idx+=1
                        if idx == len(self.modes):
                           idx = 0


                # pdb.set_trace()
                
                
                 
        