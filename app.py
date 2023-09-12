import os
from flask import Flask, Response

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def get_text():
    print('get_text');
    return Response('ok')

@app.route('/xml', methods=['GET','POST'])
def get_xml():
    print('get_xml');
    xml_data = """<?xml version="1.0" encoding="UTF-8"?>
    <root>
        <element1>Hello</element1>
        <element2>World</element2>
    </root>
    """
    return Response(xml_data, content_type='text/xml')

@app.route('/soap', methods=['GET','POST'])
def get_soap():
    print('get_soap');
    xml_data = """<?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
              <ListaContratos xmlns="http://www.mega.com.br/">
                  <Usuario>integra.mega</Usuario>
                  <Senha>integra.mega</Senha>
                  <CpfCnpj>1</CpfCnpj>
              </ListaContratos>
          </soap:Body>
      </soap:Envelope>
    """
    return Response(xml_data, content_type='text/xml')

if __name__ == '__main__':
    # Use the environment variable 'PORT' if set, otherwise use 5001 as the default
    port = int(os.environ.get('PORT', 5005))
    app.run(debug=False, port=port, host="0.0.0.0")
