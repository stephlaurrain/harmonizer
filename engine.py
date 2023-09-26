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

        @_error_decorator()
        def get_mode_idx(self, modes, code_mode):
                # print(modes)                
                for idx_mode, mode in enumerate(modes):
                        if mode['code'] == code_mode:
                                # print(idx_mode)
                                # print(self.jsprms.prms['modes']['musical'][idx_mode]['mode'])
                                return idx_mode                        

        @_error_decorator()
        def get_note_idx(self, notes, code_note):
                # idx_note = 0
                for idx_note, note in enumerate(notes):                
                        if note['code'] == code_note:
                                # print(idx_note)
                                # print(self.jsprms.prms['notes'][idx_note]['code'])
                                return idx_note
                
        @_error_decorator()
        def get_note_input(self, notes):
                lnotes = ''
                for n in notes :
                        lnotes += f"{n['code']} "                
                return input(f'note : ({lnotes}) : ')   

        @_error_decorator()
        def get_mode_input(self, modes):
                lmodes = ''
                for m in modes :
                        lmodes += f"{m['code']} "                
                return input(f'mode : ({lmodes}) : ')   
        

        @_error_decorator()
        def get_modes_by(self):
                self.trace(inspect.stack()[0])
                modes = self.jsprms.prms['modes']['musical']
                notes = self.jsprms.prms['notes']
                code_note = self.get_note_input(notes) 
                code_mode = self.get_mode_input(modes)
                                
                idx_mode = self.get_mode_idx(modes, code_mode)
                idx_note = self.get_note_idx(notes, code_note)
                idx = idx_mode
                idx_c = idx_note
                for i in range(0, len(modes)):                                               
                        print(f"{notes[idx_c]['code']} {modes[idx]['mode']}")
                        # print(modes[idx]['semiton'])
                        # print(notes[idx_c]['code'])
                        idx_c += modes[idx]['semiton']
                        # print(f'{idx_c} = idx_c')
                        if idx_c == len(notes):
                                idx_c-= len(notes)
                        
                        print('#######################')
                        # input()
                        idx+=1
                        if idx == len(modes):
                           idx = 0


                # pdb.set_trace()
                
                
                 
        