# Copyright 2022 James Adams
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# 75 x 75 x 75 mm

from .. import Base
import cadquery as cq
import math
from cqterrain import Ladder, Door, window, tile
from cadqueryhelper import grid, series, shape


def greeble(dim):
    greeble_part = (
        cq.Workplane("XY")
        .box(dim[0]-8, 2, dim[2] - 8, combine=False)
        .edges("|Y")
        .chamfer(11)
    )
    return greeble_part

def make_rung(length, width, height):
    rung = cq.Workplane("XY").box(length+1, width ,height)
    rung = rung.edges("X").fillet(.909999)
    return rung

def make_side_rail(width, height, rail_width):
    rail = (cq.Workplane("XY")
            .box( height, rail_width, width)
            .rotate((0,0,1),(0,0,0),90)
            .rotate((1,0,0),(0,0,0),90)
            )
    rail = rail.faces("<Y").edges("X").fillet(2)
    return rail

def tile_floor(dim):
    diagonal_tile = tile.slot_diagonal(
        tile_size = 21,
        height = 2,
        slot_width = 2,
        slot_height = 2,
        slot_length_padding = 7,
        slot_width_padding = 2,
        slot_width_padding_modifier = .25
    )

    rows = math.floor(dim[0]/22.5)
    columns = math.floor(dim[1]/22.5)
    tiles = grid.make_grid(diagonal_tile, [22.5,22.5], rows=rows, columns= columns).translate((0,0,(dim[2]/2)-1))

    return tiles

def sci_fi_panels(cube, dim):
    y_points = cube.faces(">Y or <Y")
    x_points = cube.faces(">X or <X")
    z_point = cube.faces(">Z")

    y_cut = y_points.box(dim[0]-8, 7, dim[2] - 8, combine=False)
    x_cut = x_points.box(7, dim[1]-8, dim[2] - 8, combine=False)
    z_cut = z_point.box(dim[0]-8, dim[1] - 8, 4, combine=False)

    y_plus_panel = greeble(dim).translate((0,(dim[1]/2)-3,0))
    y_minus_panel = greeble(dim).translate((0,-1*((dim[1]/2)-3),0))

    x_plus_ladder = __sci_fi_ladder(dim)
    x_min_door = __sci_fi_door(dim)


    cube = cube.faces("Z").edges().chamfer(2)
    floor_tiles = tile_floor(dim)
    cut_cube = (
        cube.cut(y_cut)
        .cut(x_cut)
        .cut(z_cut)
        .add(y_plus_panel)
        .add(y_minus_panel)
        .add(x_plus_ladder)
        .add(x_min_door)
        .add(floor_tiles)
        )

    cut_cube = __sci_fi_windows(dim, cut_cube)
    return cut_cube

def __sci_fi_ladder(dim):
    ladder_bp = Ladder()
    ladder_bp.height=dim[2]-8
    ladder_bp.width=3.5
    ladder_bp.rung_padding=9
    ladder_bp.make_rung = make_rung
    #ladder_bp.make_side_rail = make_side_rail
    ladder_bp.make()
    x_plus_ladder = ladder_bp.build().rotate((0,0,1),(0,0,0),-90).translate(((dim[0]/2)-2,0,0))
    return x_plus_ladder

def __sci_fi_door(dim):
    door_bp = Door()
    door_bp.width=6
    door_bp.length=35
    door_bp.height=50
    door_bp.frame_length=6
    door_bp.inner_width=5
    door_bp.make()
    x_min_door = door_bp.build().rotate((0,0,1),(0,0,0),90).translate((-1*((dim[0]/2)-3),0,-1*((dim[2]/2)-25)))
    return x_min_door

def __rail_operation(tile, size, index, bounding_box):
    rail_rotation = 0
    if index % 2 == 1:
        rail_rotation = 180
    win_rail = (
        shape.rail(length=12-3, width=5-2, height=16-3, inner_height=2.5)
        .rotate((0,0,1),(0,0,0),90)
        .rotate((0,0,1),(0,0,0),rail_rotation)
    )

    new_tile = cq.Workplane("XY").add(tile).add(win_rail)
    return new_tile

def __sci_fi_windows(dim, cube):
    win_lengh = 12
    win_width_offset = 3
    series_size = math.floor((dim[1]-8-8) / (win_lengh+win_width_offset))
    win_cut = (
        cq.Workplane("XY").box(12, 4, 16)
        .rotate((0,0,1),(0,0,0),90)
    )

    cut_series = (
        series(win_cut, series_size, width_offset=win_width_offset)
        .translate((-1*(dim[0]/2)+3,0,(dim[2]/2)-8-4-2))
    )

    frame = window.frame(length=12, width = 5, height = 16, frame_width=1.5).rotate((0,0,1),(0,0,0),90)
    frame_series = (
        series(frame, series_size, width_offset=win_width_offset, operation=__rail_operation)
        .translate((-1*(dim[0]/2)+3,0,(dim[2]/2)-8-4-2))
    )

    cube = cube.cut(cut_series).add(frame_series)
    return cube


class Cube(Base):
    def __init__(self):
        super().__init__()
        self.cube = None
        self.add_details = sci_fi_panels

    def make(self):
        super().make()
        cube = cq.Workplane("XY").box(self.length, self.width, self.height)
        cube = cube.faces("-Z").shell(-5)

        cube = self.add_details(cube, self.dimensions())
        self.cube = cube

    def build(self):
        super().build()
        return self.cube
