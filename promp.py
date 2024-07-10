from flask import Flask, render_template, request
import os





app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':



        file=''
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'File uploaded successfully'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)