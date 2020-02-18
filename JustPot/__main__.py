"""
JustPot <config_file>

Simple TCP honeypot logger

Usage:
JustPot --config FILE

Options:
--config FILE      Path to config options .ini file
-h --help          show this screen
"""
import configparser
#config_filepath = 'etc/JustPot.ini'
config_filepath = 'JustPot.ini'

config = configparser.ConfigParser()
config.read(config_filepath)
ports = config.get('default','ports',raw = True,fallback = '22,88,443,8080,8888,9999,3306')
log_filepath = config.get('default','logfile',raw = True,fallback = '/var/log/JustPot.log')

#ports log file path
print('[*]Ports %s'%ports)
print("[*]logfile %s"%logfile)

try:
    ports_list = ports.split(',')
except Exception as e:
    print('Error parsing ports: %s',ports)


HoneyPot(ports_list,log_filepath)