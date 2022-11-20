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

# 75 x  75 x 37.5 mm

import cadquery as cq

class CornerWall:
    def __init__(self):
        self.corner_wall = None

    def make(self):
        self.corner_wall = cq.Workplane("XY").box(75, 75, 37.5)

    def build(self):
        return self.corner_wall