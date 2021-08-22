# %%
# Here's an illustration of how we can execute some shell scripts from 
# Python code.
import os

# The Commands to be executed
c = '''ls
rm file.txt
touch file_by_python.txt
python
'''
os.system(c)

print('\nThe commands executed successfully.')