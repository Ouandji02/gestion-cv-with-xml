from flask import Flask, Response, request, make_response,send_file

import lxml.etree as ET
import io
import os
import json
import random
import string
import odf
from odf.opendocument import OpenDocumentText
from odf.text import P



app = Flask(__name__)
app.debug = True

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
    # Vérifie si un fichier a été envoyé dans la requête
    file = request.get_data()
    if not file:
        print()
        return 'Aucun fichier n\'a été envoyé dans la requête'

    
    # Chemin complet du dossier que vous voulez créer
    folder_path = os.path.join(app.root_path, "cvs")

    # Création du dossier s'il n'existe pas déjà
    os.makedirs(folder_path, exist_ok=True)

    try:
        # Valider le fichier XML par rapport au schéma XSD
        xsd_schema = ET.XMLSchema(ET.parse('schema.xsd'))  # Charger le fichier XSD
        xsd_schema.assertValid(ET.fromstring(file))
         # Créer le fichier dans le dossier courant
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        with open(folder_path+ "/" + filename + ".xml", 'w') as f:
            f.write(file.decode('utf-8'))
        return ET.tostring(transformXml(folder_path + "/" + filename + ".xml"), pretty_print=True)
    except Exception :
        return "Ce fichier ne correspond pas au schema defini", 400


@app.route('/api/upload/in_odt', methods = ["POST"])
def upload_fileODT():
    # Vérifie si un fichier a été envoyé dans la requête
    file = request.get_data()
    if not file:
        print()
        return 'Aucun fichier n\'a été envoyé dans la requête'

    
    # Chemin complet du dossier que vous voulez créer
    folder_path = os.path.join(app.root_path, "cvs")

    # Création du dossier s'il n'existe pas déjà
    os.makedirs(folder_path, exist_ok=True)

    try:
        # Valider le fichier XML par rapport au schéma XSD
        xsd_schema = ET.XMLSchema(ET.parse('schema.xsd'))  # Charger le fichier XSD
        xsd_schema.assertValid(ET.fromstring(file))
         # Créer le fichier dans le dossier courant
        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        with open(folder_path + "/" + filename + ".xml", 'w') as f:
            f.write(file.decode('utf-8'))
        doc = OpenDocumentText()
        para = P(text=file.decode('utf-8'))
        doc.text.addElement(para)
        # Appliquer la transformation et enregistrer le résultat dans un fichier ODT
        #odt_file = transformXml(folder_path + "/" + filename + ".xml")
        #odt_io = io.BytesIO()
        #odt_file.write(odt_io)

        #response = make_response(odt_io)
        # Définir les en-têtes pour le type de fichier ODT et le nom du fichier
        #response.headers['Content-Type'] = 'application/vnd.oasis.opendocument.text'
        #response.headers['Content-Disposition'] = 'attachment; filename=sample.odt'

        # Écriture du document ODT dans un fichier
        with open('document.odt', 'wb') as f:
            f.write(doc.saveToBytes())

           # Envoi du fichier ODT en tant que réponse
        return send_file('document.odt', attachment_filename='document.odt', as_attachment=True)
    except Exception :
        return Exception, 400


@app.route('/api/xml-to-odt')
def xml_to_odt():
    # Charger le fichier XML
    xml_file = ET.parse('cvs/thierry@gmail.com.xml')

    # Charger le fichier XSLT pour la transformation
    xslt_file = ET.parse('xslt.xsl')
    transform = ET.XSLT(xslt_file)

    # Appliquer la transformation et enregistrer le résultat dans un fichier ODT
    odt_file = transform(xml_file)
    odt_io = io.BytesIO()
    odt_file.write(odt_io)

    # Renvoyer le fichier ODT généré en tant que réponse Flask
    response = Response(odt_io.getvalue(), mimetype='application/vnd.oasis.opendocument.text')
    
    return response.headers.set('Content-Disposition', 'attachment', filename='output.odt')



