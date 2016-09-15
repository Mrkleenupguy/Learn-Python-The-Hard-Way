name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54 # converts height from inches to centimeters
weight = 180 # lbs
weight_kg = weight * 0.453592 # converts weight from pounds to kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depedning on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
# %f is for floating point numbers
print "My height %din in centimeters is %fcm" % (height, height_cm)
# %r converts any object into a string using repr()
print "My weight %rlbs in kilograms is %rkg." % (weight, weight_kg)
