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

# 75 x 75x 75 mm

from .. import Base
import cadquery as cq
from cqterrain import roof


class StairFull(Base):
    def __init__(self):
        super().__init__()
        self.stair = None

    def make(self):
        super().make()
        self.stair = roof.dollhouse_gable(self.length, self.width, self.height)

    def build(self):
        super().build()
        return self.stair
