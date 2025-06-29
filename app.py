from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
<!DOCTYPE html>
<html>
  <head>
    <title>Toggle Theme</title>
    <style>
      body {
        background-color: black;
        color: white;
        transition: background-color 0.5s, color 0.5s;
      }
      .switch {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
      }
    </style>
  </head>
  <body>
    <label class="switch">
      <input type="checkbox" id="themeSwitch">
      <span>Toggle</span>
    </label>

    <script>
      const checkbox = document.getElementById('themeSwitch');
      checkbox.addEventListener('change', () => {
        if (checkbox.checked) {
          document.body.style.backgroundColor = "white";
          document.body.style.color = "black";
        } else {
          document.body.style.backgroundColor = "black";
          document.body.style.color = "white";
        }
      });
    </script>
  </body>
</html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
