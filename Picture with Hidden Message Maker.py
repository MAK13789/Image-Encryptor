from matplotlib import pyplot as plt
letter_to_number = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26} 
temp = []
concatenated = ''
pixel_values = []
pixels = []
message = input("Give the phrase you want to encrypt in an image")
message = message.upper()
for i in range(len(message)):
    if (message[i].isalpha() == True):
        temp.append(letter_to_number[message[i]])
for j in range(len(temp)):
    concatenated += str(temp[j])
for k in range(len(concatenated)):
    if (k % 3 == 0 and k <= (len(concatenated)-3)):
        pixel_list = ''
        pixel_list += concatenated[k]
        pixel_list += concatenated[k+1]
        pixel_list += concatenated[k+2]
        pixel_values.append(pixel_list)
for l in range(len(pixel_values)):
    pixel_values[l] = int(pixel_values[l])
    if (pixel_values[l] > 255):
        pixel_values[l] = 255
for x in range(len(pixel_values)):
    if (x <= (len(pixel_values) - 3) and (x % 3 == 0)):
        temp_list = []
        temp_list.append(pixel_values[x])
        temp_list.append(pixel_values[x+1])
        temp_list.append(pixel_values[x+2])
        pixels.append(temp_list)
plt.imshow(pixels, interpolation='nearest')
plt.show()

