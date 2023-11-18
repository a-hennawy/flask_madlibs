import stories
from flask import Flask, request, render_template

story_ex = stories.story
# print(a.prompts)
app = Flask(__name__)


@app.route('/form')
def form():
    form_list = story_ex.prompts
    return render_template('form.html', prompts=form_list)


@app.route('/story')
def story():
    query_dict = {}
    for el in story_ex.prompts:
        query_dict[el] = request.args.get(el)
    story_madlib = story_ex.generate(query_dict)

    return render_template('story.html', story=story_madlib)
