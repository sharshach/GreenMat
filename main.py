#main.py
# //date created : 17 June 2019
# //created by Chilukuri Sri Harsha
# //date last modified :17 June 2019
# //modified by Chilukuri Sri  Harsha
# //
# different values
background='background.jpeg'
foreground='main.png'
final='created.png'
rc='green'#replacing color
hue=60
deviation=20 
# //
import numpy as np
import cv2
low=np.array([hue-deviation,0,0])
high=np.array([hue+deviation,255,255])
bg=cv2.imread(background)
fg=cv2.imread(foreground)
bg=cv2.cvtColor(bg,cv2.COLOR_BGR2HSV)
fg=cv2.cvtColor(fg,cv2.COLOR_BGR2HSV)
i=fg.shape[0]
k=fg.shape[1]
if i>bg.shape[0]:
	i=bg.shape[0]
if k>bg.shape[1]:
	k=bg.shape[1]
while i>0:
	i=i-1
	j=k
	while j>0:
		j=j-1
		if fg[i][j][0]>low[0] and fg[i][j][1]>low[1] and fg[i][j][2]>low[2]:
			if fg[i][j][0]<high[0] and fg[i][j][1]<high[1] and fg[i][j][2]<high[2]:
				fg[i][j]=bg[i][j]

		


				
fg=cv2.cvtColor(fg,cv2.COLOR_HSV2BGR)
cv2.imwrite(final,fg)

