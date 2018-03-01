#coding=utf-8
import os
import zipfile
import codecs
import chardet
import jieba
from glob import glob
import uniout

'''
with open('Edge of Tomorrow.srt', 'rb') as file:#,errors='ignore',encoding='utf-8'

	contents = file.read()
	detect = chardet.detect(contents)
	print(detect)
	print(detect['encoding'])

	lines = contents.decode(detect['encoding']).encode("utf8").split(b'\r\n')
	#print(lines)
	output = b''

	for i in range(len(lines)):
		#print(type(lines[i]))
		for n in range( int(len(lines)/4) ):
			bn = bytes(str(n), encoding = ('utf-8'))
			if lines[i] == bn :
				#print(lines[i])
				#print( lines[i+2])
				output += lines[i+2] + b'\n'


	open('output.txt',"wb").write( output )
'''
s = u'測試'
print( s ) 

f = open('output.txt','r')
print(f)
for line in f:
	s = '測試'
	line = line.strip()
	print( type(s) ) 
'''
file = open('Afanda.srt',errors='ignore')#,errors='ignore'encoding='utf-8'

lines = []


for line in file:
	#print (repr(line))
	lines.append(line.strip())
file.close()
output = ''

j = 1
for i in range(len(lines)):
	if lines[i] == str(j):
		if lines[i+2]:
			#print(lines[i+2])
			output += lines[i+2] +'\n'
		j += 1

print(output)
with open('output.txt', 'w') as the_file:
    the_file.write(output)
'''
