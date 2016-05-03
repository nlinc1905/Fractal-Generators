'''
A script to generate the Julia set
'''

import numpy as np
import pygame as pg

def set_color (iters):
    
    '''
    This function takes the iteration number as input and
    outputs a RGB color value.

    Play with the thresholds to find best results.
    Hardcoded threshold values copied/stolen from here:
    http://fractalart.gallery/mandelbrot-set-in-python-pygame
    God bless you for finding these and sparing me hours of work.
    '''

    v = 765*iters/200
    if v > 510:
        return (255,255,v%255)
    elif v > 255:
        return (255,v%255,0)
    else:
        return (v%255,0,0)

def julia (real_min=-2, real_max=2, imag_min=-2, imag_max=2):
    
    '''
    This function takes min and max values as input to limit
    the graph between 2 boundaries on both the real and
    imaginary axes (the complex plane).

    The output is a Julia set graph.
    '''
    
    #Pick complex number to use for c
    #Note - Python uses 'j' for imaginary numbers instead of 'i'
    print('Enter complex number to base the Julia set off of.')
    a = float(input('Choose real number: '))
    b = float(input('Choose imaginary number: '))
    c = complex(a,b)

    #Specify image size in pixels
    w = float(800)
    h = float(600)

    #Generate array of evenly spaced complex numbers
    #across the width and height of the image (the complex plane)
    #arange takes parameters (start, stop, step)
    real_range = np.arange(real_min, real_max,
                           (real_max-real_min)/w)
    imag_range = np.arange(imag_min, imag_max,
                           (imag_max-imag_min)/h)
    #print(real_range, " and ", imag_range)

    def set_coord (r,i):
        
        '''
        This function converts a coorinate in the complex plane
        to a pixel coordinate for pygame, using min-max normalization.
        '''

        #Normalize
        new_r = ((r-np.amin(real_range))/
        (np.amax(real_range)-np.amin(real_range)))*w
        new_i = ((i-np.amin(imag_range))/
        (np.amax(imag_range)-np.amin(imag_range)))*h

        return (new_r, new_i)
    
    #Initiate a pygame display with desired pixel dimensions (w,h)
    screen = pg.display.set_mode((int(w),int(h)),0,32)
    pg.display.set_caption("Julia Set")

    #Generate pixels 1 by 1 for all complex numbers
    for i in imag_range:
        for r in real_range:
            z = complex(r, i)
            iterations = 0
            #Stop iterating if distance from origin > 2
            #Otherwise stop iterating after 200 passes
            while abs(z) <= 2 and iterations <200:
                z = z**2 + c
                iterations += 1
            color = set_color(iterations)
            coords = set_coord(r,i)
            screen.fill(color, (coords,(1,1)))
            
    return pg.display.update()

