import random

linux_commands = {"TOP": "Table of processes",
              "SSH": "Secure Shell",
              "Touch": "Create new file",
              "MKDIR": "Make directory",
              "Grep": "Global regular expression print",
              "CHMOD": "Modify permissions",
              "APT": "Package Manager",
              "CAT": "Concatenate",
              "PS": "Processes",
              "PING": "Test network connectivity",
              "VIM": "Terminal text editor",
              "WHICH": "Outputs path of shell commands",
              "WHOAMI": "Displays username currently in use",
              "WC": "Word Count",
              "WGET": "Retrieve file from internet",
              "IFCONFIG": "Display network interfaces and IP's",
              "DU": "Show disk usages information",
              "SYSTEMCTL": "Use to manage service",
              "SED": "Search, replace or delete file patterns",
              "AWK": "Find and manipulate patterns in a file",
              "CURL": "Transmits data between servers using URL's",

            }

terms, definitions = random.choice(list(linux_commands.items()))

game_start = input("Welcome to the random tech term generator game. Press enter to continue\n")
print("Define this term:\n",terms) 
done_prompt = input("Press enter when you are done defining the term\n")

check_term = input("Let's check your answer. Type in the term.\n")

print(definitions)