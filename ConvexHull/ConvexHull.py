import random
import numpy as np
import matplotlib.pyplot as plt
import math

'''
Configuration
'''
numPoints = 1000

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.andgle = 0

def generatePoints(numPoints):
    points = []
    for i in range(numPoints):
        points.append(Point(random.uniform(0, 100), random.uniform(0,100)))
    return points

def crossProduct(a, b, p):
    return (b.x-a.x)*(p.y-a.y) - (b.y-a.y)*(p.x-a.x)

def isInTriangle(a, b, c, p):
    #Use sign of cross-product to judge if point p is in triangle abc
    ABAC = crossProduct(a, b, c)
    ABAP = crossProduct(a, b, p)
    BCBP = crossProduct(b, c, p)
    CACP = crossProduct(c, a, p)
    return np.sign(ABAC)==np.sign(ABAP)==np.sign(BCBP)==np.sign(CACP)


'''
Brute Froce
'''
def bruteForce(numPoints, points):
    flag = [1 for i in range (numPoints)] #All points are in the convex hull at the beginning
    
    for i in range(numPoints-3):
        if flag[i]==0: continue
        for j in range(i+1, numPoints-2):
            if flag[j]==0: continue
            for k in range(j+1, numPoints-1):
                if flag[k]==0: continue
                for l in range(k+1, numPoints):
                    if flag[l]==0: continue
                    if isInTriangle(points[i], points[j], points[k], points[l]):
                        flag[l]=0
                        continue
                    if isInTriangle(points[l], points[j], points[k], points[i]):
                        flag[i]=0
                        continue
                    if isInTriangle(points[i], points[l], points[k], points[j]):
                        flag[j]=0
                        continue
                    if isInTriangle(points[i], points[j], points[l], points[k]):
                        flag[k]=0
                        continue

    ch=[] #convex hull points
    for i in range(numPoints):
        if flag[i]:
            ch.append(points[i])
    
    #Print the result
    ch = sorted(ch, key=lambda p: (p.x, p.y)) #sort the convex hull points
    for p in points:
        plt.plot(p.x, p.y, 'b.')
    for p in ch:
        plt.plot(p.x, p.y, 'r.')

    L, R = [], []
    a ,b = ch[0], ch[-1]
    for i in range(1, len(ch)-1):
        if crossProduct(a, b, ch[i])>0:
            L.append(ch[i])
        else:
            R.append(ch[i])
    L.insert(0, a)
    L.append(b)
    R.insert(0, a)
    R.append(b)

    x = [p.x for p in L]
    y = [p.y for p in L]
    plt.plot(x, y, 'g-')


    x = [p.x for p in R]
    y = [p.y for p in R]
    plt.plot(x, y, 'g-')

    plt.show()


'''
Graham Scan
'''
def grahamScan(numPoints, points):
    #find the bottom-most and left-most point
    p0 = Point(101, 101)
    for p in points:
        if p.y < p0.y:
            p0 = p
        elif p.y == p0.y and p.x < p0.x:
            p0 = p 

    #calculate the angle
    points.remove(p0)
    for p in points:
        if p0.x == p.x:
            p.angle = math.pi/2
        elif p0.x < p.x:
            p.angle = math.atan((p.y-p0.y)/(p.x-p0.x))
        else:
            p.angle = math.atan((p.y-p0.y)/(p.x-p0.x)) + math.pi
    
    #calculate the convex hull
    points = sorted(points, key=lambda p: (p.angle))
    ch = []
    ch.append(p0)
    ch.append(points[0])
    ch.append(points[1])
    for i in range(2, len(points)):
        while crossProduct(ch[-2], ch[-1], points[i]) <= 0:
            ch.pop(-1)
        ch.append(points[i])
    
    points.insert(0, p0)
    for p in points:
        plt.plot(p.x, p.y, 'b.')
    for p in ch:
        plt.plot(p.x, p.y, 'r.')
    ch.append(p0)
    x = [p.x for p in ch]
    y = [p.y for p in ch]
    plt.plot(x, y, 'g-')
    plt.show()

'''
Divide And Conquer
'''
def divide(points):
    points = sorted(points, key=lambda p: p.x)
    mid = len(points)//2
    return points[:mid], points[mid:]

def merge(left, right):
    indexMaxYRight = right.index(max(right, key=lambda p: p.y))
    indexMinYRight = right.index(min(right, key=lambda p: p.y))
    points = (left + right[indexMinYRight:indexMaxYRight] +
            (right[indexMaxYRight:] + right[:indexMinYRight]))
    
    p0 = points[0]
    p0.angle = 0
    points.remove(p0)
    for p in points:
        if p0.y == p.y:
            p.angle = math.pi/2
        elif  p0.y > p.y:
            p.angle = math.atan((p.x-p0.x)/(p0.y-p.y))
        else:
            p.angle = math.pi - math.atan((p.x-p0.x)/(p.y-p0.y))
    
    points = sorted(points, key=lambda p: p.angle)
    ch = []
    ch.append(p0)
    ch.append(points[0])
    ch.append(points[1])
    for i in range(2, len(points)):
        while crossProduct(ch[-2], ch[-1], points[i]) <= 0:
            ch.pop(-1)
        ch.append(points[i])

    return ch

def conquer(points):
    if len(points) == 1:
        return points
    elif len(points) == 2:
        points = sorted(points, key=lambda p: (p.x, -p.y))
        return points
    elif len(points) == 3:
        points = sorted(points, key=lambda p: (p.x, -p.y))
        if crossProduct(points[0], points[1], points[2]) > 0:
            return points
        else:
            points[1], points[2] = points[2], points[1]
            return points
    
    left, right = divide(points)
    left = conquer(left)
    right = conquer(right)
    ch = merge(left, right)
    return ch
    
def divideAndConquer(points):
    ch = conquer(points)
    
    for p in points:
        plt.plot(p.x, p.y, 'b.')
    for p in ch:
        plt.plot(p.x, p.y, 'r.')
    ch.append(ch[0])
    x = [p.x for p in ch]
    y = [p.y for p in ch]
    plt.plot(x, y, 'g-')
    plt.show()


'''
Plot points
'''
def plotPoints(points):
    for p in points:
        plt.plot(p.x, p.y, 'b.')
    plt.show()


'''
Main function
'''
if __name__ == '__main__':
    points = generatePoints(numPoints)
    plotPoints(points)
    divideAndConquer(points)
