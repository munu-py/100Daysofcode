
s1 = "132 456 Wq  m e"
list1=s1.split()
s2=" ".join(word.capitalize() for word in list1)
print(s2)