#!/usr/bin/env python3

"""
Created Tuesday 5th May 2020
Author Michelle Namuyaba
Group number 6
search.cgi
This CGI scritpt returns a results page with necessary information on a specific gene.
"""

########################################################################################################################


#import python cgi module
import cgi


# Useful debugging output
import cgitb
cgitb.enable()  # Send errors to browser


# Obtaining the content of the html form
form = cgi.FieldStorage()


Accession_ID    = form.getvalue("Accession_ID")
Gene_ID     = form.getvalue("Gene_ID")
Gene_Loci = form.getvalue("Gene_Loci")
Protein_Product  = form.getvalue("Protein_Product")

print ('Content-type: text/html\n')

import os, sys
path = os.path.dirname(sys.argv[0])

# Import configuration information
import config
from config import Mysqlconfig

#import bl api
import blapi



'''
Information on a single gene returned as a table
'''

#import pandas module to convert the dataframe into an html table
import pandas as pd


#creating a variable for getallentries function in the business layer to return information on a single product.
geneinfo=blapi.getAll_Entries()


#converting the information on the single gene that is in dataframe form into an html table
geneinfo_table = geneinfo.to_html()

#testing to see that the variable created is not empty
#print(geneinfo_table)

#creating a variable to display a coding sequence
#exon_dna=blapi.get_exon_seq()
#print(exon_dna)

html  = "<head>"
html += "<title> Chromosome 1 </title>"
html += "</head>"
html += "<body>"
html += "<h1>Gene_ID</h1>\n"
html += "<p align='left'> Gene summary in table form </p>\n"
#rendering the gene information dataframe as an html table
html += "<p align='left'>" + geneinfo_table + "</p>"
html += "<p align='left'>" + exon + "</p>"
html += "<footer>"
html += "<p align='center'> Created by Group 6</p>"
html += "<p align='center'> Biocomouting project</p>"
html += "<p align='center'> PHILIPS Laura</p>"
html += "<p align='center'> NGUYEN Kyvi</p>"
html += "<p align='center'>CHILDS Fran</p>"
html += "<p align='center'>NAMUYABA Michelle</p>"
html += "</footer>"



print (html)
