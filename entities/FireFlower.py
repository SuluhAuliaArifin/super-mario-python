from entities.EntityBase import EntityBase

class FireFlower(EntityBase):
    def __init__(self, screen, spriteCollection, x, y, level, sound, gravity=0):
        super(FireFlower, self).__init__(x, y + 32, gravity)  # mulai di dalam blok
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.animation = self.spriteCollection.get("FireFlower").animation
        self.level = level
        self.sound = sound
        self.alive = True
        self.target_y = y  # posisi akhir bunga
        self.vel = 2       # kecepatan naik

    def update(self, cam):
        if self.alive:
            # animasi naik ke target_y
            if self.rect.y > self.target_y:
                self.rect.y -= self.vel
            self.animation.update()
            self.screen.blit(self.animation.image, (self.rect.x + cam.x, self.rect.y))
