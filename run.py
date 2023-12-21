import pygame

fps = 60

# one open window
class window_instance:
    def __init__(self):
        self.screen_dimensions = (720, 480)
        self.background_color = (255, 255, 255)
        self.default_text_color = (0, 0, 0)

        return
    
    def open_window(self):
        # setup pygame
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_dimensions, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        return

# one open file
class file_instance:
    # setup the file
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ""
        self.cursor_index = 0
        self.selection = (self.cursor_index, self.cursor_index)
        self.keys = []

        return
    
    def read_keyboard(self):
        # read keyboard
        keys = pygame.key.get_pressed()

        # check for key combinations
        if keys[pygame.constants.K_BACKSPACE]:
            # delete highlighted area
            self.delete_selected_text()

        return

    def insert_text():
        return
    
    def delete_selected_text(self):
        # delete
        self.text = self.text[:self.selection[0]] + self.text[self.selection[1]:]

        # update selection
        self.selection = (self.selection[0], self.selection[0])

# run the editor
def run():
    # setup editor
    window = window_instance()
    window.open_window()

    # setup file
    font = pygame.font.SysFont("monospace", 20)
    text = "Hello World!"

    # run editor
    running = True

    # game loop
    while running:
        # poll events
        for event in pygame.event.get():
            # if quit requested
            if event.type == pygame.QUIT:
                # stop program
                running = False
            # if video resize requested
            elif event.type == pygame.VIDEORESIZE:
                # resize screen
                window.screen_dimensions = (event.w, event.h)
        
        # get keys
        keys = pygame.key.get_pressed()

        # check for 'a' key
        if keys[pygame.constants.K_a] == True:
            # update text
            text += "a"

        # update label
        label = font.render(text, True, window.default_text_color)
        
        # clear frame buffer
        window.screen.fill(window.background_color)

        # draw text
        window.screen.blit(label, (0, 0))

        # update screen
        pygame.display.flip()

        # ensure framerate does not excede maximum
        window.clock.tick(fps)
    
    # quit program
    pygame.quit()

    return
