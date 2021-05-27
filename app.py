from __future__ import print_function
from flask import Flask , render_template , request , redirect,url_for
from forms import Login,Details
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_cors import CORS

app= Flask (__name__)
CORS(app)

#SECRET KEY is what flask uses to protect web form against nasty attacks by hackers; protects app
app.config['SECRET_KEY'] = 'youshallnotpass12@3' #can be any key
# #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'   #tmp is the directory where test.db is stored

db=SQLAlchemy(app)
#
class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    imageUri = db.Column(db.Text)

class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime , default= datetime.datetime.now)
    inspector = db.Column(db.String(100))
    sku_no = db.Column(db.String(100))
#
    def __str__(self):
        return f'{self.id} , {self.title} , {self.imageUri}'

@app.route('/',methods = ['GET','POST'])
def login():
    login_form = Login()
    if login_form.validate_on_submit():
        #print(todo_form.content.data)
        return redirect('/details')
    return render_template('login.html' , form= login_form)

    # return{
    #     'name': 'wasssuppp'
    # }

@app.route('/details',methods = ['GET','POST'])
def details():
    details_form = Details()
    if details_form.validate_on_submit():
        #print(todo_form.content.data)
        details =Images(title=details_form.title.data, imageUri=details_form.imageUri.data)
        db.session.add(details)
        db.session.commit()
        return redirect('/success')
    return render_template('details.html', form=details_form)

@app.route('/success',methods=['GET','POST'])
def success():
    details = Images.query.all()
    return render_template('db.html',details=details)


if __name__ == "__main__":
    app.run(debug=True)

