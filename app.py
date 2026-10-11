from flask import Flask, render_template, request
import reviewer  

app = Flask(__name__)

#Home Page
@app.route("/", methods=["GET", "POST"])
def index():
    result_text = None

    if request.method == "POST":
        user_code = request.form.get("code_input", "")

        #sanity check
        if len(user_code.strip()) < 5:
            result_text = "Please paste some code first."
        else:
            #calling the reviewer logic
            result_text = reviewer.review_code(user_code)
    return render_template("index.html", result=result_text)

if __name__ == "__main__":
    app.run(debug=True)