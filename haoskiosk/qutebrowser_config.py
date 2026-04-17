import os

config.load_autoconfig(False)

ha = os.getenv("HA_URL", "http://localhost:8123").strip()
start_page = ha + "/" + os.getenv("HA_DASHBOARD", "").strip()

c.url.start_pages = [start_page]
c.url.default_page = start_page
c.auto_save.session = False

c.window.hide_decoration = True
c.tabs.show = "never"
c.statusbar.show = "never"

c.input.insert_mode.auto_load = True
# c.input.mode_override = "passthough"
c.input.forward_unbound_keys = "auto"

c.qt.chromium.sandboxing = "disable-all"

zoom_level = os.getenv("ZOOM_LEVEL", "100").strip()
try:
    c.zoom.default = f"{max(10, int(zoom_level))}%"
except ValueError:
    c.zoom.default = "100%"

# Keep compatibility with existing gesture/REST xdotool shortcuts.
c.bindings.default = {}
c.bindings.commands = {
    "normal": {
        "<Ctrl-r>": "reload",
        "<Ctrl-Left>": "back",
        "<Ctrl-Right>": "forward",
    }
}

with config.pattern(ha + '/*') as p:
    p.content.media.audio_capture = True