from flask import Flask

app = Flask(__name__)#reserved keywords 

@app.route("/")
@app.route("/home") #decorattors 
def hello_world():
    return "<h2>Home Page with decorator</h2>"

@app.route("/about")
def about_page():
    return "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Diam vel quam elementum pulvinar etiam non quam lacus. Lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci. Vitae congue eu consequat ac felis donec et odio. Feugiat nibh sed pulvinar proin gravida hendrerit lectus. Turpis tincidunt id aliquet risus feugiat in ante metus. Pharetra pharetra massa massa ultricies mi quis hendrerit. Tristique nulla aliquet enim tortor at. Sit amet nisl suscipit adipiscing bibendum est ultricies integer. Id faucibus nisl tincidunt eget. Malesuada nunc vel risus commodo. Porta nibh venenatis cras sed. Scelerisque eleifend donec pretium vulputate.</p>"

if __name__ == '__main__': #treats file as independent python program 
    app.run(debug=True)     