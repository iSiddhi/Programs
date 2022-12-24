# import os
# try:
# if os.path.exists("DEMO2.txt"):
    # os.remove("DEMO2.txt")
# else:
    # print("file does not exist")

#try:
# this block of code will run and throw errors if there are any error

#except - this will raise the error 
#else - this will exicute if there is no error
# finally - this will execute regardless the result of try and except



try:
    f=open("demo.txt")
    try:    
         f.write("abc")
    except:
        print("error in file")
    finally:
        f.close()
except:
    print("error.error.error...........")


a=5
if a<10:
    raise Exception("value is less than 5")    




  