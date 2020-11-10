def num_there(s):
    return all(i.isdigit() for i in s)

num = '10a'
 
if num_there(num):
# check and print type num variable 
    print(type(num))  
    
    # convert the num into string  
    converted_num = int(num) 
    
    # print type of converted_num 
    print(type(converted_num)) 
    
    # We can check by doing some mathematical operations 
    print(converted_num + 20) 
else:
    print ('no number')
