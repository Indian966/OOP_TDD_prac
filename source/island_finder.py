import island_generator

class IslandFinder(island_generator.Island):

    def __init__(self):
        pass

    def finder(self):
        I = island_generator.Island(10, 10)

        # map 생성
        I.generateMap()

        # island 생성
        print(I.generateIsland(10))
        print(I.map)

        # island 3개 제거
        print(I.removeIsland(3))

        # 5,5 범위 안에 있는 island 갯수 출력
        print(I.cotains(5,5))

        # 파일에 저장
        f = open('Island_Map.txt', 'w')
        for i in I.map:
            arr = str(i) + "\n"
            f.write(arr)
        f.close()


if __name__ == "__main__":
    i = IslandFinder()
    i.finder()

