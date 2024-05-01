import subprocess

result = subprocess.run("bash -c 'xrandr'", shell=True, capture_output=True, text=True)

def find_rates():
    xrandr = result.stdout
    refresh_rate_list = []
    while xrandr.find('+') != -1:
        starpos = xrandr.find('*')
        select = xrandr[starpos-6:starpos]
        for letter in select:
            if letter.islower():
                select = select.replace(letter, "")
            elif letter == "(" or letter == ")" or letter == "\n": #or letter == " " or letter == "'":
                select = select.replace(letter, "")
        print(select)
        try:
            select = float(select) # should be done differently at some point
        except:
            return False
        select = int(select)
        if select >= 10: # fix random bug where an incorrent refresh rate would be included
            refresh_rate_list.append(select)
        try:
            xrandr = xrandr.split('*', 1)[1]
        except:
            break
    return refresh_rate_list

def find_conn_screens():
    xrandr = result.stdout
    #print(xrandr)
    screens = []
    while xrandr.find(' connected') != -1:
        selectpos = xrandr.find(' connected')
        select = xrandr[selectpos-10:selectpos]

        for letter in select:
            if letter.islower():
                select = select.replace(letter, "")
            elif letter == "(" or letter == ")" or letter == "\n":
                select = select.replace(letter, "")
        screens.append(select)
        try:
            xrandr = xrandr.split(' connected',1)[1]
            #print(xrandr)
        except:
            break
    return screens

def find_optimal(rlist, slist):
    print(rlist)
    print(slist)
    max_refresh = max(rlist)
    max_refresh_index = rlist.index(max_refresh)
    screen = slist[max_refresh_index]
    return screen, max_refresh


if find_rates():
    screen, highest_refresh = find_optimal(find_rates(), find_conn_screens())
    print(f"highest refresh rate monitor is {screen} with a refresh rate of {highest_refresh} hertz.")
    
else:
    print("An unknown error occurred determining which monitor has the highest refresh rate. \n\n ")
    print(result.stdout)
    screen = input("Please insert the identifier of your highest refresh-rate monitor. (e.g. DP-0 or HDMI-1)\n>> ")

subprocess.run(f"bash -c 'sudo echo __GL_SYNC_DISPLAY_DEVICE={screen}' >> /etc/environment", shell=True, capture_output=True, text=True)
print('Done. ENTER to reboot and finish setup.')
input("")
try:
    subprocess.run(f"reboot", shell=True, capture_output=True, text=True)
except:
    subprocess.run(f"sudo reboot", shell=True, capture_output=True, text=True)
