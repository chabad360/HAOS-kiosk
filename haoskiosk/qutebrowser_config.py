import os

config.load_autoconfig(False)

c.url.start_pages = ["about:blank"]
c.url.default_page = "about:blank"
c.auto_save.session = False

c.window.hide_decoration = True
c.tabs.show = "never"
c.statusbar.show = "never"

c.input.insert_mode.auto_enter = True
c.input.insert_mode.auto_leave = True
c.input.insert_mode.auto_load = True
c.input.forward_unbound_keys = "auto"

zoom_level = os.getenv("ZOOM_LEVEL", "100").strip()
try:
    c.zoom.default = f"{max(10, int(zoom_level))}%"
except ValueError:
    c.zoom.default = "100%"

# Keep compatibility with existing gesture/REST xdotool shortcuts.
config.bind("<Ctrl-r>", "reload")
config.bind("<Ctrl-Left>", "back")
config.bind("<Ctrl-Right>", "forward")
