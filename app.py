from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

@app.route('/')  # route for redirecting to the home page
def home():
    return render_template('abc.html')

@app.route('/searchImages', methods=['GET','POST'])
def searchImages():

    if request.method == 'POST':
      try:
        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbConn['Data']
        table = db['Applicants']

        print("entered post")
        fname = request.form['fname']
        email = request.form['email']
        phone = request.form['phone']
        ws = request.form['ws']
        gender = request.form['gender']
        married = request.form['marital status']
        ln = request.form['ln']
        nl = request.form['nl']
        skn = request.form['skn']
        level1 = request.form['level1']
        skn2 = request.form['skn2']
        level2 = request.form['level2']
        wh = request.form['wh']
        edu = request.form['edu']
        p1 = request.form['p1']
        l1 = request.form['l1']
        p2 = request.form['p2']
        l2 = request.form['l2']
        yoe = request.form['yoe']
        jt = request.form['jt']
        drone = request.form['drone']
        exp = request.form['exp']
        city = request.form['city']
        tow = request.form['tow']
        mydict = {'Full name': fname,
                  ' Email id': email,
                  ' Phone No.': phone,
                  'Whatsapp No.': ws,
                  'Gender': gender,
                  'Marital status': married,
                  'Languages Known': ln,
                  'Native Language': nl,
                  'Skill-1': skn,
                  'Level-1': level1,
                  'Skill-2': skn2,
                  'Level-2': level2,
                  'Work History': wh,
                  'Education': edu,
                  'Platfrom 1': p1,
                  'Link 1': l1,
                  'Platfrom 2': p2,
                  'Link 2': l2,
                  'Year of exp.': yoe,
                  'jt':jt,
                  'drone': drone,
                  'exp': exp,
                  'city': city,
                  'tow': tow
                  }
        x = table.insert(mydict)
        return render_template('.html')
      except:
          return 'Something went Wrong'
    else:
        return render_template('abc.html')

if __name__ == "__main__":
    app.run(debug = True)
