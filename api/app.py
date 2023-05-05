from flask import Flask, Response, request
import lxml.etree as ET
import io


app = Flask(__name__)

@app.route('/')
def transform_xml_to_HTML():

    # récupérer le corps de la requête en tant que bytes
    request_data_bytes = request.get_data()

    # décoder le corps de la requête en tant que chaîne de caractères
    request_data_str = request_data_bytes.decode('utf-8')

    print(request_data_str)

    # charger le fichier XML
    xml_data = ET.parse("cv1.xml")

    # charger le fichier XSLT
    xslt_data = ET.parse("xslt.xsl")
    transform = ET.XSLT(xslt_data)

    # transformer le fichier XML en HTML
    result = transform(xml_data)

    # renvoyer la sortie HTML sous forme de chaîne
    html_output = ET.tostring(result, pretty_print=True)
    return html_output

@app.route('/xml-to-odt')
def xml_to_odt():
    # Charger le fichier XML
    xml_file = ET.parse('cv1.xml')

    # Charger le fichier XSLT pour la transformation
    xslt_file = ET.parse('xslt.xsl')
    transform = ET.XSLT(xslt_file)

    # Appliquer la transformation et enregistrer le résultat dans un fichier ODT
    odt_file = transform(xml_file)
    odt_io = io.BytesIO()
    odt_file.write(odt_io)

    # Renvoyer le fichier ODT généré en tant que réponse Flask
    response = Response(odt_io.getvalue(), mimetype='application/vnd.oasis.opendocument.text')
    response.headers.set('Content-Disposition', 'attachment', filename='output.odt')
    return response


from flask import Flask, Response, request
import lxml.etree as ET
import io
import json


app = Flask(__name__)

@app.route('/json', methods=["POST"])
def transform_xml_to_HTML():

    # récupérer le corps de la requête en tant que bytes
    request_data_bytes = request.get_data()

    # décoder le corps de la requête en tant que chaîne de caractères
    request_data_str = request_data_bytes.decode('utf-8')

    # convertir la chaîne de caractères en un objet Python
    request_data_dict = json.loads(request_data_str)

    # charger le fichier XML
    # créer un élément racine pour l'arbre XML
    root = ET.Element('root')

    # itérer à travers les clés et les valeurs du dictionnaire Python et ajouter des éléments XML correspondants
    for key, value in request_data_dict.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    # créer une chaîne de caractères XML à partir de l'arbre XML
    xml_str = ET.tostring(root, encoding='unicode')
    
    # renvoyer une réponse XML à la requête
    return Response(xml_str, mimetype='text/xml')