# simpleMacroMaker

**simpleMacroMaker** je program kojim je moguće simulirati tipkovnicu i miš. U programu se definira lista naredbi koje se sljednim izvršavanjem mogu obavljati razne repetitivne zadatke. Moguće naredbe su:
- *MouseClick* - određuje se klik mišem (gumb, broj klikova, mjesto klika) koji će biti izvršen kao da je korišten fizički miš
- *TypeText* - određuje se tekst koji će biti upisan kao da je korištena fizička tipkovnica
- *SendHotKey* - određuje se kombinacija tikpi koja ce biti izvršena kao da je korištena fizička tipkovnica 
    - ne preporuča se korištenje više od dvije funkcijske tipke [ctrl, shift, alt, ...]
    - taskmgr - pokreće TaskManager
- *Wait* - određuje se vrijeme izraženo u milisekundama koje će program provesti čekajući
- *WaitForPixel* - određuje se pixel (x, y) za koji će se vršiti provjera pokazuje li boju (r, g, b), određuje se i vrijeme izraženo u milisekundama nakon kojega će se isponova vršiti provjera pixela

## Gašenje programa

Program je moguće ugasiti u bilo kojem trenutku izvođenja, pritiskom na tipku **Esc**.

## Tijek izvođenja

### 1. Dodavanje naredbi u listu za izvođenje

Moguće je odrediti bilo koliko naredbi te će one biti izvršene u poretku u kojem su i postavljane. Naredbe je moguće dodavati dok se ne upiše **0**.

### 2. Modificiranje liste narebi

U ovoj fazi moguće je izbrisati naredbu, dodati novu ili izvršiti listu naredbi. naredbe je moguće dodavati ili brisati dokle god se ne pokrene zvršavanje.

### 3. Izvršavanje liste naredbi

Određujeju se iznosi *timeout* i *itearation*. *Iteration* označava broj koliko puta će lista naredbi iti izvršena. *Timeout* označava broj sekundi nakon kojega će *WaitForPixel* biti zaustavljen kao i cijeli program.

Nakon toga, traži se zadnja potvrda da želimo pokrenuti program.

## Buduće dorade

1. Mogućnost spremanja i otvaranja datoteke koja sadrži postavljene naredbe za izvršavanje.
2. Izrada grafičkog sučelja
3. Dodavanje naredbe **Run** - moguće je pokrenuti bilo koji program koji je moguće pokrenuti kroz *Windowsov* **Run** naredbeni redak