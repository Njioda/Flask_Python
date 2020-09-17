from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
string = ""
s_post_inv = ""
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    #string = ""
    if request.method == 'POST':
        string = request.form['string']
    s_post_inv = ''.join(reversed(string))

    
        
    return  render_template('update.html', s_post_inv=s_post_inv)

    #return render_template('updapte.html')

    
@app.route('/update', methods=['POST'])
def update():
    #string = ""
    if request.method == 'POST':
        valeur = request.form['string']
    #s_post_inv = ''.join(reversed(string))
    update_value = string.replace(s_post_inv, valeur)
    #update_value = dict.update([string])

    #return update_value

    return  render_template('home.html', update_value=update_value)

if __name__ == '__main__':
    app.run(port=16660, debug=True)
