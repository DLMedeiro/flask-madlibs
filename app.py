from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def load_form():
    blank_inputs = story.prompts
    return render_template('form.html', inputs = blank_inputs)


@app.route('/story')
def load_story():
    text = story.generate(request.args)
    # request.args vs request.args.get('x')
    # multiple values returned vs single value?
    return render_template('story.html', text = text)