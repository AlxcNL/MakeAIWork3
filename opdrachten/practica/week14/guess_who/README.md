MIW3 Practicum
==============================
In dit practicum worden vaardigheden getraind die aansluiten bij de college's van MIW3.

## Voorbereiding

```bash
chmod +x ./install_requirements.sh
./install_requirements.sh
```

## Exercises

<ol>

<li>

### ImageCropper

#### Leerdoelen
<ul>
<li>OOP: operaties uitvoeren door het aanroepen van een class method vanuit een centrale main functie</li>
<li>ETL: informatie verkrijgen uit gegeven data</li>
</ul>

#### Gegeven

<ul>

<li>

**Images in <i>data/pics</i>**  
- <i>guess_who.jpg</i> matrix van alle personen
- <i>uitgeknipte images: alex.jpg, alfred.jpg en tom.jpg</i>
</li><br>

<li>

**Scripts in <i>src/build</i>** 
- <i>image_cropper.py</i>; Python class voor het <i>croppen</i> van images
- <i>app.py</i>; deze bevat de <u>main functie</u> waarmee alle <u>build</u> acties worden uitgevoerd
</li>

</ul>

#### Gevraagd

<p>Vul de methode <u>extractPortraits(imageCropper)</u> in app.py aan zodat voor elke persoon een portretfoto wordt uitgeknipt en opgeslagen. Gebruik daarbij gebruik van een loop en/of list comprehension.

De operaties van ImageCropper worden aangestuurd vanuit <u>main() in app.py</u> 

```bash
cd src/build
chmod +x src/build/app.py
./app.py
```

</p>

<li> 

### MongoAdapter

#### Leerdoelen
<ul>
<li>OOP: operaties uitvoeren door het aanroepen van een class method vanuit een centrale main functie</li>
<li>ETL: informatie verkrijgen uit gegeven data</li>
<li>NoSQL: indexeren in een MongoDB</li>
</ul>

### Requirements
<ul>
<li>Docker Desktop</li>
<li>MongoDB Compass</li>
</ul>

#### Gegeven

<ul>

<li>

**Start script in <i>sh</i>**  
- <i>start_mongo.sh</i>
</li><br>

<li>

**Scripts in <i>src/build</i>** 
- <i>nosql_adapter.py</i>; Python class met <i>adapter</i>
- <i>app.py</i>; deze bevat de <u>main functie</u> waarmee alle <u>build</u> acties worden uitgevoerd
    en de <strong>dictionary properties</strong></i>
</li>

</ul>

</li>

#### Gevraagd

<ol>

<li>

**Start MongoDB**

De MongoDB runt in een Docker container.
Open een extra Terminal / Git Bash en run

```bash
cd opdrachten/practica/week14/guess_who
chmod +x docker/compose/up.sh
chmod +x sh/start_mongo.sh
sh/start_mongo.sh
```

</li>

<li>

**Installeer PyMongo**

```bash
pip install pymongo
```

</li>

<li>

**Start Compass**

<ul>
<li>Start Compass en kies new connection. </li>
<li>Kies <i>Advanced Connection Options</i> -> <i>Authentication</i> -> <i>Username/Password</i></li>
<li>Klik op <i>Connect</i>.
Gebruik de gevens uit <i>src/build/nosql_adapter.py</i>
</li>
</ul>

</li>

<li>

**Maak een nieuwe database en collection**

<p>
In Compass, klik op de plus naast Database en vul het volgende in:
<ul>
<li>Database Name: guess_who</li>
<li>Collection Name: persons</li>
</ul>

</p>

</li>

<li>

**Maak een functie in app.py**

Maak een functie in app.py voor het indexeren van alle <u>persons</u> en hun <u>properties</u> m.b.v. de MongoAdapter.

</li>

<li>

**Test de indexering**

```bash
cd src/build
chmod +x src/build/app.py
./app.py
```

</li>

</ol>

</li>

</ol>

## Referenties
[Crop images with Opencv and Python](https://www.youtube.com/watch?v=r-pp7flMoQA)