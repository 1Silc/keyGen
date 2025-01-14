from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_key', methods=['POST'])
def generate_key():
    if request.method == 'POST':
        # Your key generation logic here (similar to your previous code)
        with open("list.txt", "r") as key_file:
            lines = key_file.readlines()
            random_line = random.choice(lines).strip()
        return render_template('key.html', key=random_line)
    else:
        return redirect(url_for('index')) 

if __name__ == "__main__":
    app.run(debug=True)
