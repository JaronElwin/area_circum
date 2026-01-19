import math
from area_circum import area_circum

def test_case():
    area, circumference = area_circum(5)
    assert math.isclose(area, math.pi * 25)
    assert math.isclose(circumference, 2 * math.pi * 5)
