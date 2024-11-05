from ball import Ball

class Gravity:
	def __init__(self, screen):
		self.screen = screen

		self.balls = []
		for i in range(45):
			self.balls.append(Ball(screen,10,(10,20*i+10),(i/20+2,0),1,0,0,(200,min(i*5,255),200)))
		#screen, rad, pos, vel, elasticity, friction, airResistance, col


	def process(self, keyheld, keypressed):
		for ball in self.balls:
			ball.process()
			if not ball.exist:
				self.balls.remove(ball)


	def display(self):
		for ball in self.balls:
			ball.display()