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

bp = Board()
bp.rows = 10
bp.columns = 7
bp.add_terrain(result_terrain, (0,0), (75,75,75))

bp.make()
result = bp.build()

# show_object(result)
cq.exporters.export(result,'stl/Board.stl')
