# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution(I have taken code from:https://www.w3schools.com/python/). 
# Student ID: 20220033/w1953078
# Date: 12/13/2022
#hasmalee vidanya
#initial values
list=[0,20,40,60,80,100,120]
progress=0
trailer =0
retriever=0
exclude =0
def validation():
  global a,b,c  
  while True:
            try:
                a=int(input('Please enter your credits at pass: '))
            except ValueError:
                print('Integer Required')      #validation
            else:
                if a not in list:
                    print('Out of Range')      #validation
                else:
                    break

  while True:
            try:
               b=int(input('Please enter your credits at defer: '))
            except ValueError:
                print('Integer Required')         #validation
            else:
                if b not in list:
                    print('Out of Range')          #validation
                    
                else:
                    break
  while True:
            try:
                c=int(input('Please enter your credits at fail: '))
            except ValueError:
                print('Integer Required')        #validation
            else:
                if c not in list:
                    print('Out of Range')         #validation
                    
                else:
                    break


def validation0():
  global a,b,c  
  while True:
            try:
                a=int(input('Enter your total PASS credits: '))
            except ValueError:
                print('Integer Required')      #validation
            else:
                if a not in list:
                    print('Out of Range')      #validation
                else:
                    break

  while True:
            try:
               b=int(input('Enter your total DEFER credits: '))
            except ValueError:
                print('Integer Required')         #validation
            else:
                if b not in list:
                    print('Out of Range')          #validation
                    
                else:
                    break
  while True:
            try:
                c=int(input('Enter your total FAIL credits:'))
            except ValueError:
                print('Integer Required')        #validation
            else:
                if c not in list:
                    print('Out of Range')         #validation
                    
                else:
                    break

def validation1():
    global x
    x=a+b+c
    if x!=120:
        print('Total incorrect')   #validation
        validation()



                  
#checking the progression outcome                
def outcomes():
    global validation,progress,trailer,exclude,retriever 
   
    if a==120:
        print('progress')
        progress += 1
      
    elif a==100:
        print("Progress(Module Trailer)")
        trailer +=1            #outcomes     
        
    elif c>=80:
        print("Exclude")
        exclude +=1            #outcomes     
        
    else:
        print("Module Retriever")
        retriever +=1          #outcomes
        
#creating the vertical histogram       
def my_function():
        global total
        
        print('----------------------------------------------------------\nHistogram') #Histogram 
        print()
        print('Progress' ,progress ,':', progress*'* ')
        print('Trailer',trailer, ':' , trailer*' * ' )
        print('Retriever',retriever, ':', retriever*' * ' )
        print('Excluded',exclude,':', exclude*' * ' )
        total=progress+trailer+retriever+exclude
        print()
        print( total  ,'outcomes in total.')
        print('------------------------------------------------------------')


def main_part():
 global H
 while True:
  H=str(input("enter 's' to student version or 't' to staff version:  "))
  if H=='s':
     validation()
     validation1()
     outcomes()
     break  
  if H=='t':
    while True:

      
      validation0()
      validation1()
      outcomes()
      I=(input("Would you like to enter another set of data? \n" "Enter 'y' for yes or 'q' to quit and view results: ")) #multiple outcomes

      
      if I=='y':
        True

        
      elif I=='q':
        my_function()
        return
          
      elif ValueError:
        
        print('required correct response')
        break
      
      
  elif ValueError:
        print('required valid string')
        
     
main_part() 
