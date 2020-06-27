init -5 python:
    ## Класс игровой сетки
    ## Все ячейки сетки имеют номера от 0 до n-1. Нумерация происходит построчно слева направо:
    ## Пример сетки 3x3:  0 1 2
    ##                    3 4 5
    ##                    6 7 8
    ## Живые клетки обозначаются единицей, мертвые нулем


    class world_game:

        ## Определяем размер и изображения для живой и мертовй ячейки, создаем игровую сетку
        def __init__(self, _size, life_im, death_im):
            self.life_im  = life_im
            self.death_im = death_im
            self.__size  =  _size
            self.world = [[0] * self.__size for i in range(self.__size)]
            ## Настраиваем параметры игры
            self.automatic_step = False
            self.game_start = False
            self.game_end = False

        ## Количество элементов сетки
        @property
        def cell_count(self):
            return  self.__size*self.__size

        ## Функции доступа по номерам элементов сетки
        def __getitem__(self, _key):
            return self.world[_key // self.__size][_key % self.__size]

        def __setitem__(self,_key, _value):
            self.world[_key //  self.__size][_key %  self.__size] = _value

        ## Геттер и сеттер размера
        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, _size):
            if   (_size >=3  and  _size <= 15):
                self.__size  = _size
                self.__resize_world()

        def Change_size(self,_size):
            self.size=_size

        ## Проверка клетки
        def IsLifeNum(self,num):
            return self[num]==1

        def IsLife(self,row,col):
            return self.world[row][col]==1

        ## Проверка конца игры, forcible = True - полное завершение игры по кнопке,
        ## Иначе переходим в режим настройки, если поле чисто
        def Check_end_game(self, forcible):
            if forcible:
                self.game_start = False
                self.game_automatic_step = False
                self.game_end   = True
                return "game_end"
            elif (self.__IsClearWorld()):
                self.game_start = False
                self.game_end   = False
                return "all_death"

        ## Проверка поля на пустоту
        def __IsClearWorld(self):
            zeroWorld = [[0] * self.__size for i in range(self.__size)]
            return self.world==zeroWorld


        ## Функция меняющая размер поля
        def __resize_world(self):
            self.world = [[0] * self.__size for i in range(self.__size)]

        ## Функция возвращающая изображение для данной ячейки, живое или мертвое изображение
        def cell_im(self, num_cell):
            return self.life_im if self[num_cell] else self.death_im

        ## Перерасчет состояния поля
        def evolution(self):
            mat_neighbours = self.__neighbours_count_for_all()

            for i in range(self.__size):
                for j in range(self.__size):
                    self.__new_life(i, j, mat_neighbours[i][j])
                    self.__cell_death(i, j, mat_neighbours[i][j])
            self.Check_end_game(forcible = False)

        ## Правила изменения клеток
        def __new_life(self, row, col, neighbours):
            if(self.world[row][col] == 0 and neighbours == 3):
                self.world[row][col] = 1


        def __cell_death(self, row, col, neighbours):
            if(self.world[row][col] == 1 and (neighbours < 2 or neighbours > 3)):
                self.world[row][col] = 0

        ## Считаем соседей для всех ячеек
        def __neighbours_count_for_all(self):
            mat_neighbours=[[0] * self.__size for i in range(self.__size)]

            for i in range(self.__size):
                for j in range(self.__size):
                    mat_neighbours[i][j] = self.__neighbours_count_for_cell(i,j)

            return mat_neighbours

        ## Считаем соседей для одной ячейки, если ячейка сама активна, ее надо вычесть из конечного числа соседей
        def __neighbours_count_for_cell(self,row,col):
            neighbours=0

            for i in row-1, row, (row+1) % self.__size:
                neighbours+=sum(self.world[i][col-1:(col+2) % self.__size])

            if(self.IsLife(row,col)):
                neighbours-=1
            return neighbours
