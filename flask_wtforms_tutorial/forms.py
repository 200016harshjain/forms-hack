"""Form object declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length


class ContactForm(FlaskForm):
    """Contact form."""

 
    form_data = []
    form_label = "Please describe any issues you have with your workspace."
    body = TextAreaField(
       form_label, [DataRequired(), Length(min=4, message="Your message is too short.")]
    )
    submit = SubmitField("Submit")


class SignupForm(FlaskForm):
    """Sign up for a user account."""

    email = StringField(
        "Email", [Email(message="Not a valid email address."), DataRequired()]
    )
    password = PasswordField(
        "Password",
        [DataRequired(message="Please enter a password.")],
    )
    confirmPassword = PasswordField(
        "Repeat Password", [EqualTo(password, message="Passwords must match.")]
    )
    title = SelectField(
        "Title",
        [DataRequired()],
        choices=[
            ("Farmer", "farmer"),
            ("Corrupt Politician", "politician"),
            ("No-nonsense City Cop", "cop"),
            ("Professional Rocket League Player", "rocket"),
            ("Lonely Guy At A Diner", "lonely"),
            ("Pokemon Trainer", "pokemon"),
        ],
    )
    website = StringField("Website", validators=[URL()])
    birthday = DateField("Your Birthday")
    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")

