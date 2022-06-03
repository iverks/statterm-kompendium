# A: Sammendrag

## 1: Sannsynlighet

Kombinatorikk og sannsynlighetsfordelinger finnes. En ting som særlig finnes, er muligheten for å telle multiplisiteter. Tilstander med høyere multiplisitet krever mer informasjon for å beskrives i sin helhet. Tilstander med høyere multiplisitet er mer sannsynlige enn tilstander med lavere multiplisitet.

| Høyere multiplisitet               | Lavere multiplisitet                |
| :--------------------------------- | :---------------------------------- |
| En 4x4 grid med to partikler       | En 4x4 grid med 4 partikler         |
| Etter tre terningkast; total sum 9 | Etter tre terningkast; total sum 18 |

## 2: Ekstremalverdiprinsipper og likevekt

Termodynamiske systemer har frihetsgrader - variable som systemet selv "stiller inn på" som respons på initial- og randbetingelsene (som kan være satt utenfra). Frihetsgradene til et system vil endre seg helt til netto krefter i systemet er 0. Dette er ekvivalent med at systemet vil gå mot en tilstand der den har minimal (fri) energi, maksimal multiplisitet eller en kombinasjon av de to. Prinsippet om maksimal multiplisitet forklarer gasstrykk, blanding av væsker, at gummi trekker eg sammen, og at varme strømmer fra varme til kalde delsystemer.

## 3: Varme, energi og arbeid

Termodynamikkens første lov sier at varme er en form for energiutveksling, og at summen av varme og arbeid er en størrelse $\Delta U$ som er bevart når man ser på et system og omgivelsene som helhet. Loven kan brukes til å finne varmen som utvikles i systemet hvis man kjenner arbeidet som virker på det, eller vice versa. Termodynamikkens andre lov sier at systemer beveger seg mot en tilstand med maksimal multiplisitet, og det viser seg at varme strømmer slik at multiplisiteten maksimeres. Kapittel 4 og 5 er viet til de matematiske verktøyene som er nødvendige for å kunne videreutvikle og studere prinsippene kvantitativt, som gjøres fra og med kapittel 6. På mikroskopisk nivå kan varme ses på som å forandre populasjonene innenfor energinivåene til et kvantemekanisk system, mens arbeid ses på som å forandre energinivåene i seg selv. Forbindelsen mellom den mikroskopiske og den makroskopiske verden er at den mikroskopiske totale energien E er lik den makroskopiske indre energien U.

## 4: Matematiske verktøy

Funksjoner av flere enn én variabel finnes. For å finne ekstremverdiene til slike fuksjoner, krever man at alle de partiellderiverte er null samtidig. For å finne ekstremverdiene til slike funksjoner gitt visse bibetingelser, kan man bruke metoden med Lagrangemultiplikatorer. For å integrere funksjoner av flere variable kreves det generelt at man velger en vei å integrere langs. Tilstandsfunksjonene er de funksjonene der dette valget er vilkårlig (det påvirker ikke integralet). For å sjekke om noe er en tilstandsfunksjon kan man sjekke likheten til de kryssderiverte: $\partial 2f \partial x\partial y = \partial 2f /\partial y \partial x$ for alle tilstandsfunksjoner.

## 5: Entropi og Boltzmanns lov

Entropien er en funksjon av en mengde sannsynligheter; $S = S(p1, . . . , p2)$. Det er mer sannsynlig å observere de sannsynlighetene $p \cdot i$ som maksimerer entropien, det vil si de $p \cdot i$ som gjør at $\partial S/\partial \pi = 0$ for alle i. For store systemer dominerer tilstanden med maksimal multiplisitet: man kan se bort ifra andre tilstander. Hvis det ikke finnes fysiske bibetingelser vil man observere en flat fordeling. Hvis det foreligger en fysisk betingelse om en gjennomsnittlig energi i systemet, vil man observere en eksponensiell fordeling. Kapittel 7, 8 og 9 er viet til termodynamiske prinsipper, som brukes til å utlede den fullstendige beskrivelsen av sannsynlighetsfordelingene (Boltzmanns fordelingslov) i kapittel 10.

