from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Ryan Wojciechowski! I am adding my first code change.'


#@app.route('/hello')
#def hello():
 #   return render_template('hello.html')


@app.route('/about')
def hello():
    return render_template('about.html')


@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    print(f'You entered your favorite course as: {subject}{course_number}')

    return render_template('favorite-course.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')


@app.route('/base')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()

