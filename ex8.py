# assigns a formatted string that takes four arguments of any type to formatter
formatter = "%r %r %r %r"

# uses 1, 2, 3, 4 as arugments for formatter
print formatter % (1, 2, 3, 4)
# uses four strings as arguments for formatter
print formatter % ("one", "two", "three", "four")
# uses four booleans as arguements for formatter
print formatter % (True, False, False, True)
# uses formatter as arguements for formatter
print formatter % (formatter, formatter, formatter, formatter)
# uses four strings as arguements for formatter
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
