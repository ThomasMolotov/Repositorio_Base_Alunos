import pygame

pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo som Pygame")
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))

    #aq vc desenha elementos gráficos
    pygame.display.update()

pygame.quit()