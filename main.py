import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self, image, color_key, pos, *groups):
        super().__init__(*groups)
        self.image = image
        self.image.set_colorkey(color_key)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
        self.velocity_x = 60

    def update(self, fps):
        self.rect.move_ip(self.velocity_x / fps, 0)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Машинка')
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    sprites = pygame.sprite.Group()
    car = Car(pygame.image.load('data/car2.png'), (255, 255, 255), (0, 0), sprites)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if (car.rect.right == width and car.velocity_x > 0) or (car.rect.left == 0 and car.velocity_x < 0):
            car.velocity_x = -car.velocity_x
            car.image = pygame.transform.flip(car.image, True, False)
        sprites.update(fps)
        screen.fill((255, 255, 255))
        sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
