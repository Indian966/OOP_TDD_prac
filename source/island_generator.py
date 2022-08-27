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
        self.map = None
        self.max_island = m*n

    def generateMap(self):
        m = self.m
        n = self.n
        self.map = [[0]*m for _ in range(n)]
        return self.map

    # n개의 섬 생성
    def generateIsland(self, numb):
        #numb 10
        x = 0
        y = 0
        count = 0

        while True :
            if count == numb :
                break
            self.map[x][y] = 1
            self.max_island -= 1
            if self.max_island != 0 :
                y += 1
                if y == self.n:
                    x += 1
                    y = 0
            count += 1

        result = 0
        for i in self.map :
            result += i.count(1)

        return result

    # n개의 섬 삭제
    def removeIsland(self, n):
        rest_island = (self.m * self.n) - self.max_island
        count = 0
        x = 0
        y = 0

        if n > rest_island :
            return False
        while True :
            if count == n :
                break
            if self.max_island == 0 :
                x = self.m - 1
                y = self.n - 1
                self.map[x][y] = 0
            elif x == 0 :
                self.map[x - 1][self.m - 1] = 0
                x -= 1
                y = self.n - 1
            else :
                self.map[x][y - 1] = 0
                y -= 1
            self.max_island += 1
            count += 1

        return n

    # x,y 범위 이내에 있는 섬의 갯수
    def cotains(self, x, y):
        count = 0
        for i in range(x) :
            for j in range(y) :
                if self.map[i][j] == 1 :
                    count += 1
        return count

