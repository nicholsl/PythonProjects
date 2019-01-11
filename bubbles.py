'''bubble.py'''

from graphics import *

class Bubble:

	def __init__(self, xPos, yPos, size, velocity):
		self.xPos = xPos
		self.yPos = yPos
		self.size = size
		self.velocity = velocity

		self.bubble = None
		self.highlight = None
		self.makeParts()

	def makeParts(self):
		#Bubble
		self.bubble = Circle(Point(self.xPos, self.yPos), self.size)

		#Highlight
		self.highlight = Circle(Point(self.xPos + self.size/3, self.yPos - self.size/3), self.size/4)
	
	def draw(self, window):
		self.win = window
		self.bubble.draw(self.win)
		self.highlight.draw(self.win)

	def undraw(self):
		self.bubble.undraw()
		self.highlight.undraw()

	def move(self, dx, dy):
		self.xPos = self.xPos + dx
		self.yPos = self.yPos + dy
		self.bubble.move(dx, dy)
		self.highlight.move(dx, dy)

	def step(self):
		if self.yPos < 0:
			self.redraw()
		self.move(0, self.velocity)
	
	def shimmer(self):
		

	def redraw(self):
		self.undraw()
		self.yPos = self.win.getHeight()
		self.makeParts()
		self.draw(self.win)



def test():
	win = GraphWin()
	bubble0 = Bubble(100, 180, 25, -.01)
	bubble0.draw(win)
	bubble1 = Bubble(30, 100, 40, -.04)
	bubble1.draw(win)

	while True:
		bubble0.step()
		bubble1.step()
		if win.checkMouse():
			break

test()