## 6: Termodynamiske drivkrefter

**Fundamentale** ligninger introduseres. De fundamentale ligningene for endringen i energi $dU$ og endringen i entropi $dS$ er fundamentale fordi de fullstendig spesifiserer alle endringer som kan forekomme i et enkelt termodynamisk system. $dU$ er en funksjon av kun ekstensive variable, som vil bli nyttig å vite fra og med kapittel 9. Den fundamentale ligningen for $S(U, V, N)$ er
$$dS = \frac{1}{T}dU + \frac{p}{T}dV − PM j=1 \frac {\mu j}{T}dNj$$
og har et **ekstremverdiprinsipp**: $dS = 0$ ved likevekt. Samtidig gir ligningen definisjoner av temperatur, trykk og kjemisk potensial:
$$\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N}$$
$$\frac{p}{T} = \left(\frac{\partial S}{\partial V}\right)_{U,N}$$
$$\frac{\mu _j}{T} = -\left(\frac{\partial S}{\partial N_j}\right)_{U,V,N_{i\neq j}}$$
Disse definisjonene kan kombineres med enkle **gittermodeller** for å utlede tilstandsligninger for enkle systemer, for eksempel den ideelle gassloven. Tolkninger av de termodynamiske drivkreftene er: $1/T$ er systemets tendens til å utveksle energi i form av varme, $p/T$ er systemets tendens til å endre volum, og $\mu_j/T$ er systemets tendens til å utveksle partikler. De termodynamiske drivkreftene er [**intensive størrelser**](intensiv-ekstensiv-storrelse) som er konjugater til (opptrer i par med) [**ekstensive størrelser**](intensiv-ekstensiv-storrelse), henholdsvis $U$, $V$ og $N$. Den intensive størrelsen beskriver hvordan entropien vil endres som respons på en endring av den ekstensive størrelse

## 7: Termodynamikkens logikk

Det klassiske rammeverket for termodynamikk studeres. For å unngå problemer med kinetikk (avhengighet av hastigheten til en prosess) studeres kun **kvasistatiske prosesser** - prosesser der systemet på alle tidspunkt er i likevekt. Ved å måle varme og energi i slike prosesser, kan man regne ut tilstandsfunksjoner som indre energi og entropi. I termodynamiske sykluser (når man integrerer langs en lukket kurve) summerer **tilstandsfunksjoner** til 0. Veiavhengige funksjoner summerer ikke nødvendigvis til 0, og det er derfor en motor kan konvertere varme til arbeid. Termodynamikkens andre lov kombinert med termodynamiske sykluser forklarer hvorfor det er vanskelig å konvertere varme til arbeid med høy **virkningsgrad**.

## 8: Laboratorietilstander og fri energi

I laboratoriet kan visse egenskaper til et delsystem kontrolleres med ytre betingelser. Generelt kan man kontrollere temperaturen, men ikke energien. Noen ganger er det også lettere å kontrollere trykket enn det er å kontrollere volumet. Når man ser på slike delsystemer i isolasjon, får de termodynamiske lovene en annen form som beskrives bedre med nye fundamentale funksjoner og ekstremverdiprinsipper; det er enten **Helmholtz fri energi** $F = U − T S$ eller **Gibbs fri energi** $G = H − T S = U + pV − T S$ som minimeres, avhengig av om det er henholdsvis volum eller trykk som kontrolleres utenfra. Dersom flere distinkte tilstander er mulige for et system, vil systemet innta den tilstanden som har lavest fri energi. Formen på definisjonene av F og G viser at det finnes en balanse mellom effekter som minimerer indre energi og effekter som maksimerer entropi, og at det er temperaturen som bestemmer hvilke effekter som dominerer: jo høyere temperatur, jo mer vil systemet gå mot å maksimere entropien.

