"""
JustPot <config_file>

Simple TCP honeypot logger

Usage:
JustPot --config FILE

Options:
--config FILE      Path to config options .ini file
-h --help          show this screen
"""
import sys
import configparser
from JustPot import HoneyPot
import logging 
logger  = logging.getLogger(__name__)

config_filepath = 'JustPot.ini'

config = configparser.ConfigParser()
config.read(config_filepath)
ports = config.get('default','ports',raw = True,fallback = '22,88,443,8080,8888,9999,3306')
log_filepath = config.get('default','logfile',raw = True,fallback = '/var/log/JustPot.log')

#ports log file path
logger.info('[*]Ports %s'%ports)
logger.info("[*]logfile %s"%log_filepath)

port_list = []
try:
    ports_list = ports.split(',')
except Exception as e:
    logger.error('[-]Error parsing ports: %s\nExiting',ports)
    sys.exit(1)


honeypot = HoneyPot(ports_list,log_filepath)