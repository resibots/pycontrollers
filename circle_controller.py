import numpy as np
import math


class CircleController:
	def __init__(self, params, array_dim=100):
		self.array_dim = array_dim
		self.trajs = self._compute_minitaur_trajs(params, array_dim)

	def step(self, t):
		return self.trajs[:, math.floor(t%self.array_dim)]

	def _compute_minitaur_trajs(self, p, array_dim):
		trajs = np.zeros((8, array_dim))
		k = 0
		for i in range(0, 4*2, 2):
			trajs[k,:] = self._cos(p[i],p[i+1],array_dim)
			trajs[k+1,:] = self._sin(p[i],p[i+1],array_dim)
			k += 2
		return trajs

	def _cos(self, amplitude, phase, array_dim=100):
		command = np.zeros(array_dim)
		for i in range(0, array_dim):
			command[i] = amplitude*math.cos(i + phase)
		return command
	def _sin(self, amplitude, phase, array_dim=100):
		command = np.zeros(array_dim)
		for i in range(0, array_dim):
			command[i] = amplitude*math.sin(i + phase)
		return command

if __name__ == "__main__":
	controller = CircleController([1,0,2,0,3,0,4,0])
	for i in range(0, 20000):
		traj = controller.step(i)
		print(traj[7])
