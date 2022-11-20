import cadquery as cq
from skirmishterrain import StairFull

bp = StairFull()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/stairFull.stl')
