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

import cadquery as cq
from cadqueryhelper import grid

class Board:
    def __init__(self):
        self.board = None
        self.tile = None
        self.terrain = []
        self.board_dim = None
        self.rows = 5
        self.columns = 5

    def make(self):
        self.tile = cq.Workplane("XY").box(75, 75, 4)
        self.board = grid.make_grid(self.tile, dim = [76,76], rows = self.rows, columns = self.columns)
        self.board_dim = (76*self.rows, 76*self.columns)

    def add_terrain(self, part, loc, dim):
        #print("add to", loc, dim)
        place_def = {
        "part":part,
        "location":loc,
        "dimensions":dim
        }
        self.terrain.append(place_def)


    def build(self):
        scene = cq.Workplane("XY")
        scene.add(self.board)
        scene = self.place_terrain(scene)

        return scene

    def place_terrain(self, scene):
        for piece in self.terrain:
            scene = self.place_piece(piece, scene)
        return scene

    def place_piece(self, piece, scene):
        gutter = 0.5

        #zero out the piece
        x_index = ((-1 * (self.board_dim[0] / 2)) + (piece["dimensions"][0] /2))+gutter
        y_index = ((-1 * (self.board_dim[1] / 2)) + (piece["dimensions"][1] /2))+gutter

        # apply desired location
        x_location = piece["location"][0] * (piece["dimensions"][0]+1)
        y_location = piece["location"][1] * (piece["dimensions"][1]+1)

        part = piece["part"].translate((x_index + x_location, y_index + y_location, piece["dimensions"][2]/2 + 4/2))
        scene.add(part)
        return scene
