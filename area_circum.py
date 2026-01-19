import math
def area_circum(radius):
    area = math.pi*radius*radius
    circumference = 2*math.pi*radius
    return area, circumference
if __name__ == "__main__":
    area_circum(radius=5)