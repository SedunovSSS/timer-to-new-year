import pygame, datetime as dt

pygame.init()
width, height = 800, 300 
fps = 60
font = pygame.font.SysFont('italic', 70, bold=True)
font1 = pygame.font.SysFont('italic', 40, bold=True) 
sc = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
pygame.display.set_caption("Days To New Year")
running = True
lang = 'en' # Language Russian 'ru' or English 'en'


while running:
    now = dt.datetime.today()
    newyear = dt.datetime(dt.datetime.now().year+1, 1, 1)
    d = newyear - now
    minutes, seconds = divmod(d.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days = d.days
    if lang == 'ru':
        text1, text2 = "До нового года осталось: ", f"{days} дней {hours} часов {minutes} минут {seconds} секунд."
    else:
        text1, text2 = "Until the new year is left: ", f"{days} days {hours} hours {minutes} minutes {seconds} seconds"

    sc.fill("black")
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    render = font.render(text1, 1, (0, 255, 0))
    render1 = font1.render(text2, 1, (0, 255, 0))
    sc.blit(render, (34, 65))
    sc.blit(render1, (34, 200))
    pygame.draw.rect(sc, (255, 0, 0), (0, 0, width, height), 20)
    pygame.display.flip()
    clock.tick(fps)

