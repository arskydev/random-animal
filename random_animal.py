import random
from socket import gethostname
import http.server
import socketserver

PORT = 8080
animal_name = [
    "Simba", "Mufasa", "Emil", "Jerry", "Tom", "Splinter", "Leonardo", "Michelangelo", "Donatello", "Raphael", "Shere Khan", "Balu", "Bagira"
]
animal_type = [
    "🦁", "🦊", "🐶", "🐱", "🐯", "🦄", "🐮", "🐹", "🐭", "🐰", "🐻", "🐨", "🐼", "🦥", "🦉", "🐸", "🐙", "🦖", "🐻‍❄️", "🐋"
]
colors = [
    "#FF6347", "#00FFFF", "#8A2BE2", "#5F9EA0", "#6495ED", "#B8860B", "#006400", "#8B0000", "#B22222", "#B22222", "#F08080"
]

def replace_line(filename: str, text_to_find: str, text_to_paste: str):

    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            if line.strip() == text_to_find:
                i = lines.index(line)
                line = (" " * i * 2 ) + text_to_paste + '\n'
            f.write(line)

random_animal_name = random.choice(animal_name)
random_animal_type = random.choice(animal_type)
random_color = random.choice(colors)
hostname = gethostname()

replace_line("index.html", "ANIMAL_NAME", random_animal_name)
replace_line("index.html", "ANIMAL_TYPE", random_animal_type)
replace_line("index.html", "HOSTNAME", hostname)
replace_line("style.css", "background-color: COLOR;", (" "* 4) + f"background-color: {random_color};")


Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
