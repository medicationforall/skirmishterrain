import cadquery as cq
from skirmishterrain import CornerWall

bp = CornerWall()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/CornerWall.stl')
