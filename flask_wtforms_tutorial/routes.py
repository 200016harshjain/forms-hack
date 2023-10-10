"""Routing."""
from flask import current_app as app
from flask import redirect, render_template, url_for
from bs4 import BeautifulSoup
from .forms import ContactForm, SignupForm






@app.route("/", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    api_call = "dfhdh"
    
    if form.validate_on_submit():
        form.form_data.append(form.body.data.strip())
        print(form.form_data)
        print("length",len(form.form_data))
        if(len(form.form_data) >= 1) :
            #poc to change label based on gpt response
            print("in loop")
            api_call = "gpt response"
            form.body.label.text = api_call
        #this is for rerendering a form based on when we get api call from gpt3 and can use an updated label      
        return render_template(
        "contact.jinja2", form=form, template="form-template", title="Contact Form"
    )
    
    # this is for normal rendering - separate ideally as this is fucked up 
    return render_template(
        "contact.jinja2", form=form, template="form-template", title="Contact Form"
    )



@app.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    return render_template("success.jinja2", template="success-template")
