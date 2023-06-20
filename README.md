# Learnings
[Microsoft Power BI Lab URL] { https://learn.microsoft.com/en-us/training/modules/design-model-power-bi/8-lab }

[Poe Chat GPT] { https://poe.com/ChatGPT/ }

[ ML Tutorial Project ] { https://www.youtube.com/watch?v=yY1FXX_GSco/ }

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="{{ url_for ('static',filename='css/style.css') }}">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <title>Home</title>
</head>
<body class="bg-nav">

    <nav class="navbar">
        <a class="navbar-brand text-light">Predictor</a>
    </nav>

    <div class="container">
        <div class="row">
            <div class="offset-4 col-md-4">
                <div class="card mt-100">
                    <div class="card-body">
                        <h3 class="text-md-center">Enter the details</h3><br>

                        <form class="form" action="/predict" method="POST">
                            <label>Enter Age</label><br>
                            <input type="number" name="age" class="form-control"><br>
                            <label>Enter Salary</label><br>
                            <input type="number" name="salary" class="form-control"><br><br>
                            <input type="submit" value="Predict" class="btn btn-block bg-nav btn-lg text-light">
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1c1HTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

</body>
</html>
----------------------
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('dummy.html')

if __name__=='__main__':
    app.run(debug=True)

