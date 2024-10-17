import pygame
import pygame_gui
import time
import random
import screens
import functions
import classes

pygame.init()

global WIDTH, HEIGHT
global WIN
global start_button


def main():
    clock = pygame.time.Clock()
    run = True
    active = False
    game_state = "home_screen"
    color_passive = pygame.Color('gray15')
    color_active = pygame.Color('lightskyblue3')
    color = color_passive
    name = 'Type name'
    font = pygame.font.SysFont('comicsansms',40)
    name_box = pygame.Rect(250,725/2,300,50)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break


            if game_state == "home_screen":
                screens.draw_home_screen()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_BACKSPACE]:
                    player_x = 200
                    player_y = 400
                    game_state = "lobby"
                    game_over = False


            elif game_state == "lobby":
                WIN = screens.draw_lobby()
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                #MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
                #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

                scarlet_button = classes.Button(image=pygame.image.load("images/miss scarlet.JPG"), pos=(800*.1, 725*.1), 
                                    text_input="MISS SCARLET", font=font, base_color="#d7fcd4", hovering_color="White")
                #OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                 #                   text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                #QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                 #                   text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if scarlet_button.checkForInput(MENU_MOUSE_POS):
                        print('selected Miss Scarlet')
                    elif name_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                    color = color_active if active else color_passive
                if event.type == (pygame.KEYDOWN or pygame.TEXTINPUT):
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        else:
                            name += event.unicode
                pygame.draw.rect(WIN,color,name_box,3)
                surf = font.render(name,True,color)
                WIN.blit(surf,(name_box.x+5, name_box.y-5))
                name_box.w = max(300, surf.get_width()+10)
                if event.type == pygame.K_SPACE:
                    player_x = 200
                    player_y = 400
                    game_state = "game_screen"
                    game_over = False
                pygame.display.flip()


            elif game_state == "game_screen":
                screens.draw_game_screen()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_BACKSPACE]:
                    player_x = 200
                    player_y = 400
                    game_state = "end_screen"
                    game_over = False


            elif game_state == "end_screen":
                screens.draw_end_screen()
        
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()

