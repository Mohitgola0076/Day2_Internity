'''
Exception handling increases the robustness of your code, which guards against potential failures that would cause your program to exit in an uncontrolled fashion.
'''

# 1.)  Keyboard Interrupt exception.

try:
    inp = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')
    
# Output : Caught KeyboardInterrupt


# 2.)  Zero Division Exception.

try:  
    a = 100 / 0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
else:  
    print ("Success, no error!")
    
# Output : Zero Division Exception Raised.

# 3.) Overflow Error.

try:  
    import math
    print(math.exp(1000))
except OverflowError:  
        print ("OverFlow Exception Raised.")
else:  
    print ("Success, no error!")
    
# Output :  OverFlow Exception Raised.


# 4.) Assertion Error

try:  
    a = 100
    b = "DataCamp"
    assert a == b
except AssertionError:  
        print ("Assertion Exception Raised.")
else:  
    print ("Success, no error!")
    
# Output : Assertion Exception Raised.

# 5.)  Key Error 

try:  
    a = {1:'a', 2:'b', 3:'c'}  
    print (a[4])  
except LookupError:  
    print ("Key Error Exception Raised.")
else:  
    print ("Success, no error!")
    
# Output : Key Error Exception Raised.
