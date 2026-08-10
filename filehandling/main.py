#opening a file in 'w' mode
# file=open('sample.txt','w')
# file.write("my name is reddy")
# file.close()
# print("content added")



#opening file in append mode
# file=open('sample.txt','a')
# file.write("my name is karthik")
# file.close()
# print("content added")


## add content at start  of file AND OPEN IN Append mode
#opening file in append mode
# file=open('sample1.txt','r+')
# file.seek(0)
# string="""I am a student i am leaning python course"""
# file.write(string)
# file.close()
# print("content added")



##opening a file in  read mode 
file = None
try:
    file = open('sample.txt', 'r')
    data = file.readlines()
    print(data)

except Exception as e:
    print(f"Something went wrong, because: {e}")

finally:
    if file is not None:
        file.close()