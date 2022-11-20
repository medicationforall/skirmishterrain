import cadquery as cq
from skirmishterrain import Cube

bp = Cube()
bp.make()
result = bp.build()

print(bp.dimensions())

#show_object(result)
cq.exporters.export(result,'stl/cube.stl')