@app.route('/api/json', methods=["POST"])
def transform_xml_to_HTML():

    # récupérer le corps de la requête en tant que bytes
    request_data_bytes = request.get_data()

    # décoder le corps de la requête en tant que chaîne de caractères
    request_data_str = request_data_bytes.decode('utf-8')

    # convertir la chaîne de caractères en un objet Python
    request_data_dict = json.loads(request_data_str)

    # charger le fichier XML
    # créer un élément racine pour l'arbre XML
    root = ET.Element('CV')

    # itérer à travers les clés et les valeurs du dictionnaire Python et ajouter des éléments XML correspondants
    for key, value in request_data_dict.items():
        element = ET.SubElement(root, key)
        if(key == "InformationsPersonnelles"):
            for key1, val in value.items():
                childElement = ET.SubElement(element,key1)
                childElement.text = str(val)

        if(key == "ExperiencesProfessionnelles"):
            for val in value:
                childElement = ET.SubElement(element,"Experience")
                for key2, val2 in val.items():
                  smallChildElement = ET.SubElement(childElement,key2)
                  smallChildElement.text = str(val2)

        if(key == "Formations"):
            for val in value:
                childElement = ET.SubElement(element,"Formation")
                for key2, val2 in val.items():
                  smallChildElement = ET.SubElement(childElement,key2)
                  smallChildElement.text = str(val2)

    # créer une chaîne de caractères XML à partir de l'arbre XML
    xml_str = ET.tostring(root, encoding='unicode')

     # Chemin complet du dossier que vous voulez créer
    folder_path = os.path.join(app.root_path, "cvs")

    # Création du dossier s'il n'existe pas déjà
    os.makedirs(folder_path, exist_ok=True)

    try:
        # Valider le fichier XML par rapport au schéma XSD
        xsd_schema = ET.XMLSchema(ET.parse('schema.xsd'))  # Charger le fichier XSD
        xsd_schema.assertValid(ET.fromstring(xml_str))
         # Créer le fichier dans le dossier courant
        with open(folder_path+ "/" +request_data_dict["InformationsPersonnelles"]["Email"]+".xml", 'w') as f:
            f.write(xml_str)
        return Response(xml_str, mimetype='text/xml') 
    except Exception :
        return "Ces informations ne respecte pas le format", 400

@app.route('/api/json/see', methods=["POST"])
def see_cv():

    # récupérer le corps de la requête en tant que bytes
    request_data_bytes = request.get_data()

    # décoder le corps de la requête en tant que chaîne de caractères
    request_data_str = request_data_bytes.decode('utf-8')

    # convertir la chaîne de caractères en un objet Python
    request_data_dict = json.loads(request_data_str)

    # charger le fichier XML
    # créer un élément racine pour l'arbre XML
    root = ET.Element('CV')

    # itérer à travers les clés et les valeurs du dictionnaire Python et ajouter des éléments XML correspondants
    for key, value in request_data_dict.items():
        element = ET.SubElement(root, key)
        if(key == "InformationsPersonnelles"):
            for key1, val in value.items():
                childElement = ET.SubElement(element,key1)
                childElement.text = str(val)

        if(key == "ExperiencesProfessionnelles"):
            for val in value:
                childElement = ET.SubElement(element,"Experience")
                for key2, val2 in val.items():
                  smallChildElement = ET.SubElement(childElement,key2)
                  smallChildElement.text = str(val2)

        if(key == "Formations"):
            for val in value:
                childElement = ET.SubElement(element,"Formation")
                for key2, val2 in val.items():
                  smallChildElement = ET.SubElement(childElement,key2)
                  smallChildElement.text = str(val2)

    # créer une chaîne de caractères XML à partir de l'arbre XML
    xml_str = ET.tostring(root, encoding='unicode')

     # Chemin complet du dossier que vous voulez créer
    folder_path = os.path.join(app.root_path, "cvs")

    # Création du dossier s'il n'existe pas déjà
    os.makedirs(folder_path, exist_ok=True)

    try:
        # Valider le fichier XML par rapport au schéma XSD
        xsd_schema = ET.XMLSchema(ET.parse('schema.xsd'))  # Charger le fichier XSD
        #xsd_schema.assertValid(ET.fromstring(xml_str))
         # Créer le fichier dans le dossier courant
        with open(folder_path+ "/" +request_data_dict["InformationsPersonnelles"]["Email"]+".xml", 'w') as f:
            f.write(xml_str)
        return ET.tostring(transformXml(folder_path+ "/" +request_data_dict["InformationsPersonnelles"]["Email"]+".xml"))
    except Exception :
        return "Ces informations ne respecte pas le format", 400



@app.route("/api/onecv")
def get_one_cv():
    
    cvs_dir = os.path.join(app.root_path, 'cvs')

    #Recuperation du chemin d'un cv
    file_path = os.path.join(cvs_dir, "thierry@gmail.com.xml")

    if os.path.isfile(file_path):

        # renvoyer la sortie HTML sous forme de chaîne
        html_output = ET.tostring(transform_xml(file_path), pretty_print=True)
        
        return html_output
    else:
        return "ce fichier n'existe pas"


@app.route("/api/cvs")
def get_cvs():

    cvs_dir = os.path.join(app.root_path, 'cvs')
    files = os.listdir(cvs_dir)
    response = []
    for value in files:
        cvs_dir = os.path.join(app.root_path, 'cvs')
        file_path = os.path.join(cvs_dir, value)
        response.append(transformXml(file_path))

    return files

@app.errorhandler(Exception)
def handle_exception(e):
    # log l'exception
    app.logger.error(str(e))

    # Retourne une réponse personnalisée à l'utilisateur
    return "Une erreur s'est produite"


def transformXml(file_path):
    xml_data = ET.parse(file_path)
    xslt_data = ET.parse("xslt.xsl")
    transform = ET.XSLT(xslt_data)
    return transform(xml_data)


if __name__ == '__main__':
    app.run()