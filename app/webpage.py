from flask import render_template,request,redirect, url_for
from app import app
from app.counter import LineCalculator

import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = APP_ROOT+'/static/uploads'
ALLOWED_EXTENSIONS = set(['java', 'c', 'cpp', 'js', 'ts', 'py'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/',methods=["GET","POST"])
def mainpage():
    if request.method=='POST':
        # handle the case if the post requests don't have the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # handle the case if user does not select file, browser also
        # submit an empty file without filename
        if file.filename == '':
            return redirect(request.url)
        # scan the code if file type in allowed file
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(app.config['UPLOAD_FOLDER']+'/'+filename)
            # file.stream.seek(0)
            c = LineCalculator()
            c.file_input(app.config['UPLOAD_FOLDER']+'/'+filename, filename)
            total_lines = c.total_lines
            print(total_lines)
            single_line = c.single_line
            multi_lines = c.multi_lines
            comment_lines = single_line + multi_lines
            block_line_comment = c.block_line_comment
            todo = c.todo
            #re-render the template
            return render_template("webpage.html", total_lines=total_lines, comment_lines=comment_lines,\
                                     single_line=single_line, multi_lines=multi_lines,\
                                     block_line_comment=block_line_comment, todo=todo)
    return render_template("webpage.html", total_lines=0, comment_lines=0, \
                           single_line=0, multi_lines=0, \
                           block_line_comment=0, todo=0)
