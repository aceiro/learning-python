#! /usr/bin/python
#-*- coding: utf-8 -*-

"""
Script used to parser pump mapping from Penelope's log
Developed by e2a
"""

import argparse
import os

class ArgParserMapping:
	def __init__(self):
		self.parser = argparse.ArgumentParser(
			description='''\
					Script used to parser pump mapping from Penelope's log
					This script use by default /var/log/penelope/maestro-concentrador-client	
					''',
			prog='check-mapping'
		)

		self.parser.add_argument(
			'-c',
			'--controller',
			required=True,
			help='Controller\'s used default: [Company|Eztech]',
			default=['EzTech','Company']
		)

		self.parser.add_argument(
			'-f',
			'--file_log',
			required=False,
			help="File log used by Penelope. Default: /var/log/penelope/maestro-concentrador-client" ,
			default='/var/log/penelope/maestro-concentrador-client'
		)

		self.args = vars(self.parser.parse_args())

	def print_usage(self):
		print('Parameters are not correct')
		self.parser.print_help()

	def is_valid_parameters(self):
		return self.args['controller'] in ['company','eztech']

if __name__ == "__main__":
	parser = ArgParserMapping()
	if (not parser.is_valid_parameters() ):
		parser.print_usage()


