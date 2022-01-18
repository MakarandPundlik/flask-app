from flask import Flask,render_template,url_for

app = Flask(__name__)#reserved keywords 

'''
duplicate data, just to display the contents 
'''
posts = [
    #list of dictionaries
    {
        'author':'makarand',
        'title':'My fitst blog',
        'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ornare odio rhoncus turpis tincidunt sagittis. Sed eros dui, dapibus nec feugiat sit amet, viverra et leo. Integer hendrerit nibh id facilisis congue. Phasellus augue justo, iaculis at dictum non, egestas et nibh. Suspendisse potenti. Nullam iaculis vulputate ex, id laoreet ligula fermentum eget. Curabitur cursus id erat at tempor. Vestibulum viverra ac felis vulputate egestas. Cras maximus magna sit amet augue tincidunt lobortis.',
        'date':'10-10-2020'
    },
     {
        'author':'makarand',
        'title':'second flask blog',
        'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ornare odio rhoncus turpis tincidunt sagittis. Sed eros dui, dapibus nec feugiat sit amet, viverra et leo. Integer hendrerit nibh id facilisis congue. Phasellus augue justo, iaculis at dictum non, egestas et nibh. Suspendisse potenti. Nullam iaculis vulputate ex, id laoreet ligula fermentum eget. Curabitur cursus id erat at tempor. Vestibulum viverra ac felis vulputate egestas. Cras maximus magna sit amet augue tincidunt lobortis.',
        'date':'11-10-2020'
    },
     {
        'author':'makarand',
        'title':'third flask blog',
        'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ornare odio rhoncus turpis tincidunt sagittis. Sed eros dui, dapibus nec feugiat sit amet, viverra et leo. Integer hendrerit nibh id facilisis congue. Phasellus augue justo, iaculis at dictum non, egestas et nibh. Suspendisse potenti. Nullam iaculis vulputate ex, id laoreet ligula fermentum eget. Curabitur cursus id erat at tempor. Vestibulum viverra ac felis vulputate egestas. Cras maximus magna sit amet augue tincidunt lobortis.',
        'date':'12-10-2020'
    },
    ]

@app.route("/")
@app.route("/home") #decorattors 
def hello_world():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html',title="About Page")

if __name__ == '__main__': #treats file as independent python program 
    app.run(debug=True)     