# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution(I have taken code from:https://www.w3schools.com/python/). 
# Student ID: 20220033/w1953078
# Date: 12/13/2022
# hasmalee vidanya
#initial values
dict={0,20,40,60,80,100,120}
progress=0
trailer =0
retriever=0
exclude =0
dict_2={}


def validation0():
  global a,b,c, st_id
  
  st_id=input('Enter your student id:')
  while True:
            try:
                a=int(input('Enter your total PASS credits:  '))
            except ValueError:
                print('Integer Required')      #validation
            else:
                if a not in dict:
                    print('Out of Range')      #validation
                else:
                    break

  while True:
            try:
               b=int(input('Enter your total DEFER credits:  '))
            except ValueError:
                print('Integer Required')         #validation
            else:
                if b not in dict:
                    print('Out of Range')          #validation
                    
                else:
                    break
  while True:
            try:
                c=int(input('Enter your total FAIL credits: '))
            except ValueError:
                print('Integer Required')        #validation
            else:
                if c not in dict:
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
#referances:https://www.programiz.com/python-programming      
def outcomes():
    global validation,progress,trailer,exclude,Exclude,retriever,Module_Retriever,dict_2,st_id
    
 
    if a==120:
        print('progress ')
        dict_2[st_id] = f'progress - {a},{b},{c}'
        progress += 1
        
    elif a==100:
        print("Progress(Module Trailer)  ")
        dict_2[st_id] = f'Progress (Module Trailer) - {a},{b},{c}'
        trailer +=1            #outcomes     
        
    elif c>=80:
        print("Exclude")
        dict_2[st_id] = f'Exclude - {a},{b},{c}'
        exclude +=1            #outcomes     
        
    else:
        print("Module Retriever  ")
        dict_2[st_id] = f'Module Retriever - {a},{b},{c}'
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
        
        for (element1,element2) in dict_2.items():
       
            print( element1,' : ' ,element2, end=' ')
            
        
def main_part(): #in this programme i didn't add student or staff version 
 global I
 
 while True:
      
      validation0()
      validation1()
      outcomes()
      try:
        I=(input("Would you like to enter another set of data? \n" "Enter 'y' for yes or 'q' to quit and view results: ")) #multiple outcomes
      
        if I=='y':
          True
        
        elif I=='q':
          my_function()
          return

        elif ValueError:
          print('required correct response....you have to restart the program')
          break
      except ValueError:
          print('required correct response')
      
               
     
main_part() 
