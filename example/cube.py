import cadquery as cq
from skirmishterrain import Cube

bp = Cube()
#customize here
bp.make()
result = bp.build()

print(bp.dimensions())

#show_object(result)
cq.exporters.export(result,'stl/cube.stl')

bp.width=150
bp.make()
result = bp.build()
cq.exporters.export(result,'stl/long_cube.stl')
