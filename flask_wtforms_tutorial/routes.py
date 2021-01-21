from flask import current_app as app
from flask import redirect, render_template, url_for

from .forms import ContactForm, SignupForm


@app.route("/")
def home():
    return render_template("index.jinja2", template="home-template")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form, typically used to send emails."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """User sign-up form for account creation."""
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "signup.jinja2",
        form=form,
        template="form-template"
    )


@app.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page displayed when users submit a valid forms."""
    return render_template(
        "success.jinja2",
        template="success-template"
    )