**Varmekapasiteter** introduseres - disse er målbare størrelser som kan brukes til å finne energier, entalpier og entropier, som igjen kan brukes til å finne fri energi. Termodynamiske sykluser kan brukes som verktøy for å finne ukjente størrelser basert på kjente størrelser.

## 9: Maxwellrelasjoner og blandinger

Det er mulig å ta hensyn til flere typer krefter og arbeid enn de som har blitt behandlet så langt ved å legge til nye ledd i den fundamentale ligningen for indre energi. Deretter kan man, om man vil, gjøre de samme manipulasjonene som i kapittel 8 for å få et modifisert uttrykk for fri energi - den generelle fremgangsmåten er den samme. Maxwellrelasjoner er likheter mellom partielderiverte som følger av likheten mellom andreordens kryssderiverte av tilstandsfunksjoner. Disse relasjonene gjør det mulig å regne ut størrelser som er interessante å kjenne til, men vanskelige eller umulig å måle, ut i fra andre størrelser som er lettere å måle.

**Susceptibiliteter** introduseres som et spesialtilfelle av størrelser som er enkle å måle.

## 10: Boltzmanns fordelingslov

Boltzmanns fordelingslov, som gir fordelingen av atomer og molekyler over de tilgjengelige energinivåene ved likevekt, utledes. Dersom man har en modell for hvilke energinivå som er tilgjengelige for et system, kan man bruke Boltzmanns fordelingslov til å utlede hvordan partiklene fordeler seg over energinivåene, samt finne den korresponderende partisjonsfunksjonen. Med **partisjonsfunksjonen** kan man regne ut termodynamiske og (gjennomsnittlige) fysiske størrelser, som energi, entropi, frie energier, kjemisk potensial og trykk. Partisjonsfunksjonen til et helt system er produktet av partisjonsfunksjonene til hver enkelt partikkel, skalert med $1/N!$ når det er umulig å skjelne mellom forskjellige partikler.

Ensembler introduseres som samlingen av alle mikrotilstander for et system som oppfyller visse makroskopiske betingelser. Mer konkret brukes ensembler for å referere til hvilke variable som holdes konstant (og, implisitt, hva frihetsgradene er).

## 11: Statistisk mekanikk for ideell gass

Løsningen av Schrödingerligningen for et gitt system er de distinkte **energinivåene** som er tilgjengelige for dét systemet. Ved hjelp av statistisk mekanikk (i hovedsak Boltzmanns fordelingslov og verktøyene som ble utviklet i kapittel 10) kan man utlede termodynamiske egenskaper basert på **kvantemekaniske modellsystemer**. Tre modeller beskrives:

- partikkel-i-en-boks-modellen for translasjon (bevegelse av massesenteret til molekylet)
- harmonisk-oscillator-modellen for vibrasjon langs bindinger i molekylet
- stiv rotor-modellen for rotasjon av molekylet

For hver av disse modellene gis løsningene av Schrödingerligningen uten videre forklaring, og deretter utledes partisjonsfunksjonen for hver av disse. Den totale partisjonsfunksjonen til et molekyl er produktet av de respektive partisjonsfunksjonene for translasjon, vibrasjon, rotasjon og elektrisk eksitasjon. Dens siste ignoreres ofte ved å sette den lik 1. Gjerne er det kun én av komponentene som er interessant å ta hensyn til.

Basert på denne teorien diskuteres egenskapene til en ideell gass i detalj.


## 13: Kjemisk likevekt

Basert på atomær og molekylær struktur - masser, treghetsmomenter, bindingslengder og bindingsstyrker - utledes betingelser for **kjemisk likevekt** i gassfase via partisjonsfunksjoner. Disse betingelsene uttrykkes i form av en **likevektskonstant** K, som har formen $K = N_A/N_B$ for enkle tokomponentsystemer, men er mer komplisert for reaksjoner med flere specier. Likevektskonstantens temperaturavhengighet utledes og uttrykkes i form av **van’t Hoffs ligning**. Dette generaliseres til et uttrykk for hvordan den frie energien til et vilkårlig system avhenger av temperaturen med **Gibbs-Helmholtz-ligningen**. Trykkavhengigheten til likevektskonstanten utledes også.


