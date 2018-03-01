#coding=utf-8
import os
import zipfile
import chardet
from glob import glob

#genres = ['action', 'adventure', 'animation', 'comedy', 'crime', 'drama', 'fantasy', 'horror', 'romance', 'sci_fi', 'war']
genres = ['action']

if not os.path.exists('decode/'):
	os.makedirs('decode/')

for genre in genres:

	if not os.path.exists('decode/'+genre+'/'):
		os.makedirs('decode/'+genre+'/')

	for filename in glob('unzip/'+genre+'/*.srt'):
		titlelist = filename.split('/')
		title = titlelist[-1].strip('.srt')

		with open(filename, 'rb') as file:#,errors='ignore',encoding='utf-8'

			contents = file.read()
			detect = chardet.detect(contents)
			#print(detect)
			try:
				lines = contents.decode(detect['encoding']).encode("utf8").split(b'\r\n')
				output = b''
				for i in range(len(lines)):
					#print(type(lines[i]))
					for n in range( int(len(lines)/4) ):
						bn = bytes(str(n), encoding = ('utf-8'))
						if lines[i] == bn :
							#print(lines[i])
							#print(lines[i+2])
							output += lines[i+2] + b'\n'
				fout = open('decode/'+genre+'/'+title+'.txt',"wb")
				fout.write( output )
				fout.close()
				print('success          ----- ',detect['encoding'],'---',title)
			except: 
				print('unknown encoding ----- ',detect['encoding'],'---',title)
	print('////////////  Genre: ',genre ,' done!!!\n')

