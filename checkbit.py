from PIL import Image

image = Image.open("image/images.jpg")
bit_depth = image.mode
print(bit_depth)


array = [1,2,3,4,5]
for i in array:
    print(i)
print("===========")
for i in reversed(array):
    print(i)