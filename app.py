from flask import Flask,app,render_template,request,redirect
from flask.helpers import url_for

from controllers import c_databases
from controllers import form_db

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.get('/')
def home():
    
    
    form_data = form_db.form_registro(request.form)
    
    
    #print(request.form.getlist('mostrar'))
    return render_template(
        'index.html', form = form_data,  
        mostrarDatos = 'hidden')


@app.post('/guardar')
def guardarData(): 
    form_data = form_db.form_registro(request.form)
    data= request.form
    #print(data)
    sesion={
            'host':form_data.hotst.data,
            'user':form_data.user.data,
            'password':form_data.passw.data,
            'port':form_data.puerto.data
        }
    if(data.getlist('mostrar')):
        #si esta en on, creo sesion y musetro div hidden
        #c_databases.setDataSesion(form_data)
        
        dataBases = c_databases.getDatabases(sesion)
        
        form_data = limpiar(form_data)
        
        #request.from.get('hotst)
        return render_template(
        'index.html', form = form_data, databases = dataBases, 
        mostrarDatos = '!hidden')
    else:
        #creo conexion y base de datos
        nameDatabase=form_data.baDtos.data
        print('nombre de la base'+ nameDatabase)
        c_databases.setDataSesion(sesion,nameDatabase)
        
        return redirect('/')
    
def limpiar(form_data):
    for item in form_data:
        item.data=""
    return form_data
              
    
""" print(c_databases.yo) """
app.run(debug=True)
