import cadquery as cq
from skirmishterrain import Walkway

bp = Walkway()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/walkway.stl')
