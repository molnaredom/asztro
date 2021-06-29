package modell.analogiak.bolygoJegyben;

import java.util.Locale;

public interface BolygoJegyben {
    //bolygo 0 nap 1 hold...
    //0-kos ... 11-halak
    //0altalanos , 1 apa ...

    String[][][][] analogiak = new String[][][][]{
            //nap
            {
                //kos
                    {
                            //altalnos
                            {
                                "kos nap analogia",
                                    "ez az"
                            },
                            //apa
                            {
                                "én házam én váram",
                                    "megbescsülést vár",
                                    "tiszteletet vár",
                                    "gyereknek nem lehet igaza vele szemben",
                                    "megkérdőjelezhetetlen",
                                    "küzdhet az egyerekért",
                                    "segítheti a gyerket"
                            },
                            //gyerek
                            {
                               "azt látja az apa egresszív",
                               "az apa a vállalkozásával foglalkozik"
                            },
                            // férfi
                            {
                                "ideális ha olyan párt kap aki képes alárendelődni",
                                    "a párja felnéz rá",
                                    "a párja azt éli, hogy erős férfi van mellette",
                                    "tevékenyen részt vesz az életben",
                                    "küzd, felvállalja a férfi szerepeket",
                                    "igazi macsó férfi tradícionális értelemben",
                                    "nem szabad engednie hogy a párja vagy más nő a fejére nőljön",
                                    "alázatosan küzdhet a családjáért, különben a párjával küzd majd"

                            },
                            // nő
                            {
                                "olyan férfit választ akiből kihozhatja a kost",
                                    "a férfi küzdjön érte",
                                    "harcoljanak érte",
                                    "ferfivel vállalkozás-> ő irányít",
                            },
                            //főnök
                            {
                                "viszi előre a céget",
                                    "elkapkodja a dolgokat",
                                    "előbb cselekszik utána gondolkodik",
                                    "nem lehet vele vitatkozni",
                                    "ha valamit elhatároz, tűzön vizen keresztülmegy érte , véghezviszi",
                                    "ott jó vezetőnek ahol nem kérdőjelezik meg",
                                    "állandó bizonyítási vágy, könnyen motiválható"
                            }
                    },
                    //bika nap
                    {
                            //altalnos
                            {
                                    "bika nap analogia",
                                    "ez az"
                            },
                            //apa
                            {
                                    "anyagiakben méri a szeretetét, törődését",
                                    "szerinte az anyagiakkal minden elérhető",
                                    "fárasztják a gyerekek"
                            },
                            //gyerek
                            {
                                    "erős kötődés, nagyon ragaszkodik",
                                    "igényli, hogy kiszolgálják",
                                    "azt látja az apa teremti a biztonságot",
                                    "az apára mindig lehet támaszkodni, sose ideges",
                                    "az apát csak a pénz érdekli"
                            },
                            // férfi
                            {
                                    "lusta",
                                    "élvezkedő, fontos a testiség, a szerelem",
                                    "birtokolni szeretné a párját-> tenyerén hordja",
                                    "a felelősség lehet a nőé, de az anyagiak semmiképpen",
                                    "mellette mindig sokat költ a nő, de keveset keres",
                                    "nehezen hozható ki a sodrából",
                                    "szereti a jó ételeket, a kényeztetést",
                                    "ragaszkodik a biztonságos életvitelhez"
                            },
                            // nő
                            {
                                    "anyagiságot, biztonságot, teremtést, élvezeteket él meg a párjában",
                                    "mindig féltékeny",
                                    "van kivel jókat enni(párja)"
                            },
                            //főnök
                            {
                                    "ameddig nem kell fizetést adni addig minden szuper",
                                    "nem szereti a felelősséget",
                                    "megbízható és kitartó",
                                    "nem szeretik az aprópénzt, próbál tőle megszabadulni"
                            }
                    },
                    //ikrek nap
                    {
                            //altalnos
                            {
                                    "ikrek nap analogia",
                                    "ez az"
                            },
                            //apa
                            {
                                    "nem apa inkább barátja a gyereknek",
                                    "nem tud korlátozó lenni, nem tud ragaszkodni",
                                    "a nevelést lazán veszi",
                                    "nem tud kötődni hosszútávon, rövid távon igen",
                                    "mindenhova elviszi a gyerekét, mindig történjen valami",
                                    "nem beszél komoly támákról a gyerekével, meghitten",
                                    "elvárja a gyerektől, hogy önálló legyen",


                            },
                            //gyerek
                            {
                                    "állandóan füllent(vagy csak élénk a fantáziája)",
                                    "sokat mozog, tesz-vesz, ide-oda megy",
                                    "az apját szélhámosnak látja",
                                    "az apját mindig üzletelni látja",
                                    "azt látja az apja ne, foglalkozik vele kellő időt"

                            },
                            // férfi
                            {
                                    "szórakozató vicces",
                                    "jó társaság, nem unalmas, értelmes jól beszél",
                                    "a nőt partnernak, egyenrangú társnak tekinti",
                                    "nem tud kötődni a párjához",
                                    "lehet megígér valamit, de nem teszi meg, vagy nem figyelt rád eléggé",

                            },
                            // nő
                            {
                                    "jön,megy ,sokat beszél",
                                    "intelektuális férfit választ",
                                    "mozgalmasabb életet választ a párjával",
                                    "üzlettársnak látja a párját"
                            },
                            //főnök
                            {
                                    "sokat, beszél, nem szeret hallgatni",
                                    "keresi a hallgatóságot",
                                    "nagy a szabadságigénye, munkatársai ritkán látják"

                            }

                    },
                    //rák nap
                    {
                            //altalnos
                            {
                                    "akkor lehet nap , ha megéli a rákságot, a gondoskodást",
                                    "ez az"
                            },
                            //apa
                            {
                                    "Melegen korlátozó szülő",
                                    "olyan szabályokat hoz gyerekének ahol a szeretete is meg tud nyilvánulni",
                                    "megjelennek az aggodallmak a féltés a gyerek iránt",
                                    "sokszor nem engedi felnőni a gyereket",
                                    "szüksége van arra hogy a gyerek nélküle ne tudjon lépni, szükség legyen rá"
                            },
                            //gyerek
                            {
                                    "túlérzékeny",
                                    "kötődés a család, az apa a szülők felé",
                                    "szükságesnek érzi a szülőket a dolgok átéléséhez",
                                    "azt látja az apa gondoskodik a családról",
                                    "azt látja az apjának fontos a nélkülözhetetlenség",
                            },
                            // férfi
                            {
                                    "ha gondoskodhat a családjáról, jófej  jó pasi",
                                    "önmagában nem tud erőslenni, kell mögé egy nő aki ezt az erőt képviseli",
                                    "papucsságra hasjlamos, mos ,mosogat, átcsúszhat női szerepekbe",
                            },
                            // nő
                            {
                                    "sokszor átveszi a nap szerepet és ő irányít",
                                    "ő az erősebb, ő határoz, ő dönt a párkapcsolatban, övé a felelősség",
                                    "olyan pasit választ akinek fontos a gyerek, a család",
                                    "olyan férfit választ aki tele van érzelemmel, romantikus, odafigyel az érzéseire",
                                    "választhat tutyi-mutyi férfit aki majd otthon marad a gyerekkel és ő mehet dolgozni"
                            },
                            //főnök
                            {
                                    "meg lehet vele csináltatni a munkát",
                                    "hisztis: hullámzik érzelmileg, hangulatilag",
                                    "döntéseket érzelmi alapon hoz, nem tartják jó főnöknek"
                            }

                    },

                    {  //oroszlan nap
                            //altalnos
                            {
                                  "vagyok valaki",
                                    "felnéznek rám mert bíznak bennem",


                            },
                            //apa
                            {
                                    "szeretne büszke lenni a fiára, elvárja hogy a gyerek agy is viselkedjen",
                                    "mepgpróbálja anyagi szinten oroszlánná tenni a fiát ezzel mutatva, hogy az ő fia értékes",
                                    "nem egy korlátozó típus, ráhagyja az anyára",


                                    },
                            //gyerek
                            {
                                    "azt hiszi neki minden jár ,pusztán attól hogy létezik",
                                    "lehet azt látja, hogy az apát tisztelik elismerik",
                                    "lehet azt látja, az apa szerepet játszik mert szeretné kivívni a fensőbbséget",
                                    "lehet azt látja, az apa lenyomja a körülötte lévőket",
                                    "láthatja a bátorságot a lustaságot, vagy a gyávaságot is az apjában",
                                    "vigyázni kell rá nehogy eltörják a gernincét , az önbecsülését nem szabad ledegradálni",

                            },
                            // férfi
                            {
                                   "elvárja a kényeztetést, hogy becsüljék tiszteljék, felnézzenek rá",
                                    "csak olyan nője lehet aki alárandelődik neki",
                                    "egyfajta koronaékszerként bányik a nővel",
                                    "fontos neki a nő, nem akárki az én feleségem",
                                    "a nő nem kérdőjelezheti meg, el kell fogadnia a férfi fensőbbségét",
                                    "nem szabad neki beszólni, és a nő ne hozza kellemetlen helyzetbe, kritizálni mások előtt",
                            },
                            // nő
                            {
                                    "mindig erősebb mint a férfi",
                                    "a nőn múlik a pasiból tud-e napot faragni vagy sem",
                                    "tudja mit akar és hogyan",
                                    "nehezen kerül olyan helyzetbe hogy fel tudjon nézni egy férfira",

                                     },
                            //főnök
                            {
                                    "csak felsővezetőnek jó, hogy ne kelljen senkinek alárendelődnie",
                                    "könnyen bedől a hízelgésnek, ilyenkor nem látja a valódi értéket"
                            }

                    },
                    {  //szuz nap
                            //altalnos
                            {
                                  "meg kell tanulnia ,hogy minden tökéltetes",
                                    "ha mindent elfogad azt mondják passzív vagy így nehezen lesz nap",
                                    ""


                            },
                            //apa
                            {
                                    "elvárásokat támaszt gyerekével szemben",
                                    "fontos neki ,hogy a gyereke tudással bírjon",
                                    "frusztrálja ,ha a gyerek tehetségtelen, elvárja hogy szorgalmes legyen",
                                    "vigyáznia kell a maximalizmussal , ne mással szembel legyen elvárs, max magunkkal szemben",
                                    "racionális , nem nagyon engedi közel magához a gyereket",
                                    },
                            //gyerek
                            {
                                    "tudóscsemete, jó tanuló, meg akar felelni az elvárásoknak",
                                    "ha nem tud jól teljesíteni nagyon leteszi a lécet, nehogy ne feleljen meg",
                                    "sokszor betegséget kreál, hogy az elvárások megszűnjenek",
                                    "maximalista apát lát, aki mindig dolgozik, és semmi sem elég jó neki",

                            },
                            // férfi
                            {
                                "negyon erős elvárások",
                                    "nem elég ha megcsinálod amit elvár, úgy is kell gondolnod(persze nem tudhatod mit gondol)",
                                    "ha azt érzi ,hogy nem néznek fel rá, megpróbálja a másikat lenyomni",
                                    "önbizalomhiányos, ritkán hiszi , hogy felnéznek rá",
                                    "olyan feleséget választ , hogy neki is fontos legyen az ő szűzsége",
                            },
                            // nő
                            {
                                    "ha nő éli a napot sokkal intenzívebb mint egy férfinél éa ez rettenetes",
                                    "kötözködő, munkamániás, maximalista, ez nem jó, át kellene adnia a nap szerepet",
                                    "lehet hogy szeteri , ha lenyomják, és ezért választ olyan férfit akinek semmi sem jó",

                                     },
                            //főnök
                            {
                                    "nem való vezetőnek, nem tud pozitív oldalról erősíteni, csak a hibát veszi észre",
                                    "nem akarja átadni a munkát, mer tudja ,úgyis csak ő tudja tökéletesen megcsinálni"

                            }

                    },{  //merleg nap
                            //altalnos
                            {


                            },
                            //apa
                            {
                                "jó szülő, bár nem tud nevelni",
                                    "nem tud korlátozni nem tud nemet mondani",
                                    "nagyon manipulálható, befolyásolható",
                                    "nem szabad ütköznie a gyerekkel, az apa jelölö ki a korlátokat, de az anya tartassa be",
                                    "lehetnek elvárásea, zsarolásai a gyerekkel szemben"
                                    },
                            //gyerek
                            {
                                    "nagyon meg akar felelni , nem szereti, ha kritizálják",
                                    "kettős: 1. megpróbál visszahúzódni, nehogy valamiben ne feleljen meg vagy 2. mindig felhívja magára a figyelmet, hogy észrevegyék",
                                    "kisfiú -> hogyan kell férfivá fejlődni? az apa tanítsa meg: felvállalni önmagát ",

                            },
                            // férfi
                            {
                                "semmiben sem dönt, felelőséget se nagyon vállal",
                                    "a nő tuti hogy 1000* erősebb lesz",
                                    "a karrierista pasik többsége mérleg",
                                    "könnyebb a külvilágban lennie valakinek mint a magánéletben, nem jár neki kockázattal",
                                },
                            // nő
                            {

                                     },
                            //főnök
                            {


                            }

                    },


            },
            //hold
            {
                //kos hold
                    {
                        //általános
                            {
                                "kos hold"
                            },
                            //ösztönei
                            {
                                "állandóan keresi a kihívásokat",
                                    "keresi azokat a helyzetekeet ahol ő győzhet",
                                    "erős benne a versenyszellem",
                                    "mindent az erejéből szeretne megoldani",
                                    "türelmetlen",
                                    "nem figyel a másikra, nem figyeli a másik mit reagál a dolgaira",
                                    "a választ a saját kérdésére nem hallja meg"
                            },
                            //tehetsége
                            {
                                "mindenhol ahol irányítani kell",
                                    "amikor egy konkrét célt kell megvalósítani",
                                    "ahol sok energiát kell belefektetni egy feladatba",
                            },
                            //anya
                            {
                                "erős anyatigris",
                                    "hirtelen módon képes küzdeni a gyerekért",
                                    "a gyerek azt csinálhatja amit ő, nem veszi figyelembe az ő akaratát"
                            },
                            //gyerek
                            {
                                "öntörvényű, akaratos, nehéz irányítani",
                                    "anya-gyerek csaták nem ritkák",
                                    "az anya mindenkit elnyom a környezetében"
                            },
                            //feleség
                            {
                                "legyen mivel harcolnia, a férfit tolja előre",
                                    "gyengébb párja lesz(sokkal)",
                                    "ösztönösen irányítja a családot",
                                    "nem egy házitündér, minden otthoni dolgot feladatnak fog fel",
                                    "képtelen alárendelődni, de ezt nem veszi észre"
                            },
                            // férfi
                            {
                                "erős nőt választ maga mellé",
                                    "imád harcolni a párjával",
                                    "nem szeret felelősséget vállalni",
                                    "kell neki egy olyan nő aki őt segíti"
                            },
                            //alárendeltsége
                            {
                                "csak ott tud ,ahol valakire fel tud nézni",
                                    "vagy magától rendelődik alá vagy sehogy"
                            },
                            //befogadása
                            {
                                "gyereket akar(viszont a gyereket nem akarni kell)"
                            }
                    },
                    //bika hold
                    {
                            //általános
                            {

                            },
                            //ösztönei
                            {

                            },
                            //tehetsége
                            {

                            },
                            //anya
                            {

                            },
                            //gyerek
                            {

                            },
                            //feleség
                            {

                            },
                            // férfi
                            {

                            },
                            //alárendeltsége
                            {

                            },
                            //befogadása
                            {

                            }
                    },
                    // ikrek hold
                    {
                            //általános
                            {

                            },
                            //ösztönei
                            {

                            },
                            //tehetsége
                            {

                            },
                            //anya
                            {

                            },
                            //gyerek
                            {

                            },
                            //feleség
                            {

                            },
                            // férfi
                            {

                            },
                            //alárendeltsége
                            {

                            },
                            //befogadása
                            {

                            }
                    },
                    //rák hold
                    {
                            //általános -érzelmei
                            {
                                "odaadó",
                                    "negyon erős érzelmei vannak, erős kötődés",
                                    "nagyon féltékeny",

                            },
                            //ösztönei
                            {
                                    "jók az intuíciós képességei",
                                    "megérzi átérzi, erős az empátiája",
                                    "jól teremt kapcsolatot a tudatalattival/tudattalannal",
                                    "tele van állandóan szorongással és aggodalommal"
                            },
                            //tehetsége
                            {
                                "erős a művészi tehetsége",
                                    "minden tarületen ami családhoz, otthonhoz tartozik",

                            },
                            //anya
                            {
                                  "ősanya típus",
                                    "ha 1 gyereke van nagyon csak hozzá kötődik, ha több akkor megoszlik a szeretet",
                                    "nagyon odaadó a gyereke iránt",
                                    "aggódik és szorong a gyereke miatt",
                                    "nem gyenge ,de érzelmileg kötődik"
                            },
                            //gyerek
                            {
                                "nagyon erős kötősések",
                                    "az otthonban találja mae a biztonságot, nyugalmat",
                                    "nem szeret változtani kockáztatni",
                                    "nagyon érzékeny",
                                    "jó művészi épességű"
                            },
                            //feleség
                            {
                                "jó háziasszony",
                                    "élvezi a feleség szerepet",
                                    "mindent a család felől közelít meg",
                                    "érzékeny és érzelmekben kiáradó párkapcsolat",
                            },
                            // férfi
                            {
                                    "a nőt a termékenysége miatt választja",
                                    "érzékenysége, romantikája miatt választja a nőt",
                                    "a nőt azért választja mert szereti ha a ő söt főz takarít",
                                    "gyereket, családot szeretne a nőtől"
                            },
                            //alárendeltsége
                            {
                                "ahol érzelmileg érintett ott tökéletesen alá tud rendelődkni",
                                    "ahol ő nélkülözhetetlen ott alá tud rendlődni"
                            },
                            //befogadása
                            {
                                "tökéletes befogadó",
                                    "a gyerek a befogadás számára",
                                    "gyereket csak az akarhat nála aki megtermékenyíti"
                            }
                    },
                    //oroszlán hold
                    {
                            //általános-érzelmei
                            {
                                    "nagyon ritkán mutatja a valódi önmagát",
                                    "ritkán ismerhetőek meg a valódi érzései",
                                    "ne várd, hogy előbb valljon szerelmet mint te(mert ha lapátra tennéd nem bírná az egója)",
                                    "ne várj tőle lángolást, odaadást",
                                    "büszke, tartással rendelkező"
                            },
                            //ösztönei
                            {
                                    "gyáva: kerüli a megalázó vagy alárendelt helyzeteket",
                                    "bátor: ahol érzi, hogy vagyok valaki, előjön az uralkodó hajlama",
                                    "nagylelkű,odaaoás,büszkeség",
                                    "lusta: azért nem tesz valamit, hogy más megtegye és általa átélhesse a fensőbbséget"
                            },
                            //tehetsége
                            {
                                    "mindenhol, ahol luxust, fensőbbséget hatalmat, gazdagságot képviseli",
                                    "adottságok: vezetés irányítás, uralkodás, alkotás, teremtés, kreativitás",
                            },
                            //anya
                            {
                                "általában nagyon jó anya",
                                    "szeret büszkének lenni a gyerekére",
                                    "nevelni a gyereket nem nagyon tudja, nem megy bele a kis játékokba",
                                    "neki égkő a gyerek, mint egy ékszer, így is bánik vele"
                            },
                            //gyerek
                            {
                                "anya uralkodik, imádja a környezetét vezetni",
                                    "az anya lusta, vagy hedonista, vagy uralkodó típus,(vagy más oroszlan analógiák",

                            },
                            //feleség
                            {
                                "büszke ved, nemes vad. a férfi legyen rá büszke",
                                    "nem egy konyhatündér",
                                    "first lady",
                                    "olyan férfit választ akinek olyan ahivatása, hogy nyílvánosság előtt szerepel, hogy megélhesse az oroszlánságot"
                            },
                            // férfi
                            {
                                "oroszlánná teszi a nőt aki mellette van(ezt úgy érdemes ,hogy ha ő a királynő akkor én a király)"
                            },
                            //alárendeltsége
                            {
                                "csak egy embernek",
                                    "olyan pozíciókat kell neki keresni, ahol max 1 embernek kell alárendelődni(másképp nem tud)"

                            },
                            //befogadása
                            {
                                "csak ,ha ő akarja",
                                    "csak ,ha teremteni akar, ehyébként nem"
                            }
                    },
                    //szűz hold
                    {
                            //általános- érzelemi
                            {

                            },
                            //ösztönei
                            {
                                "kritikus, viszonyít mindent mindenhez(nem tudja igazán kikapcsolni)",
                                    "mindig látja a negatív oldalt",
                                    "racionális, rációja a tapasztalaton alapszik",
                                    "keresi a tapasztalatokat, átélési lehetőségeket",
                                    "ösztönös döntésre képtelen",
                                    "mindig a hasznos dolgokat szereti, keresi, ami előreviszi az életben"
                            },
                            //tehetsége
                            {
                                "ahol másokat segíteni, támogatni kell",
                                    "mindenhol ahol elemezni kell",
                                    "jó könyvelő, számokhoz nagyon ért",
                            },
                            //anya
                            {
                                "megpróbálja könyvből nevelni a gyereket, ahogy leírtan a lehető legjobb",
                                    "megpróbál tökéletesen nevelni, ehhez mindent megad a gyerekeknek",
                                    "racionálisan kikapcsolaj az érzelmeket, van hogy valami  nem jó a gyereknek egóban, ő akkor is megteszi az érdekében",

                            },
                            //gyerek
                            {
                                "az anyának magasak az elvárásai, megpróbál ennek megfelelni",
                                    "azt érzi az anyának semmi nem jó",
                                    "az anya képes kezelni a tökéletesség kérdését és nem viszonyít",
                                    "megtanulja az anyjától a segytőkészséget, a szolgálatot, alárendeltséget, tisztaság mániát"
                            },
                            //feleség
                            {
                                "megbízható, húséges, erényes",
                                    "szégyenlős",

                            },
                            // férfi
                            {
                                "nőben keresi a megbízhatóságot, hűséget",
                                    "nőben keresi a precizitást, pontosságot, akár munkatársat",
                                    "olyan nőt keres aki szintén szeret dolgozni",
                                    "lehet hogy rendmániás nőt keres"
                            },
                            //alárendeltsége
                            {
                                "legjobb munkaerő, mindent tökéletesen póbálnak véghezvinni"
                            },
                            //befogadása
                            {
                                "ösztönöket próbálja kikapcsolni, racionális"
                            }
                    },
                    //mérleg hold
                    {
                            //általános-érzelmei
                            {
                                "mindig érzelmeket vár, és szeretné ha viszonoznák az övét",
                                    "ott nem tud érzelmileg megnyílni ahol az érzelmeit nem viszonozzák",
                            },
                            //ösztönei
                            {
                                    "keresi a harmóniát, egyenssúlyt békességet",
                                    "keresi a pozitív visszajelzéseket",
                                    "kompromisszumkedvelő, nem szeret másokkal szembeszállni ha nem muszáj",
                                    "döntőképesságe nem túl erős",
                                    "jó a diplomáciaérzéke",
                                    "nem önérvényesítő típus, mindig a külvilágot figyeli",
                                    "szeretne másoknak megfelelni"
                            },
                            //tehetsége
                            {
                                    "az emberi kapcsolatokban",
                                    "olyan élethelyzetekben ahol átéli az egyensúlyt és elfogadást kap",
                                    "jól megérzi hogy lehet a másik emberhez közel kerülni",
                                    "jó a művészetekben, színészeti dolgokban",
                                    "jó nyilvános szereplő"
                            },
                            //anya
                            {
                                    "jó kacsolatot próbál kialakítani a gyerekkel",
                                    "fontos neki mit mondanak a gyerekéről, ez befolyásolja a nevelésben",
                                    "a külvilág megfelelésének mgefelelően neveli a gyerekét",
                                    "a gyerek szülő fejére nőhet, és már ő irányít a kapcsolatban",
                                    "a párkapcsolat fontosabb mint a gyerek"
                            },
                            //gyerek
                            {
                                    "minden határt megpróbál átlépni/elérni",
                                    "nagyon hisztis, folyton azt tezsteli vajon szeretik-e szülei ",
                                    "harmonikusan éli meg a gyerekkort",
                                    "láthatja, hogy az anya folyton szerepet játszik",
                                    "láthatja hogy az anyja kétszínű",
                                    "látja az anyja kompromisszumkötő készségét",
                                    "látja hogy az anyja nagyon nőies"
                            },
                            //feleség
                            {
                                    "fontos neki a párkapcsolaat és szeretné ha tökéletes lenne",
                                    "nem a tipikus háziasszony, ő továbbra is nő szeretne lenni",
                                    "a páron keresztül kell kiteljesednie, nem önállóan"
                            },
                            // férfi
                            {
                                "szép nőt keres, aki nőies",
                                    "fontos neki hogy a nő adjon magára",
                                    "szereti ha a nő engedelmes,alárendelt és azt teszi amit mond",
                                    "szeretne büszke lenni a párjára, és hogy elismerjék őt"
                            },
                            //alárendeltsége
                            {
                                    "akkor tud ha fontos neki a párja",
                            },
                            //befogadása
                            {
                                    "ha fontos neki a párja akkor befogadó",
                                    "ha meg akarja szerezni a másikat akkor igen",
                                    "ha nem tetszik a másik nem eljátszik egy szerepet"
                            }
                    },
                    //skorpió hold
                    {
                            //általános -érzelemi
                            {
                                    "szélsőséges, vagy mindent vagy semmit",
                                    "vagy óriási szenvedélyek, vagy teljes hidegség",
                                    "átmenetiek,nehezen észlelhetőek",
                                    "visszaigazolást vár arra,vajon szeretnek-e engem",
                            },
                            //ösztönei
                            {
                                    "igazi öszönember, jók a megérzései, érzéekenyen reagál mindenre",
                                    "erős empátiakészség, azt hiszi hogy másokban is nagy aztán nagyot csalódik",
                                    "féltékeny, mást tapasztal mint amit szeretne",
                                    "halállal, elmúlással, tudattalannal való kapcsolat",
                                    "fél a veszteségtől, öszönösen próbálja ezt kikerülni",
                            },
                            //tehetsége
                            {
                                    "ahol a tudattalannal, elmúlással,halállal foglakozhat",
                                    "művészetben",
                                    "mások értékének megőrzése: pénz, anyagiak, emberi élet",



                            },
                            //anya
                            {
                                    "nagyon jó anya, de van amikor hárítják, és nem akarnaka zok lenni"
                            },
                            //gyerek
                            {
                                   "magányosan éli a gyermekkorát",
                                   "érzelmileg kicsit zárkózott, nehezen nyílik meg nehezen  barátkozik" ,
                                    "panaszkodik a szülőre, hogy nem szeretik nme úgy szeretik",
                                    "figyeli hogy mit csinál a szülő, mit csinál az anya",
                            },
                            //feleség
                            {
                                    "lelki társat keres, de ez nem fog sikerülni",
                                    "a másik nem érezheti amit ő, így nem is létezik lelki társ",
                                    "nagyon sok érzelmet lehet tőle kapni, ha pont azt szeretné",
                                    "nagyon tud szeretni, nagyon tud gyűlölni",
                                    "ha keresztbetettél neki, ne számíts megbocsájtásra",
                                    "ha szeret magától szeret, nem lehet kényszeríteni"
                            },
                            // férfi
                            {
                                " a szexuális kisugárzása alapján választja a párt",
                                "azért válaszztja a nőt hogy jókat harcolhasson vele"
                            },
                            //alárendeltsége
                            {
                                "semilyen módon nem rendelősik alá, csak ha ő akarja, de akkor sem érzed h így lenne"
                            },
                            //befogadása
                            {
                                    "legkevésbé befogadó jegy"
                            },
                            //munka:
                            {
                                    "tűzoltó","banki trezort őrző","testőr","mentős"
                            }

                    },




                    //vizonto hold
                    {
                            //általános
                            {
                                "a kötődései átmenetiek- ha ős zerelmes én nem ha én akkor ő nem",
                                    "repülő és a reptér- tudni akarja h van valaki aki engem szeret, de ne korlátozzon"
                            },
                            //ösztönei
                            {
                                    "keresi a szabadságot, kreatív",
                                    "vonzódik a különleges helyzetekhez dolgokhoz",
                                    "keresi a másságot",
                                    "az a dolga hogy kiegészítse a világot amivel a másságot képviseli"
                            },
                            //tehetsége
                            {
                                "kreativitas, sok utazas, sok valtozatossag ahol csak a kiindulópont adott"
                            },
                            //anya
                            {
                                "házasságon kívüli anya",
                                    "örökbe fogad",
                                    "nevelőszülőség",
                                    "külföldi pár(akár szinesbőrű)",
                                    "császárral szülés",
                                    "jó anya tud lenni, de az hogy őt a gyerek korlátozza az lehetetlen"
                            },
                            //gyerek
                            {
                                "kettősség: ragaszkodik az anyához nagyon 2. szabadghyerek akit fogni kell",
                                    "azt érzi az én anyám szabad akart lenni mellettem",
                                    "anya tanítja: mindent érted teszek, egyedül nevelés"
                            },
                            //feleség
                            {
                                "nem neki való",
                                 "olyan párra van szüksége aki korlátozza, ha nem tudja elfogadni menekülni fog",
                                    "olyan párra vágyik ahol egyenrangú a kapcsolat,kivesszük a közös jót",
                                    "olyan férfit talál aki a független nőt keresi"
                            },
                            // férfi
                            {
                                "menekül minden kötöttségtől",
                                    "legjobb ha kiszolgáltatott neki a nő",
                                    "azért választja a nőt mert különleges más mint a többi, érdekes",
                                    "vagy csak szabad akar lenni es egyilyen lany mellett tud leginkabb az lenni",
                                    "legjobb szerető típus"
                            },
                            //alárendeltsége
                            {
                                "nem szeret alárendelődni",
                                    "inkább a melléreendeltség az övé"
                            },
                            //befogadása
                            {
                                "gyerekvállalásban is kell valami különleges, eltérő a hagyományostól"
                            }
                    }
            },


            {//merkur
                    {//kos
                            {//altlanos

                            },
                            {//gondolkodasa
                                    "tele van versenyszellemmel",
                                    "fontos neki a gyozelem",
                                    "mindenkivel versenyezni akar, le akar győzni",
                                    "nehezen fogja fel ha valaki ellenáll neki",
                                    "nagyon erősen meg akar győzni az igazáról",
                                    "gyorsak a reakciói",
                                    "jól vág az esze csak előbb cselekszik mint gondolkozik",
                                    "türelmetlen, nem tud semmit kivárni",
                            },
                            {//kapcsolatteremtés
                                    "agresszívan teremt kapcsolatot",
                                    "mindent gyorsan akar megszerezni"
                            },
                            {//kommunikacio
                                    "azt hiszi az az erősebb aki hangosabb",
                                    "szeretné hogy társaságben odafigyeljenek rá",
                            },
                            {//mozgékonyság
                                    "\"beveszi a várat aztán megy tovább, nem aar várban lakni\"",
                                    "sokszor olyanon vitatkozik aminek semmi értelme nincs",
                            },
                            {//gyermekkora
                                    "olyan nevelést kap és olyan élethelyzetekbe kerül, ahol akaratát érvényesíteni tudja",
                                    "sokszor harcolnia kell a testvérrel",
                                    "sokszor sportioskolába jár, vagy olyan helyre ahol edzenie kell, pörög az élet",
                            },
                            {//tanulása
                                    "ami érdekli azért mindent megtesz",
                                    "amiben ott van a lehetőség hogy győzzön ott tenni is fog érte",
                                    "állandóan veresenyhelyzetben kell tartani",
                                    "olyan dolgokat tanuljon ahol mindig igaza lehet"
                            },
                            {//elfogadása
                                    "mindent elfogad, amit akar, de semmi mást nem",
                                    "ha mondják neki hogy el kellene fogadni ,annál kisebb esélye lesz hogy tényleg elfogadja",
                                    "ha ő nem akarja nem fog menni"
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                                    "lassú, megfontolt",
                                    "anyagias",
                                    "alapos, sokszor átrágja a dolgokat",
                                    "tiszta paraszti észjárás",
                                    "birtoklás és az anyagiak motiválják",
                                    },
                            {//kapcsolatteremtés
                                    "nem teremt könnyen kapcsolatot, inkább a begtartásra törekszik",
                                    "Olyan kapcsolatokra törekszik amit meg is tud tartani",
                                    "nem szeret hitelt felvenni, mert abban nincs benne a biztonság"
                                    },
                            {//kommunikacio
                                    "lassan kommunikál",
                                    "előnyösebb ha írásban kommunikálhat, mert ott jobban át tudja goldolni mit írjon",
                                    "nem túl jó a problébamegoldó képessége",
                                    "egy egy problémány napokig rágódik",
                                    },
                            {//mozgékonyság
                                    "híresen lusta",
                                    "kényelem, nyubalom , biztonság motiválja",
                                    "nem szeret változtatni, ragaszkodik a helyzetekhez",
                                    },
                            {//gyermekkora
                                    "nyugalomban békességben stabilitásban telik",
                                    "szülők anyagilag motiválják",
                                    },
                            {//tanulása
                                    "nem gyors de alapos",
                                    "amit megtanul azt tudja is, jó az emlékezőképessége, mély a tudása",
                                    },
                            {//elfogadása
                                    "anyag szinten fogad el",
                                    "aki nem sérti a nyugalmát és nem akar elvenni tőle semmit, azt elfogadja",
                                    "ha kibillentik a biztonságból azt nem tudja elfogadni"
                            }
                    },
                    {//ikrek
                            {//altlanos

                            },
                            {//gondolkodasa
                                    "furfangos, ravasz",
                                    "jó eszű, jó reakciójú",
                                    "mindenre tud megoldást találni",
                                    "kíváncsi, információt szeretne adni és kapni",
                                    "nem kíván elköteleződni semmi mellett"
                            },
                            {//kapcsolatteremtés
                                    "könnyen teremt kapcsolatot emberekkel tárgyakkal",
                                    "a kapcsolatainak többsége nem túl mély",
                                    "nagyon sok ismerőse van",
                                    "jól tudja alkalmazni kapcsolatait a hétköznapokban"
                            },
                            {//kommunikacio
                                    "jól kommunikál",
                                    "idegennyelvekhez is jó adottsága van",
                                    ""
                            },
                            {//mozgékonyság-változtatasi kepesseg
                                    "bármikor tud változtatni",
                                    "vagy éppen jön valahonnan, vagy éppen megy valahova",
                                    "nem szabad beleragadnia helyzetekbe, mert neki fontos a változás"
                            },
                            {//gyermekkora
                                    "nagyon változatos",
                                    "gyakran elválnak a szülők, vagy iskolát vált, vagy költöznek sok változás a környezetében",
                                    "mindig van mit tanulni, mindig van információ amire szert tehet",
                            },
                            {//tanulása
                                    "legjobb rövid távú tanuló, vizsgákra pl nagyon jól fel tud készülni, aztán elfelejti",
                                    "nagyon jó memória, hallásból látásból is minden megmarad",
                            },
                            {//elfogadása
                                    "könnyen fogad el helyzeteket, főleg ha nem fontos számára",
                                    "egyszer valami nagyon fontos neki, nemsokára már annyira mégse lesz fontos",
                                    "könnyebben túllép dolgokon",
                                    "ha őt megcsalják, a másik azt hiszi mekkora problémát okoz ezzel, de valójában a megcsaló jobban megsínyli"
                            }
                    },
                    {//rak
                            {//altlanos

                            },
                            {//gondolkodasa
                                    "érzelmileg dönt, mindent így közelít meg",
                                    "fontos a múlt és a család",
                                    "intuitív döntései vannak, ehhez jó érzéke van",
                                    "nem vesz tudomást azokról a folgokról amik sértik ez érzelmeit",
                                    "ha azt mondja 'úgy érzem', akkor racionális alapon nem tudod lebeszélni, neki az úgy van és kész",
                            },
                            {//kapcsolatteremtés
                                    "érzelem alapáján hoz létre kapcsolatot emberekkel és tárgyakkal is",
                                    "neki a szimpátia érzelem alapú, ha nem vagy szimpatikus neki nem lesz jó kapcsolat",
                                    "őrizget régi tárgyakat, főleg ha családtól, vagy régi emlékből van",
                                    "szereti a romantikát, hogy valami érzéki is legyen"
                            },
                            {//kommunikacio
                                    "olyat szeretne mondani amire mindenki kíváncsi(itt jön a pletyka)",
                                    "ha valaki tud valamit akkor ő biztos, lehet hozzá fordulni bármivel",
                                    "szeretne nélkülözhetetlen lenni kapcsolataiban",
                                    "az érzelmeket sokkal jobban le tudja írni mint szóban kimondani",
                            },
                            {//mozgékonyság-változtatasi kepesseg
                                    "amig szeret nem változtat, amikor már nem akkor változtat",
                                    "ha kötődik nem változtat, ha nem akkor vált"
                            },
                            {//gyermekkora
                                    "fontos neki a család, és hogy tudjon velük beszélni",
                                    "gyakran úgy érzi elvesztette az édesannyát, ha testvére születik",
                            },
                            {//tanulása
                                    "érzelmi alapon tanul, kötődik a tanárhoz , tantárgyhoz is, vagy pont nem akkor utálja",
                                    "nem képes racionálisan tanulni"
                            },
                            {//elfogadása
                                    "amihez érzelmileg kötődnek azt korlátlanul elfogadják",
                                    "olyan dolgokat is elfogad pl gyerekekben amit nem kellene, néha túl megengedő"
                            }
                    },
                    {//oroszlan
                            {//altlanos
                                "Kulcsmondata: Ha hallgattál volna, bölcs maradtál volna.",
                                    "Nem szabad versenyeztetni, olyan hely kell neki , ahol tudása kommunikációja, MEGKÉRDŐJELEZHETETLEN",

                            },
                            {//gondolkodasa
                                "fensőbbségtudat: én aztán vagyok valaki",
                                    "nagyvonalú tud lenni",
                                    "könnyen befolyásolhatóak, nagyon hiúak, könnyen bedőlnek a szép szavaknak"
                            },
                            {//kapcsolatteremtés
                                "felülről teremt kapcsolatot: ami értékes , ami különleges az jöhet, ami nem érdekes azzal nem foglalkozik kizárja",
                                    "párkapcsolatban fontos, hogy büszkel lehessen a kapcsolatra",

                            },
                            {//kommunikacio
                                "nem megy bele olyan kommunikációba, ahol alul maradhat",
                                    "ha nincs versenyhelyzet nagyra van magával , egyébként meg nyuszi",
                                    "nem szereti ha megkérdőjelezik amit ő mond, nem szeret vitatkozni",
                                    "szeret fensőbbséggel beszélni",
                                    "szeret kioktato lenni",
                                    "szereti önmagát megkoronázni"
                            },
                            {//mozgékonyság-változtatasi kepesseg
                                "az alattvalókat nem szívesen cseréli le",
                                    "ha olyan helyzetben van ahol nem érzi, hogy vagyok valaki, képes változtatni",
                            },
                            {//gyermekkora
                                "kettősség: vagy tenyerén hordja a szülő, mindent megadnak neki, támogatják esgítik, hogy kiteljesüljön" +
                                        "vagy olyan közegből jön, ahol mindig lenyomták lehúzták ezért be akarja bizonyítani, hogy én is érek annyit mint más",
                                    "sokszor olyanok a testvérei ,akik közt ő lehet a király",
                                    "vigyázni kell vele, nehogy megtörjék a gerincét, az egóját"
                            },
                            {//tanulása
                                "ha tudod motiválni, nagyon jó tanuló tud lenni(látnia kell mi lesz az eredménye",

                            },
                            {//elfogadása
                                "a dícséretet igen, a főhajtást igen, a kritikát nem",
                                    "elfogadhatatlannak tartják a megalázó helyzeteket"
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                            },
                            {//kapcsolatteremtés
                            },
                            {//kommunikacio
                            },
                            {//mozgékonyság-változtatasi kepesseg
                            },
                            {//gyermekkora
                            },
                            {//tanulása
                            },
                            {//elfogadása
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                            },
                            {//kapcsolatteremtés
                            },
                            {//kommunikacio
                            },
                            {//mozgékonyság-változtatasi kepesseg
                            },
                            {//gyermekkora
                            },
                            {//tanulása
                            },
                            {//elfogadása
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                            },
                            {//kapcsolatteremtés
                            },
                            {//kommunikacio
                            },
                            {//mozgékonyság-változtatasi kepesseg
                            },
                            {//gyermekkora
                            },
                            {//tanulása
                            },
                            {//elfogadása
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                            },
                            {//kapcsolatteremtés
                            },
                            {//kommunikacio
                            },
                            {//mozgékonyság-változtatasi kepesseg
                            },
                            {//gyermekkora
                            },
                            {//tanulása
                            },
                            {//elfogadása
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                            },
                            {//kapcsolatteremtés
                            },
                            {//kommunikacio
                            },
                            {//mozgékonyság-változtatasi kepesseg
                            },
                            {//gyermekkora
                            },
                            {//tanulása
                            },
                            {//elfogadása
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                            },
                            {//kapcsolatteremtés
                            },
                            {//kommunikacio
                            },
                            {//mozgékonyság-változtatasi kepesseg
                            },
                            {//gyermekkora
                            },
                            {//tanulása
                            },
                            {//elfogadása
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                            },
                            {//kapcsolatteremtés
                            },
                            {//kommunikacio
                            },
                            {//mozgékonyság-változtatasi kepesseg
                            },
                            {//gyermekkora
                            },
                            {//tanulása
                            },
                            {//elfogadása
                            }
                    },
                    {//bika
                            {//altlanos

                            },
                            {//gondolkodasa
                            },
                            {//kapcsolatteremtés
                            },
                            {//kommunikacio
                            },
                            {//mozgékonyság-változtatasi kepesseg
                            },
                            {//gyermekkora
                            },
                            {//tanulása
                            },
                            {//elfogadása
                            }
                    },
            }

    };


}
