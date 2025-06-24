from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница
@app.route("/")
def home():
    return render_template("index.html")

# Симптомы и лечение
@app.route("/symptoms")
def symptoms():
    return render_template("symptoms.html")

# Калькулятор ИМТ
@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    bmi = None
    category = ""
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"]) / 100  # переводим в метры
        bmi = round(weight / (height ** 2), 1)
        if bmi < 18.5:
            category = "Недостаточный вес"
        elif 18.5 <= bmi < 25:
            category = "Норма"
        else:
            category = "Избыточный вес"
    return render_template("bmi.html", bmi=bmi, category=category)

# Контакты
@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)