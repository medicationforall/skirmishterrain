import cadquery as cq
from skirmishterrain import Tower

bp = Tower()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/tower.stl')
