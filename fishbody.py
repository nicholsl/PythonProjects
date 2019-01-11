'''from graphics import*

win = GraphWin()
fishbody = Oval(Point(10,100),Point(150,187.5))
fishbody.draw(win)

fishbodymoved = fishbody.clone(10)
fishbodymoved.move(20,0)
#fishbodymoved.draw(win)

fishtail = Polygon('''

'''pacman.py

   Jed Yang and friends, 2016-10-14

   This is collaboratively written with students over the course of one
   lecture.  I polished up the code a bit after class.  I tried to use as much
   code that people sent me in class as possible.  This really is a group
   effort!

   Read through this code and make sure you understand everything, including
   the question I ask at the bottom about getMouse() versus checkMouse().
'''

from graphics import *

class Pacman:

   def __init__(self, x, y, radius, color, velocity):
      '''Initialize our Pacman.'''
      # Store these arguments as instance variables.
      self.x = x
      self.y = y
      self.radius = radius
      self.color = color
      self.velocity = velocity

      # Create placeholders for primitive graphical elements.  This step is
      # technically unnecessary, but it does provide a way to remind us the
      # list of variables.
      self.head = None
      self.eye = None
      self.mouth = None
      # Populate these placeholders with the graphical elements.
      self.makeParts()

   def makeParts(self):
      '''Create the parts.'''
      # Head
      self.head = Circle(Point(self.x, self.y), self.radius)
      self.head.setFill(self.color)

      # Eye: using fractions of radius to get the proportions constant
      self.eye = Circle(Point(self.x, self.y - self.radius / 2), self.radius / 4)
      self.eye.setFill('black')

      # Mouth
      if self.velocity > 0: # mouth pointing to the right
         self.mouth = Polygon(
            Point(self.x, self.y),
            Point(self.x + self.radius, self.y + self.radius),
            Point(self.x + self.radius, self.y - self.radius))
      else: # mouth pointing to the left
         self.mouth = Polygon(
            Point(self.x, self.y),
            Point(self.x - self.radius, self.y + self.radius),
            Point(self.x - self.radius, self.y - self.radius))
      self.mouth.setFill('black')

   def draw(self, window):
      '''Draw the parts to a window.'''
      self.win = window # Record the window in case we need to refer to it later
      self.head.draw(window)
      self.eye.draw(window)
      self.mouth.draw(window)

   def undraw(self):
      '''Undraw the parts.'''
      self.head.undraw()
      self.eye.undraw()
      self.mouth.undraw()

   def move(self, dx, dy):
      '''Move the parts.'''
      self.x = self.x + dx
      self.y = self.y + dy
      self.head.move(dx, dy)
      self.eye.move(dx, dy)
      self.mouth.move(dx, dy)

   def step(self):
      '''Move based on velocity.  Reverses when we hit the right edge.'''
      if self.x > self.win.getWidth() or self.x < 0:
         self.reverse()     
      self.move(self.velocity, 0)

   def reverse(self):
      '''Reverses the direction.'''
      self.undraw() # remove the old one
      self.velocity = -self.velocity # reverses velocity
      self.makeParts() # this will make new parts with mouth in new direction
      self.draw(self.win)

def testModule():
   '''Demo the module.  When imported, this will not run.'''
   import time

   winHeight = 300
   winWidth = 500
   win = GraphWin('Pacman Module Test', winWidth, winHeight)
   win.setBackground(color_rgb(0,0,0))

   # make a Pacman and draw it in the window
   pac = Pacman(winWidth/2, winHeight/2, 50, color_rgb(255, 255, 0), 10)
   pac.draw(win)

   print('Pacman test.  Click the window to quit.')
   while True:
      # animate the Pacman
      pac.step()
      if win.checkMouse():   # Why do I use checkMouse() instead of getMouse()?
         break
      time.sleep(0.02)
   
if __name__ == '__main__':
   testModule()

