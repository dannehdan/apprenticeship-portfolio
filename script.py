import os, time
directory = 'projects'
outfilename = './versions/Release-0-Dan-Marshall.md'

with open(outfilename, 'a') as outfile:
  for fname in sorted(os.listdir(directory)):
    print(fname)
    with open(('./' + directory + '/' + fname), 'r') as readfile:
      outfile.write(readfile.read() + '\n\n')