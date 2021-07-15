dict_a={
    "A" :"Hello",
    "B" : "World",
    "C" : "Buddy",
    "D" : "Welcome"
}
n=input().split()

for i in range(len(n)):
    if n[i]=="and":
        s1=n[i-1]
        s2=n[i+1]
        s=dict_a[s1]+dict_a[s2]
    if n[i]=="or":
        s1=n[i-1]
        s2=n[i+1]
        s=dict_a[s1] or dict_a[s2]
print(s)