import matplotlib.pyplot as plt
import numpy as np
import math
from vectors import *


def dot(v, w):
    x, y, z = v
    X, Y, Z = w
    return x * X + y * Y + z * Z


def unit(v):
    x, y, z = v
    mag = length(v)
    return x / mag, y / mag, z / mag


def length(v):
    x, y, z = v
    return math.sqrt(x * x + y * y + z * z)


def vector(b, e):
    x, y, z = b
    X, Y, Z = e
    return X - x, Y - y, Z - z


def scale(v, sc):
    x, y, z = v
    return x * sc, y * sc, z * sc


def add(v, w):
    x, y, z = v
    X, Y, Z = w
    return x + X, y + Y, z + Z


def distance(p0, p1):
    return length(vector(p0, p1))


def pnt2line(pnt, start, end):  # all points have to be 3D (e.g., x,y,x)
    line_vec = vector(start, end)
    pnt_vec = vector(start, pnt)
    line_len = length(line_vec)
    line_unitvec = unit(line_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0 / line_len)
    t = dot(line_unitvec, pnt_vec_scaled)
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    nearest = scale(line_vec, t)
    dist = distance(nearest, pnt_vec)
    nearest = add(nearest, start)
    return dist, nearest


def distance_formula(pt1, pt2):
    return math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

height_in_cm = [163, 185, 167, 184, 180, 160, 175, 174]
weight_in_kg = [54, 93, 90, 102, 88, 50, 70, 91]
age_in_years = [18, 22, 68, 31, 24, 25, 32, 55]
x = np.arange(len(height_in_cm))

z = np.polyfit(x=height_in_cm, y=weight_in_kg, deg=1)
p = np.poly1d(z)
start = (0, p(0), 0)
end = (250, p(250), 0)

for height, weight in zip(height_in_cm, weight_in_kg):
    let_pnt = (height, weight, 0)
    let_dist, pnt_on_line = pnt2line(let_pnt, start, end)
    new_x = (height + pnt_on_line[0]) / 2
    new_y = (p(height) + pnt_on_line[1]) / 2
    plt.plot([height, new_x], [weight, new_y])

# plt.plot([157, 187], [p(157), p(187)], c='blue')
# for i in range(len(height_in_cm)):
#     plt.scatter(height_in_cm[i], weight_in_kg[i])
# plt.xlabel("Height (cm)")
# plt.ylabel("Weight (kg)")
# plt.title("Sample of 8 people's height & weight")
# plt.show()

fig, ax = plt.subplots()
points = []

for height, weight in zip(height_in_cm, weight_in_kg):
    let_pnt = (height, weight, 0)
    let_dist, pnt_on_line = pnt2line(let_pnt, start, end)
    new_x = (height + pnt_on_line[0]) / 2
    new_y = (p(height) + pnt_on_line[1]) / 2
    points.append((new_x, new_y))

ax.set_title("2D projection onto one axis")

x2 = sorted(height_in_cm)
x2[0] = 155
# this creates the trend line:
# plt.plot(x, y, c='blue')
# fig.patch.set_visible(False)
ax.axis('off')



# print(points)
distances = []
total_distances = 0
for i in range(len(points)):
    # print(points[i])
    # print(f"\nDist between first two points:\n{distance_formala(points[i], points[i+1])}")
    distance_len = distance_formula((157, p(157)), points[i])
    total_distances += distance_len
    distances.append(distance_len)

print(distances)
print(total_distances)
# print(f"\n\nDist between first two points:\n{distance_formala(points[0], points[1])}")
ax.plot([0, 190], [0, 0], c='blue', zorder=1)  # the zorder is needed to put the line behind the points
total = 0
for d in distances:
    ax.scatter(d+total, 0, zorder=2)
    total += d
plt.show()
