from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# ------------------------
# Page routes
# ------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ministries")
def ministries():
    return render_template("ministries.html")

@app.route("/youth")
def youth():
    return render_template("youth.html")

@app.route("/sermons")
def sermons():
    return render_template("sermons.html")

@app.route("/sunday school")
def sundayschool():
    return render_template("sunday school.html")

@app.route("/kingdom men")
def kingdommen():
    return render_template("kingdom men.html")

@app.route("/youth ministry")
def youthministry():
    return render_template("youth ministry.html")

@app.route("/women ministry")
def womenministry():
    return render_template("women ministry.html")

@app.route("/worship team")
def worshipteam():
    return render_template("worship team.html")


# ------------------------
# Contact form route
# ------------------------
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Gmail credentials (use App Password)
        sender_email = "kimanimargaret46@gmail.com"
        receiver_email = "kimanimargaret46@gmail.com"
        app_password = "fikouqwfjeejmtlh"  # 16-char App Password

        # Compose email
        body = f"""
New Contact Form Submission:

Name: {name}
Email: {email}
Message: {message}
        """

        msg = MIMEText(body)
        msg["Subject"] = "New Message from Church Website"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Reply-To"] = email

        try:
            # Connect to Gmail SMTP server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.send_message(msg)
                print("Email sent successfully!")

            # Render professional confirmation page
            return render_template("contact_success.html", name=name)

        except Exception as e:
            print("Error sending email:", e)
            return f"Error sending email: {e}"

    # GET request → show the contact form
    return render_template("contact.html")


# ------------------------
# Run server
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
