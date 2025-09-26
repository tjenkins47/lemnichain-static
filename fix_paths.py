import os

# Root folder for your static site
ROOT = r"D:\Consulting\Clients\Ralph Vince\Web Page\LemniChainStatic"

# Replacements: (old, new)
REPLACEMENTS = [
    ("/static/css/", "/css/"),
    ("/static/js/", "/js/"),
    ("/static/graphics/", "/graphics/"),
    ("/static/pdfs/", "/pdfs/"),
    ('{% include "navbar.html" %}', """
<div id="navbar-placeholder"></div>
<script>
fetch("/html/navbar.html")
  .then(r => r.text())
  .then(html => document.getElementById("navbar-placeholder").innerHTML = html);
</script>
"""),
]

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    for old, new in REPLACEMENTS:
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {path}")

def main():
    for root, _, files in os.walk(ROOT):
        for file in files:
            if file.endswith(".html"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
