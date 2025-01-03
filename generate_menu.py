import os
import json

def generate_menu():
    root_dir = './html-files/zu-ZA'
    menu = {}

    menu = [
        file for file in os.listdir(root_dir) if file.endswith('.html') and file != "index.html"
    ]

    with open('menu.json', 'w') as f:
        json.dump(menu, f, indent=4)

if __name__ == "__main__":
    generate_menu()
