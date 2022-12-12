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
chmod +x src/buildapp.py
./app.py
````

</p>

</li>

</ol>

## Referenties
[Crop images with Opencv and Python](https://www.youtube.com/watch?v=r-pp7flMoQA)