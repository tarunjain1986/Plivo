'''
Created on 22-Oct-2016

@author: tarunjain
'''
import json
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import copy

class Parsers:
  
    def globalTbParser(self):
        
        logger.info("Parsing global Test Bed File")
        self.HOME_PATH = BuiltIn().get_variable_value("${HOME_PATH}", '/Users/tarun/Documents/WorkSpace/Plivo')
        self.URL =  BuiltIn().get_variable_value("${URL}", 'https://manage.plivo.com')
        self.BROWSER =  BuiltIn().get_variable_value("${BROWSER}", 'Firefox');
        logger.info(self.HOME_PATH)
        with open(self.HOME_PATH+ "/Configs/GlobalTb.json","r") as json_data:   
            testbed_data = json_data.read()
            BuiltIn().set_global_variable("${parserFlag}",0)
        try:
            testbed_json = json.loads(json.dumps(json.loads(testbed_data)))
            testbed_json["AutomationServer"]["HOME_PATH"] = self.HOME_PATH
            testbed_json["DesktopBrowser"]["URL"] = self.URL
            testbed_json["DesktopBrowser"]["BROWSER"] = self.BROWSER
            BuiltIn().set_global_variable("${globalTestBed}",testbed_json)
            BuiltIn().set_global_variable("${parserFlag}",1)
        except (ValueError,UnboundLocalError) as e:
            print "Exception is\n"+str(e)
            
    
    def localTbParser(self):
        logger.info("Parsing Local Test Bed File")
        self.suitename = BuiltIn().get_variable_value("${SUITE SOURCE}").split('/')
        self.globaltb = BuiltIn().get_variable_value("${globalTestBed}",None)
        self.references = {}                                    
        with open(self.globaltb["AutomationServer"]["HOME_PATH"]+'/PlivoTests/'+'/'+self.suitename[len(self.suitename)-1].split('.')[0]+'/'+self.suitename[len(self.suitename)-1].split('.')[0]+'.tb',"r") as json_data:
                testbed_data = json_data.read()
      
        try:
            self.ltb =json.loads(json.dumps(json.loads(testbed_data))) 
            for key,value in self.ltb["References"].iteritems():
                if value in self.globaltb.keys():
                    self.references[key] = copy.deepcopy(self.globaltb[value])
                    for lkey,lvalue in self.ltb[key].iteritems():
                        if lkey in self.references[key].keys() or "temp" in lkey:
                            self.references[key][lkey]=lvalue
                        else:
                            raise AssertionError(lkey+" Key Not Exist as in Global Test Bed File")
                else:
                    raise AssertionError(value+" Key Not Exist as in Global Test Bed File")
           
            BuiltIn().set_global_variable("${references}",self.references) 
                   
        except (ValueError,UnboundLocalError) as e:
            print "Exception is\n"+str(e)
            
    def runSetup(self):
        
        if(BuiltIn().get_variable_value("${parserFlag}") != 1):
            self.globalTbParser()
        self.localTbParser()
            

    