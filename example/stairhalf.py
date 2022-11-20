import cadquery as cq
from skirmishterrain import StairHalf

bp = StairHalf()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/stairhalf.stl')
