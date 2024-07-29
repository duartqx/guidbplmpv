import gi
gi.require_version("Gtk", "4.0")
gi.require_version('Adw', '1')
gi.require_version('GdkX11', '4.0')
from gi.repository import Gdk, GdkX11, Gtk, Adw
from mpv import MPV

import locale
locale.setlocale(locale.LC_NUMERIC, "C")

def get_player(win_id: str) -> MPV:
    player = MPV(
        wid=win_id,
        input_default_bindings=True,
        input_vo_keyboard=True,
        osc=True,
    )

    @player.key_binding("q")
    def _(state, name, char):
        player.stop()

    return player

class MainWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here   pass
        self.player = None

        self.styles_manager = Adw.StyleManager.get_default()
        self.styles_manager.set_color_scheme(Adw.ColorScheme.PREFER_DARK)

        self.set_title("My GTK Hello World")
        box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        styles_manager = Adw.StyleManager.get_default()
        styles_manager.set_color_scheme(Adw.ColorScheme.PREFER_DARK)

        drawing_area = Gtk.DrawingArea()
        drawing_area.set_vexpand(True)
        drawing_area.set_hexpand(True)

        self.set_content(drawing_area)

        drawing_area.realize()

        x11_surface = GdkX11.X11Surface.get_xid(self.get_surface())

        def play(btn: Gtk.Button):
            if self.player is not None:
                return

            self.player = get_player(x11_surface)

            @self.player.key_binding("f")
            def _(state, name, char):
                self.fullscreen()

            self.player.wait_until_playing("/home/duartqx/Media/Videos/[ASW] Kaijuu 8-gou - 01 [1080p HEVC][DCC2A44E].mkv")

            self.player = None

        playbutton = Gtk.Button(label="Play")
        playbutton.connect("clicked", play)

        box1.append(playbutton)

        self.set_content(box1)

        self.present()

class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = App(application_id="com.duartqx.GuiDbPlMPV")
app.run(None)

