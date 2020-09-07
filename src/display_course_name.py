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
    print("|__/ | ___] |___ |  \ |___  |  |___")
    print("___  _ ____ ____ ____ ____ ___ ____")
    print("|  \ | [__  |    |__/ |___  |  |___")


def display_course_name_line_two():
    """Prints the first line of the course name."""
    print("[__   |  |__/ |  | |     |  |  | |__/ |___ [__")
    print("___]  |  |  \ |__| |___  |  |__| |  \ |___ ___]")
    print("____ ___ ____ _  _ ____ ___ _  _ ____ ____ ____")


def display_separator():
    """Prints a blank line separator."""
    print()


if __name__ == "__main__":
    display_course_name_line_two()
    display_separator()
    display_separator()
    display_course_name_line_one()
