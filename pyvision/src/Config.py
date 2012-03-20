#!/usr/bin/env  python
#########################################################
#	Name:  	Config.py				#
#	Description:  Handles and loads configfile	#
#########################################################
#  -*- coding: UTF-8 -*-

import os
import logging
import ConfigParser


class  Config(object):
    """ Loads config file """
    configfile=""
    _section = "Server"
    _DEFAULTOPTIONS = "type memory path host user"
    _myoptions = {}

    def __init__(self, configfile):
        logging.debug("Using %s", configfile)
        self.setconfigfile(configfile)

    def setconfigfile(self,configfile):
        self.configfile = configfile

    def get(self, option):
        if self._myoption[option]: 
            return self._myoption[option]
        else:
            return None
    
    def readoptions(self, parser, section):
        try:
            for option in str.split(self._DEFAULTOPTIONS):
                if parser.has_option(section, option):
                    value = parser.get(section, option)
                    self._myoptions[option] = value
                else:
                    logging.info("Option %s not set", option)
            print self._myoptions
        except ConfigParser.NoSectionError as nse:
            logging.error(nse)
 
    def load(self):
        configfile = self.configfile
        if os.path.isfile(configfile):
            logging.warn("Loading configuration from : %s", configfile)
            configparser = ConfigParser.ConfigParser()
            configparser.read(configfile)
            self.readoptions(configparser, self._section)
            
            return True
        else:
            logging.warn("Configuration file %s does not exists", configfile)
            return False
            