## 14: Likevekt mellom væsker, faste stoffer og gasser

Likevekten mellom **kondensert fase** (samlebegrep for væske eller fast stoff) og gass er en balanse mellom **bindingsenergier** som holder partikler sammen i kondensert fase ved lav temperatur, og økningen i (translasjonell) entropi som oppnås ved å gå over i gassfase. Det **kjemiske potensialet** i en fase tolkes som partiklenes tendens til å forlate den fasen. Dermed er gassfasen og den kondenserte fasen i likevekt når partiklene har like stor tendens til å forlate gassfasen som de har til å forlate den kondenserte fasen: $\mu_{gass} = \mu_{kondensert}$. Likevekten kan også beskrives i form av et **damptrykk**, som er et mål på tettheten av partikler i gassfase. For å utlede formen til $\mu_{kondensert}$ og $\mu_{gass}$ brukes henholdsvis en gittermodell og den ideelle gassmodellen.

**Clausius’ ligning** gir stigningstallet til koeksistenskurven i et $p$, $T$-fasediagram. Det vil si at den beskriver hvordan faselikevekt avhenger av trykk og temperatur. **Clausius-Clapeyron-ligningen** er en tilnærming av Clausius’ ligning som benytter at volumet til en (ideell) gass er mye større enn volumet til kondensert materiale.

Ut i fra en gittermodell utledes et uttrykk for **overflatespenning**, som er kostnaden i fri energi for å flytte en partikkel fra det indre av materialet til overflaten. Det er det samme som å si at det er kostnaden i fri energi per partikkel for å øke overflatearealet.

## 15: Løsninger og blandinger

Gittermodeller utvikles for **ideelle** og **regulære løsninger**. I et system med to komponenter $A$ og $B$ finnes det flere måter å organisere partiklene på slik at $A$- og $B$-partikler er flettet sammen i en blanding, enn det finnes måter å organisere partiklene på slik at de er adskilt i separate faser. Dette gir opphav til en entropisk drivkraft for blanding, som er den eneste drivkraften som gjelder i en **ideell løsning**.

I en **regulær løsning** tar man også hensyn til attraktive interaksjoner mellom molekyler. Man tar imidlertid kun hensyn til interaksjoner mellom nærmeste naboer. En slik modell kalles en **Bragg-Williams-modell**, og i et slikt system avhenger graden av blanding av hvor sterke $AB$-interaksjonene er i forhold til $AA$-interaksjoner og $BB$-interaksjoner. Dette forholdet uttrykkes gjennom en parameter $\chi _{AB}$, som er proporsjonal med forskjellen mellom styrken på $AB$-interaksjonene og gjennomsnittet av $AA$- og $BB$-interaksjonene. Denne parameteren påvirker forskjellen i fri energi mellom blanding og adskilte faser, og dermed også likevekten mellom de to tilstandene.

Et uttrykk for **grenseflatespenning**, som er kostnaden i fri energi for å flytte en partikkel fra det indre av et materiale til grenseflaten mellom to kondenserte faser, utledes. Grenseflatespenningen er kostnaden i fri energi per partikkel for å øke grenseflatearealet.

Bragg-Williams-modellen antar at partiklene spres uniformt når de blandes - den tar dermed ikke hensyn til at antallet $AB$-interaksjoner øker med graden av blanding eller at sannsynligheten for å finne en partikkel på en gitt plass i gitteret avhenger av hvilke partikler som er i nærheten. Den fungerer derfor ikke dersom det er store forskjeller i interaksjonsenergier. En mer sofistikert modell må ta hensyn til dette i partisjonsfunksjonen. Modellen ignorerer bidraget fra rotasjon og vibrasjon til partisjonsfunksjonen - dette bidraget er likt i de to fasene for små molekyler, men ikke for komplekse molekyler og polymerer - derfor fungerer ikke Bragg-Williams-modellen for systemer med slike komponenter.

