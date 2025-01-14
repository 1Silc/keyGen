import random

def GenerateKey(filename):
    """
    Generates a key by reading a random line from a specified file.

    Args:
        filename: The path to the file containing the list of keys.

    Returns:
        The randomly selected key.
    """
    with open(filename, "r") as key_file:
        lines = key_file.readlines()
        random_line = random.choice(lines).strip()
        return random_line

def write_key_to_html(key, output_filename="key.html"):
    """
    Writes the generated key to an HTML file.

    Args:
        key: The key to be written to the HTML file.
        output_filename: The name of the output HTML file.
    """
    with open(output_filename, "w") as html_file:
        html_file.write(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Generated Key</title>
</head>
<body>
    <h1>Generated Key:</h1>
    <p>{key}</p>
</body>
</html>
""")

if __name__ == "__main__":
    key_file = "list.txt"  # Replace with the actual path to your file
    generated_key = GenerateKey(key_file)
    write_key_to_html(generated_key)
