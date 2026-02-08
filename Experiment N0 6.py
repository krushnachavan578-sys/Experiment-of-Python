#student in exam
cet = {"alice", "bob"}
jee = {"bob", "eve"}
neet = {"alice", "eve"}
print("All student:", cet | jee | neet) #union
print("student in all exam:", cet & jee & neet) #intersection
print("cet but not jee:",cet-jee) #difference
    
