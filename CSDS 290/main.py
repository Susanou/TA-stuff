import argparse
import sys
import pandas as pd
import os

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

def get_data(df, team):

    total = 0
    inov = 0
    fun = 0

    for k,v in df.iterrows():
        #print(v)
        try:
            if v.iloc[0] == team:
                inov += v.iloc[1]
                fun += v.iloc[2]
                total += 1
            elif v.iloc[3] == team:
                inov += v.iloc[4]
                fun += v.iloc[5]
                total += 1
            elif v.iloc[6] == team:
                inov += v.iloc[7]
                fun += v.iloc[8]
                total += 1
            elif v.iloc[9] == team:
                inov += v.iloc[10]
                fun += v.iloc[11]
                total += 1
        except:
            pass
    


    #print(total)


    print("General Feedback")
    print(colors.fg.cyan + f"Innovation {(inov/total):.2f}/10")
    print(colors.fg.green + f"Fun {(fun/total):.2f}/10")
    print(colors.reset)
    print("Game Feedback:\n\nPresentation Feedback:")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TA grading programm. Gives the average of each Concept, Fun, Time to implement, and understanding after presentation")
    
    parser.add_argument('t', type = int, help='team number that you want to inspect')
    parser.add_argument('path', type = str, help='CSV file to inspect')

    args = parser.parse_args()

    if args.t and os.path.exists(args.path):
        df = pd.read_csv(args.path)

        #Sanitizing the DataFrame
        df.drop(df.iloc[:, [0,1,2,3,7,8,12,13,17,18,22,23,24,25,26,27]], axis=1, inplace=True)

        df.drop(df[~((df['Which group are you reviewing?'] == args.t) | (df['Which group are you reviewing?.1'] ==args.t) | (df['Which group are you reviewing?.2'] ==args.t) | (df['Which group are you reviewing?.3'] ==args.t))].index, inplace=True)

        get_data(df, args.t)


    else:
        parser.print_help()