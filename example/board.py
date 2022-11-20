import cadquery as cq
from skirmishterrain import (
    Cube,
    Rectangle,
    StairFull,
    StairHalf,
    Building,
    Tower,
    Bridge,
    Walkway,
    CornerWall,
    HalfWall,
    Board
)

bp_terrain = Cube()
bp_terrain.make()
result_terrain = bp_terrain.build()

bp_terrain_2 = Rectangle()
bp_terrain_2.length= 225
bp_terrain_2.make()
result_terrain_2 = bp_terrain_2.build()

bp_terrain_3 = StairFull()
bp_terrain_3.make()
result_terrain_3 = bp_terrain_3.build()

bp = Board()
bp.rows = 10
bp.columns = 7
bp.add_terrain(result_terrain, (0,0), bp_terrain.dimensions(), (0,0))
bp.add_terrain(result_terrain_2, (3,1), bp_terrain_2.dimensions(), (1,0))
bp.add_terrain(result_terrain_3, (3,2), bp_terrain_3.dimensions(), (0,0), 180)

bp.make()
result = bp.build()

#show_object(result)
cq.exporters.export(result,'stl/Board.stl')
