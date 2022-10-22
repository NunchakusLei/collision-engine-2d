# Copyright (c) 2018 Chenrui Lei
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math
import cmath


# GCD and LCM are not in math module.
# They are in gmpy, but these are simple enough:
# Source:
# https://gist.github.com/endolith/114336/
# eff2dc13535f139d0d6a2db68597fad2826b53c3
# Aug 25th, 2018
def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


class Point2D:
    """
    Mathematical representation of 2D point: (x, y)
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if type(other) is Point2D:
            if self.x == other.x and self.y == other.y:
                return True
        return False

    def __str__(self):
        return "Point2D(x=%f, y=%f)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point2D(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point2D(x, y)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Point2D(x, y)

    def __neg__(self):
        x = -self.x
        y = -self.y
        return Point2D(x, y)

    def find_distance(self, another_point):
        if type(another_point) is not Point2D:
            raise TypeError(
                "Cannot find distance between '{:s}' and '{:}'".format(
                    type(self).__name__, type(another_point).__name__
                )
            )
        return math.sqrt(
            (another_point.x - self.x) ** 2 + (another_point.y - self.y) ** 2
        )

    def rotate(self, theta, center=None):
        """
        theta: in radian
        center: a Point2D object
        """
        if center is None:
            center = Point2D(0, 0)

        # # transfer
        # pt = self - center
        # # rotate
        # pt_rotated = Point2D(
        #     int(math.cos(theta) * pt.x - math.sin(theta) * pt.y),
        #     int(math.sin(theta) * pt.x + math.cos(theta) * pt.y)
        # )
        # # transfer back
        # return pt_rotated + center

        # Source: http://effbot.org/zone/tkinter-complex-canvas.htm
        cangle = cmath.exp(theta * 1j)
        offset = complex(center.x, center.y)
        v = cangle * (complex(self.x, self.y) - offset) + offset
        return Point2D(v.real, v.imag)

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)


class Line2D:
    """
    Mathematical representation of 2D line: a*x + b*y + c = 0
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_2_points(cls, point1, point2):
        if point1 == point2:
            raise Exception("Cannot use two identical points to define a line.")
        x1, y1, x2, y2 = point1.x, point1.y, point2.x, point2.y
        if x1 == x2:
            a, b, c = 1, 0, -x1
        else:
            a = y2 - y1
            b = -(x2 - x1)
            c = (x2 - x1) * y1 - (y2 - y1) * x1
        return cls(a, b, c)

    def __eq__(self, other):
        if self.is_parallel(other):
            if self.c * other.b == other.c * self.b:
                return True
        return False

    def __str__(self):
        return "Line2D(%dx + %dy + %d = 0)" % (self.a, self.b, self.c)

    def __repr__(self):
        return self.__str__()

    def is_parallel(self, another_line):
        if self.a != 0 and another_line.a != 0:
            if self.b / self.a == another_line.b / another_line.a:
                return True
        elif self.a == 0 and another_line.a == 0:
            return True
        return False

    def is_perpendicular(self, another_line):
        if self.a != 0 and self.b != 0:
            if another_line.b / self.a == -another_line.a / self.b:
                return True
        elif self.a == 0 and another_line.b == 0:
            return True
        elif self.b == 0 and another_line.a == 0:
            return True
        return False

    def find_perpendicular(self, through_point):
        a = -self.b
        b = self.a
        c = -(a * through_point.x + b * through_point.y)
        return Line2D(a, b, c)

    def find_distance(self, point):
        return abs(self.a * point.x + self.b * point.y + self.c) / math.sqrt(
            self.a**2 + self.b**2
        )

    def find_intersection(self, another_line):
        if self.is_parallel(another_line):
            return False
        if (
            self.b != 0
            and not math.isclose(self.b, 0, rel_tol=1e-4)
            and another_line.b != 0
            and not math.isclose(another_line.b, 0, rel_tol=1e-4)
        ):
            lowest_common_multiple = lcm(self.b, another_line.b)
            self_multipler = lowest_common_multiple / self.b
            another_multipler = lowest_common_multiple / another_line.b
            x = another_multipler * another_line.c - self_multipler * self.c
            x = x / (self_multipler * self.a - another_multipler * another_line.a)
            y = (self.a * x + self.c) / -self.b
        else:
            if self.b == 0 or math.isclose(self.b, 0, rel_tol=1e-4):
                x = -self.c / self.a
                y = -(another_line.a * x + another_line.c) / another_line.b
            else:
                x = -another_line.c / another_line.a
                y = -(self.a * x + self.c) / self.b

        return Point2D(x, y)


