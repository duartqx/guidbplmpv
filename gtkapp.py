import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

def on(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("My GTK Hello World")
    win.present()

app = Gtk.Application(application_id="com.duartqx.GuiDbPlMPV")
app.connect("activate", on)
app.run(None)