## Solvatering og overføring mellom faser

I systemer av to komponenter der én av komponentene kan forlate den kondenserte fasen til gassfase, eller til andre kondenserte faser, avhenger denne partikkelutvekslingen av konsentrasjonen til den komponenten i løsningen. Slike systemer kan studeres gjennom gittermodeller for å forklare, blant annet, hvorfor man øker **kokepunktet** og synker **frysepunktet** til en væske ved å legge til salt. Å legge til salt på én side av en halvgjennomtrengelig membran gir opphav til et **osmotisk trykk**.

**Partisjonskoeffisienten** er forholdet mellom konsentrasjonen av et løst stoff i ett løsemiddel og konsentrasjonen av det samme stoffet i et annet løsemiddel.

En gittermodell for **dimerisering** av oppløste stoffer i et løsemiddel utledes og brukes til å beskrive **hydrofob effekt**.

## 17: Fysisk kinetikk

Fysisk kinetikk beskriver statistisk termodynamikk for systemer som ikke er i likevekt, men holdes ved en konstant tilstand (**steady state**) av ytre krefter. **Strømning** av energi og partikler kan forekomme både på grunn av ytre krefter og på grunn av **gradienter**; energi strømmer der det er temperaturgradienter, og partikler strømmer der det er konsentrasjonsgradienter. Dette beskrives med **Ficks lover** og diffusjonsligningen, differensialligninger for konsentrasjon med hensyn på tid og rom. Strømningsraten er proporsjonal med gradienten, og proporsjonalitetskonstanten kalles diffusjonskonstanten. Partikkelstrøm er analogt med varmestrøm, som beskrives av Fouriers lov, der proporsjonalitetskonstanten er termisk konduktivitet.

Dersom det er flere forskjellige typer gradienter til stede i et system, er de resulterende strømningene ikke uavhengige; for eksempel vil en elektrostatisk potensialforskjell også drive en varmestrøm. **Onsagerrelasjonene** beskriver symmetrien mellom de koblede strømningene.

## 19: Kjemisk kinetikk

Kjemisk kinetikk beskjeftiger seg med hastighetene til kjemiske reaksjoner. Hastigheten til en kjemisk reaksjon kan uttrykkes med en **ratekonstant**, som er sterkt temperaturavhengig og beskrives med **Arrheniusligningene**. Temperaturavhengigheten kan forstås ved å se på overgangstilstanden i reaksjonen og **aktiveringsenergien** for å nå denne tilstanden. Uttrykk for rate- og likevektskonstantene kan utledes med overgangstilstandsteori, som gjennomgås overfladisk.

**Primærisotopeffekten** forklarer hvorfor reaksjonsrater er forskjellige for molekyler med forskjellige isotoper.

**Katalyse** forskynder kjemiske reaksjoner ved å senke aktiveringsenergien. **Brønsteds lov** forteller at reaksjonen som en syre katalyserer, går raskere jo sterkere syra er.

## 20: Couloumbs lov om elektrostatiske krefter

Elektrostatiske interaksjoner beskrives av Coulombs lov, og har **lang rekkevidde**: det elektrostatiske potensialet faller som funksjon av $1/r$. Interaksjoner mellom ladninger er svakere i **polariserbare** (dielektriske) medier fordi mediet endrer seg til å motvirke feltet fra ladningene. Graden av slik motvirkning beskrives av den dielektriske konstanten til mediet.

Elektrostatiske krefter summerer som vektorer og beskrives med elektrostatiske felt. **Gauss’ lov** beskriver forholdet mellom ladningen innenfor en flate og fluksen av det elektrostatiske feltet ut av flaten.

## 21: Elektrostatisk potensial

