from flask import Flask, request
from flask_cors import CORS
import psycopg2

# Flask Config
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins': "*"}})

# Banco de dados Config
host = "localhost"
port = "5432"
dbname = "TesteW"
user = "postgres"
password = "idk"

conn_string = "host={0} port={1} user={2} password={3} dbname={4}".format(host, port, user, password, dbname)
conn = psycopg2.connect(conn_string)

class Empresa:
    def __init__(self, name, doc, about, active, site):
        self.name = name
        self.doc = doc
        self.about = about
        self.active = active,
        self.site = site
        
class Cliente:
    def __init__(self, name, doc, about, active, site):
        self.name = name
        self.doc = doc
        self.about = about
        self.active = active,
        self.site = site
        
class Oferta:
    def __init__(self, customer_id, from_, to_, initial_value, amount, amount_type):
        self.customer_id = customer_id
        self.from_ = from_
        self.to_ = to_ 
        self.initial_value = initial_value
        self.amount = amount
        self.amount_type = amount_type
        
class Lance:
    def __init__(self, cliente_id, oferta_id, value, amount):
        self.cliente_id = cliente_id
        self.oferta_id = oferta_id
        self.value = value
        self.amount = amount
        
        
# Routes
@app.route('/')
def index():
    return "Hello World"

#Rotas Empresa
@app.route('/empresa/new', methods=['POST'])
def addEmpresa():
    data = request.json
    
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO empresas(name, doc, about, active, site) VALUES('{0}', '{1}', '{2}', {3}, '{4}');""".format( data["name"], data["doc"], data["about"], data["active"], data["site"],))
    conn.commit()
    cursor.close()
    
    return "Ok"

@app.route('/empresa/getAll', methods=['GET'])
def getAllEmpresas():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empresas")
    return cursor.fetchall()
    
#Rotas Cliente
@app.route('/cliente/new', methods=['POST'])
def addCliente():
    data = request.json
    
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO clientes(name, doc, about, active, site) VALUES('{0}', '{1}', '{2}', {3}, '{4}');""".format( data["name"], data["doc"], data["about"], data["active"], data["site"],))
    conn.commit()
    cursor.close()
    
    return "Ok"

@app.route('/cliente/getAll', methods=['GET'])
def getAllClientes():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()


#Rotas Oferta
@app.route('/oferta/new', methods=['POST'])
def addOferta():
    data = request.json
    
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO oferta (customer_id, "from", "to", initial_value, amount, amount_type) VALUES('{0}', '{1}', '{2}', {3}, '{4}', '{5}');""".format( data["id_customer"], data["from"], data["to"], data["initial_value"], data["amount"], data["amount_type"]))
    conn.commit()
    cursor.close()
    
    return "Ok"

@app.route('/oferta/getAllByEmpresa/<empresa_id>', methods=['GET'])
def getAllOfertaByEmpresa(empresa_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM oferta WHERE customer_id = {0}".format(empresa_id))
    return cursor.fetchall()
    

@app.route('/oferta/getAll', methods=['GET'])
def GetOferta():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM oferta")
    return cursor.fetchall()


#Rotas Lances
@app.route('/lance/new', methods=['POST'])
def addLance():
    data = request.json
    
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO lance (cliente_id, oferta_id,value,amount) VALUES('{0}', '{1}', '{2}', {3});""".format( data["id_provider"], data["id_offer"], data["value"], data["amount"]))
    conn.commit()
    cursor.close()
    
    return "Ok"

@app.route("/lance/getAllByOferta/<oferta_id>")
def getAllLancesByOferta(oferta_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lance WHERE oferta_id = {0}".format(oferta_id))
    return cursor.fetchall()

@app.route("/lance/getAllByCliente/<cliente_id>")
def getAllLancesByCliente(cliente_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lance WHERE cliente_id = {0}".format(cliente_id))
    return cursor.fetchall()



if __name__ == "__main__":
    app.run(debug=True)