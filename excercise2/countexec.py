
import os

def count_scripts(directory):
    script_counts = {}
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            with open(path, encoding="latin-1") as f:
                first_line = f.readline().strip()
                if first_line.startswith("#!"):
                    interpreter = first_line[2:]
                    script_counts[interpreter] = script_counts.get(interpreter, 0) + 1
    return script_counts

if __name__ == "__main__":
    directory = input("Enter directory path: ")
    script_counts = count_scripts(directory)
    for interpreter, count in sorted(script_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{count} {interpreter}")