Ladninger i rommet produserer et elektrostatisk potensial, og dette potensialet beskriver forskjeller i energi mellom to punkter i rommet for en testladning med ladning 1. Potensialet kan regnes ut som et veiintegral av kraften på ladningen mens den beveger seg fra det ene til det andre punktet. Eventuelt kan det regnes ut gjennom **Poissons ligning** og randbetingelser. For problemer med blandet symmetri kan man bruke **speilladningsmetoden**, der den faktiske ladningsfordelingen i et område erstattes med en fiktiv ladningsfordeling som gir de riktige randbetingelsene.

## 22: Elektrokjemisk likevekt

Det elektrokjemiske potensialet er en generalisering av det kjemiske potensialet som tar hensyn til ladde molekyler, som er nyttig i situasjoner der partiklene drives både av kjemiske interaksjoner og elektriske felt, for eksempel i syre-base-reaksjoner eller redoksreaksjoner. **Elektrokjemisk potensial** er hovedeksempelet på hvordan et **ekstra energiledd** kan legges til i de fundamentale ligningene, og hvordan man tar hensyn til energier og potensialer som avhenger av rom.

**Halvcellepotensialer** og **Nernsts ligning** innføres som en introduksjon til elektrokjemi. **Elektrokjemi** beskriver hvordan ioner beveger seg fra ett medium til et annet, batterier, og hvordan ioner binder seg til overflater.

## 23: Saltløsninger og batteriteknologi

Merk: dette kapitlet går litt bort fra pensum i boka i sammenheng med NTNU's satsing på batteriteknologi.

Dersom du legger et ladet molekyl i vann og tilsetter salt vil saltet løse seg og sverme rundt det ladde molekylet. Det vil **skjolde** molekylet. Effekten til skjoldet er å øke hvor fort potensialet avtar rundt partikkelen. Vi vet fra elmag at potensialet rundt en ladet partikkel avtar radielt $V \propto 1/r$, men i en saltløsning avtar det da enda fortere (eksponensielt). Dette betyr det samme som at **Debye-lengden** blir kortere.

Introduserte **Poisson-Boltzmann** og **Debye-Hückel** modellene for saltløsninger.
**Poisson-Boltzmann**-ligningen er en komplisert differentialligning som beskriver det elektrostatiske potensialet som en funksjon av avstand fra en ladd partikkel i en saltløsning. Den forutsetter at vi kjenner saltkonsentrasjonen langt unna partikkelen $$ og det elektrostatiske potensialet på flaten av den ladde partikkelen $\psi_0$ (eller en tilsvarende verdi som ladningstettheten $\rho_0$).

**Debye-Hückel**-ligningen er en _linearisering_ av Poisson-Boltzmann ligningen. Den er på formen $\Nabla^2\psi \eq \kappa^2\psi$ der $\kappa^2$ er en konstant. $1/\kappa$ kalles **Debye-lengden** og henger sammen med hvor langt unna en partikkel har en betydelig påvirkning på det elektrostatiske potensialet.

Demonstrasjon av et enkelt batteri (en galvanisk celle).

**Litium** har det største negative **halvcellepotential**et på rundt $-3V$. Det er et lite atom, og kan dermed pakkes tett for å lage kompakte batterier. Disse egenskapene gjør litium til et svært gunstig materiale i batteriteknologi. Elektrolytten i batteriet er typisk en polymergele som $Li^+$-ionene lett kan reise gjennom.

Litium har høy etterspørsel, men det finnes lite av det i verden. Det er vanskelig å resirkulere fra elektrolytter og elektroder, så i fremtiden kommer mangel til å være et problem.

## 24: Intermolekylære interaksjoner

Intermolekylære bindinger er svake interaksjoner som holder væsker og faste stoffer sammen, og som gjør trykket i en **van der Waals-gass** lavere enn trykket til en ideell gass ved lav tetthet.

Ved små avstander tiltrekker molekyler som regel hverandre på grunn av **London-dispersjonskrefter** (kvantefluktuasjoner i ladningsfordelinger og påfølgende polarisering), men ved enda mindre avstander frastøter de hverandre på grunn av Paulis eksklusjonsprinsipp. Summen av de to effektene modelleres som et **Lennard-Jones-potensial**, som er null der de to bidragene kansellerer. Dette er **bindingslengden**.

