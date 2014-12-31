import math
shape = raw_input("What shape will you be getting the area for?\n"+
                  "enter 'r' for rectangle,\n"+
                  "enter 's' for square,\n"+
                  "enter 'c' for circle,\n"+
                  "enter 'e' for ellipse\n"+
                  "enter 't' for triangle\n: ")
shape = shape.lower()
if shape == 'r': #check if shape is rectangle and calculate input
  height = raw_input("Enter the height of your rectangle: ")
  width = raw_input("Enter the width of your rectagle: ")
  area = int(height)*int(width)
  print "The area of your rectangle is %s square units." %area
elif shape == 's': #check if shape is square and calculate input
  height = raw_input("Enter the height of your square: ")
  area = int(height)**2
  print "The area of your square is %s square units." %area
elif shape == 'c': #check if shape is circle and calculate input
  radius = raw_input("Enter the radius of the circle: ")
  area = math.pi*(int(radius)**2)
  print "The area of your circle is %s square units." %area
elif shape == 'e': #check if shape is ellipse an calculate input
  height = raw_input("Enter the height of your ellipse: ")
  width = raw_input("Enter the width of your ellipse: ")
  area = int(height)*int(width)*math.pi
  print "The area of your ellipse is %s square units." %area
elif shape == 't': #check if shape is triangle and calculate input"
  base = raw_input("Enter the base of your triangle: ")
  height = raw_input("Etner the height of your triangle: ")
  area = (int(base)*int(height))/2
  print "The area of your triangle is %s square units." %area
else:
  print "You did not enter a valid option."
