
'''
Rohan Gala
10432287

FE 595
HW 1
Python Refresher

'''

# Importing numpy for creating the graphs
import numpy as np                                    

# Importing matplotlib.pyplot for ploting the graphs 
import matplotlib.pyplot as plt                       


# Taking values from 0 to 360(2pi) for the cycle of sine/cosine.
period = np.arange(0,2*np.pi,0.01)                    

# Sine Graph and Cosine Graph
sine = np.sin(period )
cosine = np.cos(period )                              


# Plotting both the graphs
plt.plot(period , sine , period , cosine)             

# Creating Legends
plt.subplot().legend(['Sine','Cosine'])               #

# Creating X and Y axes
plt.subplot().axhline(y=0, color='k')
plt.subplot().axvline(x=0, color='k')

# Displaying the plot
plt.show()