Intermolekylære interaksjoner kan delvis forstås som elektrostatiske interaksjoner mellom ladningsfordelinger, både på grunn av asymmetrisk ladningsfordeling internt i molekylene, på grunn av molekylenes rotasjonsfrihet og på grunn av polariserbarheten til molekylene.

## 25: Faseoverganger

Faseoverganger skjer der to eller flere tilstander er stabile på samme tidspunkt. For eksempel vil det være mulig, når væskene $A$ og $B$, at det dannes to faser - en med høy konsentrasjon av $A$, og en med høy konsentrasjon av $B$. **Vektstangregelen** kan brukes til å finne andelen av hver fase dersom man kjenner blandingsforholdet totalt sett. Hvorvidt det vil oppstå én eller to faser, avhenger blant annet av molforholdet mellom de to komponentene. Tilsvarende er stoffer ved kokepunktet i en likevekt mellom væske- og gassfase. Økning i temperatur vil forskyve likevekten fra et tofasesystem til et énfasesystem fordi bidraget fra økning i entropi blir sterkere og fasiliterer blanding av komponentene. Hvis temperaturen er høyere enn den kritiske temperaturen $T_C$ , får man et énfasesystem uavhengig av molforholdet mellom de to komponentene.

Det som fundamentalt bestemmer om man har et én- eller flerfasesystem, er hvorvidt den frie energien $F$, som funksjon av konsentrasjonen $x$ til en av komponentene, har ett eller flere lokale minima. Dersom man kjenner $F(x)$ kan man finne andelen av hver komponent i hver fase ved å tegne tangenten til $F(x)$ ved to punkter. Disse punktene er i nærheten av, men ikke nødvendigvis de samme som, de lokale minimumspunktene til $F(x)$.

## 27: Adsorpsjon, binding og katalyse

Molekyler som binder seg til overflater og til bindingspunkter på andre molekyler kalles **ligander**. Ved å øke konsentrasjonen av ligander øker man andelen av de tilgjengelige bindingspunktene (eller, for en gittermodell for overflaten, plassene i gitteret) som er opptatt, som fører til metning av systemet. Prinsippet er relevant for både katalyse og **binding til proteiner**.

**Sabatiers prinsipp** for **heterogen katalyse** er at en katalysator bør binde seg sterkt nok til reaktantene til å kunne katalysere reaksjonen, men svakt nok til å kunne gi slipp på produktet. Det finnes altså en optimal bindingsentalpi mellom katalysatoren og substratet.

**Langmuirmodellen** beskriver binding og metning når bindingspunktene er uavhengige av hverandre. Med **Michaelis-Menten-modellen** utledes en ligning for enzymers kinetikk som er til forveksling lik Langmuirs adsorpsjonsligning (men merk at den Michaelis-Menten beskriver en reaksjonsrate, mens Langmuir beskriver tettheten av molekyler på en overflate).

## 32: Polymerløsninger

Polymermolekyler er mye større enn typiske (små) løsemiddelmolekyler, ofte med en faktor på over $10^3$. Denne størrelsesforskjellen har viktige konsekvenser for termodynamikken til polymerløsninger. For polymerer i løsning er volumfraksjonen mye større enn molfraksjonen, så man kan ikke regne med at polymerene har de samme egenskapene som de som ble utledet med grunnlag i molfraksjoner, fordi polymermolekylene ikke kan behandles på lik linje med løsemiddelmolekylene. I stedet må hver monomer - hvert segment på størrelse med løsemiddelmolekyl - behandles som et løsemiddelmolekyl. **Flory-Huggins-modellen** brukes til å utlede entropi- og energiforskjellen når polymerer blandes inn i et løsemiddel. Modellen fungerer dersom det ikke er sterke interaksjoner mellom monomerer, og vil derfor ikke fungere like godt for å beskrive proteiner med både hydrogen- og disulfidbindinger.
