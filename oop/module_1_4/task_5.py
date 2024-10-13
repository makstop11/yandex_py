class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data: list):
        self.data = data

    # draw - рисовать
    def draw(self):
        for num in self.data:
            start = Graph.LIMIT_Y[0]
            end = Graph.LIMIT_Y[1]

            # if num >= start and num <= end:
            if start <= num <= end:
                print(num, end=' ')
        print()

graph_1 = Graph()

first_data: list[int] = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]

# set - установить data - данные
graph_1.set_data(first_data)
graph_1.draw()
