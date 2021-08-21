# %%
# Here is a piece of code that shows how to open a text file and append some 
# text in it.
f = open('file.txt', 'a')

print(f)

s_write = '''This is a piece of text to be written on the file.
This is a newline. 
This is another new line.
'''

f.write(s_write)
f.close()

# %%
