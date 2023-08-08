from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/names')
def names():
    names = ["ben", "harry", "bob", "jay", "matt", "bill"]
    b_names =[]
    for name in names:
        for letter in name:
            if letter == "b":
                b_names.append(name)
                break
            
    return render_template('names.html', b_names=b_names)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')