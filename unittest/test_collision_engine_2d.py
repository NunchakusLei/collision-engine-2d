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

import sys
sys.path.append("..") # Adds higher directory to python modules path.
from collision_engine_2d import *
import unittest
import math

class TestPoint2D(unittest.TestCase):
    # def __init__(self, testname, arg):
    #     super(TestPoint2D, self).__init__(testname)
    #     # self._arg = arg
        
    def setUp(self):
        self.point_a = Point2D(10, 5)
        self.point_b = Point2D(5, 0)
        
    def test_point2d_declearation(self):
        point_a = Point2D(10, 5)
        self.assertTrue(True)
        
    def test_point2d_eq(self):
        self.assertFalse(self.point_a == self.point_b)
        self.assertTrue(self.point_a == self.point_a)
        self.assertTrue(self.point_b == self.point_b)
        self.assertTrue(Point2D(10, 5) == self.point_a)
        self.assertFalse(self.point_a == 0)
        self.assertFalse(self.point_a == False)
        
    def test_point2d_str(self):
        self.assertEqual(
            "Point2D(x=%f, y=%f)" % (self.point_a.x, self.point_a.y),
            str(self.point_a)
        )
        self.assertEqual(
            "Point2D(x=%f, y=%f)" % (self.point_b.x, self.point_b.y),
            str(self.point_b)
        )
        
    def test_point2d_add(self):
        self.assertEqual(
            Point2D(0, 0) + Point2D(10, 100),
            Point2D(10, 100)
        )
        
    def test_point2d_sub(self):
        self.assertEqual(
            Point2D(0, 0) - Point2D(10, 100),
            Point2D(-10, -100)
        )
        
    def test_point2d_mul(self):
        self.assertEqual(
            Point2D(10, 100) * 4,
            Point2D(40, 400)
        )
        
    def test_point2d_neg(self):
        self.assertEqual(
            -Point2D(10, 100),
            Point2D(-10, -100)
        )
        
    def test_point2d_find_distance(self):
        self.assertEqual(
            self.point_a.find_distance(self.point_b), math.sqrt(50)
        )
        self.assertEqual(
            Point2D.find_distance(self.point_a, self.point_b), 
            math.sqrt(50)
        )
        with self.assertRaises(TypeError):
            self.point_a.find_distance(10)
        
    
        
class TestLine2D(unittest.TestCase):
    def setUp(self):
        self.line_a = Line2D(10, 5, 5)
        self.line_b = Line2D(2, 1, 1)
        self.line_c = Line2D(5, -10, -3)
        self.line_d = Line2D(20, 10, 3)
        self.line_e = Line2D(10, 5, 3)
        
    def test_line2d_declearation(self):
        point_a = Line2D(10, 5, 3)
        Line2D.from_2_points(Point2D(1, 2), Point2D(5, 2))
        self.assertTrue(True)
        with self.assertRaises(Exception):
            Line2D.from_2_points(Point2D(1, 2), Point2D(1, 2))

        
    def test_line2d_eq(self):
        self.assertFalse(self.line_a == self.line_c)
        self.assertTrue(self.line_a == self.line_b)
        self.assertTrue(self.line_c == self.line_c)
        self.assertTrue(
            Line2D(0, -1, 2) == Line2D.from_2_points(
                Point2D(1, 2), Point2D(5, 2)
            )
        )
        
    def test_line2d_str(self):
        self.assertEqual(
            "Line2D(%dx + %dy + %d = 0)" % (
                self.line_a.a, 
                self.line_a.b, 
                self.line_a.c
            ),
            str(self.line_a)
        )
        
    def test_line2d_is_paralled(self):
        self.assertTrue(
            self.line_a.is_parallel(self.line_b)
        )
        self.assertFalse(
            self.line_a.is_parallel(self.line_c)
        )
        
    def test_line2d_is_perpendicular(self):
        self.assertTrue(
            self.line_a.is_perpendicular(self.line_c)
        )
        self.assertFalse(
            self.line_a.is_perpendicular(self.line_b)
        )
        
    def test_find_intersection(self):
        self.assertFalse(
            Line2D.find_intersection(self.line_a, self.line_b)
        )
        self.assertEqual(
            Line2D.find_intersection(self.line_e, self.line_c),
            Point2D(-0.12, -0.36)
        )
        
        
        
