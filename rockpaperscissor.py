from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Rock Paper Scissors</title>
    <style>
        body{
            font-family:Arial,sans-serif;
            background:linear-gradient(to right,#667eea,#764ba2);
            color:white;
            text-align:center;
            margin-top:60px;
        }

        .container{
            width:450px;
            margin:auto;
            background:white;
            color:black;
            padding:30px;
            border-radius:15px;
            box-shadow:0 0 15px gray;
        }

        h1{
            color:#4b0082;
        }

        button{
            padding:12px 20px;
            margin:10px;
            font-size:18px;
            border:none;
            border-radius:10px;
            cursor:pointer;
            background:#4CAF50;
            color:white;
        }

        button:hover{
            background:#45a049;
        }

        h2{
            color:#d35400;
        }
    </style>
</head>
<body>

<div class="container">

<h1>✊ Rock Paper Scissors ✋</h1>

<form method="POST">

<button name="choice" value="rock">🪨 Rock</button>

<button name="choice" value="paper">📄 Paper</button>

<button name="choice" value="scissors">✂️ Scissors</button>

</form>

{% if user %}

<hr>

<h2>Your Choice: {{ user }}</h2>

<h2>Computer Choice: {{ computer }}</h2>

<h2>{{ result }}</h2>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    user = None
    computer = None
    result = None

    if request.method == "POST":

        user = request.form["choice"]
        computer = random.choice(choices)

        if user == computer:
            result = "🤝 It's a Tie!"

        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            result = "🎉 You Win!"

        else:
            result = "💻 Computer Wins!"

    return render_template_string(
        html,
        user=user,
        computer=computer,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
