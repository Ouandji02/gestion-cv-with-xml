from flask import Flask, request
import xmltodict
import lxml.etree as ET
import json
import xmlschema
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.debug = True


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/')
def transform_xml():

    # récupérer le corps de la requête en tant que bytes
    request_data_bytes = request.get_data()

    # décoder le corps de la requête en tant que chaîne de caractères
    request_data_str = request_data_bytes.decode('utf-8')

    # renvoyer la sortie HTML sous forme de chaîne
    html_output = ET.tostring(transformXml("cv1.xml"), pretty_print=True)
    return html_output

@app.route('/api/upload/in_html', methods = ["POST"])
def upload_file():
    xml_file = request.get_data()

    if not xml_file:
        return 'Aucun fichier n\'a été envoyé dans la requête', 400

    with open('schema.xsd', 'r') as f:
            xsd_content = f.read()
            schema = xmlschema.XMLSchema(xsd_content)

    try:
        is_valid = schema.is_valid(xml_file)

        if is_valid :
            xml_dict = xmltodict.parse(xml_file)
            return json.dumps(xml_dict), 200
        else :
            print("Hello, ce n'est pas au bon format attendu")
        return "Le fichier est au bon format ", 200
    except Exception :
        return "Ce fichier n'est pas au bon format", 400

def transformXml(file_path):
    xml_data = ET.parse(file_path)
    xslt_data = ET.parse("xslt.xsl")
    transform = ET.XSLT(xslt_data)
    return transform(xml_data)

if __name__ == '__main__':
    app.run()