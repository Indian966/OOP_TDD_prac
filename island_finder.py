import random
import island_generator

class IslandFinder(island_generator.Island):

    def __init__(self):
        pass

    def finder(self):
        I = island_generator.Island(10, 10)

        # map 생성
        map = I.generateMap()

        # island 생성
        island_list = I.generateIsland(10)
        print(island_list)

        # map에 island 표시
        for x, y in island_list:
            map[x][y] = 1

        # island 3개 제거
        print(len(I.removeIsland(3)))
        print(I.removeIsland(3))

        # 5,5 범위 안에 있는 island 갯수 출력
        print(I.cotains(5,5))

        # 파일에 저장
        f = open('Island_Map.txt', 'w')
        for i in map:
            arr = str(i) + "\n"
            f.write(arr)
        f.close()


if __name__ == "__main__":
    i = IslandFinder()
    i.finder()

