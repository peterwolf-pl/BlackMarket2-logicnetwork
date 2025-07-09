import os
import textwrap

def read_and_wrap(filepath, max_length=1600):
    if not os.path.isfile(filepath):
        print(f"Błąd: Plik {filepath} nie istnieje.")
        return

    print(f"\n--- Zawartość pliku: {filepath} ---\n")

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    wrapped_lines = textwrap.wrap(content, width=max_length, replace_whitespace=False)

    for line in wrapped_lines:
        print(line)

if __name__ == '__main__':
    current_dir = os.getcwd()

    # Pobierz wszystkie pliki z wyjątkiem tych z rozszerzeniem .png
    all_files_except_png = [f for f in os.listdir(current_dir)
                            if os.path.isfile(f) and not f.lower().endswith('.png')]

    # Przetwarzaj każdy plik
    for file in all_files_except_png:
        read_and_wrap(file)
