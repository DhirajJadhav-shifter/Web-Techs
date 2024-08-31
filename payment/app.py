from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Define the form HTML as a template
form_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Form</title>
</head>
<body>
    <form action="/submit" method="POST">
        <label for="card_number">Card Number</label>
        <input type="text" id="card_number" name="card_number" placeholder="###-###-###" required><br>

        <label for="expiry_date">Expiry Date</label>
        <input type="text" id="expiry_date" name="expiry_date" placeholder="DD-MM-YY" required><br>

        <label for="cvv">CVV Number</label>
        <input type="text" id="cvv" name="cvv" placeholder="xxx" required><br>

        <label for="card_holder_name">Card Holder Name</label>
        <input type="text" id="card_holder_name" name="card_holder_name" placeholder="Enter your Name" required><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(form_template)

@app.route('/submit', methods=['POST'])
def submit():
    card_number = request.form['card_number']
    expiry_date = request.form['expiry_date']
    cvv = request.form['cvv']
    card_holder_name = request.form['card_holder_name']
    
    # Connect to SQLite database
    conn = sqlite3.connect('C:/Users/HP/OneDrive/Desktop/pp.html/payment/your_database.db')
    cursor = conn.cursor()
    
    # Insert data into the database
    cursor.execute('''
        INSERT INTO payments (card_number, expiry_date, cvv, card_holder_name)
        VALUES (?, ?, ?, ?)
    ''', (card_number, expiry_date, cvv, card_holder_name))
    
    conn.commit()
    conn.close()
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Submission Successful</title>
    </head>
    <body>
        <h1>Form data submitted successfully</h1>
        <a href="/">Go back to the form</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)



