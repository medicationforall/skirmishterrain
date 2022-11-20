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

import cadquery as cq
from cadqueryhelper import grid

class Board:
    def __init__(self):

        self.board_dim = None
        self.rows = 5
        self.columns = 5
        self.tile_length = 75
        self.tile_width= 75
        self.tile_height = 4
        self.gutter=1
        self.tile = None
        self.board = None
        self.terrain = []


    def make(self):
        self.tile = cq.Workplane("XY").box(self.tile_length, self.tile_width, self.tile_height)
        self.board = grid.make_grid(self.tile, dim = [self.tile_length+self.gutter,self.tile_width+self.gutter], rows = self.rows, columns = self.columns)
        self.board_dim = ((self.tile_length+self.gutter)*self.rows, (self.tile_width+self.gutter)*self.columns)

    def build(self):
        scene = cq.Workplane("XY")
        scene.add(self.board)
        scene = self.place_terrain(scene)
        return scene

    def add_terrain(self, part, loc, dim, offset=(0,0), rotate=0):
        place_def = {
        "part":part,
        "location":loc,
        "dimensions":dim,
        "offset":offset,
        "rotate":rotate
        }
        self.terrain.append(place_def)

    def place_terrain(self, scene):
        for piece in self.terrain:
            scene = self.place_piece(piece, scene)
        return scene

    def place_piece(self, piece, scene):
        gutter = 0.5

        #zero out the piece
        x_center = (piece["dimensions"][0] /2)
        y_center = (piece["dimensions"][1] /2)
        x_index = ((-1 * (self.board_dim[0] / 2)) + piece['offset'][0] + x_center)+gutter
        y_index = ((-1 * (self.board_dim[1] / 2)) + piece['offset'][1] + y_center)+gutter

        # apply desired location
        x_location = piece["location"][0] * (self.tile_length+self.gutter)
        y_location = piece["location"][1] * (self.tile_width+self.gutter)

        part = (
            piece["part"]
            .rotate((0,0,1), (0,0,0), piece['rotate'])
            .translate((x_index + x_location, y_index + y_location, piece["dimensions"][2]/2 + 4/2))
        )
        scene.add(part)
        return scene
