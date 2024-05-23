# Define a formatter string with four placeholders.
formatter = "{} {} {} {}"

# Use the formatter to print integers.
print(formatter.format(1, 2, 3, 4))


# Use the formatter to print strings.
print(formatter.format("one", "two", "three", "four"))


# Use the formatter to print boolean values.
print(formatter.format(True, False, False, True))


# Use the formatter to print the formatter string itself, repeated four times.
print(formatter.format(formatter, formatter, formatter, formatter))


# Use the formatter to print a custom message spread across multiple lines.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

