
import subprocess
import re

def exec_command(command):
    try:
        ret = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("Command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        return False
    ret = ret.decode('utf-8')
    return ret

def get_windows_coordinates(win_name):
    command = 'wmctrl -G -l -x |grep {}'.format(win_name)
    ret = exec_command(command)
    lines = ret.split("\n")
    windows = []
    for line in lines:
        if line.strip() == '':
            continue
        sections = line.split()
        win = {"id": sections[0], "x": int(sections[2]), "y": int(sections[3]), "width": int(sections[4]), "height": int(sections[5])}
        windows.append(win)
    return windows

def get_screens():
    ret = exec_command('xrandr | grep " connected"')
    lines = ret.split("\n")
    screens = []
    for line in lines:
        if line.strip() == '':
            continue
        # Example: eDP-1 connected 1920x1200+3840+0 (normal left inverted right x axis y axis) 288mm x 180mm
        m = re.match(r'(.+?) connected (?:primary )?(\d+)x(\d+)\+(\d+)\+(\d+)', line)
        screen = {"name": m.group(1), "h": int(m.group(2)), 'v': int(m.group(3)), 'offset_h': int(m.group(4)), 'offset_v': int(m.group(5))}
        screens.append(screen)
    ordered_screens = sorted(screens, key=lambda d: d['offset_h'])
    return ordered_screens
    
def move_win(win_id, pos_x, pos_y, width, height):
    command = "wmctrl -i -r {} -e 0,{},{},{},{}".format(win_id, pos_x, pos_y, width, height)
    ret = exec_command(command)
    return ret

def move_win_to_screen(args):
    screens = get_screens()
    windows = get_windows_coordinates(args.WinName)
    if len(screens) < int(args.Monitor):
        return False
    for win in windows:
        for screen in screens:
            if win['x'] > screen['offset_h'] and win['x'] < screen['offset_h'] + screen['h']:
                diff_h = win['x'] - screen['offset_h']
        print(diff_h)
        new_pos_x = screens[int(args.Monitor)-1]['offset_h']+diff_h
        move_win(win['id'], new_pos_x, win['y'], win['width'], win['height'])

    return "toto"