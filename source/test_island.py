import unittest
from source import island_generator


class TestGenerateMap(unittest.TestCase):

    # generate한 list가 존재하는지
    def test_generate_island_exist(self):
        I = island_generator.Island(10, 10)
        expect = 10
        self.assertEqual(len(I.generateIsland(10)), expect)

    # island의 갯수가 격자의 용량과 같은지
    def test_generate_island_size(self):
        I = island_generator.Island(10, 10)
        expect = 10
        self.assertEqual(expect, len(I.generateIsland(10)))

    # island 삭제 후 리스트의 크기가 다른지
    def test_remove_island(self):
        I = island_generator.Island(10, 10)
        island_list = I.generateIsland(10)
        list_size = len(island_list)
        self.assertGreater(list_size, len(I.removeIsland(3)))

    # island가 x,y 범위 이내에 존재하는지
    def test_cotains(self):
        I = island_generator.Island(10, 10)
        I.generateIsland(10)
        result = I.cotains(5,5)
        expect = 0
        self.assertGreater(result, expect)