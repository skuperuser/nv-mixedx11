# nv-mixedx11

On x11, the refresh rate on NVIDIA gpu's is capped at your lowest refresh rate monitor. This script aims to fix that.

This script aims to fix this (in a somewhat hacky way), allowing X11 to properly sync to the high refresh rate monitor, and using force composition pipeline instead to prevent tearing. 

To use, simple copy & paste this one-liner:
```bash
git clone https://github.com/vtholde/nv-mixedx11 && cd nv-mixedx11 && chmod +x nvidia-mixedrefresh.sh && ./nvidia-mixedrefresh.sh
```
**NOTE:** In some cases, this approach does come with it's own limitations. When playing video's on your secondary monitor (or doing other things that cause many refreshes), performance on your high-refresh rate monitor *may* suffer. If the script doesn't work properly for you, consider switching to [wayland](https://wayland.freedesktop.org/)
