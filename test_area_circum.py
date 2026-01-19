import math
from area_circum import area_circum

def test_case():
    area, circumference = area_circum(5)
    assert area == math.pi * 25
    assert circumference == 2 * math.pi * 5
