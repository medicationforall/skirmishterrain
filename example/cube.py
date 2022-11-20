import cadquery as cq
from skirmishterrain import Cube

bp = Cube()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/cube.stl')
