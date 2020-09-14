"""Display the name of the course using individual characters."""

# First line of the course name:

# ___  _ ____ ____ ____ ____ ___ ____
# |  \ | [__  |    |__/ |___  |  |___
# |__/ | ___] |___ |  \ |___  |  |___

# Second line of the course name:

# ____ ___ ____ _  _ ____ ___ _  _ ____ ____ ____
# [__   |  |__/ |  | |     |  |  | |__/ |___ [__
# ___]  |  |  \ |__| |___  |  |__| |  \ |___ ___]

def display_course_name_line_one():
    """Prints the first line of the course name."""
    print("___  _ ____ ____ ____ ____ ___ ____")
    print("|  \ | [__  |    |__/ |___  |  |___")
    print("|__/ | ___] |___ |  \ |___  |  |___")


def display_course_name_line_two():
    """Prints the first line of the course name."""
    print("____ ___ ____ _  _ ____ ___ _  _ ____ ____ ____")
    print("[__   |  |__/ |  | |     |  |  | |__/ |___ [__")
    print("___]  |  |  \ |__| |___  |  |__| |  \ |___ ___]")


def display_separator():
    """Prints a blank line separator."""
    print()


if __name__ == "__main__":
    display_course_name_line_one()
    display_separator()
    display_separator()
    display_course_name_line_two()
