# Modern Python
A Udemy.com class


***

### PrintUtils library

Many of these use the `printutils` library located here:

>  **/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/printutils/**

Import with: `from printutils import *`


**`clear()`**

    Pass on laptop

**`bl()`**

    Outputs a single blank line

**`sep( padchar="-", padlength=20 )`**

    Outputs a character a number of times
    to make a visual separator

**`bannerline( s="", padchar="-", padlength=10 )`**

    Print a certain length line (padlength) padded
    with a charcters (padchar) ending at an arrow head
    and a short text description (s)

**`bannerhead(s="", padchar="-")`**

    Print comment (s) with a line of characters (padchar) below

**`expected(comment="", expected="", padchar="-", line_inset=0)`**

    Print a comment (can be multiple lines) with possible line insets,
    then a separator line with or without inset as the length,
    then the expected text with possible line insets

**`banner(s="", padchar="-", indentlength=4)`**

    Outputs a decorative headline banner with
    character lines (padchar) the max length of the
    text to be printed (s) at top and bottom plus spacing
    (indentlength)

**`print_ind(s="", indent_level=1, spaces=4)`**

    Print text (s) indented 4 spaces (spaces) x
    an indent level (indent_level)
