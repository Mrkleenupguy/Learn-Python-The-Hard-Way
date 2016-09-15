# assign x with a formatted string
x = "There are %d types of people." % 10
# assign binary to a string
binary = "binary"
# assign do_not to a string
do_not = "don't"
# assigns a formatted string to y
y = "Those who know %s and those who %s." % (binary, do_not) # string in a string x2
# prints var x
print x
# prints var y
print y
# prints formatted string with what ever x may be
print "I said: %r." % x # string in a string
# prints formatted string with y using string flag
print "I also said: '%s'." % y # string in a string
# assigns boolean value to variable
hilarious = False
# assigns formatted string with flag to variable
joke_evaluation = "Isn't that joke so funny!? %r"
# prints variable that needs formate arguments with a variable as the argument
print joke_evaluation % hilarious
# assigns a string to w
w = "This is the left side of..."
# assigns a string to e
e = "a string with a right side."
# prints an appended string where e is appended to w
# using + with two strings appends them
print w + e
