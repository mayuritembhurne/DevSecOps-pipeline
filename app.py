import subprocess

user_input = input("Enter text: ")

command = ["echo", user_input]

subprocess.run(command)
