from time import sleep
import datetime
import sys
import os
from os import path
import inspect
import utils.file_utils as file_utils
import utils.mylog as mylog
import utils.jsonprms as jsonprms
from engine import Engine

class Harmo:
    
    def trace(self, stck):
        self.log.lg(f"{stck.function} ({ stck.filename}-{stck.lineno})")

    def init_main(self, jsonfile):
        try:
            self.root_app = os.getcwd()
            self.log = mylog.Log()
            self.log.init(jsonfile)
            self.trace(inspect.stack()[0])
            jsonFn = f"{self.root_app}{os.path.sep}data{os.path.sep}conf{os.path.sep}{jsonfile}.json"
            self.jsprms = jsonprms.Prms(jsonFn)
            self.log.lg("=HERE WE GO=")
            keep_log_time = self.jsprms.prms["keep_log"]["time"]
            keep_log_unit = self.jsprms.prms["keep_log"]["unit"]
            self.log.lg(f"=>clean logs older than {keep_log_time} {keep_log_unit}")
            file_utils.remove_old_files(
                f"{self.root_app}{os.path.sep}log", keep_log_time, keep_log_unit
            ) 
        except Exception as e:
            self.log.errlg(f"Wasted ! : {e}")
            raise

    def main(self, command="", jsonfile="", param1="", param2=""):
        try:
            print(f"params=command={command}, jsonfile={jsonfile}, param1={param1}, param2={param2}")
            self.init_main(jsonfile)
            self.trace(inspect.stack()[0])

            engine = Engine(self.trace, self.log, self.jsprms)
            if command == "test": 
                engine.get_modes_by()               
                # input("Waiting 4 k : ")           
            
        except KeyboardInterrupt:
            print("==Interrupted==")
            pass
        except Exception as e:
            print("GLOBAL MAIN EXCEPTION")
            self.log.errlg(e)
            
        finally:
            print("do disconnect")

    