# My script 

import sys



def about_me():
    print("\nMy name is Albert Quainoo")
    print("I am 20 years of age. I am 6 foot 1 in height")
    print("My hobbies include playing video games, listening to music, reading about things I find interesting, working out, and general tech stuff such as programming, troubleshooting, and random projects ")
    

def projects_list():
    print("\nNotAimLabs - An aim trainer based on the gridshot scenario built in Unity with C#")
    print ("Repo link - https://github.com/Albert-Quainoo/NotAimLabs")
    print("\nA simple pharmacy inventory management system written in C# with the WinForms framework")
    print("Repo link - No repo link since I forgot to make a remote repo and lost the entire codebase")
    print("\nInstalling MacOS on my gaming laptop through Opencore")
    print("Reddit post with the specifics - https://www.reddit.com/r/hackintosh/comments/18r4faq/sonoma_running_on_ryzen_9_5900hx_well_kind_of/")
    print("\nSignedIN - An interactive sign language learning web app for the Ghanaian Sign Language, built with Next (STILL IN DEVELOPMENT)")
    print("Link - https://signed-in-eb13d.web.app/")

def quit_program():
    sys.exit()


while True:
    print("Welcome to my program!")
    print("\n 1. About me")
    print("\n 2. My projects")
    print("\n 3. Quit")
    user_answer = input("\nPlease enter an option: ").strip()
    if user_answer in ['1', '2', '3']:
        break
    else:
        print("Invalid option, please try again")

if user_answer == '1':
    about_me()

elif user_answer == '2':
    projects_list()

elif user_answer == '3':
    quit_program()




