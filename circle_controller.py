#! /usr/bin/env python
#| This file is a part of the pyite framework.
#| Copyright 2019, INRIA
#| Main contributor(s):
#| Jean-Baptiste Mouret, jean-baptiste.mouret@inria.fr
#| Eloise Dalin , eloise.dalin@inria.fr
#| Pierre Desreumaux , pierre.desreumaux@inria.fr
#|
#| Antoine Cully, Jeff Clune, Danesh Tarapore, and Jean-Baptiste Mouret.
#|"Robots that can adapt like animals." Nature 521, no. 7553 (2015): 503-507.
#|
#| This software is governed by the CeCILL license under French law
#| and abiding by the rules of distribution of free software.  You
#| can use, modify and/ or redistribute the software under the terms
#| of the CeCILL license as circulated by CEA, CNRS and INRIA at the
#| following URL "http://www.cecill.info".
#|
#| As a counterpart to the access to the source code and rights to
#| copy, modify and redistribute granted by the license, users are
#| provided only with a limited warranty and the software's author,
#| the holder of the economic rights, and the successive licensors
#| have only limited liability.
#|
#| In this respect, the user's attention is drawn to the risks
#| associated with loading, using, modifying and/or developing or
#| reproducing the software by the user in light of its specific
#| status of free software, that may mean that it is complicated to
#| manipulate, and that also therefore means that it is reserved for
#| developers and experienced professionals having in-depth computer
#| knowledge. Users are therefore encouraged to load and test the
#| software's suitability as regards their requirements in conditions
#| enabling the security of their systems and/or data to be ensured
#| and, more generally, to use and operate it in the same conditions
#| as regards security.
#|
#| The fact that you are presently reading this means that you have
#| had knowledge of the CeCILL license and that you accept its terms.
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
