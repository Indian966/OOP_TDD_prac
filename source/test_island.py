import unittest
from source import island_generator


class TestGenerateMap(unittest.TestCase):

    # generate한 list가 존재하는지
    def test_generate_island_size(self):
        I = island_generator.Island(10, 10)
        I.generateMap()
        expect = 10
        result = I.generateIsland(10)
        self.assertEqual(expect, result)

    # island 삭제 후 리스트의 크기가 다른지
    def test_remove_island(self):
        I = island_generator.Island(10, 10)
        I.generateMap()
        I.generateIsland(10)
        expect = 3
        result = I.removeIsland(3)
        self.assertEqual(expect, result)

    # island가 x,y 범위 이내에 몇개 존재하는지
    def test_cotains(self):
        I = island_generator.Island(10, 10)
        I.generateMap()
        I.generateIsland(20)
        expect = 10
        result = I.cotains(5,5)
        self.assertEqual(expect, result)