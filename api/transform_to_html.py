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