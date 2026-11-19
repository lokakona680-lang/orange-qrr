from flask import Flask, request, render_template_string

app = Flask(__name__)
names = []

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orange QR Demo</title>
<style>
body {
  background:#fff4eb;
  font-family:Arial;
  text-align:center;
  padding:35px 15px;
}
.card {
  background:white;
  padding:25px;
  border-radius:20px;
  max-width:360px;
  margin:auto;
}
h1 {color:#ff7900;}
input,button {
  width:100%;
  padding:14px;
  margin-top:12px;
  box-sizing:border-box;
  border-radius:10px;
}
input {border:1px solid #ddd;}
button {
  background:#ff7900;
  color:white;
  border:0;
  font-weight:bold;
}
</style>
</head>
<body>
<div class="card">
<h1>🍊 ORANGE QR</h1>
<p>صفحة تجريبية غير رسمية</p>
<p>أدخل اسمك للمشاركة في التجربة:</p>
<form method="POST">
<input name="name" placeholder="الاسم" required maxlength="60">
<p><label>
<input type="checkbox" name="consent" required>
أوافق على إرسال اسمي إلى صاحب التجربة.
</label></p>
<button type="submit">إرسال</button>
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
        consent = request.form.get("consent")

        if name and consent:
            names.append(name)
            message = "تم إرسال الاسم بنجاح!"
    return render_template_string(HTML, message=message)

@app.route("/admin")
def admin():
    return "<h1>الأسماء التجريبية</h1>" + "".join(
        f"<p>{name}</p>" for name in names
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
