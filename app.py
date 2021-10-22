from flask import Flask,app,render_template,request,redirect
from flask.helpers import url_for

from controllers import c_databases
from controllers import form_db

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.get('/')
def home():
    
    
    form_data = form_db.form_label(request.form)
    dataBases = c_databases.getDatabases()
    
    #print(request.form.getlist('mostrar'))
    return render_template(
        'index.html', form = form_data, databases = dataBases, 
        mostrarDatos = 'hidden')


@app.post('/guardar')
def guardarData():    
    data= request.form
    print(data)
    if(data.getlist('mostrar')):
        form_data = form_db.form_label(request.form)
        for item in form_data:
            item.data=""
        
        dataBases = c_databases.getDatabases()
        
        return render_template(
        'index.html', form = form_data, databases = dataBases, 
        mostrarDatos = '!hidden',dataNew= data)
    else:
        return redirect('/')
        
    
""" print(c_databases.yo) """
app.run(debug=True)
