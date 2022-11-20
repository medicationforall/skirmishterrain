import cadquery as cq
from skirmishterrain import HalfWall

bp = HalfWall()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/HalfWall.stl')
