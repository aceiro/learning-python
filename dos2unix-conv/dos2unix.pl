#!/usr/local/bin/python3.7
"""
A simple script and library to convert files or strings from dos like
line endings with Unix line line endings.

By e2a / Ref https://realpython.com/read-write-files-python/
"""

import argparse
import os

def str2unix(input_str: str) -> str:
	r"""\
	Converts the string from \r\n line endings to \n

	Parameters
	----------
	input_str
		The string whose line endings will be converted

	Returns
	-------
		Line converted string
	"""
	r_str = input_str.replace('\r\n','\n')
	return r_str

def dos2unix(source_file: str, dest_file: str):
	"""\
	Converts a file that contains Dos like endins into Unix like

	Parameters
	----------
	source_file
		The path to the source file to be converted

	dest_file
		The path to the converted file for output
	"""

	with open(source_file, 'r') as reader:
		dos_content = reader.read()

	unix_content = str2unix(dos_content)

	with open(dest_file, 'w') as writer:
		writer.write(unix_content)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
			description="Script that convert a DOS like file to an Unix like file",
	)
	parser.add_argument(
		'source_file',
		help='The location of the source'
	)

	parser.add_argument(
		'--dest_file',
		help="Location of dest file",
		default=None
	)

	args = parser.parse_args()
	s_file = args.source_file
	d_file = args.dest_file

	if d_file is None:
		file_path, file_extension = os.path.splitext(s_file)
		d_file = f'{file_path}_unix{file_extension}'

	dos2unix(s_file, d_file)

	print __file__
