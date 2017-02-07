import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ApplicationWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Python-Vlc Media Player")
        self.player_paused = False
        self.is_player_active = False
        self.connect("destroy", Gtk.main_quit)

    def show(self):
        self.show_all()

    def setup_objects_and_events(self):
        self.playback_button = Gtk.Button()
        self.stop_button = Gtk.Button()

        self.play_image = Gtk.Image.new_from_icon_name(
                "gtk-media-play",
                Gtk.IconSize.MENU
        )
        self.stop_image = Gtk.Image.new_from_icon_name(
                "gtk-media-stop",
                Gtk.IconSize.MENU
        )
        self.playback_button.set_image(self.play_image)
        self.stop_button.set_image(self.stop_image)

        self.playback_button.connect("clicked", self.toggle_player_playback)
        self.stop_button.connect("clicked", self.stop_player)

        self.draw_area = Gtk.DrawingArea()
        self.draw_area.set_size_request(300, 300)
        self.draw_are.connect("realize", self._realized)

        self.hbox = Gtk.Box(spacing=6)
        self.hbox.pack_start(self.playback_button, True, True, 0)
        self.hbox.pack_start(self.stop_button, True, True, 0)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.vbox)
        self.vbox.pack_start(self.draw_area, True, True, 0)
        self.vbox.pack_start(slef.hbox, False, False, 0)

    def toggle_player_playback(self, widget, data=None):
        if self.is_player_active == False and self.player_paused == False:
            self.player.play()
            self.playback_button.set_image(self.pause_image)
            self.is_player_active = True
        elif self.is_player_active == True and self.player_paused == True:
            self.player.pause()
            self.playback_button.set_image(self.play_image)
            self.player_paused = True
        else:
            pass

    def stop_player(self, widget, data=None):
        self.player.stop()
        self.is_player_active = False
        self.playback_button.set_image(self.play_image)

if __name__ == '__main__':
    window = ApplicationWindow()
    window.setup_objects_and_events
    window.show()
    Gtk.main()
