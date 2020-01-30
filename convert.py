import sys
import subprocess
import pdfkit
inputfile = 'virus_ann.ipynb'
temp_html = inputfile[0:inputfile.rfind('.')]+'.html'
command = 'ipython nbconvert --to html ' + inputfile
subprocess.call(command,shell=True)
print('============success===========')
output_file =inputfile[0:inputfile.rfind('.')]+'.pdf'
pdfkit.from_file(temp_html,output_file)
subprocess.call('rm '+temp_html,shell=True)