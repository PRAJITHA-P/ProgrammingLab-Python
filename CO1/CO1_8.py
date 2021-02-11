"""Get a string from an input string where all occurrences of first character replaced with
‘$’, except first character.
[eg: onion -> oni$n] """
string1=input("Enter a string=")
char=string1[0]
string1=string1.replace(string1[0],"$")
print(char+string1[1:])
