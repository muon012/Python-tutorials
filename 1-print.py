a = 12
b = 3
print((((a + b) / 3) - 4) * 12)

c = a + b
d = c / 3
e = d - 4
f = e * 12
print(f)

name = "Francis"
number = "9,909 ,900"
parrot = 'Norwegian Blue'
print(parrot) # Returns 'Norwegian Blue';
print(parrot[8]) # Returns 'n';
print(parrot[-5]) # Returns ' ' because it is the fifth index from the end. Start from 1 not zero when using negatives;
print(parrot[0:6]) # Returns the elements from 0-6 which are "Norweg"; It EXCLUDES the last index.
print(parrot[:6]) # Returns All the elements from index 0 - 6 EXCLUDING index 6. Same result as above;
print(parrot[6:]) # Returns values from index 6 and on 'ian Blue';
print(parrot[-4:-2]) # Returns "BL" as those are index -4, -3; It EXCLUDES index -2, the last index.
print(parrot[6]) # Returns "i";
print('The sky is ' + parrot)
print(name[0:6:2]) # Start at index 0 and don't include index 6; Jump every 2 elements; It returns "Fac";
print("hi " * 5 + " 4") # Returns "hi hi hi hi hi  4";
print("for" in "fork") # Returns "True";
print(" Blue" in parrot) # "Returns "True";
print(" " in number) # Returns "True";
print(parrot[::-1]) # Returns "eulB naigewroN" as it prints the string in reversed order;
