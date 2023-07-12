import re

def xprop_parser(input):
    result = {
        "win_maximized": 0,
        "win_maximized_horizontal": 0,
        "win_maximized_vertical": 0,
        "win_hidden": 0,
        "win_minimized": 0,
        "win_modal": 0,
        "win_sticky": 0,
        "win_shaded": 0,
        "win_fullscreen": 0,
        "win_above": 0,
        "win_below": 0
    }
    match = re.search(r'_NET_WM_STATE\(ATOM\) = (.*)$', input, re.MULTILINE)
    if match:
        values = match.group(1).split(", ")
        for v in values:
            if v == '_NET_WM_STATE_MAXIMIZED_HORZ':
                result['win_maximized_horizontal'] = 1
            if v == '_NET_WM_STATE_MAXIMIZED_VERT':
                result['win_maximized_vertical'] = 1
            if v == '_NET_WM_STATE_MODAL':
                result['win_modal'] = 1
            if v == '_NET_WM_STATE_STICKY':
                result['win_sticky'] = 1
            if v == '_NET_WM_STATE_SHADED':
                result['win_shaded'] = 1
            if v == '_NET_WM_STATE_HIDDEN':
                result['win_hidden'] = 1
            if v == '_NET_WM_STATE_FULLSCREEN':
                result['win_fullscreen'] = 1
            if v == '_NET_WM_STATE_BELOW':
                result['win_below'] = 1
            if v == '_NET_WM_STATE_ABOVE':
                result['win_above'] = 1

    if result['win_maximized_horizontal'] == 1 and result['win_maximized_vertical'] == 1:
        result['win_maximized'] = 1
    if result['win_hidden'] == 1:
        result['win_minimized'] = 1

    return result

