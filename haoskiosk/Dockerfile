################################################################################
# Add-on: HAOS Kiosk Display (haoskiosk)
# File: Dockerfile
# Version: 1.3.1
# Copyright Jeff Kosowsky
# Date: April 2026
################################################################################

ARG BUILD_FROM=ghcr.io/home-assistant/base:latest
FROM $BUILD_FROM

ARG BUILD_VERSION
ENV ADDON_VERSION=${BUILD_VERSION}

COPY <<EOF /etc/apk/repositories 
https://dl-cdn.alpinelinux.org/alpine/edge/main 
https://dl-cdn.alpinelinux.org/alpine/edge/community
EOF

RUN cat /etc/apk/repositories >&2

#===============================================================================
##### Install X, Browser and all necessary dependencies
RUN apk update && apk upgrade --no-cache\
     && apk add --no-cache \
## Xserver and graphics
     xorg-server \
     xf86-video-modesetting \
     mesa-dri-gallium \
     mesa-egl \
     mesa-gles \
     libdrm \
     mesa-vulkan-intel \
     vulkan-loader \
### X utils
     xdotool \
     xinput \
     xrandr \
     xset \
#     xev \
     libxkbcommon \
     setxkbmap \
### Input, udev
     xf86-input-libinput \
     libinput \
#     libinput-tools \
     udev \
     libinput-udev \
     libevdev \
     evtest \
### Window, mouse, keyboard management
     openbox \
     onboard \
     unclutter-xfixes \
     ttf-dejavu \
     dbus \
     dconf \
### Linux utils
     bash \
     util-linux \
     patch \
     scrot \
### Full Timezone info
     icu-data-full \
### Python libraries
     py3-pip \
     py3-xlib \
### Sound
     pulseaudio-utils \
#     alsa-utils alsa-plugins-pulse \
### Video
#     gstreamer-tools \
#     gst-libav \
### VNC (for debugging) - run: x11vnc -display :0 -forever & \
     x11vnc \
# Browser
     qutebrowser \
    && rm -rf /var/cache/apk/*

#===============================================================================

##### Set the display variable
ENV DISPLAY=:0

##### Copy over 'xorg.conf.default' and qutebrowser config file
COPY xorg.conf.default /etc/X11/
COPY qutebrowser_config.py /root/.config/qutebrowser/config.py
COPY translations/*.yaml /translations/

COPY run.sh /
RUN chmod a+x /run.sh

COPY mouse_touch_inputs.py gesture_commands.json /
COPY rest_server.py /
RUN pip install --no-cache-dir  --break-system-packages aiohttp #Required for rest_server.py

# USER 800:800

CMD ["/run.sh"]
