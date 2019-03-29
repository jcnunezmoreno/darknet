import os
import numpy
import sys 
 
images  = os.listdir(sys.argv[1])
all_image_names = []
for image in images:
	all_image_names.append(os.path.join(sys.argv[1], image))

numpy.savetxt(os.path.join(sys.argv[1], "list.txt"), all_image_names, fmt='%s')

