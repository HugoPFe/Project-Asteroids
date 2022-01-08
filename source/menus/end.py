from menus.menus import Main
from ui import *
from media.paths import title_font
from components.constants import SCREEN_WIDTH, SCREEN_HEIGHT

# TODO: Modularization

class EndScreen(Main):
    """ Abstract class for End screens """

    def __init__(self, game):
        Main.__init__(self)

        # Fonts
        self.fonts = FontsGroup(screen=Main.screen, font_name=title_font,
                                size=45, color=(255, 255, 255), bg_color=(0, 0, 0))
        self.main_text = None
        self.score_text = Font(f'Pontuação: {game.player.score}', (SCREEN_WIDTH / 2, 180), 'center')

        # Buttons
        self.menu_button = RectangleButton(
            screen=Main.screen, 
            x=Main.screen_rect.centerx, y=460,
            width=110, height=40, label='Menu',
            padding=5, 
            callback=lambda: self.back_to_mainmenu()
        )

    def loop(self):
        self.fonts.render_fonts()
        self.render_buttons()

    def set_main_text(self, txt):
        self.main_text = Font(txt, (SCREEN_WIDTH / 2, 100), 'center')
        self.fonts.add_fonts(self.main_text, self.score_text)
        self.score_text.configure(size=30)

    def try_again(self, game):
        """ Break the game's loop and start a new game """

        self.back_to_mainmenu()
        self.change_screen(game.__class__) # TODO: temp


class GOScreen(EndScreen):
    def __init__(self, game):
        """ Class for Game Over screen """

        EndScreen.__init__(self, game)

        self.set_main_text('Game Over!')

        self.try_button = RectangleButton(
            screen=Main.screen, x=Main.screen_rect.centerx, y=400,
            width=130, height=50, label='Tentar\nnovamente',
            padding=17, callback=lambda: self.try_again(game)
        )

        self.add_buttons(self.try_button, self.menu_button)


class WinScreen(EndScreen):
    def __init__(self, game):
        """ Class for Win screen """

        EndScreen.__init__(self, game)

        self.set_main_text('Você Venceu!!')

        self.try_button = RectangleButton(
            screen=Main.screen, x=Main.screen_rect.centerx, y=400,
            width=130, height=50, label='Jogar\nnovamente',
            padding=17, callback=lambda: self.try_again(game)
        )

        self.add_buttons(self.try_button, self.menu_button)


__all__ = ['GOScreen', 'WinScreen']
