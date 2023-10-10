"""Routing."""
from flask import current_app as app
from flask import redirect, render_template, url_for
from bs4 import BeautifulSoup
from .forms import ContactForm, SignupForm





@app.route("/", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    
    
    if form.validate_on_submit():
        form.form_data.append(form.body.data.strip())
        print(form.form_data)
        print("length",len(form.form_data))
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2", form=form, template="form-template", title="Contact Form"
    )



@app.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    return render_template("success.jinja2", template="success-template")
