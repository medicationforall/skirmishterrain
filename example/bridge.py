import cadquery as cq
from skirmishterrain import Bridge

bp = Bridge()
bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/Bridgebridge.stl')
