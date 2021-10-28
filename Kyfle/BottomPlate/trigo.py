#!/usr/bin/env python3
from math import cos, sin, tan, acos, asin, atan, radians, degrees, sqrt
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    
    def dist(p1, p2):
        return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
        
        
P = Point
        
        
@dataclass
class Line:
    a: float
    b: float
    c: float
    
    @classmethod
    def from_2_points(cls, p1, p2):
        try:
            a = (p2.y - p1.y) / (p2.x - p1.x)
            b = -1
        except ZeroDivisionError:
            a = 1
            b = 0
            
        c = p1.y - (a * p1.x)
        
        return cls(a, b, c)
        
    @classmethod
    def vertical(cls, x):
        return cls(1, 0, -x)
        
    def intersect(l1, l2):
        return Point(
            ((l1.b * l2.c) - (l2.b * l1.c)) / ((l1.a * l2.b) - (l2.a * l1.b)),
            ((l1.c * l2.a) - (l2.c * l1.a)) / ((l1.a * l2.b) - (l2.a * l1.b)),
        )
        
        
L = Line


@dataclass
class Circle:
    c: Point
    r: float
    
    def point_at_angle(circle, angle):
        return Point(
            circle.c.x + (cos(angle) * circle.r),
            circle.c.y - (sin(angle) * circle.r)
        )
    
    def a_from_x(circle, x):
        return acos((x - circle.c.x) / circle.r)
        
    def y_from_a(circle, a):
        return circle.c.y - (sin(a) * circle.r)
        
    def y_from_x(circle, x):
        return circle.y_from_a(circle.a_from_x(x))
        
    def a_from_y(circle, y):
        return asin((circle.c.y - y) / circle.r)
        
    def x_from_a(circle, a):
        return circle.c.x + (cos(a) * circle.r)
        
    def x_from_y(circle, y):
        return circle.x_from_a(circle.a_from_y(y))
        
    def tangente_line(circle, angle):
        # tan() is length between point on the circle at
        # that angle (p1) and intercepting point on the
        # X-axis (p2).
        
        p1 = circle.point_at_angle(angle)
        
        # Intercepting point on X-axis is the hypotenuse
        # in the right triangle formed by the radius and
        # the tangente.
        p2 = Point(
            circle.c.x + sqrt((tan(angle) * circle.r)**2 + circle.r**2),
            circle.c.y 
        )
        
        return Line.from_2_points(p1, p2)
        
        
center = Point(161.760381, 199.9936)

# Arc above thumb cluster

rail_center = Point(78.769198, 126.790093)
r_rail = rail_center.dist(center)

r_new = r_rail + 1.1 + 3
print(f'New radius: {r_new}')

old_arc_start = Point(100.987117, 106.578718)
r_old = old_arc_start.dist(center)

new_y = center.y - sin(acos((old_arc_start.x - center.x) / r_new)) * r_new
new_arc_start = Point(old_arc_start.x, new_y)
print(f'Displacement: {old_arc_start.dist(new_arc_start)}')

# 

other_r = Point(80.765891, 118.995125).dist(center)
print(f'Other R: {other_r}, diff: {other_r - r_new}')

# Intersecting lines

tenting_line = L.vertical(96.6125)
l2 = L.from_2_points(P(102.174433, 163.064671), P(69.989314, 130.879552))

# Arc above all

r_top_arc_old = 176.257272
highest_rail = P(162.12625, 22.375)
r_top_arc = highest_rail.dist(center) + 1.1 + 3
top_arc = Circle(center, r_top_arc)
print(f'Top arc radius: {r_top_arc} (diff: {r_top_arc - r_top_arc_old})')

# Right corner to arc

right_edge_x = 237.22038
intersecting_angle = top_arc.a_from_x(right_edge_x)
corner = Circle(P(0, 0), 1)
corner.c.y = top_arc.y_from_x(right_edge_x - (1 - corner.x_from_a(intersecting_angle))) - corner.y_from_a(intersecting_angle)
corner.c.x = right_edge_x - corner.r
print(f'Corner at {corner}, with arc angle of {-degrees(intersecting_angle):.1f}')

# Position of M5 hole at left of top arc

# M5 mounting hole is defined by a 10mm diameter circle.
# We want that circle to be tangential to the top arc.
# Two tangential circles have their centers on the same
# line that the one that pass by their respective center
# (ie. radius) and tangent point. Ie. the two centers and
# the tangent point are on the same line.

# As the X position of the M5 hole is fixed, the center of
# the M5 hole is at the intersection between that vertical
# line of known X and a circle similar to the top arc circle
# minus 10/2=5mm on the radius.
m5_x_line = 98.638899
top_arc_minus5 = Circle(top_arc.c, top_arc.r - 5)
m5_circle = Circle(Point(m5_x_line, top_arc_minus5.y_from_x(m5_x_line)), 5)

# Then the tangent point is at the angle defined by that line
# passing through both centers and tangent point. The center
# of the M5 circle being at the intersection of the M5 X-line
# and the top arc minus 5 circle, the angle we search is just
# given by that M5 center point lying on the top arc minus 5 circle
intersecting_angle = top_arc_minus5.a_from_x(m5_x_line)
top_arc_M5_tangent = top_arc.point_at_angle(intersecting_angle)

# And from that tangent point, the partial circle forming
# the M5 hole goes up to the X-line (before having another
# corner radius but going in the other way).
m5_arc_angle = 180 - (degrees(intersecting_angle) - 90)

print(f'Left top M5 hole at {m5_circle}, with arc at the same center, starting at {top_arc_M5_tangent} over an angle of {-m5_arc_angle:.1f}')
