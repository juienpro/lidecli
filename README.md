# LideCLI - The Linux Desktop CLI

![image](https://user-images.githubusercontent.com/121452426/231865865-d56446e6-6095-4238-9fcd-091bd15a9c59.png)

Lidecli (Linux Desktop CLI) is an unified command-line tool to interact with X, Wayland, Window Managers and Desktop Environments.
Currently, interacting with your Desktop Environment/Window Manager is not "so easy". Depending of the DE you use, you need to mix the following techniques/tools: 

- you need to code (for instance, with AwesomeWM, you need to do everything with LUA)
- you need to interact with the API provided by your DE, usually with ugly D-BUS calls
- you need to play with tools like wmctrl, xdotool, etc. working only for X and not for Wayland.

The goal of Lidecli is to provide a library of commands to interact with the DE/WM you use. This library is searchable and each command is tagged, so you'll know what is the underlying tool(s) the command is using. 

## Usage

The code is a Python 3 script. You just need to clone this repository. Some examples of usage:

**Show the list of all supported commands**
```
./lidecli.py -l 
```

**Show the list of all commands compatible/using a tool (search by tag)**
```
./lidecli.py -t wmctrl -l
```

**Show the list of all commands for X but not for KDE**
```
./lidecli.py -t x11 -n kde -l
```

**Show the help of a command**
```
./lidecli.py x-win-id-maximize -h
```

**Launch a command**
```
./lidecli.py x-win-name-maximize Firefox
```

## Command currently implemented

As I am currently using KDE Plasma (very great except its command-line API) on X, the current database contains around 170 ready-to-use commands, mainly using **KDE API with qdbus**, and **wmctrl**, **xprop** or **xwininfo**.

### KDE status

Currently, almost all KDE commands available through `qdbus org.kde.kglobalaccel /component/kwin org.kde.kglobalaccel.Component.invokeShortcut` have been implemented. To get a precise status, there is a script in the `tools` folder that outputs the list of commands remaining to be implemented.

## Contributing

It's particularly easy to contribute and to add your custom commands, whatever your current dekstop environment.

### Defining a command

The database is a simple Python file called `db.py`. This file contains all defined commands. Each command has the following properties:

- Its calling name (eg. `kde-move-id-desktop-up`)
- A description for the end-user
- A list of `forwarded_arguments` (arguments needed to run the command)
- A potential list of `forwarded_options`
- The command to be launched
- The DEs and versions where it has been tested successfully ("versions_working")
- The DEs and versions where it has been tested unsuccessfully ("versions_not_working")
- A list of tags

**Simple example of a command**

```
{
  "name": "x-list-windows-wmctrl",
  "description": "Get Windows list with wmctrl",
  "versions_working": [("x11", "all")],
  "versions_not_working": [],
  "command": "wmctrl -l",
  "tags": ["x11", "windows", "wmctrl"]
},

```
This is self-explanatory.

### Basic conventions

With Lidecli, we try to comply with some basic conventions.

### Command name conventions

- The name of the command starts by the main subsystem involved. Here it's X, so the command starts by `x-`. On Wayland it would be `wayland-`. For a simple KDE d-bus call, it would just start by "kde-". 
- The second word of the command name is usually the action performed: list, toggle, get, focus, set, etc.
- The next one or two words is the subject of the action: windows, desktops, screens, monitors, etc.
- You'll find many commands containing "win-id" or "win-name", like `x-win-id-maximize` and `x-win-name-maximize`. The first one allows you to maximize a window specified by it's ID, the second one by its name (eg `./lidecli.py x-win-name-maximize Firefox`).

### Tags conventions

Tags are very useful to find a command, so they must be set properly. Usually, the first ones are the main subsystem involved (x11, wayland, kde...). Then, there is a tag defining the subject of the action: windows, desktops, screens, etc.
Finally, there are one or two tags to define the underlying tools needed to run the command: wmctrl, qdbus, etc.

If a command supports a JSON output, you should add "json" at the end of the tag list.

### Support of several commands

In the simple WMCtrl example above, you'll notice that the command executed effectively is specified in the "command" key. Lidecli supports also a "commands" key, where you can define a list of commands to execute. See the detailed example below.

### Forwarded options

You can "forward" options to the executed command. Let's take the example below.

```
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
}

```

Here, when you launch `./lidecli.py kde-monitors`, the executed command will be `kscreen-doctor -o`.
However, if you launch `./lidecli.py kde-monistors -j`, the executed command will be `kscreen-doctor -j`.

### Forwarded arguments

Arguments can be forwarded to the command launched. More importantly, they can be positionned where you want, using `#1#` for the first argument, `#2#` for the second argument, etc.

Example:

```
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

```

Here, the command is doing a grep on the output of `wmctrl -l`, with a `grep '#1#'` where `#1#` will be replaced by the first argument passed to the `x-get-winid` command.
If you launch `./lidecli.py x-get-winid Firefox`, then the command executed will be: `wmctrl -l |grep -v wmctrl | grep -v x-get-winid | grep 'Firefox' | cut -d ' ' -f1`

If you just to put the argument(s) at the end of the command line, it's not mandatory to add `#1#`. By default, all needed arguments mentionned will be forwarded to the end of the command launched. 

### Custom Python callbacks

Lidecli supports custom Python callbacks, mainly to parse the output of a command.

Let's take the example below:
```
 {
    "name": "x-is-win-maximized",
    "description": "Check if a Window is maximized",
    "forwarded_arguments": [
       { "name": "WinID", "description": "The windows ID"}
    ],
    "versions_working": [("x11", "all")],
    "versions_not_working": [],
    "command": "xprop -id",
    "callback": {
      "function": "xprop_parser",
      "output_key": "win_maximized"
    },
    "tags": ["x11", "windows", "xprop"]
 },
```

Here, the command `xprop -id <WinID>` will be launched. Then its output will be send to the `xprop_parser` function of the file `callbacks.py`.

A callback should return a dictionary of values. The result returned to the end-user will be the `output_key` of this dictionary.

In this case, we just need to write one parser function for xprop, and then returns the relevant key in our various commands.

### Saving temporarily the results of commands

It may be useful to save temporarily the result of a command. It's particularly useful to save the current focused Window to be restored later, so when you launch the command through a keybinding, your focused window is not lost.

Lidecli has the option "-s" which save the result of the command in a "register" for later use. There are 9 registers (1 to 9), the last one being reserved for the commands defined in `db.py`. The registers 1 to 8 can be used freely by any other scripts.

Let's say you need a bash script to move all your windows without losing the focus of the current one.

```
#!/bin/bash

# Get the ID of the focused Window and store it in the Register n°1
./lidecli.py -s 1 x-current-focus-id

## Do your stuff

# Restore the focus by calling x-focus-id with the content of the register n°1
./lidecli.py x-focus-id #s1#

```

You don't have to use Bash/environment variables. You can if you want, but registers might be easier.

The temporary data is saved in the file `config.ini`. A later version of Lidecli may also use this config file to store other configuration variables.

### Calling Lidecli from Lidecli

In the `db.py` file, you'll notice that sometimes we use "./self" in the commands.
./self just call Lidecli itself, to call another command. More details below.

### Detailed example of a command launching multiple commands

```
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
}
```

In this example, you'll notice several things. 
- First, there are several commands launched when kde-move-win-id-desktop-up is invoked. Let's detail each step. 
- ./self is used to call Lidecli itself, to get the currently focused window and store it in the reserved register.
- After the `qdbus` call, the focus is restored using `./self x-focus-id #s9#`
- The tags contain "x11" and "kde", but not "wayland". Indeed, this command contains several calls to `wmctrl` which would only work on X, not on Wayland, despite the `qdbus` command should work on both. 

## Feedbacks

This tool is not perfect, but it may be a nice start to build a full library of CLI commands to interact with the various Desktop Environments.
Your contributions would be welcomed! 

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/juienpro)
