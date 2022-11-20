import cadquery as cq
from skirmishterrain import Rectangle

bp = Rectangle()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/rectangle.stl')
