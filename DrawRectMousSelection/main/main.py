import pygame as pg

pg.init()

sc = pg.display.set_mode((500,500))

clock = pg.time.Clock()

pg.mouse.set_visible(False)

start_cords = None

def DRAW_RECT(x,y,w,h):
    pg.draw.rect(sc,(0,0,0), (x, y, w, h),1)

sc.fill((255,255,255))
pg.display.update()

while True:
    clock.tick(60)

    keys_mouse = pg.mouse.get_pressed()

    sc.fill((255,255,255))

    pos = pg.mouse.get_pos()

    if pg.mouse.get_focused():
        pg.draw.circle(sc, (0,0,0), pos, 7)
        

    if keys_mouse[0]:
        if start_cords is None:
            start_cords = pg.mouse.get_pos()

        move_cords = pg.mouse.get_pos()

        width = (move_cords[0] - start_cords[0])* -1 if move_cords[0] - start_cords[0] < 0 else move_cords[0] - start_cords[0]  

        height = (move_cords[1] - start_cords[1]) * -1 if move_cords[1] - start_cords[1] < 0 else move_cords[1] - start_cords[1]

        if start_cords[0] < move_cords[0]:
            if start_cords[1] < move_cords[1]:
                #right down
                DRAW_RECT(start_cords[0], start_cords[1], width, height)

            elif start_cords[1] > move_cords[1]:
                #right up
                DRAW_RECT(start_cords[0], move_cords[1], width, height)

        elif start_cords[0] > move_cords[0]:
            if start_cords[1] < move_cords[1]:

                #left down
                DRAW_RECT(move_cords[0], start_cords[1], width,height)

            elif start_cords[1] > move_cords[1]:
                #left up
                DRAW_RECT(move_cords[0], move_cords[1], width, height)

    elif keys_mouse[0] == False:
        start_cords = None

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()