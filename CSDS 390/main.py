import argparse
import sys
import pandas as pd
import os
import re
import numpy as np
import json

class colors:
    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold'''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

def get_data(df, c):

    students = {}

    regex = r"(.*) \[(.*)\]$"

    for name, grades in df.iteritems():
        match = re.search(regex, name)
        #print(match)
        if match != None:
            if match.group(2) not in students:
                students[match.group(2)] = {}

            notes = []

            for g in grades:
                if g == "Excellent":
                    notes.append(4)
                elif g == "Good":
                    notes.append(3)
                elif g == "Fair":
                    notes.append(2)
                elif g == "Poor":
                    notes.append(1)
            
            students[match.group(2)][match.group(1)] = np.average(notes)
        else:
            comments = grades.fillna('').tolist()
        

    print(json.dumps(students, sort_keys=True, indent = 2))
    if c:
        print('\n'.join(comments))






if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TA grading programm. Gives the average of each Concept, Fun, Time to implement, and understanding after presentation")
    
    parser.add_argument('-r', '--recursive', action='store_true', default=False, help='Go through all files and compute all statistics at once')
    parser.add_argument('-c', '--comment', action='store_true', default=False, help='display the comments')
    parser.add_argument('path', type = str, help='CSV file to inspect')

    args = parser.parse_args()

    if args.recursive and os.path.exists(args.path):
            print('Start data collection')
            for file in os.listdir(args.path):
                df = pd.read_csv(os.path.join(args.path, file))

                #Sanitizing the DataFrame
                df.drop(df.iloc[:, 0:3], axis=1, inplace=True)
                get_data(df, args.comment)

    elif os.path.exists(args.path):
        df = pd.read_csv(args.path)

        #Sanitizing the DataFrame
        df.drop(df.iloc[:, 0:3], axis=1, inplace=True)

        

        get_data(df, args.comment)


    else:
        parser.print_help()