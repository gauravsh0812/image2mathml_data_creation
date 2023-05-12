import chardet

file_path = '/home/skema/img2mml/gauravs_data_for_paper/data/im2latex-103K/formulas.lst'

# Read the contents of the file as binary data
with open(file_path, 'rb') as file:
    byte_data = file.read()

# Detect the encoding of the byte data
result = chardet.detect(byte_data)
encoding = result['encoding']

print(f"The file encoding is: {encoding}")
