import math
import matplotlib.pyplot as plt
from matplotlib import animation

# Backend TKAgg seems to always work, while some others do not
import matplotlib
matplotlib.use('TKAgg')

#Initials
roadlength    = 50
numcars       = 12
numframes     = 200

#Storing vec
positions     = []
theta         = []
r             = []
color         = []

#Simulation of traffic acc 4.1
for i in range(numcars):
    positions.append(i*2)
    theta.append(0)
    r.append(1)
    color.append(i)

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.axis('off')

#Animation
def animate(framenr):
    for i in range(numcars):
        positions[i] += 1
        theta[i] = positions[i]*2*math.pi/roadlength

    return ax.scatter(theta, r, c=color),

# Call the animator, blit=True means only re-draw parts that have changed
anim = animation.FuncAnimation(fig, animate,
                               frames=numframes, interval=50, blit=True, repeat=False)

plt.show()
