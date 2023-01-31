

class MicrocontrollerInterface:
    tray_open = None

    def __init__(self, tray_closed_callback):
        self.tray_closed_callback = tray_closed_callback

    def open_tray(self, tray: int):
        self.tray_open = tray

    def close_tray(self):
        self.tray_open = None
        self.tray_closed_callback()


def open_tray(tray: int):
    print(f"tray {tray} opened! please close it :)")
