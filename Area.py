import os
import time
from math import pi
#Imports the maths pi module
def area_circle():#Defines the formula for finding area of a circle
    print("The formula for finding the area of a circle is πr² or πd")
    try:
        inp = int(input("* Enter '1' to use formula: πr²\n* Enter '2' to use formula:πd\n"))
        if inp > 2 or inp < 1:
            print("Input allowed is 1 & 2")
        elif inp == 1:
            print("You chose formula;πr²")
            radius = int(input("Enter the radius of the circle here: "))
            area = (pi * (radius*2))
            print("The area of the circle is ", area)
        elif inp == 2:
            print("You chose formula; πd")
            diameter = int(input("Enter the diameter here: "))
            area = (pi * diameter)
            print("The area of the circle is ",area)
        
        
        
      # Except statements prevent errors  
    except TypeError:
        print("Input not allowed") 
    except SyntaxError:
        print("Input not allowed")   
    except NameError:
        print("Input not allowed")
    except TypeError:
        print("Input not allowed")
    except ValueError:
        print("Input not allowed")
        

      

def area_square():
    print("The formula for finding the area of the square is lenght by 4")  
    try:
        length = int(input("Enter the length of one side of the square\n")) 
        area = (length * 4)                  
        print("The area of the square is ",area)             
    except TypeError:
        print("Input not allowed") 
    except SyntaxError:
        print("Input not allowed")   
    except NameError:
        print("Input not allowed")
    except TypeError:
        print("Input not allowed")
    except ValueError:
        print("Input not allowed")
        
         
def area_rectangle():
    while True:
        print("The formula for finding the area of a rectangle is length by width or breadth")
        try:
            length = int(input("Enter the length of the rectangle: "))
            width = int(input("Enter the width or breadth here: "))
            area = (length * width)
            print("The area of the rectangle is",area)
            break
        except TypeError:
            print("Input not allowed, try again") 
            time.sleep(1)
            os.system("clear")
        except SyntaxError:
            print("Input not allowed, try again")   
            time.sleep(1)
            os.system("clear")
        except NameError:
            print("Input not allowed, try again")
            time.sleep(1)
            os.system("clear")
        except TypeError:
            print("Input not allowed, try again")
            time.sleep(1)
            os.system("clear")
        except ValueError:
            print("Input not allowed, try again")
            time.sleep(1)
            os.system("clear")
    
