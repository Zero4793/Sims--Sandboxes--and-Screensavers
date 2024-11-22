from util.ball import Ball
import random

class Gravity:
	def __init__(self, screen, _):
		self.screen = screen

		self.balls = []
		for i in range(16):
			self.balls.append(Ball(screen,
						  pos=(random.randint(0,screen.get_width()), random.randint(0,screen.get_height())),
						  vel=(random.uniform(-5,5), random.uniform(-5,5)),
						  bodyGrav=1,
						  repel=100,
						  spaceJelly=0,
						  collide=True,
						  elasticity=0.5,
						  radius = random.randint(10,20)
						  ))


	def process(self, keyheld, keypressed):
		for ball in self.balls:
			for other in self.balls:
				if ball == other: continue
				ball.force(other)
		for ball in self.balls:
			ball.process()
			ball.wallCollide()
			if not ball.exist:
				self.balls.remove(ball)


	def display(self):
		for ball in self.balls:
			ball.display()