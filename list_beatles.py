beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(member)

del beatles[3]
del beatles[3]

beatles.insert(0,"Ringo Starr")

# testing list legth
print("The Fab", len(beatles))
print(beatles)