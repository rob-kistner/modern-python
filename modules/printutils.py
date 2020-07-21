#
#   printutils
#
#   A collection of print utilties to use
#    when testing python scripts or following
#    along with code-along tutorials.
#
import json # for json.dumps()

def bl():
    """ ----------------------------
        Just print a blank line (bl)
    ---------------------------- """
    print()


def clear():
    """ --------------
        Pass on laptop
    -------------- """
    pass


def sep ( padchar="-", padlength=20 ):
    """ -------------------------------------
        Outputs a character a number of times
        to make a visual separator

        args:
            padchar (string, default: "-"):
                The character to repeat

            padlength (int, default: 20):
                The amount of repeats to make
    ------------------------------------- """
    print( padchar * padlength )


def pl(output):
    """ ------------------------------------
        print output following by a blank line

        args:
            output:
                the thing to print
    ------------------------------------ """
    print(output)
    print()

def var_dump( varname, varval ):
    """ ----------------------------------------
        Output the named of the variable and the 
        variables value
    ---------------------------------------- """
    print(f'{varname}: {varval}')


def jprint( data, indent=4 ):
    """ ----------------------------------------
        Print out a pretty JSON view of 
        dict data
    ---------------------------------------- """
    print(json.dumps(data, indent=indent))


def banner(s="", padchar="-", indentlength=4, spaced=True):
    """ -----------------------------------------------------
        Outputs a decorative headline banner with
        character lines (padchar) the max length of the
        text to be printed (s) at top and bottom plus spacing
        (indentlength)

        args:
            s (string):
                the text string to print

            padchar (string, default: '='):
                character to use for banner padding

            indentlength (integer, default: 4):
                number of spaces to indent
            
            spaced (bool, default: True)
                add blank lines before and after 
                the banner text
    ----------------------------------------------------- """
        # remove blank lines from comment and
        # split them into a list at character returns
    s_lines = s.strip().split("\n")
        # also strip the individual comment lines
    s_lines = list(map(lambda line: line.strip(), s_lines))
        # calculate line length including line_inset on
        # front and back
    line_length = len(max(s_lines, key=len)) + 2 * indentlength

    if spaced: print()
    print(padchar * line_length)
    [print(" " * indentlength + line) for line in s_lines]
    print(padchar * line_length)
    if spaced: print()


def big_banner(s="", padchar="*", indentlength=4, spaced=True):
    """ -----------------------------------------------------
        Outputs a top-level decorative headline banner with
        character lines (padchar) the max length of the
        text to be printed (s) at top and bottom plus spacing
        (indentlength) and interior vertical bars on left and right.

        args:
            s (string):
                the text string to print

            padchar (string, default: '='):
                character to use for banner padding

            indentlength (integer, default: 4):
                number of spaces to indent
            
            spaced (bool, default: True)
                add blank lines before and after 
                the banner text
    ----------------------------------------------------- """
        # remove blank lines from comment and
        # split them into a list at character returns
    s_lines = s.strip().split("\n")
        # also strip the individual comment lines
    s_lines = list(map(lambda line: line.strip(), s_lines))
        # calculate line length including line_inset on
        # front and back
    line_length = len(max(s_lines, key=len)) + 2 * indentlength
        # blank line if spaced = True, followed by padchars
    if spaced: print()
    print(f"{padchar * (line_length+2)}")
        # print each line with vert bars on either end
    for line in s_lines:
        ind = (" " * indentlength)
        currline = padchar + ind + line
        endspacing = line_length - len(currline) - 3
        print(f"{padchar}{ind}{line}{ind}{endspacing * ' '}{padchar}")
        # blank line if spaced = True, followed by padchars
    print(f"{padchar * (line_length+2)}")
    if spaced: print()


def bannerline ( s, char='-', pad=30, surround=True ):
    """ ----------------------------------------------------
        Print a single line banner
        surrounded by characters on both sides

        args:
            s (string, required):
                the banner text to output

            char (string, default: '-'):
                the top / bottom line characters

            pad (int, default: 30):
                the amount of surround characters

            surround (bool, default: True):
                if true, adds a blank line to top and bottom
    ---------------------------------------------------- """
    s = ' %s ' % s
    if surround: print()
    print(s.center(len(s) + pad, char))
    if surround: print()


def bannerhead ( s, padchar="-" ):
    """ -----------------------------------------------------------
        Print comment (s) with a line of characters (padchar) below

        args:
            s (string):
                the comment string to print

            padchar (string, default: "-"):
                the character to print as a line
    ----------------------------------------------------------- """
    s_lines = s.strip().split("\n")
    s_lines = list(map(lambda line: line.strip(), s_lines))
    line_length = len(max(s_lines, key=len))

    print()
    [print(line) for line in s_lines]
    print(padchar * line_length)


def prints(output):
    """ ---------------------------------------------
        Print a string with blank lines above & below

        args:
            output (string, required):
                the text string to print
    --------------------------------------------- """
    bl()
    print(output)
    bl()


def print_ind(s="", indent_level=1, spaces=4):
    """ ----------------------------------------------------------
        Print text (s) indented
        number of spaces (spaces) x an indent level (indent_level)

        args:
            s (string):
                the text string to print

            indent_level (integer, default: 1):
                the level multiplier for the indent,
                number to be multiplied with spaces
                param

            spaces (integer, default: 4)
                the base number of spaces to use for
                the indent
    ---------------------------------------------------------- """
    print(" " * int(indent_level * spaces) + str(s))


def expected (comment="", expected="", padchar="-", indent=0):
    """ ------------------------------------------------------------------
        Print a comment (can be multiple lines) with possible line insets,
        then a separator line with or without inset as the length,
        then the expected text with possible line insets

        args:
            comment (string, default: ''):
            expected (string, default: ''):
            padchar (string, default: '-'):
            line_inset (integer, default: 0):
    ------------------------------------------------------------------ """
        # remove blank lines from comment and
        # split them into a list at character returns
    comment_lines = comment.strip().split("\n")
        # also strip the individual comment lines
    comment_lines = list(map(lambda line: line.strip(), comment_lines))
        # calculate line length including indent on
        # front and back
    line_length = len(max(comment_lines, key=len)) + (indent*2)
        # inset_str to place at beginning and end of line
    inset_str = " " * indent

        # blank line at the top
    print()
        # print each comment line plus the insets
    [print(inset_str + line + inset_str) for line in comment_lines]
        # print separatator
    print(padchar * line_length)
        # print inset and the expected string
    if type(expected) not in (tuple, dict, list):
        print(f'{inset_str}{expected}')
    elif type(expected) is dict:
        print(json.dumps(expected, indent=4))
    else:
        for expected_item in expected:
            print(f'{inset_str}{expected_item}')