class TestLineSegment2D(unittest.TestCase):
    # def setUp(self):
    def test_line_segment2d_declearation(self):
        with self.assertRaises(Exception):
            LineSegment2D(Point2D(1, 2), Point2D(1, 2))
        LineSegment2D(Point2D(1, 2), Point2D(5, 2))
        
    # def test_line_segment2d_find_intersection(self):
    #     TODO
        
        
        
class TestCollisionEngine2D(unittest.TestCase):
    # def setUp(self):
        
    def test_collision_engine2d_point_line_collision(self):
        # point = Point2D(0, 0)
        # point_movement = Point2D(10, 10) 
        # line_segment = LineSegment2D(
        #     Point2D(5, 20),
        #     Point2D(5, -20)
        # ) 
        # line_segment_movement = Point2D(0, 0)
        # 
        # self.assertTrue(
        #     CollisionEngine2D.point_line_collision(
        #         point, point_movement, line_segment, line_segment_movement
        #     )
        # )
        # 
        # point = Point2D(394, 386)
        # point_movement = Point2D(1, 1) 
        # line_segment = LineSegment2D(
        #     Point2D(395, 345),
        #     Point2D(395, 445)
        # ) 
        # line_segment_movement = Point2D(0, 0)
        # 
        # self.assertTrue(
        #     CollisionEngine2D.point_line_collision(
        #         point, point_movement, line_segment, line_segment_movement
        #     )
        # )
        # 
        # point = Point2D(255, 260.9735)
        # point_movement = Point2D(0, 4.7385) 
        # line_segment = LineSegment2D(
        #     Point2D(146, 266),
        #     Point2D(373, 266)
        # ) 
        # line_segment_movement = Point2D(0, -1)
        # 
        # self.assertTrue(
        #     CollisionEngine2D.point_line_collision(
        #         point, point_movement, line_segment, line_segment_movement
        #     )
        # )
        
        point = Point2D(384, 260.9735)
        point_movement = Point2D(1, 4.7385) 
        line_segment = LineSegment2D(
            Point2D(373, 266),
            Point2D(640, 266)
        ) 
        line_segment_movement = Point2D(0, -1)
        
        self.assertTrue(
            CollisionEngine2D.point_line_collision(
                point, point_movement, line_segment, line_segment_movement
            )
        )
        
        point = Point2D(419, 233.215)
        point_movement = Point2D(1, -4.2475) 
        line_segment = LineSegment2D(
            Point2D(373, 231),
            Point2D(640, 231)
        ) 
        line_segment_movement = Point2D(0, -1)
        
        self.assertTrue(
            CollisionEngine2D.point_line_collision(
                point, point_movement, line_segment, line_segment_movement
            )
        )
        
        point = Point2D(375, 232.454)
        point_movement = Point2D(1, 5.5715) 
        line_segment = LineSegment2D(
            Point2D(308, 235),
            Point2D(524, 235)
        ) 
        line_segment_movement = Point2D(0, -1)
        
        self.assertTrue(
            CollisionEngine2D.point_line_collision(
                point, point_movement, line_segment, line_segment_movement
            )
        )
        
        point = Point2D(375, 232.454)
        point_movement = Point2D(1, 0) 
        line_segment = LineSegment2D(
            Point2D(308, 235),
            Point2D(524, 235)
        ) 
        line_segment_movement = Point2D(0, -5)
        
        self.assertTrue(
            CollisionEngine2D.point_line_collision(
                point, point_movement, line_segment, line_segment_movement
            )
        )
        
        
if __name__ == "__main__":
    """
    Main function for testing
    """
    # ### Simplest unit test
    # unittest.main()
    
    # ### Passing arguments into unit test
    # suite = unittest.TestSuite()
    # suite.addTest(TestPoint2D('test_point2d_declearation', [10, 5, 5, 0]))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    
    # ### Using test suite
    # test_module.setUpModule = setUpModule
    # test_module.tearDownModule = tearDownModule
    suite_point2d = unittest.TestLoader().loadTestsFromTestCase(TestPoint2D)
    suite_line2d = unittest.TestLoader().loadTestsFromTestCase(TestLine2D)
    suite_line_segment2d = unittest.TestLoader().loadTestsFromTestCase(
        TestLineSegment2D
    )
    suite_collision_engine2d = unittest.TestLoader().loadTestsFromTestCase(
        TestCollisionEngine2D
    )
    
    suite = unittest.TestSuite([
        suite_point2d,
        suite_line2d,
        suite_line_segment2d,
        suite_collision_engine2d,
        ])
    # unittest.TextTestRunner().run(suite)
    unittest.TextTestRunner(verbosity=2).run(suite)