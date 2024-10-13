import pygame, os

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blabalalsfnjksdhaf;hsd")

img = pygame.image.load(os.path.join("img", "testtest.png"))
w = 600
h = 400
player = pygame.transform.scale(img, (600,400))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(player,(50,70))
    pygame.display.update()


pygame.quit()
