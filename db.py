def commands():
    return [
        {
            "name": "kde-list-shortcuts",
            "description": "Get all supported KWin configurable shortcuts",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.shortcutNames",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": [ "x11", "wayland", "kde", "windows", "qdbus"]
        },
        {
            "name": "kde-monitors",
            "description": "Get the list of the monitors and their configuration",
            "command": "kscreen-doctor",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "forwarded_options": [
                { "param": "-o", "description": "", "default": True },
                { "param": "-j", "description": "Get the output as JSON" }
            ],
            "tags": ["x11", "wayland", "kde", "monitors", "json"],
        },
        {
            "name": "kde-invoke-shortcuts",
            "description": "Invoke a KWin conigurable shortcut",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut",
            "forwarded_arguments": [
                { "name": "Shortcut", "description": "The shortcut to execute"}
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "sway-list-windows",
            "description": "Get Windows list with Sway on Wayland",
            "command": "swaymsg -t get_tree",
            "versions_working": [],
            "versions_not_working": [],
            "tags": ["wayland", "sway", "windows"]
        },
        {
            "name": "x-list-windows-wmctrl",
            "description": "Get Windows list with wmctrl",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "wmctrl -lx",
            "tags": ["x11", "windows", "wmctrl"]
        },
        {
            "name": "x-list-windows-xwininfo",
            "description": "Get Windows list with xwininfo",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xwininfo -root -tree | grep '\"[^\"]*\"'",
            "tags": ["x11", "windows", "xwininfo"]
        },
        {
            "name": "x-get-winid",
            "description": "From the class name of a window, output the Win ID",
            "forwarded_arguments": [
                { "name": "Label", "description": "Part of the class name to look for"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "wmctrl -l |grep -v wmctrl | grep -v x-get-winid | grep '#1#' | cut -d ' ' -f1",
            "tags": ["x11", "windows", "wmctrl"]
        },
        {
            "name": "x-is-win-maximized",
            "description": "Check if a Window is maximized",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_maximized"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-maximized-h",
            "description": "Check if a Window is maximized horizontally",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_maximized_horizontal"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-maximized-v",
            "description": "Check if a Window is maximized vertically",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_maximized_vertical"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-minimized",
            "description": "Check if a Window is minimized",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_minimized"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-modal",
            "description": "Check if a Window is modal",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_modal"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-sticky",
            "description": "Check if a Window is sticky",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_sticky"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-shaded",
            "description": "Check if a Window is shaded",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_shaded"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-fullscreen",
            "description": "Check if a Window is fullscreen",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_fullscreen"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-above",
            "description": "Check if a Window is above others",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_above"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
            "name": "x-is-win-below",
            "description": "Check if a Window is below others",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The windows ID"}
            ],
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "command": "xprop -id #1#",
            "callback": {
                "function": "xprop_parser",
                "output_key": "win_below"
            },
            "tags": ["x11", "windows", "xprop"]
        },
        {
           "name": "x-focus-id",
            "description": "Give focus to a Window (by ID)",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The Window ID"}
            ],
            "command": "wmctrl -i -a #1#",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
           "name": "x-focus-name",
            "description": "Give focus to a Window (by name)",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The substring to match the Window Name"}
            ],
            "command": "wmctrl -a",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
           "name": "x-current-focus-id",
            "description": "Get the WinID having the focus",
            "command": "xprop -root _NET_ACTIVE_WINDOW |cut -d ' ' -f5",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "xprop" ]
        },
        {
            "name": "x-set-win-id-fullscreen",
            "description": "Set a Window specified by its WinID to full screen",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The Window ID"}
            ],
            "command": "wmctrl -i #1# -b add,fullscreen",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-set-win-name-fullscreen",
            "description": "Set a Window specified by its name to full screen",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The substring to match the Window name"}
            ],
            "command": "wmctrl #1# -b add,fullscreen",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-unset-win-id-fullscreen",
            "description": "Unset fullscreen for a Window specified by its WinID",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The Window ID"}
            ],
            "command": "wmctrl -i #1# -b remove,fullscreen",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-unset-win-name-fullscreen",
            "description": "Unset fullscreen for a Window specified by its name",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The substring to match the Window name"}
            ],
            "command": "wmctrl #1# -b remove,fullscreen",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "kde-toggle-win-fullscreen",
            "description": "Toogle fullscreen for the current Window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Fullscreen'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-close-win",
            "description": "Close the current window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Close'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-kill-win",
            "description": "Kill the current window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Kill Window'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "x-kill-win-id",
            "description": "Kill a window specified by its WinID",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to kill"}
            ],
            "command": "wmctrl -ic #1#",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-kill-win-name",
            "description": "Kill a window specified by its name",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The part of the window name to kill"}
            ],
            "command": "wmctrl -c #1#",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },

        {
            "name": "kde-switch-to-desktop",
            "description": "Switch to a particular desktop",
            "forwarded_arguments": [
                { "name": "DesktopIndex", "description": "The index of the desktop, starting from 1"}
            ],
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Desktop #1#'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-current-win-to-desktop",
            "description": "Move a window to a particular desktop",
            "forwarded_arguments": [
                { "name": "DesktopIndex", "description": "The index of the desktop, starting from 1"}
            ],
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Desktop #1#'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-to-desktop",
            "description": "Move a window specified by ID to a particular desktop",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
                { "name": "DesktopIndex", "description": "The index of the desktop, starting from 1"}
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Desktop #2#'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "desktops", "qdbus", "wmctrl" ]
        },
        {
            "name": "kde-move-win-name-to-desktop",
            "description": "Move a window specified by name to a particular desktop",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
                { "name": "DesktopIndex", "description": "The index of the desktop, starting from 1"}
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#'",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Desktop #2#'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "desktops", "qdbus", "wmctrl" ]
        },
        {
            "name": "kde-switch-to-screen",
            "description": "Switch to a particular screen",
            "forwarded_arguments": [
                { "name": "Number", "description": "The screen number to switch to"},
            ],
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Screen #1#'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-switch-to-previous-screen",
            "description": "Switch to the previous screen",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Previous Screen'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-switch-to-next-screen",
            "description": "Switch to the next screen",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Next Screen'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-switch-to-right-screen",
            "description": "Switch to the screen at the right",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Screen to the Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-switch-to-left-screen",
            "description": "Switch to the screen at the left",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Screen to the Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-switch-to-screen-below",
            "description": "Switch to the screen below",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Screen Below'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-switch-to-screen-above",
            "description": "Switch to the screen above",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Screen Above'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-toggle-win-decorate",
            "description": "Toggle the decoration of the current Window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window No Border'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-toggle-win-id-decorate",
            "description": "Toggle the decoration of a window specified by its ID",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to decorate/undecorate"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window No Border'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "qdbus", "wmctrl" ]
        },
        {
            "name": "kde-toggle-win-name-decorate",
            "description": "Toggle the decoration of a window specified by its name",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The Win name to decorate/undecorate"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window No Border'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "qdbus", "wmctrl" ]
        },

        {
            "name": "kde-move-current-win-to-screen",
            "description": "Move a window to a particular screen",
            "forwarded_arguments": [
                { "name": "screen_index", "description": "The index of the screen, starting from 0"}
            ],
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Screen #1#'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-to-screen",
            "description": "Move a window specified by ID to a particular screen",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
                { "name": "ScreenIndex", "description": "The index of the desktop, starting from 0"}
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Screen #2#'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "windows", "qdbus", "wmctrl" ]
        },
        {
            "name": "kde-move-win-name-to-screen",
            "description": "Move a window specified by name to a particular screen",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
                { "name": "ScreenIndex", "description": "The index of the screen, starting from 0"}
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#'",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Screen #2#'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "windows", "qdbus", "wmctrl" ]
        },
        {
            "name": "kde-move-win-to-all-desktop",
            "description": "Move the current window to all desktops",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window On All Desktops'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-to-all-desktops",
            "description": "Move a window specified by ID to all desktops",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window On All Desktops'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "desktops", "qdbus", "wmctrl" ]
        },
        {
            "name": "kde-move-win-name-to-all-desktops",
            "description": "Move a window specified by name to all desktops",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#'",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window On All Desktops'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "desktops", "qdbus", "wmctrl" ]
        },
        {
            "name": "kde-tile-win-bottom",
            "description": "Tile the current Window to the bottom",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-tile-win-id-bottom",
            "description": "Tile a Window specified by its WinID to the bottom",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-name-bottom",
            "description": "Tile a Window specified by its name to the bottom",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-left",
            "description": "Tile the current Window to the left",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-tile-win-id-left",
            "description": "Tile a Window specified by its WinID to the left",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-name-left",
            "description": "Tile a Window specified by its name to the left",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-bottom-left",
            "description": "Tile the current Window to the bottom left",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-tile-win-id-bottom-left",
            "description": "Tile a Window specified by its WinID to the bottom left",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-name-bottom-left",
            "description": "Tile a Window specified by its name to the bottom left",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-top-left",
            "description": "Tile the current Window to the top left",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-tile-win-id-top-left",
            "description": "Tile a Window specified by its WinID to the top left",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-name-top-left",
            "description": "Tile a Window specified by its name to the top left",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-top",
            "description": "Tile the current Window to the top",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-tile-win-id-top",
            "description": "Tile a Window specified by its WinID to the top",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-name-top",
            "description": "Tile a Window specified by its name to the top",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-top-right",
            "description": "Tile the current Window to the top right",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-tile-win-id-top-right",
            "description": "Tile a Window specified by its WinID to the top right",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-name-top-right",
            "description": "Tile a Window specified by its name to the top right",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Top Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-right",
            "description": "Tile the current Window to the right",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-tile-win-id-right",
            "description": "Tile a Window specified by its WinID to the right",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-name-right",
            "description": "Tile a Window specified by its name to the right",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-bottom-right",
            "description": "Tile the current Window to the bottom right",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-tile-win-id-bottom-right",
            "description": "Tile a Window specified by its WinID to the bottom right",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-tile-win-name-bottom-right",
            "description": "Tile a Window specified by its name to the bottom right",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to tile"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Quick Tile Bottom Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "windows", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-walk-wins-current-application",
            "description": "Walk through Windows of the current application",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Walk Through Windows of Current Application'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-walk-wins-current-application-reverse",
            "description": "Walk through Windows of the current application (reverse)",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Walk Through Windows of Current Application (Reverse)'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-toggle-win-move",
            "description": "Move a window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Move'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-increase-win-opacity",
            "description": "Increase the opacity of the current Window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Increase Opacity'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-decrease-win-opacity",
            "description": "Decrease the opacity of the current Window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Decrease Opacity'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "x-set-win-id-opacity",
            "description": "Set the opacity of a Window specified by its WinID",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID"},
                { "name": "Opacity", "description": "The opacity (number between 0 and 100)"},
            ],
            "command": 'xprop -id #1# -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY "$(printf 0x%x $((0xffffffff * #2# /100)))"',
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "xprop" ]
        },
        {
            "name": "x-set-win-name-opacity",
            "description": "Set the opacity of a Window specified by its name",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A substring for the targeted Windows name"},
                { "name": "Opacity", "description": "The opacity (number between 0 and 100)"},
            ],
            "command": 'xprop -name "#1#" -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY "$(printf 0x%x $((0xffffffff * #2# /100)))"',
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "xprop" ]
        },
        {
            "name": "kde-switch-to-desktop-up",
            "description": "Switch to one desktop up",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch One Desktop Up'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-switch-to-desktop-right",
            "description": "Switch to one desktop to the right",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch One Desktop to the Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-switch-to-desktop-down",
            "description": "Switch to one desktop down",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch One Desktop Down'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-switch-to-desktop-left",
            "description": "Switch to one desktop to the left",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch One Desktop to the Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-switch-to-next-desktop",
            "description": "Switch to the next desktop",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Next Desktop'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-switch-to-previous-desktop",
            "description": "Switch to the previous desktop",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch to Previous Desktop'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },

        {
            "name": "kde-move-win-to-next-desktop",
            "description": "Move the current window to the next desktop",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Next Desktop'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-to-next-desktop",
            "description": "Move a window specified by its WinID to the next desktop",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Next Desktop'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-to-next-desktop",
            "description": "Move a window specified by its name to the next desktop",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the window name to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Next Desktop'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-to-previous-desktop",
            "description": "Move the current window to the previous desktop",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Previous Desktop'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-to-previous-desktop",
            "description": "Move a window specified by its WinID to the previous desktop",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Previous Desktop'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-to-previous-desktop",
            "description": "Move a window specified by its name to the previous desktop",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the window name to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Previous Desktop'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-switch-win-right",
            "description": "Switch to the window at the right of the current one",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch Window Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-switch-win-left",
            "description": "Switch to the window at the left of the current one",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch Window Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-switch-win-up",
            "description": "Switch to the window above the current one",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch Window Up'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-switch-win-down",
            "description": "Switch to the window below the current one",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Switch Window Below'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },

        {
            "name": "kde-move-win-screen-right",
            "description": "Move the current window to the screen at the right",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen to the Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-screen-right",
            "description": "Move a window specified by its ID to the screen at the right",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen to the Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-screen-right",
            "description": "Move a window specified by its name to the screen at the right",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen to the Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-screen-left",
            "description": "Move the current window to the screen at the left",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen to the Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-screen-left",
            "description": "Move a window specified by its ID to the screen at the left",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen to the Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-screen-left",
            "description": "Move a window specified by its name to the screen at the left",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen to the Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-screen-down",
            "description": "Move the current window to one screen down",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen Down'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-screen-down",
            "description": "Move a window specified by its ID one screen down",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen Down'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-screen-down",
            "description": "Move a window specified by its name one screen down",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen Down'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-screen-up",
            "description": "Move the current window to one screen up",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen Up'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-screen-up",
            "description": "Move a window specified by its ID one screen up",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen Up'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-screen-up",
            "description": "Move a window specified by its name one screen up",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Screen Up'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },

        {
            "name": "kde-move-win-to-next-screen",
            "description": "Move the current window to the next screen",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Next Screen'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-to-next-screen",
            "description": "Move a window specified by its ID to the next screen",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Next Screen'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-to-next-screen",
            "description": "Move a window specified by its name to the next screen",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Next Screen'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-to-previous-screen",
            "description": "Move the current window to the previous screen",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Previous Screen'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "screens", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-to-previous-screen",
            "description": "Move a window specified by its ID to the previous screen",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Previous Screen'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-to-previous-screen",
            "description": "Move a window specified by its name to the previous screen",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window to Previous Screen'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "screens", "wmctrl", "qdbus" ]
        },


        {
            "name": "kde-move-win-desktop-right",
            "description": "Move the current window to the desktop at the right",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop to the Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-desktop-right",
            "description": "Move a window specified by its ID to the desktop at the right",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop to the Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-desktop-right",
            "description": "Move a window specified by its name to the desktop at the right",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop to the Right'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-desktop-left",
            "description": "Move the current window to the desktop at the left",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop to the Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-desktop-left",
            "description": "Move a window specified by its ID to the desktop at the left",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop to the Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-desktop-left",
            "description": "Move a window specified by its name to the desktop at the left",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop to the Left'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-desktop-down",
            "description": "Move the current window to one desktop down",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop Down'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-desktop-down",
            "description": "Move a window specified by its ID one desktop down",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop Down'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-desktop-down",
            "description": "Move a window specified by its name one desktop down",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop Down'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-desktop-up",
            "description": "Move the current window to one desktop up",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop Up'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "desktops", "qdbus" ]
        },
        {
            "name": "kde-move-win-id-desktop-up",
            "description": "Move a window specified by its ID one desktop up",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -i -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop Up'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-move-win-name-desktop-up",
            "description": "Move a window specified by its name one desktop up",
            "forwarded_arguments": [
                { "name": "WinName", "description": "A part of the name of the window to move"},
            ],
            "commands": [
                "./self -s 9 x-current-focus-id",
                "wmctrl -a #1#",
                "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window One Desktop Up'",
                "./self x-focus-id #s9#",
            ],
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "kde", "desktops", "wmctrl", "qdbus" ]
        },
        {
            "name": "kde-zoom-in",
            "description": "Zoom in",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'view_zoom_in'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "various", "qdbus" ]
        },
        {
            "name": "kde-zoom-out",
            "description": "Zoom out",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'view_zoom_out'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "varioius", "qdbus" ]
        },
        {
            "name": "kde-zoom-reset",
            "description": "Zoom reset",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'view_actual_size'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "various", "qdbus" ]
        },
        {
            "name": "kde-win-maximize",
            "description": "Maximize the current window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Maximize'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-win-maximize-horizontal",
            "description": "Maximimze the current window horizontally",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Maximize Horizontal'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-win-maximize-vertical",
            "description": "Maximimze the current window vertically",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Maximize Vertical'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "x-win-id-maximize-horizontal",
            "description": "Maximize a window (by ID) horizontally",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to maximize"}
            ],
            "command": "wmctrl -ir #1# -b add,maximized_horz",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-win-id-maximize-vertical",
            "description": "Maximize a window (by ID) vertically",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to maximize"}
            ],
            "command": "wmctrl -ir #1# -b add,maximized_vert",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-win-id-maximize",
            "description": "Maximize a window (by ID)",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to maximize"}
            ],
            "command": "wmctrl -ir #1# -b add,maximized_vert, maximized_horz",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-win-id-unmaximize",
            "description": "Unmaximize a window (by ID)",
            "forwarded_arguments": [
                { "name": "WinID", "description": "The WinID to unmaximize"}
            ],
            "command": "wmctrl -ir #1# -b remove,maximized_vert, maximized_horz",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-win-name-maximize-horizontal",
            "description": "Maximize a window (by name) horizontally",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The name of the Window to maximize"}
            ],
            "command": "wmctrl -r #1# -b add,maximized_horz",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-win-name-maximize-vertical",
            "description": "Maximize a window (by name) vertically",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The name of the Window to maximize"}
            ],
            "command": "wmctrl -r #1# -b add,maximized_vert",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-win-name-maximize",
            "description": "Maximize a window (by name)",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The name of the Window to maximize"}
            ],
            "command": "wmctrl -ir #1# -b add,maximized_vert, maximized_horz",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "x-win-name-unmaximize",
            "description": "Unmaximize a window (by name)",
            "forwarded_arguments": [
                { "name": "WinName", "description": "The name of the Window to unmaximize"}
            ],
            "command": "wmctrl -ir #1# -b remove,maximized_vert, maximized_horz",
            "versions_working": [("x11", "all")],
            "versions_not_working": [],
            "tags": ["x11", "windows", "wmctrl" ]
        },
        {
            "name": "kde-win-minimize",
            "description": "Minimize the current window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Minimize'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-switch-to-next-window",
            "description": "Switch focus to the next window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Walk Through Windows'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-switch-to-previous-window",
            "description": "Switch focus to the next window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Walk Through Windows (Reverse)'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-expose",
            "description": "Show a global overview of windows",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Expose'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "various", "qdbus" ]
        },
        {
            "name": "kde-overview",
            "description": "Show a global overview of desktops and windows",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Overview'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "various", "qdbus" ]
        },

        {
            "name": "kde-expose-all",
            "description": "Show a global overview of all windows",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'ExposeAll'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "various", "qdbus" ]
        },
        {
            "name": "kde-show-desktop",
            "description": "Show the desktop",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Show Desktop'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "various", "qdbus" ]
        },

        {
            "name": "kde-grow-win-vertically",
            "description": "Grow the current window vertically",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Grow Vertical'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-grow-win-horizontally",
            "description": "Grow the current window horizontally",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Grow Horizontal'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },

        {
            "name": "kde-move-mouse-to-focus",
            "description": "Move the mouse to the current window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'MoveMouseToFocus'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "mouse", "qdbus" ]
        },
        {
            "name": "kde-move-mouse-to-center",
            "description": "Move the mouse to the center of the current screen",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'MoveMouseToCenter'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "mouse", "qdbus" ]
        },

        {
            "name": "kde-move-window-above",
            "description": "Move the current window above other windows",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Above Other Windows'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-move-window-below",
            "description": "Move the current window below other windows",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Below Other Windows'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },

        {
            "name": "kde-move-window-lower",
            "description": "Move the window lower",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Lower'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        
        {
            "name": "kde-move-window-pack-right",
            "description": "Move the current window to the edge of the window at the right",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Pack Right'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-move-window-pack-left",
            "description": "Move the current window to the edge of the window at the left",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Pack Left'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-move-window-pack-down",
            "description": "Move the current window to the edge of the bottom window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Pack Down'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-move-window-pack-up",
            "description": "Move the current window to the edge of the next upper window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Pack Up'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-resize-win",
            "description": "Resize the current window with the mouse",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Resize'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-edit-tiles",
            "description": "Launch the GUI to edit tiles",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Edit Tiles'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "various", "qdbus" ]
        },
        {
            "name": "kde-toggle-night-color",
            "description": "Toggle KDE night color",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Toggle Night Color'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "various", "qdbus" ]
        },
        {
            "name": "kde-toggle-win-shade",
            "description": "Toggle shade of the current window",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Shade'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },
        {
            "name": "kde-move-win-to-center",
            "description": "Move the current window to the center of the screen",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Move Center'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },

        {
            "name": "kde-shrink-win-horizontal",
            "description": "Shrink the current window horizontally if it is not maximized",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Shrink Horizontal'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },

        {
            "name": "kde-shrink-win-vertical",
            "description": "Shrink the current window vertically if it is not maximized",
            "command": "qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut 'Window Shrink Vertical'",
            "versions_working": [("kde", "5.27.3")],
            "versions_not_working": [],
            "tags": ["x11", "wayland", "kde", "windows", "qdbus" ]
        },



    ]
