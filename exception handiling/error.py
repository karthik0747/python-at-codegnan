#exceptional handling blocks
'''try:
    a=int(input())
    b=int(input())
    c=a+b
    print(c)
except:
    print("Some thing wrong in try block")
else:
    print("There is no Exception in try block")
finally:
    print("Program done")'''



#exceptional handling blocks
#with an exception
'''try:
    a=int(input())
    b=int(input())
    c=a+b
    print(c)
except:
    print("Some thing wrong in try block")
else:
    print("There is no Exception in try block")
finally:
    print("Program done")'''


#exceptional handling blocks
#exception with an exception class
'''try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception as e:
    print(f"Some thing wrong in try block:{e}")'''



#exceptional handling blocks
#define multiple exceptions with difference except block
'''try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(f"Zero division not possible:{e}")
except IndexError as e:
    print(f"We cant access element at this position:{e}")
except Exception as e:
    print(f"Some thing wrong in try block:{e}")'''

#exceptional handling blocks
#define multiple exceptions with difference except block
try :
    arr=[1,2,3,4]
    c=arr[10]
    print(c)
except ZeroDivisionError as e:
    print(f"Zero division not possible:{e}")
except IndexError as e:
    print(f"We cant access element at this position:{e}")
except Exception as e:
    print(f"Some thing wrong in try block:{e}")

#exceptional handling blocks
#define multiple exceptions with difference except block
'''try :
    a=10
    c=len(a)
    print(c)
except ZeroDivisionError as e:
    print(f"Zero division not possible:{e}")
except IndexError as e:
    print(f"We cant access element at this position:{e}")
except Exception as e:
    print(f"Some thing wrong in try block:{e}")'''

