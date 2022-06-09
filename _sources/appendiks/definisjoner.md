# B: Definisjoner

Denne siden er ikke ment for å bli lest fra topp til bunn, men inneholder en samling av definisjoner som jeg syntes var vanskelige å huske.

(intensiv-ekstensiv-storrelse)=

## Intensive og ekstensive størrelser

En instensiv størrelse er en egenskap som ikke avhenger av volumet til et system. En ekstensiv størrelse er det omvendte, en størrelse som avhenger av volumet til et system.

|    Intensiv     | Ekstensiv |
| :-------------: | :-------: |
|   masstetthet   |   masse   |
| ladningstetthet |  ladning  |

Vi ser her at den intensive størrelsen er den volumderiverte av den ekstensive. I statterm pleier vi å operere med andre sammenhenger enn bare dette.

|      Intensiv      | Ekstensiv | Variabel |
| :----------------: | :-------: | :------: |
|    masstetthet     |   masse   |  volum   |
|  ladningstetthet   |  ladning  |  volum   |
|       trykk        |  energi   |  volum   |
|        1/T         |  entropi  |  energi  |
| kjemisk potensiale |  energi   |  antall  |

(partition-function)=

## Partition function

Partisjonsfunksjonen er en funksjon som gir ut et heltall, nemlig antallet microstates systemet kan ha.

(linearisering)=

## Linearisering

Linearisering er en vanlig og generell teknikk for å utlede modeller.

Generelt sett innebærer det å taylorutvikle en funksjon $f(x,y)$ rundt en verdi som vi antar modellen alltid er nærme, td. $y\approx y_0$. Da får vi at

$$f(x,y) \approx f(x,y)\Big|_{y=y_0}+(y-y_0)\frac{\partial f}{\partial y}\Big|_{y=y_0}$$

(bragg-williams)=

## Bragg-Williams

Bragg-Williams tilnærmingen er å anta at alle molekylene er uniformt fordelt (ofte på en lattice). Dette gir ikke helt mening, fordi: Hvis vi har A-molekyler og B-molekyler, og AB-bindinger er mer gunstige enn BB-bindinger og AA-bindinger, så er det egentlig mer sannsynlig at B-molekylene er nært et A-molekyl enn et annet B-molekyl.

Bragg-Williams tilnærmingen blir også kalt mean-field approximation.

(exchange-parameter)=

## Utvekslingsparameteren

Utvekslingsparameteren $\chi_{AB}$ er definert som

$$
\chi_{AB} = \frac{z}{kT}(w_{AB}-\frac{w_{AA}+w_{BB}}{2})
$$

og sier noe om forskjellen i styrke mellom AB-bindinger og AA- og BB-bindinger. Den er sentral i det energidrevne bidraget til drivkraften bak blanding.

(lenker)=

## Lenker

Dette kompendiet baserer seg på lenker for å kjapt finne definisjonene til kompliserte konsepter som brukes mye. Da slipper vi å kludre til tekstene med masse bisetninger, og du slipper å google annethvert ord.
