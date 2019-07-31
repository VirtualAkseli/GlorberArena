from flask import Flask, render_template
app = Flask(__name__)
  
posts = ["Tämä on varsin harmillista", "Sienestämisen underground-skene", "Kallioluolan mysteeri; kirkko vai katakombi?"]


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/index")
def content():
	return render_template("posts.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
