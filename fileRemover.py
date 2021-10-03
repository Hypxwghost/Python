from os import listdir, remove
from PIL import Image

mypath = input('Directory: ')
opt = int(input('''Delete files by:
					[1] - Size
					[2] - Coming soon
					[3] - Coming soon
					[4] - Coming soon
					[5] - Coming soon
				'''))

img_list = []
width_list = []
height_list = []
count = 0

if opt == 1:
	height = int(input('Min height: '))
	width = int(input('Min width: '))
	
	for image in listdir(mypath):
		img_list.append(image)
		width_list.append(Image.open(mypath+image).width)
		height_list.append(Image.open(mypath+image).height)
	print('Images done\n')

	for x in width_list:
		if x < width:
			remove(mypath+img_list[count])
			del height_list[count]
		count += 1
	count = 0
	print('Widht done\n')

	for x in height_list:
		if x < height:
			remove(mypath+img_list[count])
		count += 1
	count = 0
	print('All done\n')
