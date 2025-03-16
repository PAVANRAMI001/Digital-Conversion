
print('''Only This Type Of Conversion Is Avaible:

1.)Binary_To_Hexadecimal
2.)Binary_To_Octal
3.)Binary_To_Decimal
4.)Decimal_To_Hexadecimal
5.)Decimal_To_Octal
6.)Decimal_To_Binary
7.)Octal_To_Binary
8.)Octal_To_Decimal
9.)Hexadecimal_To_Octal
10.)Hexadecimal_To_Binary
11.)Hexadecimal_To_Decimal

''')

def Hexadecimal_To_Octal(Number):
     
    Hexadecimal_To_Binary(Number)
    Binary_To_Octal(result)
    
def Hexadecimal_To_Binary(Number):

    global result
    
    value={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111','':''}    
    convert=[]
    
    for i in range(0,len(Number)):
        convert.append(value[Number[i]])

    result=''.join(convert)
    print("The Binary number Is : ",result)
    
def Hexadecimal_To_Decimal(Number):

    value={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    Sum=0
    power=len(Number)
  
    for i in range(0,power):
      
        if Number[i] in value:
            Convert=(value[Number[i]])*pow(16,(power-i)-1)
            
        else:
            Number[i]=int(Number[i])
            Convert=(Number[i])*pow(16,(power-i)-1)
        Sum += Convert
       
    print('The Decimal Number Is :',Sum)

def Octal_To_Binary(Number):

    value={'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111','':''}
    Number=str(Number)
    Number=list(Number)
    convert=[]
    
    for i in range(0,len(Number)):

        convert.append(value[Number[i]])
        
    result=''.join(convert)
    print("The Binary number Is : ",result)
    

def Octal_To_Decimal(Number):

    Sum=0
    Number=str(Number)
    Number=list(Number)    
    power=len(Number)
  
    for i in range(0,power):

        Number[i]=int(Number[i])
        Convert=(Number[i])*pow(8,(power-i)-1)
        Sum += Convert
       
    print('The Decimal Number Is :',Sum)

def Binary_To_Hexadecimal(Number):

    sumN=0
    Convert=[]
    result=[]
    value={'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F','':''}
   
    Number=str(Number) 
    Number=list(Number)
    limit=len(Number)
    x=limit
        
    for i in range(4,(limit*4)-4,4):

        if limit<4:
            break
        
        joinS=''.join(Number[limit-i:x:1])
        Convert.append(joinS)
        x=limit-i
        sumN += len(joinS)      
        if joinS=='':
                break
            
    difference=limit-sumN
    if sumN<limit:
                    
        if difference==1:

            Number.insert(0,'0')
            Number.insert(1,'0')
            Number.insert(2,'0')
            joinS=''.join(Number[0:4:1])
            Convert.append(joinS)
     
        elif difference==2:
            
            Number.insert(0,'0')
            Number.insert(1,'0')
            joinS=''.join(Number[0:4:1])
            Convert.append(joinS)
          
        else:
            if difference==3:
                
                
                Number.insert(0,'0')
                joinS=''.join(Number[0:4:1])
                Convert.append(joinS)
            else:
                #print("The Difference is 0!!!")
                pass                             
    else:        
        pass

    for j in range(0,len(Convert)):
        
        result.append(value[Convert[j]])
        
    result.reverse()   
    conversion=''.join(result)
    print("The Conversion Of Binary To Hexadecimal Is :",conversion)    

def Binary_To_Octal(Number):

    sumN=0
    Convert=[]
    result=[]
    value={'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7','':''}    
    Number=str(Number)    
    #This Is Anothere Algorithm
    '''if limit%3==1:
        Number = '00' + Number
    elif limit%3==2:
        Number = '0' + Number
    else:
        pass'''
    Number=list(Number)

    limit=len(Number)

    x=limit    
    
    for i in range(3,(limit*3)-3,3):
                       
        joinS=''.join(Number[limit-i:x:1])
        Convert.append(joinS)
        x=limit-i
        sumN += len(joinS)
        
        if joinS=='':
                break
            
    difference=limit-sumN    
    if sumN<limit:
                    
        if difference==1:

            Number.insert(0,'0')
            Number.insert(1,'0')
            joinS=''.join(Number[0:3:1])
            Convert.append(joinS)
     
        else:
            if difference==2:
                Number.insert(0,'0')
                joinS=''.join(Number[0:3:1])
                Convert.append(joinS)
          
            else:
                print("The Difference is 0!!!")
                pass
    else:
        pass    

    for j in range(0,len(Convert)):
        
        result.append(value[Convert[j]])
        
    result.reverse()    
    conversion=''.join(result)
    print("The Conversion Of Binary To Octal Is :",conversion)
    
def Decimal_To_Hexadecimal(Number):

    Convert=[]
    
    value={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    
    for i in range(0,Number):

        if Number==0:
            #Convert.append(0)
            break
        
        mod=Number%16
        Number=Number//16
        if mod>9:
            Convert.append(value[mod])
        else:
            
            Convert.append(str(mod))
    
    Convert.reverse()
    Convert=''.join(Convert)
    print(f"The Conversion Of This Decimal Into Hexadecimal Is : ",Convert)

def Decimal_To_Octal(Number):

    Convert=[]
    
    for i in range(0,Number):

        if Number==0:
            #Convert.append(0)
            break
        
        mod=Number%8
        Number=Number//8
            
        Convert.append(mod)
        
    print(Convert)
    print(f"The Conversion Of This Decimal Into Octal Is : ",end='')
  
    for j in range(len(Convert)-1,0,-1):
        
        Binary_num=Convert[j]
        print(Convert[j],end='')
        if j==1:
            print(Convert[0],end='')

def Binary_To_Decimal(Number):

    Sum=0
    Number=str(Number)
    Number=list(Number)
    
    power=len(Number)
  
    for i in range(0,power):

        Number[i]=int(Number[i])
        Convert=(Number[i])*pow(2,(power-i)-1)
        Sum += Convert

       
    print('The Decimal Number Is :',Sum)
   

 
   
def Decimal_To_Binary(Number):
    
    Convert=[]
    
    for i in range(0,Number):

        if Number==0:
            #Convert.append(0)
            break
        
        mod=Number%2
        Number=Number//2
        mod = str(mod)    
        Convert.append(mod)

    Convert.reverse()
    result=''.join(Convert)
    print(f"The Conversion Of This {Number} Into Binary Is : {result}")

input_type=input("Enter the Type Of Input Number:").title()   
output_type=input("Enter the Type Of Output Number:").title()
      
function_name=input_type+'_To_'+output_type

if function_name in globals():
    Number=input("Enter The "+input_type+" Number:")
    if input_type=='decimal' or input_type=='Decimal':
        Number=int(Number)

    if input_type=='hexadecimal' or input_type=='Hexadecimal':
        Number=str(Number)
        Number=list(Number)
    
    globals()[function_name](Number)
else:
    print("Enter The Valid Function Name!!!!")
