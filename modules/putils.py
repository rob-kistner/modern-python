class Putils:
    """
    A collection of print utilties to use when testing python scripts or following code-along tutorials.
    """
    import json  # for json.dumps()

    def __init__(self, char="-", indent=4):
        self.__char = char
        self.__indent = indent

    # getters / setters

    def get_char(self):
        return self.__char

    def get_indent(self):
        return self.__indent

    def set_char(self, char):
        self.__char = char

    def set_indent(self, indent):
        self.__indent = indent

    # methods

    def bl(self):
        """ ----------------------------
            Just print a blank line
        ---------------------------- """
        print()

    def sep(self, char=_Putils__char, pad=20):
        """ -------------------------------------
            Outputs a character a number of times
            to make a visual separator.
        ------------------------------------- """
        print(char * pad)

    def pl(self, output):
        """ ------------------------------------
            print output following by a blank line
        ------------------------------------ """
        print(output)
        print()

    def var_dump(self, varname, varval):
        """ ----------------------------------------
            Output the named of the variable and the 
            variables value
        ---------------------------------------- """
        print(f'{varname}: {varval}')

    def jprint(self, data, indent=4):
        """ ----------------------------------------
            Print out a pretty JSON view of 
            dict data
        ---------------------------------------- """
        print(json.dumps(data, indent=indent))

    def banner(self, s="", char=self.__char, pad=self.__indent, spaced=True):
        """ -----------------------------------------------------
            Outputs a decorative headline banner with
            character lines (char) the max length of the
            text to be printed (s) at top and bottom plus spacing
            (pad)
        ----------------------------------------------------- """
        # remove blank lines from comment and
        # split them into a list at character returns
        s_lines = s.strip().split("\n")
        # also strip the individual comment lines
        s_lines = list(map(lambda line: line.strip(), s_lines))
        # calculate line length including line_inset on
        # front and back
        line_length = len(max(s_lines, key=len)) + 2 * pad

        if spaced:
            print()
        print(char * line_length)
        [print(" " * pad + line) for line in s_lines]
        print(char * line_length)
        if spaced:
            print()


def big_banner(s="", char="*", pad=self.__indent, spaced=True):
    """ -----------------------------------------------------
        Outputs a top-level decorative headline banner with
        character lines (char) the max length of the
        text to be printed (s) at top and bottom plus spacing
        (pad) and interior vertical bars on left and right.
    ----------------------------------------------------- """
    # remove blank lines from comment and
    # split them into a list at character returns
    s_lines = s.strip().split("\n")
    # also strip the individual comment lines
    s_lines = list(map(lambda line: line.strip(), s_lines))
    # calculate line length including line_inset on
    # front and back
    line_length = len(max(s_lines, key=len)) + 2 * pad
    # blank line if spaced = True, followed by chars
    if spaced:
        print()
    print(f"{char * (line_length+2)}")
    # print each line with vert bars on either end
    for line in s_lines:
        ind = (" " * pad)
        currline = char + ind + line
        endspacing = line_length - len(currline) - 3
        print(f"{char}{ind}{line}{ind}{endspacing * ' '}{char}")
        # blank line if spaced = True, followed by chars
    print(f"{char * (line_length+2)}")
    if spaced:
        print()

    def bannerline(self, s, char=self.__char, pad=30, surround=True):
        """ ----------------------------------------------------
            Print a single line banner
            surrounded by characters on both sides
        ---------------------------------------------------- """
        s = f" {s} "
        if surround:
            print()
        print(s.center(len(s) + pad, char))
        if surround:
            print()

    def bannerhead(self, s, char=self.__char):
        """ -----------------------------------------------------------
            Print comment (s) with a line of characters (char) below
        ----------------------------------------------------------- """
        s_lines = s.strip().split("\n")
        s_lines = list(map(lambda line: line.strip(), s_lines))
        line_length = len(max(s_lines, key=len))

        print()
        [print(line) for line in s_lines]
        print(char * line_length)

    def prints(self, output):
        """ ---------------------------------------------
            Print a string with blank lines above & below
        --------------------------------------------- """
        bl()
        print(output)
        bl()

    def print_ind(self, s="", indent_level=1, spaces=4):
        """ ----------------------------------------------------------
            Print text (s) indented
            number of spaces (spaces) x an indent level (indent_level)
        ---------------------------------------------------------- """
        print(" " * int(indent_level * spaces) + str(s))

    def expected(self, comment="", expected="", char=self.__char, indent=0):
        """ ------------------------------------------------------------------
            Print a comment (can be multiple lines) with possible line insets,
            then a separator line with or without inset as the length,
            then the expected text with possible line insets
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
        print(char * line_length)
        # print inset and the expected string
        if type(expected) not in (tuple, dict, list):
            print(f'{inset_str}{expected}')
        elif type(expected) is dict:
            print(json.dumps(expected, indent=4))
        else:
            for expected_item in expected:
                print(f'{inset_str}{expected_item}')
