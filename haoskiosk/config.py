# pyright: reportUndefinedVariable=false
config.load_autoconfig(False)
c.statusbar.show = 'never'
c.tabs.show = 'never'
c.tabs.tabs_are_windows = True
c.window.hide_decoration = True
c.zoom.levels = ['150%']
c.zoom.text_only = False
c.zoom.default = '150%'
c.colors.webpage.preferred_color_scheme = 'dark'
config.unbind('<F11>', mode='normal')
config.bind('<Escape>', 'mode-enter passthrough')
config.unbind('<Shift-Escape>', mode='passthrough')
c.input.mode_override = 'passthrough'
