blocks = int(input("Enter the number of blocks: "))
layer = 1
height = 0

while blocks >= layer:
    blocks -= layer
    layer += 1 
    height += 1
    
print("The height of the pyramid:", height)

# The code calculates the height of a pyramid based on the number of blocks provided by the user. 
# It uses a while loop to determine how many layers can be built with the given blocks, incrementing 
# the layer and height until there are not enough blocks left to build the next layer.
