import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random as rnd

#Set array
nbs = np.array([[1,0],[0,1],[-1,0],[0,-1]])

#Implement near-near function
def spread_fire(s,L,x,y):
    count = 0
    for nb in range(0,4):
        nx = (x + nbs[nb,0] + L) % L
        ny = (y + nbs[nb,1] + L) % L
        if s[nx,ny] == 1:
            count += 1
            s[nx,ny] = 2
            # Spread the fire recursively
            count += spread_fire(s,L,nx,ny)
    return count

# Change the length acc. 5.12
L = 40
# The chance of growing a new tree
g = 0.1
# The change of a tree being struck by lightning
f = 0.1

#Choose no. steps and itterations
numSteps = 5000
numIterationsPerFrame = 10

# s=0: empty
# s=1: a tree
# s=2: a tree that just caught fire at time t
s = np.zeros((L,L))

# Number of fires for each fire size. Inialized to >0 for log-log plotting.
nc = np.full(L*L,0.1)

#Plotting and Animation
fig = plt.figure()
ax = fig.add_subplot(121)
im = ax.imshow(s, cmap=None, vmin=0, vmax=2, interpolation='nearest')

ay = fig.add_subplot(122)
#ay.set_xlim(0,1)
ay.loglog()

ax.set_position([0.1,0.2,0.5,0.7])
ay.set_position([0.68,0.2,0.28,0.7])
ay.set_ylim(1, numSteps)
plot, = ay.plot(range(0,L*L), nc)

def animate(framenr):
    global L, s
    for it in range(0,numIterationsPerFrame):
        for x in range(0,L):
            for y in range(0,L):
                if s[x,y] == 0:
                    if rnd.random() < g:
                        s[x,y] = 1
                else:
                    if s[x,y] == 1:
                        if rnd.random() < f:
                            s[x,y] = 2
                    else:
                        if s[x,y] == 2:
                            s[x,y] = 3

        for x in range(0,L):
            for y in range(0,L):
                # Spread the fire
                if s[x,y] >= 2:
                    c = spread_fire(s,L,x,y)
                    nc[c] += 1

        # Show last iteration before removing dead trees
        if (it == numIterationsPerFrame - 1):
            im.set_array(s)
            plot.set_data(range(0,L*L), nc)

        # Remove dead trees
        for x in range(0,L):
            for y in range(0,L):
                # Spread the fire
                if s[x,y] == 2:
                    s[x,y] = 0

    return im,ay

anim = animation.FuncAnimation(fig, animate, frames=numSteps//numIterationsPerFrame, interval=25, blit=False, repeat=False)
plt.show()
