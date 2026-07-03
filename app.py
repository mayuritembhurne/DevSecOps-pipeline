import subprocess

user_input = input("Enter text: ")

subprocess.run(
    ["echo", user_input],
    check=True,
    shell=False
)
