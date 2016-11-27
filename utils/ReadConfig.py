# -*- coding: UTF-8 -*- 
'''
utils.ParserConfig is a part of the project bangu.
bangu is an open-source project which follows MVC design pattern mainly based on python.

Copyright (C) 2014 - 2016, Vlon Jang(WeChat:wangqingbaidu)
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China.

The codes are mainly developed by Zhiwei Zhang.
As an open-source project, your can use or modify it as you want.

Contact Info: you can send an email to 564326047@qq.com(Vlon) 
  or visit my website www.wangqingbaidu.cn

Note: Please keep the above information whenever or wherever the codes are used.
'''
import GetBanguHome

import ConfigParser, os
class BanguConfig:
    """
    This class is used to initialize bangu configurations.
    Parameters
    -------------
    @cfgfile: Path to config file.
    
    Functions
    -------------
    @__valid_config: Check all configurations settings.
    @__valid_XXX_section: Check XXX section settings.
    @get_XXX_settings: return XXX section settings.
    """
    def __init__(self, cfgfile = GetBanguHome.getHome(os.getcwd()) + '/bangu.cfg'):
        if not os.path.exists(cfgfile):
            print 'Config file %s read failed!' %cfgfile
            exit()
            
        self.configuration = {}
        cf = ConfigParser.ConfigParser()
        cf.read(cfgfile)
        for sec in cf.sections():
            self.configuration[sec] = {}
            for k, v in cf.items(sec):
                self.configuration[sec][k] = v
        
        self.__valid_config()
        
    def __valid_config(self):
        self.__valid_pins_section()
        self.__valid_weather_pins_section()
        
        
    
    def __valid_pins_section(self):
        if self.configuration.has_key('pins'):
            tmp = {}
            for pin in self.configuration['pins'].keys():
                try:
                    low = self.configuration['pins'][pin].lower()
                    if 0 < int(pin) < 41 and low in ['in', 'out']:
                        tmp[int(pin)] = low
                except:
                    print "Wrong configure of pins %s=%s" %(pin, self.configuration['pins'][pin])
            self.configuration['pins'] = tmp    
            
    def __valid_weather_pins_section(self):        
        if self.configuration.has_key('pins') and self.configuration.has_key('weatherLED'):
            tmp = {}
            for wpin in self.configuration['weatherLED'].keys():
                try:
                    low = wpin.lower()
                    pin = int(self.configuration['weatherLED'][wpin])
                    if not self.configuration['pins'].has_key(pin):
                        self.configuration['pins'][pin] = 'out'
                        print 'pin %d is add to be out' %pin
                    assert self.configuration['pins'][pin] == 'out'
                    tmp[low] = pin
                except:
                    print "Wrong configure of pins %s=%s or this pin is set to be `in`" \
                        %(wpin, self.configuration['weatherLED'][wpin])
            self.configuration['weatherLED'] = tmp    
        
    def get_pins_settings(self):
        return {} if not self.configuration.has_key('pins') else self.configuration['pins']
    
    def get_basic_settings(self):
        return {} if not self.configuration.has_key('basic') else self.configuration['basic']
    
    def get_weather_pins_settings(self):
        return {} if not self.configuration.has_key('weatherLED') else self.configuration['weatherLED']

configurations = BanguConfig()  