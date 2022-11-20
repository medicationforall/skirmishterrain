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

bp_cube = Cube()
bp_cube.make()
result_cube = bp_cube.build()

bp = Board()
bp.add_terrain(result_cube, (2,2), (75,75,75))
bp.make()
result = bp.build()


#show_object(result_cube)
show_object(result)
cq.exporters.export(result,'stl/Board.stl')
