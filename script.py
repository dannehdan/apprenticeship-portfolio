import os, time
from re import search
projectdirectory = 'projects'
headerdirectory = 'headers'
outfilename = './versions/Release-1-Dan-Marshall.md'


def create_contents():
  with open('./headers/2-contents.md', 'w') as outfile:
    for fname in sorted(os.listdir(projectdirectory)):
      with open(('./' + projectdirectory + '/' + fname), 'r') as readfile:
        lines = readfile.readlines()
        for line in lines:
          if line.find('#') != -1:
            output = line.replace(' ','- ', 1)
            output = output.replace('#','',1)
            output = output.replace('#','\t')
            outfile.write(output)

def create_body():
  with open('./headers/3-body.md', 'w') as outfile:
    for fname in sorted(os.listdir(projectdirectory)):
      print(fname)
      with open(('./' + projectdirectory + '/' + fname), 'r') as readfile:
        outfile.write(readfile.read() + '\n\n')

def create_full_version():
  with open(outfilename, 'w') as outfile:
    for fname in sorted(os.listdir(headerdirectory)):
      print(fname)
      with open(('./' + headerdirectory + '/' + fname), 'r') as readfile:
        outfile.write(readfile.read() + '\n\n')



def generate_version():
  create_contents()
  create_body()
  create_full_version()

generate_version()