class LineSegment2D(Line2D):
    def __init__(self, point1, point2):
        temp_line = Line2D.from_2_points(point1, point2)
        Line2D.__init__(self, temp_line.a, temp_line.b, temp_line.c)
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return (
            "Line2D(%dx + %dy + %d = 0) " % (self.a, self.b, self.c)
            + str(self.point1)
            + " "
            + str(self.point2)
        )

    def __repr__(self):
        return self.__str__()

    def find_intersection(self, another_line_segment):
        intersect_point = Line2D.find_intersection(self, another_line_segment)
        if intersect_point != False:
            xmax = max(self.point1.x, self.point2.x)
            xmin = min(self.point1.x, self.point2.x)
            ymax = max(self.point1.y, self.point2.y)
            ymin = min(self.point1.y, self.point2.y)

            if (
                (
                    intersect_point.x <= xmax
                    or math.isclose(intersect_point.x, xmax, rel_tol=1e-4)
                )
                and (
                    intersect_point.x >= xmin
                    or math.isclose(intersect_point.x, xmin, rel_tol=1e-4)
                )
                and (
                    intersect_point.y <= ymax
                    or math.isclose(intersect_point.y, ymax, rel_tol=1e-4)
                )
                and (
                    intersect_point.y >= ymin
                    or math.isclose(intersect_point.y, ymin, rel_tol=1e-4)
                )
            ):

                xmax = max(another_line_segment.point1.x, another_line_segment.point2.x)
                xmin = min(another_line_segment.point1.x, another_line_segment.point2.x)
                ymax = max(another_line_segment.point1.y, another_line_segment.point2.y)
                ymin = min(another_line_segment.point1.y, another_line_segment.point2.y)

                if (
                    (
                        intersect_point.x <= xmax
                        or math.isclose(intersect_point.x, xmax, rel_tol=1e-4)
                    )
                    and (
                        intersect_point.x >= xmin
                        or math.isclose(intersect_point.x, xmin, rel_tol=1e-4)
                    )
                    and (
                        intersect_point.y <= ymax
                        or math.isclose(intersect_point.y, ymax, rel_tol=1e-4)
                    )
                    and (
                        intersect_point.y >= ymin
                        or math.isclose(intersect_point.y, ymin, rel_tol=1e-4)
                    )
                ):
                    return intersect_point
        return False


# class Line2D:
#     # def __init__(slop, shift):
#     #     self.slop = slop
#     #     self.yshift = yshift
#     def __init__(self, x1, y1, x2, y2):
#         if x1 == x2:
#             self.slop = None
#             self.shift = x1
#         else:
#             self.slop = (y1 - y2) / (x1 - x2)
#             self.shift = y1 - x1 * self.slop
#
#     def intercetWith(self, line):
#         if self.slop == line.slop and self.shift == line.shift:
#             return 'any'
#         else:
#             x = (line.shift - self.shift) / (self.slop - line.slop)
#             y = x * self.slop + self.shift
#             return (x, y)


class GeomatricObject:
    """Object representation in 2D"""

    def __init__(self, vertex, edges):
        """Object class constructor

        Args:
            vertex (:obj:`list`): A list of vertexes. Each vertex is  a :obj:`Point2D`.
            edges (:obj:`list`): A list of vertex index pair. The vertex index in
                argument vertex.

        """
        self.vertex = vertex
        self.edges = edges
        self.movement = Point2D(0, 0)


class CollisionEngine2D:
    @staticmethod
    def point_line_collision(
        point, point_movement, line_segment, line_segment_movement
    ):
        if (point_movement - line_segment_movement) == Point2D(0, 0):
            return False
        point_moving_line_seg = LineSegment2D(
            point, point + point_movement - line_segment_movement
        )
        intersect_point = LineSegment2D.find_intersection(
            point_moving_line_seg, line_segment
        )
        # moved_line_segment = LineSegment2D(
        #     line_segment.point1+line_segment_movement,
        #     line_segment.point2+line_segment_movement
        # )
        # intersect_point2 = LineSegment2D.find_intersection(
        #     point_moving_line_seg,
        #     moved_line_segment
        # )
        if intersect_point:  # or intersect_point2!=False:
            return True
        return False


# if __name__ == "__main__":
#     point = Point2D(0, 0)
#     point_movement = Point2D(10, 10)
#     line_segment = LineSegment2D(
#         Point2D(5, 20),
#         Point2D(5, -20)
#     )
#     line_segment_movement = Point2D(0, 0)
#
#     print(
#         CollisionEngine2D.point_line_collision(
#             point, point_movement, line_segment, line_segment_movement
#         )
#     )
