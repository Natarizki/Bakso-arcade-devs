import pygame, sys, json, os, random
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bakso Bangi Arcade")
font = pygame.font.SysFont(None, 32)

hard_mode_unlocked = False

def draw_text(text, x, y, color=(255,255,255)):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def bakso_clicker():
    coins = 0
    click_btn = pygame.Rect(200, 150, 200, 80)
    exit_btn = pygame.Rect(WIDTH//2 - 60, HEIGHT - 60, 120, 40)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((50, 30, 30))
        draw_text("Bakso Clicker", 40, 40)
        draw_text(f"Coins: {coins}", 40, 80)
        pygame.draw.rect(screen, (200, 100, 100), click_btn)
        pygame.draw.rect(screen, (100, 200, 100), exit_btn)
        draw_text("Click Bakso!", click_btn.x + 40, click_btn.y + 25)
        draw_text("Exit", exit_btn.x + 35, exit_btn.y + 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if click_btn.collidepoint(event.pos): coins += 1
                if exit_btn.collidepoint(event.pos): running = False
        pygame.display.flip()
        clock.tick(30)

def horror_escape():
    escaped = False
    escape_btn = pygame.Rect(200, 150, 200, 80)
    exit_btn = pygame.Rect(WIDTH//2 - 60, HEIGHT - 60, 120, 40)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((20, 20, 20))
        draw_text("Horror Escape", 40, 40)
        if escaped:
            draw_text("You Escaped!", 200, 100)
        pygame.draw.rect(screen, (150, 0, 0), escape_btn)
        pygame.draw.rect(screen, (100, 100, 100), exit_btn)
        draw_text("Escape!", escape_btn.x + 60, escape_btn.y + 25)
        draw_text("Exit", exit_btn.x + 35, exit_btn.y + 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if escape_btn.collidepoint(event.pos): escaped = True
                if exit_btn.collidepoint(event.pos): running = False
        pygame.display.flip()
        clock.tick(30)

def train_to_bali():
    distance = 0
    move_btn = pygame.Rect(200, 150, 200, 80)
    exit_btn = pygame.Rect(WIDTH//2 - 60, HEIGHT - 60, 120, 40)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((30, 30, 60))
        draw_text("Train to Bali", 40, 40)
        draw_text(f"Distance: {distance} km", 40, 80)
        pygame.draw.rect(screen, (0, 150, 200), move_btn)
        pygame.draw.rect(screen, (200, 100, 100), exit_btn)
        draw_text("Move Train", move_btn.x + 50, move_btn.y + 25)
        draw_text("Exit", exit_btn.x + 35, exit_btn.y + 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if move_btn.collidepoint(event.pos): distance += 10
                if exit_btn.collidepoint(event.pos): running = False
        pygame.display.flip()
        clock.tick(30)

def bakso_runner():
    steps = 0
    run_btn = pygame.Rect(200, 150, 200, 80)
    exit_btn = pygame.Rect(WIDTH//2 - 60, HEIGHT - 60, 120, 40)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((20, 60, 20))
        draw_text("Bakso Runner", 40, 40)
        draw_text(f"Steps: {steps}", 40, 80)
        pygame.draw.rect(screen, (0, 200, 100), run_btn)
        pygame.draw.rect(screen, (200, 50, 50), exit_btn)
        draw_text("Run!", run_btn.x + 80, run_btn.y + 25)
        draw_text("Exit", exit_btn.x + 35, exit_btn.y + 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if run_btn.collidepoint(event.pos): steps += 1
                if exit_btn.collidepoint(event.pos): running = False
        pygame.display.flip()
        clock.tick(30)

def bakso_warung_dusun():
    bowls = 0
    serve_btn = pygame.Rect(200, 150, 200, 80)
    exit_btn = pygame.Rect(WIDTH//2 - 60, HEIGHT - 60, 120, 40)
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((60, 40, 20))
        draw_text("Bakso Warung Dusun", 40, 40)
        draw_text(f"Bowls Served: {bowls}", 40, 80)
        pygame.draw.rect(screen, (150, 100, 50), serve_btn)
        pygame.draw.rect(screen, (100, 200, 100), exit_btn)
        draw_text("Serve Bakso", serve_btn.x + 40, serve_btn.y + 25)
        draw_text("Exit", exit_btn.x + 35, exit_btn.y + 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if serve_btn.collidepoint(event.pos): bowls += 1
                if exit_btn.collidepoint(event.pos): running = False
        pygame.display.flip()
        clock.tick(30)
def leaderboard_viewer():
    clock = pygame.time.Clock()
    back_button = pygame.Rect(WIDTH//2 - 60, HEIGHT - 80, 120, 50)
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as f:
            scores = json.load(f)
    else:
        scores = []

    running = True
    while running:
        screen.fill((20, 20, 20))
        draw_text("🏆 Leaderboard - Top Levels", WIDTH//2 - 120, 40)
        for i, score in enumerate(scores):
            draw_text(f"{i+1}. Level {score}", WIDTH//2 - 60, 100 + i * 40)

        pygame.draw.rect(screen, (200, 50, 50), back_button)
        draw_text("Back", back_button.x + 35, back_button.y + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False

        pygame.display.flip()
        clock.tick(30)

def main_menu():
    clock = pygame.time.Clock()
    buttons = [
        ("Bakso Clicker", bakso_clicker),
        ("Horror Escape", horror_escape),
        ("Train to Bali", train_to_bali),
        ("Bakso Runner", bakso_runner),
        ("Bakso Warung Dusun", bakso_warung_dusun),
        ("Kecap Tycoon", kecap_tycoon),
        ("Leaderboard", leaderboard_viewer),
        ("Exit", lambda: sys.exit())
    ]
    button_rects = []
    for i, (label, _) in enumerate(buttons):
        btn = pygame.Rect(180, 80 + i * 40, 240, 35)
        button_rects.append(btn)

    while True:
        screen.fill((40, 40, 60))
        draw_text("🎮 Bakso Bangi Arcade", WIDTH//2 - 140, 30)
        for i, (label, _) in enumerate(buttons):
            btn = button_rects[i]
            pygame.draw.rect(screen, (100 + i*20, 100, 200), btn)
            draw_text(label, btn.x + 40, btn.y + 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, (_, action) in enumerate(buttons):
                    if button_rects[i].collidepoint(event.pos):
                        action()

        pygame.display.flip()
        clock.tick(30)

main_menu()