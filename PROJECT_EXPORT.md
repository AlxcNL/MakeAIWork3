# Export van project

<ol>

<li>

Paden aanpassen

chmod +x convert_path.py && ./convert_path.py "relative\path\to\model"

<ul>

<li>In VsCode selecteer je het bestand met de rechtermuisknop en kies je 'Copy Relative Path'</li>
<li>Pas het pad aan als het om een sub-directory of juist hoger gelegen directory gaat</li>
<li>Test de start-scripts vanuit een (git bash) terminal</li>

</ul>

</li>
<br>

<li>
Pycache verwijderen

```bash
rm -r {project_directory}/__pycache__
```
</li>

<li> 
Map p3 aanmaken en daarin alle code en data kopieren

```bash
mkdir p3 && cp -r {project_directory} p3/
```

Map p3 toevoegen en committen met git

```bash
git add p3 && git commit -m "Deliverable Periode 2"
```

</li>

<li>

Git export van p3 maken

```bash
git archive -o "../{voornaam}_{achternaam}.zip" HEAD:p3
```

</li>

<li>

Testen en uploaden

<ol>

<li>p3.zip op een adere locatie uitpakken en testen</li>

<li>p3.zip uploaden naar eigen Teams kanaal -> Deliverables periode 2

</li>

</ol>
