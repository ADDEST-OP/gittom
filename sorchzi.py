"""
	** Sorchzi v0.1 **

	Sorchzi uses the Shodan search engine to get a list of IoT-devices.
	it uses the Shodan-API to save information to text file.

    Copyright (C) 2020  Mikael Nilsson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import shodan
import getopt
import sys
from datetime import datetime

# Preset string and bool
verboseSearch = False
makeFile = False
searchInput = ""


# Help text
def helptext():
	print("""Sorchzi v0.1 Copyright (C) 2020  Mikael Nilsson
This program comes with ABSOLUTELY NO WARRANTY; for details read gpl-3.0.txt.
This is free software, and you are welcome to redistribute it under certain conditions, refer to gpl-3.0.txt.

USEAGE: sorchzi.py [option] {search string}

 -s, --search   Search shodan for stuff!
 -h, --help     Heelp! Do you need help? Call poolia, old swedish joke :)
 -o, --output   Write information to file, named by search tag.
 -v             Show more information.

""")

# GPL licence text
def gpl_licence():
	print("""\nserchzi sends search information to gather it from shodan.io website.
	Copyright (C) 2020  Mikael Nilsson

	This program is free software: you can redistribute it and/or modify 
	it under the terms of the GNU General Public License as published by 
	the Free Software Foundation, either version 3 of the License, or 
	(at your option) any later version.

	This program is distributed in the hope that it will be useful, 
	but WITHOUT ANY WARRANTY; without even the implied warranty of 
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License 
	along with this program.  If not, see <https://www.gnu.org/licenses/>\n""")

# Search through Shodan for IP open to the world
def search_shodan(search_string, b_makefile_option, b_verbose_option):

	# Get time
	time = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')

	# File name
	file_name = "shodan_search_" + str(search_string) + "_" + str(time) + ".txt"

	# *********************************
	# Open and read file for api key
	my_key = open("key", "r").read()
	shodan_api_key = my_key
	api = shodan.Shodan(shodan_api_key)
	# *********************************

	print("Sorchzi starts searching through Shodan...\n")

	# Verbose output
	if b_verbose_option:
		print("Search string: " + str(search_string))
		print("Write to file: " + file_name)

	try:
		# Search through Shodan API
		results = api.search(str(search_string))

		# Show the results
		print("Results found: {}".format(results["total"]))

		# writes to file
		if b_makefile_option:
			f = open(file_name, "a")
			f.write("Results found: {}".format(results["total"]))
			f.write("\n\n")

		# Goes thru list for matched results
		for result in results["matches"]:
			print("IP: {}\n".format(result["ip_str"]))
			if b_verbose_option:
				print(result["data"])
				print("\n")

			# writes to file
			if b_makefile_option:
				f.write('IP: {}\n'.format(result['ip_str']))
				f.write(result['data'])
				f.write('\n\n')

		print('Results found: {}'.format(results['total']))

		# writes to file
		if b_makefile_option:
			f.write('Results found: {}'.format(results['total']))
			f.write('')

	except shodan.APIError as e:
		print('Error: {}'.format(e))

	# close file
	if b_makefile_option:
		f.close()

	exit()


def main(argv):
	global verboseSearch
	global searchInput
	global makeFile

	# Get args and options for command line
	try:
		opts, args = getopt.getopt(argv, "hos:v", ["help", "output", "search="])
	except getopt.GetoptError:
		print("sorchzi.py -s <search string>")
		sys.exit(2)

	# Go through args to find options
	for o, a in opts:
		if o == "-v":
			verboseSearch = True
		elif o == "-h" or o == "--help":
			helptext()
			sys.exit()
		elif o == "-o" or o == "--output":
			makeFile = True
		elif o == "-s" or o == "--search":
			searchInput = a
		else:
			assert False, "unhandled option"

	if searchInput != "":
		search_shodan(searchInput, makeFile, verboseSearch)
	else:
		print("Something went wrong! Did you type it correctly?")
		print("At least type -s {strings to search for} as in this example under.")
		print("USEAGE: sorchzi.py -s <search string>")

if __name__ == "__main__":
	main(sys.argv[1:])
