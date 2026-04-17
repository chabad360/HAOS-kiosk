"""
Add-on: HAOS Kiosk Display (haoskiosk)
File: qutebrowser_config.py
Version: 1.3.1
"""

import os
from qutebrowser.config import configexc


def _as_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    value = value.strip().lower()
    if value == "true":
        return True
    if value == "false":
        return False
    return default


def _as_int(value: str | None, default: int, minimum: int) -> int:
    try:
        parsed = int(value or default)
    except (TypeError, ValueError):
        return default
    return parsed if parsed >= minimum else default


config.load_autoconfig(False)

c.auto_save.session = False
c.url.default_page = "about:blank"
c.url.start_pages = ["about:blank"]
c.tabs.show = "never"
c.statusbar.show = "never"
c.window.hide_decoration = True

dark_mode = _as_bool(os.getenv("DARK_MODE"), True)
zoom_level = _as_int(os.getenv("ZOOM_LEVEL"), 100, 10)

c.colors.webpage.preferred_color_scheme = "dark" if dark_mode else "light"
c.zoom.default = f"{zoom_level}%"

for setting, value in (
    ("input.mode_override", "passthrough"),
    ("input.insert_mode.auto_load", True),
):
    try:
        config.set(setting, value)
    except configexc.Error as err:  # pragma: no cover
        print(f"[haoskiosk] qutebrowser setting skipped: {setting} ({err})")

for mode in ("normal", "passthrough"):
    config.bind("<Ctrl-r>", "reload", mode=mode)
    config.bind("<Ctrl-Left>", "back", mode=mode)
    config.bind("<Ctrl-Right>", "forward", mode=mode)

config.bind("<Ctrl-Alt-Escape>", "mode-enter normal", mode="passthrough")
config.bind("<Ctrl-Alt-t>", "open -t")
config.bind("<Ctrl-Alt-Shift-t>", "tab-close")
config.bind("<Ctrl-Alt-w>", "open -w")
config.bind("<Ctrl-Alt-Shift-w>", "close")
config.bind("<Ctrl-Alt-Left>", "tab-prev")
config.bind("<Ctrl-Alt-Right>", "tab-next")
