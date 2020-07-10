#!/usr/bin/env python3

"""
Created Tuesday 5th May 2020
Author Michelle Namuyaba
Group number 6
Listall.cgi
This CGI script obtains all the entries from the BL layer and formats them for
HTML display as a table. The table displayed is a summary table of all gene entries. The format obtained from the business layer is a dataframe.
'''
########################################################################################################################
#import python cgi module
import cgi
# Useful debugging output
import cgitb
cgitb.enable()  # Send errors to browser
print ('Content-type: text/html\n')
import os, sys
path = os.path.dirname(sys.argv[0])
# Import configuration information
import config
from config import Mysqlconfig
#import business layer api
import blapi
#import pandas module to convert the dataframe from the business layer into an html table.
import pandas as pd
###########################################################################################################################
#creating a variable for the summary table
summary_info=blapi.get_summary_table()
#converting the summary table dataframe to an html table
#https://pythonexamples.org/pandas-render-dataframe-as-html-table/
summaryinfo_table = summary_info.to_html()
#testing that the variable is functioning
#print(summaryinfo_table)
###########################################################################################################################
#html code to generate webpage
html  = "<head>"
html += "<title> Chromosome 1 </title>"
html += "</head>"
html += "<body>"
html += "<h1>SUMMARY TABLE</h1>\n"
html += "<p align='left'> Summary table for all gene entries.</p>\n"
html += "<p align='left'>" + summaryinfo_table + "</p>"
html += "<footer>"
html += "<p align='center'> Created by Group 6</p>"
html += "<p align='center'> Biocomputing project</p>"
html += "<p align='center'> PHILIPS Laura</p>"
html += "<p align='center'> NGUYEN Kyvi</p>"
html += "<p align='center'>CHILDS Fran</p>"
html += "<p align='center'>NAMUYABA Michelle</p>"
html += "</footer>"



print (html)
