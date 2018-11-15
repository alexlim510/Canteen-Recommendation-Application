# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 10:29:03 2018

@author: win10
"""

from_cor = (1.3535285933806145, 103.68827099377593)
dest  = 'Pioneer Food Court'
def convert_coordinates_bus_html(from_coordinates, destination):
    # usually for bus there are three options
    # lst of the three bus options
    bus_lst = []
    # http://maps.ntu.edu.sg/m?q=Tanjong%20Hall%20of%20Residence%20-%20Block%2020B%20to%20Pioneer%20Food%20Court&d=b&p=0&fs=m
    bus_0 = 'http://maps.ntu.edu.sg/m?q=' + str(from_coordinates[0]) + '%2C+' + str(from_coordinates[1]) + '%20to%20' + '+'.join(destination.split(' ')) + '&d=b&p=0&fs=m'
    bus_1 = 'http://maps.ntu.edu.sg/m?q=' + str(from_coordinates[0]) + '%2C+' + str(from_coordinates[1]) + '%20to%20' + '+'.join(destination.split(' ')) + '&d=b&p=1&fs=m'
    bus_2 = 'http://maps.ntu.edu.sg/m?q=' + str(from_coordinates[0]) + '%2C+' + str(from_coordinates[1]) + '%20to%20' + '+'.join(destination.split(' ')) + '&d=b&p=2&fs=m'
    bus_lst.extend([bus_0, bus_1, bus_2]) 
    return bus_lst
    
lst = convert_coordinates_bus_html(from_cor, dest)
for i in lst:
    print(i)