package modell.analogiak.alapAnalogiak;

import java.util.Random;

public interface JegyAnalogia {
    // 3d tomb
    // 0 személyi jellemző - minőségbeli  3 szint - feladatok szintei
    // 1 szemelyi jellemző - minoseg nelkuli 3 szint
    // 2 tárgyi jellmező 4 szint -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
    //
    //

    //                    "hit általi biztonság", "tudja hogy mindig annyia van amennyinek lennie kell"
    //            },
    //            {  //kozepso
    //                    "azért ad hogy kapjon", "kényelmes"
    //            },
    //            {   //also
    //                    "mások küzdenek érte", "másokkal agressszív"
    //            }
    //    }

    String[][][][] jegyek = new String[][][][]{

            {//-----------KOS-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint
                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "kos"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },


            {//-----------BIKA-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "hit általi biztonság", "tudja hogy mindig annyia van amennyinek lennie kell"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "bika"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------IKREK-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "amit mond amit tesz amit gondol nem válhat el egymástól"},
                            {  //kozepso
                                    "üzletel"},
                            {   //also
                                    "lop"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "ikrek flso", },
                            {  //kozepso
                                    "ikrek koezp"},
                            {   //also
                                    "ikrek"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "ikrek"},
                            {
                                    "világoskék", "pöttyös", "hullámos"},
                            {
                                    "váll"},
                            {
                                    "újságíró"},
                    }

            },

            {//-----------RÁK-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "alárendeli magát egy gyengébb akaratnak"},
                            {  //kozepso
                                    "nélkülözhetetlen"},
                            {   //also
                                    "aggódik",}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "bika"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------OROSZLAN-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "másokért uralkodik"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "bika"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------SZŰZ-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "minden úgy tökéletes ahogy van", "szükségszerűség"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "szuz"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------MÉRLEG-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "önelfogadás"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "bika"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------SKORPIÓ-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "az érzéseivel mindenki egyedül van"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "skorpio"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------NYILAS-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "nincsenek véletlenek"},
                            {  //kozepso
                                    ""},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "nyilas"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------BAK-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "mások céljai az én céljaim is"},
                            {  //kozepso
                                    "saját céljaiért küzd"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "bak"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------VÍZÖNTŐ-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "mindig azt teszem ami a másiknak jó, ha rossz ha jó az nekem"},
                            {  //kozepso
                                    "másság"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "vízonto"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },

            {//-----------HALAK-----------------
                    {  // 0. személyi jellemző - minőségbeli  3 szint - feladatok szintei
                            {  //felso
                                    "egység","nekem nem kell tudnom amit a másik mert ketten együttvéve úgyis tudjuk"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}
                    },
                    {//  1.  szemelyi jellemző - minoseg nelkuli 3 szint

                            {  //felso
                                    "másokért küzd", "rájön hogy nem csak önnmagáért kell tennie"},
                            {  //kozepso
                                    "mésokkal küzd magáért", "domináló"},
                            {   //also
                                    "mások küzdenek érte", "másokkal agressszív"}

                    },
                    {// 2 tárgyi jellmező 4 szint       -0 jegy  -1 külső jegy pl szin, -2 testresz -3 foglalkozások
                            {
                                    "halak"},
                            {
                                    "piros", "rövid", "egyenes"},
                            {
                                    "fej", "fog", "haj", "köröm", "szőr"},
                            {
                                    "sebész", "lövész", "katona", "sportoló"},
                    }

            },






};





static void randomAnalogia(String megadottJegy) {
        Random random = new Random();

        int i = 0;

        for (String[][][] s : jegyek) {
            if (s[2][0][0].equals(megadottJegy)) {
                int t1 = random.nextInt(3);
                int t2 = random.nextInt(jegyek[i][t1].length );
                int t3 = random.nextInt(jegyek[i][t1][t2].length);


                System.out.println(jegyek[i][t1][t2][t3]);
            }

            i++;

        }

    }
}
