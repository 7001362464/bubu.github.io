from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def my_form():
    return render_template('new3.html');
@app.route('/',methods=['post'])
def my_form_post():
    text=requist.form['username'];
    processedtext=text.upper();
    return processedtext;
if __name__=="__main__":
    app.run();
