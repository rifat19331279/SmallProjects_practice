import os
import sys
from PIL import Image


input_folder=sys.argv[1]
output_folder=sys.argv[2]

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

for i, filename in enumerate(os.listdir(input_folder)):
	img=Image.open(f'{input_folder}/{filename}')
	clean_name=os.path.splitext(filename)[0]
	img.save(f'{output_folder}/{clean_name}.png', 'png')
	print(f'conversion {i+1} done!- {filename}')