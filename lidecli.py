#!/usr/bin/env python3
import argparse
import subprocess
from prettytable import PrettyTable
import sys
import json
import os
import configparser
import callbacks
import db

version = "1.0.2"
verbose = False
outer_args = None
inner_args = None

def get_command_by_name(name):
    for command in db.commands():
        if name == command['name']:
            return command
    return False

def print_commands(args):
    table = PrettyTable(["\033[33mCommand\033[0m", "\033[33mDescription\033[0m", "\033[33mTags\033[0m", "\033[33mOK\033[0m", "\033[33mKO\033[0m"])
    R = "\033[0;31;40m" #RED
    G = "\033[0;32;40m" # GREEN
    Y = "\033[0;33;40m" # Yellow
    B = "\033[0;34;40m" # Blue
    N = "\033[0m" # Reset
    table.align = "l"

    for cmd in db.commands():
        if args.tag and args.tag not in cmd.get("tags", []):
            continue
        if args.no_tag and args.no_tag in cmd.get("tags", []):
            continue
        command_name = "\033[32m{}\033[0m".format(cmd["name"])
        working = []
        not_working = []
        if cmd['versions_working'] and (len(cmd['versions_working']) > 0):
            for v in cmd['versions_working']:
                working.append(v[0]+" "+v[1])
        else:
            working = ['?']

        if cmd['versions_not_working'] and (len(cmd['versions_not_working']) > 0):
            for v in cmd['versions_not_working']:
                not_working.append(v[0]+" "+v[1])
        else:
            not_working = ['?']

        table.add_row([command_name, cmd["description"], ", ".join(cmd.get("tags", [])), ' - '.join(working), '-'.join(not_working) ])
    print(table)

def read_temporary_variable(index):
    config = configparser.ConfigParser()
    path = os.path.dirname(__file__)
    config_file = "{}/config.ini".format(path)
    config.read(config_file)
    key = 'TMP_RESULT_'+str(index)
    return config['TMP_STORAGE'][key]

def set_temporary_variable(index, value):
    config = configparser.ConfigParser()
    path = os.path.dirname(__file__)
    config_file = "{}/config.ini".format(path)
    config.read(config_file)
    key = 'TMP_RESULT_'+str(index)
    config['TMP_STORAGE'][key] = value
    with open(config_file, 'w') as configfile:
        config.write(configfile)

def exec_command(args):
    if args.command =='var':
        if args.index:
            print(read_temporary_variable(int(args.index)))
        return
    command = get_command_by_name(args.command)
    if "command" in command:
        str_command = command["command"]
    else:
        str_command = ' && '.join(command['commands'])

    for option in command.get('forwarded_options', []):
        param = option['param'].replace('-', '')
        if getattr(args, param) == True:
            str_command += ' -' + param

    for idx, argument in enumerate(command.get('forwarded_arguments', [])):
        param = getattr(args, argument["name"])
        if (param != None):
            formated_param = '#{}#'.format(idx+1)
            if formated_param in str_command:
                str_command = str_command.replace(formated_param, param)
            else:
                str_command += '  ' + param

    # Replace stored variables
    for register in range(1, 10):
        value = read_temporary_variable(register)
        str_command = str_command.replace('#s'+str(register)+'#', value)

    # Replace './self'
    fullpath = os.path.abspath(__file__)
    str_command = str_command.replace('./self', fullpath)

    if (args.verbose):
        print("Command:" + str_command)
    try:
        ret = subprocess.check_output(str_command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("Command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        return
    ret = ret.decode('utf-8')
    if "callback" in command:
        function = getattr(callbacks, command["callback"]["function"])
        ret = function(ret)
        print(ret["win_maximized"], end='')
    else:
        print(ret, end='')
    if (args.store):
        set_temporary_variable(9, ret)

parser = argparse.ArgumentParser(description="Plasma API")
parser.add_argument("-v", "--verbose", action="store_true", help="Display the command actually executed")
parser.add_argument("-l", "--list", dest="pretty_table", action="store_true", help="Pretty display of all commands")
parser.add_argument("-j", "--json", action="store_true", help="Display the DB in JSON")
parser.add_argument("-t", "--tag", help="Filter by tag")
parser.add_argument("-n", "--no-tag", help="Do not include this tag in results")
parser.add_argument("-s", "--store", help="Store the result in a variable")
subparsers = parser.add_subparsers(title="Commands", help='Command help', dest="command")

command_parsers = {}
for command in db.commands():
    command_parsers[command['name']] = subparsers.add_parser(command['name'], help="{}".format(command['description']))
    for option in command.get('forwarded_options', []):
        command_parsers[command['name']].add_argument(option['param'], default=option.get('default', False), action="store_true", help=option['description'])
    for option in command.get('forwarded_arguments', []):
        command_parsers[command['name']].add_argument(option['name'], nargs="?", help=option['description'])

command_parsers['var'] = subparsers.add_parser('var', help="Output a temporary variable")
command_parsers['var'].add_argument('index', nargs="?", help="The index of temporary variable to display")

args = parser.parse_args()
if not args.pretty_table:
    if not args.command:
        parser.print_usage()
    else:
        exec_command(args)
else:
    if args.json:
        print(json.dumps(db.commands()))
    else:
        print_commands(args)
