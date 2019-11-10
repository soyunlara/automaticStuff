#Se puede mejorar enormemente

import os
downloadsFolder = 'E:\\Descargas\\One Piece\\'
folders = os.listdir(downloadsFolder)
for f in  folders:
	n_files = len(os.listdir(downloadsFolder+f))
	if n_files == 0:
	    print(f[13:63]+" -> Empty One")
	else: 
	    print(f[13:63]+" -> All Good. Files found: %d" % n_files)