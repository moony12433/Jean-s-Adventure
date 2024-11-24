import pygame
import sys
import random
pygame.init()
font = pygame.font.SysFont(None, 36)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jean's adventure")

jellyfish_img = pygame.image.load(f"Jellyfish1.png").convert_alpha()
jellyfish_img = pygame.transform.scale(jellyfish_img,(15, 15))

jellyfish_x = SCREEN_WIDTH /2 -6
jellyfish_y = SCREEN_HEIGHT /2 -30

jean_x = SCREEN_WIDTH / 2 - 6
jean_y = SCREEN_HEIGHT / 2 - 30

gravity = 900
velocity_y = 0

jean_size = 50
jump_power = -650

jean_img = pygame.image.load(f"jean.png").convert_alpha()
jean_img = pygame.transform.scale(jean_img, (50, 50))
3
frame = 0

Hotel_Wall_img = pygame.transform.scale(
	pygame.image.load(f"Hotel_Wall2.png").convert(),
	(SCREEN_WIDTH, SCREEN_HEIGHT)
)
Hotel_Wall_imgX = 0

speed = 30

platform_width = 100
platform_height = 25

platform_list = []

platform_img = pygame.image.load(f"couch.png")
platform_img = pygame.transform.scale(platform_img, (platform_width, platform_height))

num_platforms = 2

#pygame.rect(400, 600, 128, 10)

def update_jean(delta):
	global jean_img, jean_x, jean_y, font, velocity_y

	velocity_y += gravity * delta
	jean_y += velocity_y * delta

	key_pressed = pygame.key.get_pressed()
	if key_pressed[pygame.K_a]:
		jean_x -= 5
	elif key_pressed[pygame.K_d]:
		jean_x += 5
	if jean_y >850:
		jean_y = 200
		jean_x = 400
	jean = pygame.Rect(jean_x, jean_y, jean_img.get_width(), jean_img.get_height())

	for platform in platform_list:
		if jean.colliderect(pygame.Rect(platform[0], platform[1], platform_width, platform_height)):
			jean_y = platform[1] - jean_img.get_height() #platform[1] stores the platform's y coordinate
			velocity_y = 0
			if key_pressed[pygame.K_SPACE]:
				velocity_y = jump_power

def redrawWindow():
	screen.fill('black')
	screen.blit(Hotel_Wall_img, (Hotel_Wall_imgX,0))

#def updatejellyfish(delta):
	#global jellyfish_img, jellyfish_x, jellyfish_y
	#jellyfish = pygame.Rect(jellyfish_x, jellyfish_x, jellyfish_img.get_width(), jellyfish_img.get_height())
	#if jellyfish.collidedict(pygame.Rect(jean_x, jean_y, jean_img.get_width(), jean_img.get_height())):
		#unning = False
		#pygame.quit()
		#ƒsys.exit()

def draw_setting():
	global jean_x
	print(len(platform_list))
	for platform in platform_list:
		# screen.blit is how you draw one surface (like images) onto another (like our window)
		screen.blit(platform_img, (platform[0], platform[1], platform_width, platform_height))
		#pygame.draw.rect(screen, "white", (platform[0], platform[1], platform_width, platform_height))
		

def generate_platforms():
	platform_list.append((400, 600))
	platform_list.append((200, 400))
	platform_list.append((400, 200))

def game_loop():
	global Hotel_Wall_img, jean_img, jean_x, jean_y, font, velocity_y, Hotel_Wall_imgX, jellyfish_img, jellyfish_x, jellyfish_y
	clock = pygame.time.Clock()
	clock.tick(speed)
	Hotel_Wall_imgX -= 1
	if Hotel_Wall_imgX <Hotel_Wall_img.get_width() * -1:
		Hotel_Wall_imgX = Hotel_Wall_img.get_width()
	#delta = 0

	running = True
	while running:
		delta = clock.tick(60) / 1000

		redrawWindow()
		draw_setting()
		update_jean(delta)
		#updatejellyfish(delta)

		# Here is an instance of event handling, checking if the user wants to exit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				sys.exit()
		
		screen.blit(jean_img, (jean_x, jean_y))
		pygame.display.flip()


generate_platforms()
game_loop()