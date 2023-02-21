from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.email_model import Email

@app.route("/")
def index():
    return render_template("email.html")


# form submission route
@app.route("/add_email", methods=["POST"])
def add_email():
    print("adding email")
    print("check valid here")

    if not Email.validate_email(request.form):
        return redirect("/")

    Email.create(request.form)
    return redirect("/success")


# results route
@app.route("/success")
def show_emails():
    emails = Email.get_all()
    return render_template("results.html", emails = emails)


# route to delete an email
@app.route("/delete/<int:email_id>")
def delete(email_id):

    Email.delete({"id":email_id})

    return redirect("/success")