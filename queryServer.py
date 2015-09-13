from spyne import Application, srpc, ServiceBase, Array, Integer, Unicode, Iterable, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from flask import Flask
from flask.ext.spyne import Spyne



app = Flask(__name__)
spyne = Spyne(app)

@app.route("/")
def hello():
    return "Hello From Quickbooks!"


class SomeSoapService(spyne.Service):    
    __service_url_path__ = '/soap/someservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()
    
    @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def echo(str, cnt):
        for i in range(cnt):
            yield str
            

if __name__ == "__main__":
    app.run(port=5000,debug=True)
