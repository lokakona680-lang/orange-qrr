from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ORANGE QR DEMO</title>
<style>
body {
    background:#fff3e8;
    font-family:Arial;
    text-align:center;
    padding:40px 15px;
}
.card {
    background:white;
    padding:25px;
    border-radius:20px;
    max-width:380px;
    margin:auto;
}
h1 {color:#ff7900;}
input,button {
    width:100%;
    padding:14px;
    margin-top:15px;
    box-sizing:border-box;
    border-radius:10px;
}
input {border:1px solid #ddd;}
button {
    background:#ff7900;
    color:white;
    border:0;
}
.notice {font-size:13px;color:#666;}
</style>
</head>
<body>
<div class="card">
<h1>🍊 ORANGE QR DEMO</h1>
<p>مشروع تجريبي مستقل وغير تابع لـ Orange Maroc</p>
<form method="POST">
<input name="name" placeholder="أدخل اسمك" required>
<p class="notice">اسمك سيُستخدم داخل هذه التجربة فقط
ولن يتم تخزينه أو إرساله إلى جهة أخرى.</p>
<button type="submit">تجربة الصفحة</button>
</form>
<p>{{ message }}</p>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            message = "مرحبا " + name + "، التجربة نجحت!"
    return render_template_string(PAGE, message=message)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
