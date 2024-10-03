import sys
import pygame

def printall(list):
    for cell in list:
        print(cell)

def start_screen(filename):
    """
    Returns the pygame reference of the screen to use with screen.blit.
    """
    with open(filename, "rt") as f:
        # Skip the first two lines (P3 and comment line)
        f.readline()
        f.readline()

        # Clean the line before splitting
        width, height = map(int, ''.join(f.readline().split('\x00'))[:-1].split(' '))
        
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("PPM Image Viewer")

    return screen, width, height


# trying to change it so that over a single loop
def decode(filename):
    file = open(filename, 'rt')
    screen, width, height = start_screen(filename)
    y = 0; x = 0

    surface = pygame.Surface((width, height))

    file.readline()
    file.readline()
    file.readline()
    file.readline()
    file.readline()

    for line in file.readlines():
        if line.split('\x00')[1] == '\n' or line == ['']: continue

        r, g, b = map(int, ''.join(line.split('\x00'))[:-1].split(' '))
        color = pygame.Color(r, g, b, 255) 
        surface.set_at((x, y), color)

        y = y + 1 if x >= width else y
        x = x + 1 if x <  width else 0
    file.close()

    screen.blit(surface, (0,0))
    pygame.display.flip()

    #run the thing endlessly
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

    pygame.quit()

#['ÿþP3']

if len(sys.argv) != 2:
    print("Uso: python ppm_runner.py <nombre_del_archivo_ppm>")
    sys.exit(1)

filename = sys.argv[1]

decode(filename)