from flask import Flask, render_template, request, redirect, url_for, session
import db
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template("listIndex.html", tasks=db.getTasks())

@app.route('/task', methods=['POST','GET'])
def task():
    newtask=request.form.get['taskname']
    db.addTask(newtask)
    return render_template("insertTask_page.html", description=newtask,urgency=db.getUrgency(newtask))

@app.route('/delete', methods=['POST','GET'])
def delete():
    id=request.form.get('taskname')
    if id != None:
        db.deleteTask(id)
    return render_template("delete_page.html")

if __name__ == '__main__':
    app.run()
