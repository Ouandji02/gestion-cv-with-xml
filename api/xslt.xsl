<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <title>CV</title>
      </head>
      <body>
        <h1>Curriculum Vitae</h1>
        <h2>Informations personnelles</h2>
        <table>
          <tr>
            <td>Nom :</td>
            <td><xsl:value-of select="CV/InformationsPersonnelles/Nom"/></td>
          </tr>
          <tr>
            <td>Prénom :</td>
            <td><xsl:value-of select="CV/InformationsPersonnelles/Prenom"/></td>
          </tr>
          <tr>
            <td>Email :</td>
            <td><a href="mailto:{CV/InformationsPersonnelles/Email}">
              <xsl:value-of select="CV/InformationsPersonnelles/Email"/></a></td>
          </tr>
          <tr>
            <td>Téléphone :</td>
            <td><xsl:value-of select="CV/InformationsPersonnelles/Telephone"/></td>
          </tr>
        </table>
        
        <h2>Expériences professionnelles</h2>
        <xsl:for-each select="CV/ExperiencesProfessionnelles/Experience">
          <h3><xsl:value-of select="Poste"/> chez <xsl:value-of select="Entreprise"/></h3>
          <table>
            <tr>
              <td>Période :</td>
              <td><xsl:value-of select="DateDebut"/> - <xsl:value-of select="DateFin"/></td>
            </tr>
            
            <tr>
              <td>Description :</td>
              <td><xsl:value-of select="Description"/></td>
            </tr>
          </table>
        </xsl:for-each>
        
        <h2>Formations</h2>
        <xsl:for-each select="CV/Formations/Formation">
          <h3><xsl:value-of select="Diplome"/> à <xsl:value-of select="Etablissement"/></h3>
          <table>
           <tr>
              <td>Diplome :</td>
              <td><xsl:value-of select="Diplome"/></td>
            </tr>
           <tr>
              <td>Etablissement :</td>
              <td><xsl:value-of select="Etablissement"/></td>
            </tr>
            <tr>
              <td>Date d'obtention :</td>
              <td><xsl:value-of select="DateObtention"/></td>
            </tr>
          </table>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
  
</xsl:stylesheet>
