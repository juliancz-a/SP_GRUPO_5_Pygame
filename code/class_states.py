class States:
    def __init__(self) -> None:
        self.button = {
            "button_draw" : False,
            "button_option" : None

        }
        self.quit = False

    
    def select_option(self, button):
        self.button["button_option"] == button[0]