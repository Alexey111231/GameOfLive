###########################################
## Основной скрипт

##  Создаем игру
##  В цикле ждем взаимодействия, который закончит игру
##  Игровая логика находится в файле экрана и класса игры
###########################################
label start:


    $ world = world_game(15,"images/life.jpg","images/death.jpg")

    show screen grid_game
    label check:
        $ result = ui.interact()
        if world.game_end:
            hide screen grid_game
            jump end
    jump  check

    label end:
    "Конец игры"
    return
