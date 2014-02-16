#!/usr/bin/env python
import sys
import re
import commands
import os.path

target = 'result.mp4'
starti = 1
if not os.path.isfile(sys.argv[1]):
	target = sys.argv[1]
	starti = 2
if os.path.isfile(target):
	print target + " already exists"
	sys.exit(-1)
print ">> saving result as: " + target

files = sys.argv[starti:]
if len(files) <= 1:
	print "not enough mp4 file provided to merge"
	sys.exit(-1)
# 1 - 2 - 1-2 Prerequisites.mp4 
def coursera(x):
	x = re.sub(r'^\D*', '', x)
	a, b, c = re.split(r'\W*', x, 2)
	return int(a)*100 + int(b)

def q(x):
	return re.sub(r'\'', '\'\\\'\'', x)

files.sort(key=coursera)
print "\n".join(files)
cmd = "/Applications/Avidemux2.6.app/Contents/Resources/bin/avidemux --load '" + q(files[0])
for x in files[1:]:
	cmd = cmd + "' --append '" + q(x)
cmd = cmd + "' --output-format mp4v2 --save '" + target + "' --quit"
#cmd = cmd + "' --video-codec FFmpeg4 --output-format MP4 --save result.mp4 --quit"

#print cmd

commands.getoutput(cmd)
