# Managing Data and Processes
# Environment Variables

#!/usr/bin/anv python3

import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", "")) # the getMethod allows us to specify a default value when the key that we're looking for isn't in the dictionary

# we define the variable by just setting a value using the equal sign and leaving no spaces in between. Along with this, the export keyword tells a shell that we want the value we set to be seen by any commands that we call. 
export FRUIT=Pineapple



# Data Streams
# More About Input Functions

''' Now, you may have noticed that most of the Python code samples we've used include the line 

#!/usr/bin/env python3

Now, this is important, because it sets the Python version to Python 3.

There are some subtle differences in how data streams are handled in Python 3 and older versions, such as Python 2. Let’s just focus on input() and raw_input(), 
because they work differently in Python 2 and 3, and you would want to use one or the other depending on the Python version.

 '''

# In Python 2
# Taking an input from a user, raw_input should be used:

>>> my_number = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
1337
>>> print(my_number)
1337
>>>

# Now, this is important, because, raw_input does not evaluate an otherwise valid Python expression. 
# In simple terms, raw_input will just get a string from a user, where input will actually perform basic maths and the like. See below:

>>> my_raw_input = raw_input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1  # This is treated like a raw string.
>>> my_input = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1 # This is treated like an expression.
>>> print(my_raw_input)
123 + 1
>>> print(my_input)
124 # See that the expression was evaluated!

#In Python 2 input(x) is just eval(raw_input(x)). eval() will just evaluate a generic string as if it were a Python expression.

#In Python 3
#Taking an input from a user, input should be used. See the below sample:

>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> type(my_number)
<class 'str'>

# Notice that the expression is treated just like a string. It is not evaluated.
# If we want to, we can call eval() and that will actually execute the string as an expression:

>>> my_number = input('Please Enter a Number: \n')
Please Enter a Number: 
123 + 1
>>> print(my_number)
123 + 1
>>> eval(my_number)
124

'''
Finally, it’s worth noting, raw_input doesn’t natively exist in Python 3, but there are some 
tricky ways to force the interpreter to evaluate raw_input in backwards compatible ways. 
This can be useful for modernizing legacy Python code without rewriting large portions of it. 
Research on this topic is better left to the reader, as there are lots of fun (and sometimes scary) ways of doing this.
'''

'''

Summary
Python 2 and Python 3 handle input and raw_input differently.

In Python 2

input(x) is roughly the same as eval(raw_input(x))
raw_input() is preferred, unless the author wants to support evaluating string expressions.
eval() is used to evaluate string expressions.
Standard Library Docs:

https://docs.python.org/2/library/functions.html#input
https://docs.python.org/2/library/functions.html#raw_input
https://docs.python.org/2/library/functions.html#eval
In Python 3

Input handles string as a generic string. It does not evaluate the string as a string expression.
raw_input doesn’t exist, but with some tricky techniques, it can be supported.
eval() can be used the same as Python 2.
Standard Library Docs: 

https://docs.python.org/3/library/functions.html#input
https://docs.python.org/3/library/functions.html#eval



Q: Which command will print out the exit value of a script that just ran successfully?
A: echo $?
Echo will print out the exit value (question mark variable) of a script that just ran successfully.

Q: Which command will create a new environment variable?
A: export
This command will create a new environment variable, and give it a value.

Q: Which I/O stream are we using when we use the input function to accept user input in a Python script?
A: STDIN
STDIN is the standard I/O stream for input.

Q: What is the meaning of an exit code of 0?
A: The program ended successfully.
An exit value of 0 always indicates the program exited without error.

Q: Which statements are true about  input and raw_input in Python 2? (select all that apply)
A: input performs basic math operations -  In Python 2, input evaluates the user's input as an expression.
raw_input gets a string from the user.
'''

# Running System Commands in Python

import subprocess
subprocess.run(["date"])

'''
A system command that sends ICMP packets can be executed within a script by using which of the following?

subprocess.run
''''

# Obtaining the Output of a System Command

>>> result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
>>> print(result.returncode)
0
>>> print(result.stdout)
b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'' # b stands for array of bytes
>>> print(result.stdout.decode().split()) # This method applies an encoding to transform 
# the bytes into a string. By default, it uses a UTF-8 encoding which is what we want. So 
# with all that said, let's transform our array of bytes into a string and then split it into several pieces.
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

'''
So we just looked at the captured standard output. But what about standard error? 
If we use the capture output parameter and the command writes any output to 
standard error, it will be stored in the std or attribute of the completed process 
instance.
'''

>>> result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
>>> print(result.returncode)
1
>>> print(result.stdout)
b'' # empty
>>> print(result.stderr)

# Advanced Subprocess Management

import os
import subprocess

''''
So in this code, we start by calling the copy method of the OS environ dictionary 
that contains the current environment variables.
Calling 'copy' method of the os.environ dictionary will copy the current environment 
variables to store and prepare a new environment.
''''

my_env = os.environ.copy()

'''
This creates a new dictionary that we can change as needed without modifying 
the original environment. The change that we're doing in this script is adding 
one extra directory to the path variable.
'''

my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)

'''
If we're automating a one-off, well-defined task, we're developing a solution 
quickly is the biggest requirement, then using system commands and subprocesses can help a lot.
'''

'''
QUIZ:
Question 1
What type of object does a run function return?
A: CompletedProcess. This object includes information related to the execution of a command.

Question 2
How can you change the current working directory where a command will be executed?
A: Use the cwd parameter. This will change the current working directory where the command will be executed.

Question 3
When a child process is run using the subprocess module, which of the following are true? (check all that apply)
A: 
- The child process is run in a secondary environment. To run the external command, a secondary environment is created for the child subprocess, where the command is executed.
- The parent process is blocked while the child process finishes. While the parent process is waiting on the subprocess to finish, it’s blocked, meaning the parent can’t do any work until the child finishes.
- Control is returned to the parent process when the child process ends. After the external command completes its work, the child process exits, and the flow of control returns to the parent.

Question 4
When using the run command of the subprocess module, what parameter, when set to True, allows us to store the output of a system command?
A: capture_output. The capture_output parameter allows us to get and store the output of the system command we're using.

Question 5
What does the copy method of os.environ do?
A: Creates a new dictionary of environment variables. The copy method of os.environ makes a new copy of the dictionary containing the environment variables, making modification easier.
'''

# What are log files?
#!/usr/bin/env python3
import sys
import re

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)


import re
def show_time_of_pid(line):
  pattern = r"^([A-Z][a-z]+\s\d+\s\d+:\d+:\d+).*\[(\d+)\]"
  result = re.search(pattern, line)
  return "{} pid:{}".format(result[1], result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


# Making Sense out of the Data

usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print (usernames)