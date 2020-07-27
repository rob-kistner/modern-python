#
#   printutils
#
#   A collection of print utilties to use
#    when testing python scripts or following
#    along with code-along tutorials.
#
import json  # for json.dumps()
import termcolor as tc  # colorize banner output, etc.

# globals
gColor = "yellow"


    # justify strings, add space 
    # in front, back, or both sides
_ljust = lambda s, size: f'{s}{" "*size}'
_rjust = lambda s, size: f'{" "*size}{s}'
_just = lambda s, size: f'{" "*size}{s}{" "*size}'


def _str_to_lines( s ):
    """ ----------------------------------------
        Private:
        Return list of lines striped of whitespace
     ---------------------------------------- """
    lines = list(map(lambda line: line.strip(), s.split("\n")))
    if lines[0] == "": lines.pop(0)
    if lines[len(lines)-1] == "": lines.pop()
    return lines 


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


def sep ( char="-", pad=20 ):
    """ -------------------------------------
        Outputs a character a number of times
        to make a visual separator
    ------------------------------------- """
    print( char * pad )


def pl( *output ):
    """ ------------------------------------
        print output following by a blank line
    ------------------------------------ """
    for line in output: print(str(line))
    print()


def var_dump( varname, varval ):
    """ ----------------------------------------
        Output the named of the variable 
        and the variables value
    ---------------------------------------- """
    print( f'{varname}: {varval}' )


def jprint( data, indent=4 ):
    """ ----------------------------------------
        Print out a pretty JSON 
        view of dict data
    ---------------------------------------- """
    if type(data) == dict:
        print(json.dumps(data, indent=indent))
    else:
        raise TypeError("jprint requires dict data.")


def banner( s="", char="-", pad=4, spaced=True ):
    """ -----------------------------------------------------
        Outputs a decorative headline banner with
        character lines (char) the max length of the
        text to be printed (s) at top and bottom plus 
        spacing (pad)
    ----------------------------------------------------- """
        # make a list of all the lines & strip 
        # whitespace from front & back
    s_lines = _str_to_lines(s)
        # calculate line length including line_inset on
        # front and back
    longest_line = len(max(s_lines, key=len)) + 2 * pad
        # output all content
    if spaced: print()
    print(tc.colored(char * longest_line, gColor))
    [print(tc.colored(" " * pad + line, gColor)) for line in s_lines if line]
    print(tc.colored(char * longest_line, gColor))
    if spaced: print()


def big_banner( s, char="*", pad=4, spaced=True ):
    """ -----------------------------------------------------
        Outputs a top-level decorative headline banner with
        character lines (char) the max length of the
        text to be printed (s) at top and bottom plus spacing
        (pad) and interior vertical bars on left and right.
    ----------------------------------------------------- """
        # make a list of all the lines & strip 
        # whitespace from front & back
        # add blank lines to front & back
    s_lines = _str_to_lines(s)
    s_lines.insert(0, "")
    s_lines.append("")
        # calculate line length including line_inset on
        # front and back
    longest_line = len(max(s_lines, key=len)) + 2 * pad
        # output all content
    if spaced: print()
    print(tc.colored(char * (longest_line + 2), gColor))
    for line in s_lines:
        ind = (" " * pad)
        currline = char + ind + line
        endspacing = longest_line - len(currline) - 3
        print(tc.colored(f"{char}{ind}{line}{ind}{endspacing * ' '}{char}", gColor))
    print(tc.colored(char * (longest_line + 2), gColor))
    if spaced: print()


def bannerline ( s, char='-', size=6, surround=True ):
    """ ----------------------------------------------------
        Print a single line banner
        surrounded by characters on both sides
    ---------------------------------------------------- """
    s = f" {s} "
    if surround: print()
    print(tc.colored(s.center(len(s) + size, char), gColor))
    if surround: print()


def bannerhead ( s, char="-" ):
    """ -----------------------------------------------------------
        Print comment (s) with a line of characters (char) below
    ----------------------------------------------------------- """
    s_lines = _str_to_lines(s)
    longest_line = len(max(s_lines, key=len))
    print()
    [print(tc.colored(line, gColor)) for line in s_lines]
    print(tc.colored(char * longest_line, gColor))


def prints( output ):
    """ ---------------------------------------------
        Print a string with blank lines above & below
    --------------------------------------------- """
    bl()
    print(output)
    bl()


def print_ind( s="", indent_level=1, spaces=4 ):
    """ ----------------------------------------------------------
        Print text (s) indented
        number of spaces (spaces) x an indent level (indent_level)
    ---------------------------------------------------------- """
    print(" " * int(indent_level * spaces) + str(s))


def expected( comment="", *expected, char="-", pad=0 ):
    """ ------------------------------------------------------------------
        Print a comment (can be multiple lines) with possible line insets,
        then a separator line with or without inset as the length,
        then the expected text with possible line insets
    ------------------------------------------------------------------ """
        # remove blank lines from comment and
        # split them into a list at character returns
    s_lines = _str_to_lines(comment)
        # calculate line length including pad on
        # front and back
    line_length = len(max(s_lines, key=len)) + (pad*2)
        # inset_str to place at beginning and end of line
    inset_str = " " * pad
        # output all content
    print()
    [print(tc.colored(inset_str + line + inset_str, gColor)) for line in s_lines]
    print(tc.colored(char * line_length, gColor))
        # output all expected comments
    for item in expected:
        if type(item) not in (tuple, dict, list):
            print(f'{inset_str}{item}')
        elif type(item) is dict:
            print(json.dumps(item, pad=4))
        else:
            print(f'{inset_str}{item}')