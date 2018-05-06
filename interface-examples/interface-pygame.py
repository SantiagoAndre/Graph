import pygame,sys
from pygame.locals import *
from math import pow

def collision_detection(circle,(newx,newy),circles):
	_,_,sfradius = circle
	for other in circles:
		if other == circle:
			continue
		_,(otx,oty),otradius = other
		mindistance = sfradius + otradius
		if  abs(newx-otx) > mindistance or abs(newy-oty) > mindistance:
			continue
		otpoints = [(x,y) for x in range(otx- otradius, otx + otradius,2) for y  in range(oty- otradius, oty + otradius,2) if pow(x-otx,2) + pow(y-oty,2) == pow(otradius,2)]
		for (otpointx,otpointy) in otpoints:
			if ((pow(otpointx-newx,2) + pow(otpointy-newy,2)) <= pow(sfradius,2)):
				return True
	return False
if __name__ == "__main__":

	#variables
	circles = [((1,2,3),(40,40),40),((1,2,3),(180,40),40),((1,2,3),(260,40),40),((1,2,3),(500,40),40),((1,2,3),(120,600),40),((1,2,3),(120,200),40),((1,2,3),(40,280),40)]
	edges = [(1,3),(1,5),(3,2),(4,5),(6,3),(6,4),(0,5),(0,6),(0,2)]
	black_color = (0,0,0)
	green_color = (0,255,0)
	red_color = (122,2,2)

	pygame.init()
	display = pygame.display.set_mode((800,1000))
	pygame.display.set_caption("Graph")
	display.fill(red_color)
	#show text
	myfont = pygame.font.SysFont('Freesansbold.ttf', 30)
	textsurface = myfont.render('Click on display, please', True, (255,255,255))
	display.blit(textsurface,(0,0))
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		[x,y] = pygame.mouse.get_pos()
		(click,_,_) = pygame.mouse.get_pressed()
		if not click:
			continue

		#clear display 
		pygame.draw.rect(display,red_color,(0,0,800,1000))
		#draw edges
		for (i,f) in edges:
			_,posi,_ = circles[i]
			_,posf,_ = circles[f]
			pygame.draw.line(display,green_color,posi,posf)
		
		for i,circle in enumerate(circles):
			color,(posx,posy), radius = circle
			#mov node
			if ((pow(x-posx,2) + pow(y-posy,2)) < pow(radius,2)) and not collision_detection(circle,(x,y),circles):
				circles[i] = (color,(x,y),radius)
			#draw node
			pygame.draw.circle(display,color,(posx,posy),radius)
		pygame.display.update()

		#myfont = pygame.font.SysFont('Freesansbold.ttf', 30)
		#textsurface = myfont.render('Click on display, please', True, (0, 0, 	0))
		#display.blit(textsurface,(0,0))
		#rotate = "http://programarcadegames.com/python_examples/f.php?lang=es&file=text_rotate.py"
			



