if [ $(id -u) = 0 ]; then
  echo "I should not be run as root!"
  exit 1
fi

echo "This script aims to make mixed refresh rate monitors work flawlessly on Nvidia + X11"
echo ""
echo "Please do the following:"
echo "1. Open NVIDIA X Server settings"
echo "2. Go to X Server XVideo Settings > Sync to your high refresh rate monitor"
echo "3. Go to OpenGL Settings > Uncheck Allow Flipping"
echo "4. Click 'Quit' in the bottom right corner and confirm"
echo ""
echo "After completing the steps above, press enter to install. A startup task will be run automatically on every login."
read a
echo "Writing to file $HOME/.nvidia-mixedrefresh.sh ..."

to_write='
#!/bin/bash

# This script assumes you have done the following in the NVIDIA X server settings:
# You have disabled *Allow Flipping* in nvidia-settings (can be changed in OpenGL Settings)
# You are syncing to the highest refresh rate capable monitor (can be changed in X Server XVideo Settings)

# Code underneath needs to be run at every boot.

nvidia-settings --load-config-only

# Enables force composition pipeline (fixes tearing on secondary monitors)
s="$(nvidia-settings -q CurrentMetaMode -t)"

if [[ "${s}" != "" ]]; then
  s="${s#*" :: "}"
  nvidia-settings -a CurrentMetaMode="${s//\}/, ForceCompositionPipeline=On\}}"
fi
'

# do the actual writing
cat > "$HOME/.nvidia-mixedrefresh.sh" << EOF
$to_write
EOF


echo "updating .profile ..."
echo '. "$HOME/.nvidia-mixedrefresh.sh"' >> "$HOME/.profile"

echo "setting permissions ..."
chmod +x "$HOME/.nvidia-mixedrefresh.sh"

echo "executing startup task ..."
. "$HOME/.nvidia-mixedrefresh.sh" > /dev/null 2>&1

echo "done."
