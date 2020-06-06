#
#   printutils
#
#   A collection of print utilties to use
#    when testing python scripts or following
#    along with code-along tutorials.
#

""" ----------------------------
    Just print a blank line (bl)
---------------------------- """
def bl(): print()


""" --------------
    Pass on laptop
-------------- """
def clear():
    pass


""" -------------------------------------
    Outputs a character a number of times
    to make a visual separator

    args:
        padchar (string, default: "-"):
            The character to repeat

        padlength (int, default: 20):
            The amount of repeats to make
------------------------------------- """
def sep ( padchar="-", padlength=20 ):
    print( padchar * padlength )


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
----------------------------------------------------- """
def banner(s="", padchar="-", indentlength=4):
        # remove blank lines from comment and
        # split them into a list at character returns
    s_lines = s.strip().split("\n")
        # also strip the individual comment lines
    s_lines = list(map(lambda line: line.strip(), s_lines))
        # calculate line length including line_inset on
        # front and back
    line_length = len(max(s_lines, key=len)) + 2 * indentlength

    print()
    print(padchar * line_length)
    [print(" " * indentlength + line) for line in s_lines]
    print(padchar * line_length)
    print()

""" ----------------------------------------------------
    Print a single line banner
    surrounded by characters on both sides

    @params
        s (string, required):
            the banner text to output

        char (string, default: '-'):
            the top / bottom line characters

        amount (int, default: 30):
            the amount of surround characters

        surround (bool, default: True):
            if true, adds a blank line to top and bottom

    @returns void
---------------------------------------------------- """
def bannerline ( s, char='-', amount=30, surround=True ):
    s = ' %s ' % s
    if surround: print()
    print(s.center(len(s) + amount, char))
    if surround: print()


""" -----------------------------------------------------------
    Print comment (s) with a line of characters (padchar) below

    args:
        s (string):
            the comment string to print

        padchar (string, default: "-"):
            the character to print as a line
----------------------------------------------------------- """
def bannerhead ( s="", padchar="-" ):
    s_lines = s.strip().split("\n")
    s_lines = list(map(lambda line: line.strip(), s_lines))
    line_length = len(max(s_lines, key=len))

    print()
    [print(line) for line in s_lines]
    print(padchar * line_length)


""" ---------------------------------------------
    Print a string with blank lines above & below

    args:
        s (string, required):
            the text string to print
--------------------------------------------- """
def printsurround(s):
    bl()
    print(s)
    bl()


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
def print_ind(s="", indent_level=1, spaces=4):
    print(" " * int(indent_level * spaces) + str(s))


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
def expected (comment="", expected="", padchar="-", line_inset=0):
        # remove blank lines from comment and
        # split them into a list at character returns
    comment_lines = comment.strip().split("\n")
        # also strip the individual comment lines
    comment_lines = list(map(lambda line: line.strip(), comment_lines))
        # calculate line length including line_inset on
        # front and back
    line_length = len(max(comment_lines, key=len)) + (line_inset*2)
        # inset_str to place at beginning and end of line
    inset_str = " " * line_inset

        # blank line at the top
    print()
        # print each comment line plus the insets
    [print(inset_str + line + inset_str) for line in comment_lines]
        # print separatator
    print(padchar * line_length)
        # print inset and the expected string
    print(inset_str + expected)
