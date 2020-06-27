################################################################################
#Мой экран

screen grid_game:
    ## Таймер. Если включен автоматический режим, то каждую секунду расчитывает новое поле
    timer 1.0 action If ((world.automatic_step and world.game_start and not world.game_end), Function(world.evolution),Function(lambda: None)) repeat True

    ## Игровой мир, если игра не началась и не закончилась(режим настройки), то по нажатию на элемет сетки меняетсяс состояние
    grid world.size world.size xalign 0.5 yalign 0.5 spacing 1:

        for cell_num in range(world.cell_count):
            imagebutton xalign 0.05*world.size yalign 0.05*world.size:
                idle (world.cell_im(cell_num))
                hover (world.cell_im(cell_num))

                action If(not world.game_start and not world.game_end, If( world.IsLifeNum(cell_num), Function(world.__setitem__, cell_num, 0), Function(world.__setitem__, cell_num, 1) ) )

    #Кнопки управления
    vbox xpos 0.75 ypos 0.65:
        textbutton If(world.automatic_step,"Режим: автоматический","Режим: пошаговый") text_color "#ffff00" action ToggleVariable("world.automatic_step")

        textbutton "Увеличить поле"  text_color "#ffff00" action If ((not world.game_end and not world.game_start), Function(world.Change_size, world.size+1))

        textbutton "Уменьшить поле"  text_color "#ffff00" action If ((not world.game_end and not world.game_start), Function(world.Change_size, world.size-1))

        textbutton "Эволюция" text_color "#ffff00" action If ((not world.automatic_step and world.game_start), Function(world.evolution),Function(lambda: None))

        textbutton If(world.game_start,"Пауза","Старт") text_color "#ffff00" action ToggleVariable("world.game_start")

        textbutton "Завершить игру" text_color "#ffff00" action Function(world.Check_end_game, forcible=True)
