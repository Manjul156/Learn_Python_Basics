import math
def circle(radius):
    circumference = (2*math.pi)*radius
    area = (math.pi)*(radius**2)
    return round(circumference,3),round(area,3)

cir , area = circle(4)

print(f"area : {area} and circumference : {cir}")