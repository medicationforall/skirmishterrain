import cadquery as cq
from skirmishterrain import Building

bp = Building()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/building.stl')
