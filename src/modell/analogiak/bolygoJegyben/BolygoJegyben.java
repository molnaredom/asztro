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
                                    "elvárja a gyerektől, hogy önáló legyen",


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
                                    "ha gondoskodhat a családjáról, fófej  jó pasi",
                                    "önmagában nem tud erőslenni, kell mögé egy nő aki ezt az erőt képviseli",
                                    "papucsságra hasjlamos, mos ,mosogat, átcsúszhat női szerepekbe",
                            },
                            // nő
                            {
                                    "soksor átveszi a nap szerepet és ő irányít",
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
                                "gyereket akar(viszont a ygereket nem akarni kell)"
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
                    //oroszlán hold
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
                    //skorpió hold
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
                    }
            }

    };


}
