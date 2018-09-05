import random
import numpy as np

def calculate_pi(num_points):
    inside = 0
    total = num_points

    for i in range(0,total):
        x = random.random()**2
        y = random.random()**2
        if np.sqrt(x + y) < 1:
            inside +=1
        
    return float(4 * inside/total)