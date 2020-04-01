#!/usr/bin/env python
# coding: utf-8

# # Joy Ride - Part 3: Parallel Parking
# In this section you will write a function that implements the correct sequence of steps required to parallel park a vehicle.
# 
# NOTE: for this segment the vehicle's maximum speed has been set to just over 4 mph. This should make parking a little easier.
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/2/26/ParallelParkingAnimation.gif)

# If you have never heard of WASD keys, please check out this [link](https://en.wikipedia.org/wiki/Arrow_keys#WASD_keys).
# 
# ## Instructions to get started
# 
# 1. Run the cell below this one by pressing `Ctrl + Enter`.
# 1. Click the button that says "Load Car Simulator". The simulator will appear below the button.
# 1. Run the cell below the simulator, marked `CODE CELL` (hit `Ctrl + Enter`). 
# 1. Try to drive the car using WASD keys. You might notice a problem...
# 1. Press the **Reset** button in the simulator and then modify the code in the `CODE CELL` as per the instructions in TODO comments.
# 1. When you think you've fixed the problem, run the code cell again. 
# 
# #### NOTE - Depending on your computer, it may take a few minutes for the simulator to load! Please be patient.
# 

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<link rel="stylesheet" type="text/css" href="buttonStyle.css">\n<button id="launcher">Load Car Simulator </button>\n<button id="restart">Restart Connection</button>\n<script src="setupLauncher.js"></script><div id="simulator_frame"></sim>\n<script src="kernelRestart.js"></script>')


# In[ ]:


# CODE CELL

# Before/After running any code changes make sure to click the button "Restart Connection" above first.
# Also make sure to click Reset in the simulator to refresh the connection.
# You need to wait for the Kernel Ready message.


car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def control(pos_x, pos_y, time, velocity):
    """ Controls the simulated car"""
    global car_parameters
    
    
    # TODO: Use WASD keys in simulator to gain an intuitive feel of parallel parking.
    # Pay close attention to the time, position, and velocity in the simulator.
    
    # TODO: Use this information to make decisions about how to set your car parameters
    
    # In this example the car will drive forward for three seconds
    # and then backs up until its pos_y is less than 32 then comes to a stop by braking
    if time < 1:
        car_parameters['throttle'] = -1
        car_parameters['steer'] = 0
    elif 39.5 > pos_y > 34.5:
        car_parameters['throttle'] = -1
        car_parameters['steer'] = 1
    elif 34.5 >= pos_y > 31.5:
        car_parameters['throttle'] = -1
        car_parameters['steer'] = -1
    else:
        car_parameters['throttle'] = 0
        car_parameters['brake'] = 1
    
    return car_parameters
    
import src.simulate as sim
sim.run(control)


# # Submitting this Project!
# Your parallel park function is "correct" when:
# 
# 1. Your car doesn't hit any other cars.
# 2. Your car stops completely inside of the right lane.
# 
# Once you've got it working, it's time to submit. Submit by pressing the `SUBMIT` button at the lower right corner of this page.

# In[ ]:


def control(pos_x, pos_y, time, velocity):
    """ Controls the simulated car"""
    global car_parameters
    
    if time < 3:
        car_parameters['throttle'] = 0,5
    elif pos_y > 41 and pos_x < 128:
        car_parameters['throttle'] = -1
    elif pos_y > 36 or pos_x < 125:
        car_parameters['throttle'] = -0,5
        car_parameters['steer'] = 5
    elif pos_y > 32.5:
        car_parameters['throttle'] = -0,2
        car_parameters['steer'] = -5
    else:
        if pos_y < 32:
            car_parameters['steer'] = 0
            car_parameters['throttle'] = 2
        else:
            car_parameters['brake'] = 1
    return car_parameters
import src.simulate as sim
sim.run(control)

