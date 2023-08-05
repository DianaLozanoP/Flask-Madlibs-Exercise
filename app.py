from flask import Flask, request, render_template
from stories import Story, story

app = Flask(__name__)


@app.route("/")
def form_1():
    return render_template("form1.html")


@app.route("/finalstory")
def give_story():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural_noun = request.args['plural_noun']
    final_story = story.generate(
        {"place": place, "noun": noun, "verb": verb, "adjective": adjective, "plural_noun": plural_noun})
    return render_template("finalstory.html", final_story=final_story)
