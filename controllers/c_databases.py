from models import m_databases

def getDatabases (dataSesion):
    #print('desde c_databases')
    #print(dataSesion)
    dataBases = m_databases.getDatabases(dataSesion)
    return dataBases
def setDataSesion(dataSesion,nameDatabase):
    #print(dataSesion)
    m_databases.createDatabases(dataSesion,nameDatabase)


""" yo = m_databases.hola
print('hola  '+yo) """