from abc import *
import random


class AbstractMap(metaclass=ABCMeta):
    @abstractmethod
    def generateMap (self) :
        pass

    @abstractmethod
    def generateIsland(self):
        pass

    @abstractmethod
    def removeIsland(self):
        pass

    @abstractmethod
    def cotains(self):
        pass

class Island(AbstractMap) :
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.island_list = None

    def generateMap(self):
        m = self.m
        n = self.n
        map = [[0]*m for _ in range(n)]
        return map

    # n개의 섬 생성
    def generateIsland(self, numb):
        x_list = list(random.sample(range(0, self.m), numb))
        y_list = list(random.sample(range(0, self.n), numb))
        xy = []
        for i, j in zip(x_list, y_list):
            xy.append(tuple([i, j]))
        # xy.sort(key=lambda x: (x[0],x[1]))
        self.island_list = xy

        return self.island_list

    # n개의 섬 삭제
    def removeIsland(self, n):
        for i in range(n) :
            self.island_list.pop()
        return self.island_list

    # x,y 범위 이내에 있는 섬의 갯수
    def cotains(self, x, y):
        count = 0
        for i,j in self.island_list :
            if i <= x and j <= y :
                count += 1
        return count

