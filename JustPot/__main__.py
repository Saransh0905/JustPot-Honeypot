"""
JustPot <config_file>

Simple TCP honeypot logger

Usage:
JustPot <config_filepath>

Options:
<config_filepath>  Path to config options .init file
-h --help          show this screen
"""

from docpot import docpot 
args = docpot(__doc__)

print('Config file: %s',args['<config_filepaths>'])


