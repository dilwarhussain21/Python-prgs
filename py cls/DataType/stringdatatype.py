name = 'KodNest'
print(id(name))

s1 = 'Code with KodNest'
print(s1[0]) #0th index value from s1 string
print(s1[1]) #1st index value from s1 string
print(s1[3]) #3rd index value from s1 string
print(s1[4]) #4th index value from s1 string

print('Length of s1 is:',len(s1)) #17
print(s1[16]) #last index (last digit - 1 (that is first digit))
print(s1[-1]) #last index in another way

s2 = 'Kodnest'
sub_string = s2[0:3]
print(sub_string) #kod (n will not be printed because of last digit - 1)

s3 = 'Code'
print(s3.upper()) #CODE
s4 = 'CODE'
print(s3.lower()) #code
