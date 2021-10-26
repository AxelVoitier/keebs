#!/usr/bin/env python3
from math import cos, sin, tan, acos, asin, atan, radians, degrees, sqrt
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    
    def dist(p1, p2):
        return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
        
        
center = Point(161.760381, 199.9936)

rail_center = Point(78.769198, 126.790093)
r_rail = rail_center.dist(center)

r_new = r_rail + 1.1 + 3
print(f'New radius: {r_new}')

old_arc_start = Point(100.987117, 106.578718)
r_old = old_arc_start.dist(center)

new_y = center.y - sin(acos((old_arc_start.x - center.x) / r_new)) * r_new
new_arc_start = Point(old_arc_start.x, new_y)
print(f'Displacement: {old_arc_start.dist(new_arc_start)}')
