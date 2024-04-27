# nv-mixedx11

Normally, the refresh rate on NVIDIA + x11 is capped at your lowest refresh rate monitor. This script aims to fix that.

This script aims to fix this (in a somewhat hacky way) by disabling 'Allow Flipping', allowing X11 to properly sync to the high refresh rate monitor, and using force composition pipeline instead to prevent tearing. 

**NOTE":** In some cases, this approach does come with it's own limitations. When playing video's on your secondary monitor (or doing other things that cause many refreshes), performance on your high-refresh rate monitor *may* suffer.
