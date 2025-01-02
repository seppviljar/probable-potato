import os
import json

def generate_menu():
    root_dir = './html-files'
    menu = {}

    for lang in ['es', 'pt']:
        lang_dir = os.path.join(root_dir, lang)
        menu[lang] = [
            file for file in os.listdir(lang_dir) if file.endswith('.html')
        ]

    with open('menu.json', 'w') as f:
        json.dump(menu, f, indent=4)

if __name__ == "__main__":
    generate_menu()