# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20211230(IIT ID) / w1898910
# Date: 16/04/2022


#-------------------------------

#variable for validation part
crdt_range=range(0,121,20)
valid_total=False

#variable for continue entering data
data_loop=True

#variable for Selecting to the  version
version=0

# variables for horizontal histogram
progress=0
trailer=0
retriever=0
excluded=0
count=1

# extension for printing data (part 3)
progression_list=[]

#----------------------------------------------
# function for Horizontal Histogram

def histogram():
    print("-"*60)
    print("Horizontal Histogram")
    print("Progress",progress,"\t: "+"*"*progress)
    print("Trailer",trailer,"\t: "+"*"*trailer)
    print("Retriever",retriever,"\t: "+"*"*retriever)
    print("Excluded",excluded,"\t: "+"*"*excluded+"\n")
    print(count,"outcomes in total")
    print("-"*60)
#----------------------------------------------
# function for validation part


def inputdata():
    global valid_total,crdt_pass,crdt_range,crdt_defer,crdt_fail
 
            #validation(2)
  
    while(not(valid_total)):
        #validation of credit at PASS
        
        while(True):    
            try:
                crdt_pass=int(input("Please enter your credits at pass\t: "))
                if(crdt_pass in crdt_range):
                    break
                else:
                    print("Out of range\n")
            except(ValueError):
                print('Integer required\n')
        
        
        #validation of credit at DEFER
        
        while(True):      
            try:
                crdt_defer=int(input("Please enter your credit at defer\t: "))
                
                if(crdt_defer in crdt_range):
                    break
                else:
                    print("Out of range\n")
            except(ValueError):
                print("Integer required\n")
       

        #validation of credit at FAIL
        
        while(True):
            try:
                crdt_fail=int(input("Please enter your credit at fail\t: "))
                if(crdt_fail in crdt_range):
                    break
                else:
                    print("Out of range\n")
            except ValueError:
                print("Integer required\n")
  
        if(crdt_pass+crdt_defer+crdt_fail)==120:
            valid_total=True
        else:
            print("Total incorrect\n")
#----------------------------------------------------
# function for progression outcomes

def progression():

    global crdt_pass,crdt_fail,progress,trailer,retriever,excluded,output
  # Progression outcome
    if(crdt_pass==120):
        print("Progress")
        progress+=1
        output="Progress"       #print data
        
    elif(crdt_pass==100):
        print("Progress (module trailer)")
        trailer+=1
        output="Progress (module trailer)"          #print data
        
    elif((crdt_pass==80) or (crdt_pass==60)):
        print("Do not Progress – module retriever")
        retriever+=1
        output="Module retriever"           #print data
        
    elif((crdt_pass<=40) and (crdt_fail>=80)):
        print("Exclude")
        excluded+=1
        output='Exclude'        # print data
        
    else:
        print("Do not progress – module retriever")
        retriever+=1
        output='Retriever'      #print data

#---------------------------------------------------------------
# Selecting the staff / students version

version=input("Type 'Staff' for staff version or 'Student' for student version : ")

if(version== 'student' or version=="Student"):
    print('\nStudent Version\n')
    
    inputdata()

    progression()

#----------End of the Student version----------------------------------

#--------------Start of the Staff version------------------------------

elif version=="staff" or version =="Staff":
    print()
    print('Staff Version with Histogram\n')
    #--------------------------------------------------
    while data_loop:
           #---------validation part--------------
        inputdata()

            #----------progression outcomes--------

        progression()

            #-------data list--------
        progression_list.append((output,' - ',crdt_pass,', ',crdt_defer,', ',crdt_fail))

            #-------continue to enter data ----------   
       
        while(True):
            print("\nWould you like to enter another set of data?")
            entry=input("Enter 'y'for yes or 'q' to quit and view results: ")
            print()

            if(entry=="y"):
                data_loop=True
                valid_total=False
                count=count+1
                break
                    
            elif(entry=="q"):
                data_loop=False
                histogram()
                break
                    
            else:
                data_loop=False
                print("Invalid response.Try again.")

   #---------------- part 2--------------------
                #vertical histogram
 
                #using two dimensional list

    print("Progress ",'Trailer  ','Retriever',' Excluded ')
    vertical_hist=[[],[],[],[]]
    for x in range(progress):
        vertical_hist[0].append("   *")

    for x in range(trailer):
        vertical_hist[1].append("   *")

    for x in range(retriever):
        vertical_hist[2].append("   *")

    for x in range(excluded):
        vertical_hist[3].append("    *")

    for i in range(max(progress,trailer,retriever,excluded)):
        for x in vertical_hist:
            try:
                print(x[i],end='      ')
            except:
                print('    ',end='      ')
        print()
            
                   
    #------------------------------------
    #to print data
        
    print("-"*60)
    for row in progression_list:
        for col in row:
            print(col, end='')
        print()
else:
    print("Invalid input run the program again")

#---------------------------------------------------------------------------------------------------------------------



