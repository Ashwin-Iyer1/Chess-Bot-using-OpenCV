

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
Polygons = []

for row in range(8):
    for col in range(8):
        x1 = col * 85
        y1 = row * 85
        x2 = x1 + 85
        y2 = y1 + 85
        
        polygon = Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])
        Polygons.append(polygon)
polygonlist = list(Polygons)
print(polygonlist)
