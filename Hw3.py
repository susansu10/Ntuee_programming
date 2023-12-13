import random
import abc
import os, sys
import time
from collections import deque

mmap = [['0' for j in range(12)] for i in range(12)]


def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')
    if 'ipykernel' in sys.modules:
        from IPython.display import clear_output as clear
        clear()

        
# Create Obstacle Way
def is_prime(num) -> int:
    if num <= 1:
        return 0
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return 0
    return 1


def generate_map():
    for i in range(1, 11) :
        for j in range(1, 11):
            if is_prime(i*10+j) == 1:
                mmap[i][j] = 'x'
            else:
                mmap[i][j] = '*'

    print("Original Map")
    little_world.output_map()

    
    
class little_world:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f'-> Welcome to [{self.name}] world !!')
        print()
        
    @staticmethod    
    def output_map():
        for i in range(0, 12) :
            for j in range(0, 12):
                print(mmap[i][j]," ", end='')
            print()
            
    @staticmethod
    def is_valid(i, j) -> int:
        return 1 <= i <= 10 and 1 <= j <= 10


    
class animal(abc.ABC):
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.start_i = 10
        self.start_j = 10
        self.direction = [(1,-1,0), (2,1,0), (3,0,-1), (4,0,1)] #(op:1,上 / op:2,下 / op:3,左 / op:4,右)
        
        if self.species == 'sheep':
            mmap[self.start_i][self.start_j] = 'S'
        else:
            mmap[self.start_i][self.start_j] = 'D'

    
    def info(self):
        print(f'-> Created a animal : [{self.species}] , name : [{self.name}], eat : [{self.food}]')
        print()

    @abc.abstractmethod
    def walk_eat(self):
        pass
    
        
class sheep(animal):
    
    def walk_eat(self):
        
        print("請輸入操作")
        operation = int(input())
        
        if (operation < 1 or operation > 4):
            print("輸入錯誤")
        else:
            for op, dx, dy in self.direction:
                if operation == op:
                    next_i, next_j = self.start_i+dx, self.start_j+dy
                    if ( little_world.is_valid(next_i, next_j) == 1) :
                        
                        if mmap[next_i][next_j] == '0' or mmap[next_i][next_j] == 'x':
                            print("Sheep Stop Move Facing Obstacle !")
                        elif mmap[next_i][next_j] == 'G':
                            print("Congrats ! Sheep eat it !")
                            mmap[next_i][next_j] = '$'
                            return 1
                        else:
                            print("Sheep Move !") # map[i][j] = '*'
                            mmap[self.start_i][self.start_j] = '*'
                            mmap[next_i][next_j] = 'S'
                            self.start_i, self.start_j = next_i, next_j
                        
                        little_world.output_map()
                    else:
                        print("超出邊界")
                        
                    return self.walk_eat()

                
class dog(animal):
    # Using BFS way to eat food 
    def walk_eat(self, food_i, food_j):
        self.direction = [(-1,0), (1,0), (0,-1), (0,1)]
        queue = deque([(self.start_i, self.start_j, 0)])

        visited = [[0 for j in range(12)] for i in range(12)]
        dis = [[-1 for j in range(12)] for i in range(12)]

        visited[self.start_i][self.start_j] = 1
        dis[self.start_i][self.start_j] = 0

        while len(queue) != 0 :
            (now_i, now_j, dist) = queue.popleft()

            # 如果可能走的路徑 queue 中剛好 pop 出的 i,j 正是目標，則找到路徑
            if now_i == food_i and now_j == food_j :
                print("Find the Path ! Min_dist = ", dist)
                self.print_path(dis, food_i, food_j)
                return 1

            # 把上下左右有可能走的 i, j, 要花費的距離存到 queue 中
            for dx, dy in self.direction:
                next_i, next_j = now_i+dx, now_j+dy
                if (little_world.is_valid(next_i, next_j) == 1):
                    if (visited[next_i][next_j] != 1) and mmap[next_i][next_j] != 'x' :
                        dis[next_i][next_j] = dist + 1
                        add_path_dist = dist + 1
                        queue.append((next_i, next_j, add_path_dist))
                        visited[next_i][next_j] = 1
                        if mmap[next_i][next_j] != 'M':
                            mmap[next_i][next_j] = 'B'
                        print("Dog Move !")
                        little_world.output_map()
    
    def print_path(self, dis, food_i, food_j):
        
        while dis[food_i][food_j] != 0:
            for dx, dy in self.direction:
                next_i, next_j = food_i+dx, food_j+dy
                if dis[next_i][next_j] == dis[food_i][food_j]-1:
                    mmap[next_i][next_j] = '$'
                    food_i = next_i
                    food_j = next_j
                    break
        mmap[food_i][food_j] = 'D'


   
    
class food:
    
    def __init__(self, food):
        self.food = food
        
    def info(self):
        print(f'-> Your anamal eat : [{self.food}]')
        print()
    
    def generate(self) -> tuple:
        i = 1
        while i != 0 :
            food_i = random.randint(1,11)
            food_j = random.randint(1,11)
            
            if(little_world.is_valid(food_i, food_j) == 1):
                if mmap[food_i][food_j] != 'x' and mmap[food_i][food_j] != 'S' and mmap[food_i][food_j] != 'D':
                    if self.food == 'grass':
                        mmap[food_i][food_j] = 'G'
                    else:
                        mmap[food_i][food_j] = 'M'
                    i = i - 1
        return food_i, food_j



if __name__ == '__main__':
    # print("---Start First Way---")
    # # Todo 1                    
    # generate_map()

    # your_world = little_world('Wonderland')
    # your_world.info()

    
    # your_sheep = sheep('Alice', 'sheep', 'grass')
    # your_sheep.info()

    # your_sheep_food = food('grass')
    # your_sheep_food.info()
    # your_sheep_food.generate()

    # little_world.output_map()

    
    # your_sheep.walk_eat()


    # little_world.output_map()

    # print("---Wait for 5 seconds, will change to second way---")
    # time.sleep(5)
    # clear_output()

    print("---Start Second Way---")
    generate_map()

    your_dog = dog('Bob', 'dog', 'meat')
    your_dog.info()

    your_dog_food = food('meat')
    your_dog_food.info()
    meat_i, meat_j = your_dog_food.generate()

    little_world.output_map()

    your_dog.walk_eat(meat_i, meat_j)
    little_world.output_map()

