'''smileyface.py

   Liz Nichols, 2016-10-05
   Draws a smiley face. No guarantees for friendliness.

   Adapted from programs written by Jeff Ondich, and adapted by Jed Yang
   
   Note - this program requires import of the graphics library written by John Zelle 
   for use with the book "Python Programming: An Introduction To Computer Science"

'''

from graphics import *

def eyes(window,y):
	eyeColor= color_rgb(0, 0, 255)
	outlineColor = color_rgb(0,225,0)
	eyeleft = Circle(Point(180,y),25)
	eyeleft.setOutline(eyeColor)
	eyeleft.setFill(eyeColor)
	eyeleft.draw(window)
	
	eyeright=Circle(Point(320, y),25)
	eyeright.setFill(eyeColor)
	eyeright.setOutline(eyeColor)
	eyeright.draw(window)
	
def mouth(window):
	mouthColor=color_rgb(236,101,33)
	mouthMain=Rectangle(Point(150,300), Point(350,350))
	mouthMain.setOutline(mouthColor)
	mouthMain.setFill(mouthColor)
	mouthMain.draw(window)
	
	mouthLeft=Rectangle(Point(100,200), Point(150,350))
	mouthLeft.setFill(mouthColor)
	mouthLeft.setOutline(mouthColor)
	mouthLeft.draw(window)
	
	mouthRight=Rectangle(Point(350,200), Point(400,350))
	mouthRight.setFill(mouthColor)
	mouthRight.setOutline(mouthColor)
	mouthRight.draw(window)

def main():   
	windowWidth = 600
	windowHeight  = 500
	window = GraphWin('Smile', windowWidth, windowHeight)
	backgroundColor = color_rgb(167, 192, 115)
	window.setBackground(backgroundColor)

	try:
		eyes(window, 100)
		mouth(window)

	except ImportError:
		print ("Don't forget the graphics library!")

	print('Click the smile window to quit')
	window.getMouse()
if __name__=='__main__':
	main()


