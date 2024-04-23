import pygame
from Maze import Maze_duplicate
pygame.init()

font = pygame.font.Font(None, 32)
# m,n = map(int,input("nhap m n di:").split())
sc = pygame.display.set_mode((1200,600))
# Tạo một hộp nhập liệu


input_box = pygame.Rect(500, 280, 140, 32)  # Đặt hộp nhập liệu ở giữa cửa sổ
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
generated_maze = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    # Chuyển đổi text thành số và gọi hàm maze.generate_maze()
                    m, n = map(int, text.split('x'))
                    maze = Maze_duplicate(1200//m)
                    maze.generate_maze(sc)
                    text = ''
                    generated_maze = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                maze.tracePath((0,0),(m-1,n-1),maze.maze_map(),maze.grid_cells,sc)
                print(maze.maze_map())
    if not generated_maze:
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        sc.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(sc, color, input_box, 2)

    pygame.display.flip()

