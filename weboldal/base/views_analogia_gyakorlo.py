from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import QuizForm, QuestionForm, AnswerForm
from django.forms import inlineformset_factory


def index(request):
    Quiz.objects.all().delete()

    kvizkeszito(
        ido=30,
        kerdesszam=3,
        kviznev="Mindig csak ez az 1 kviz van",
        leiras="jo kviz lesz"
    )

    para = {'quiz': Quiz.objects.all()}
    return render(request, "index.html", para)


@login_required(login_url='/login')
def quiz(request, myid):
    quiz = Quiz.objects.get(id=myid)
    return render(request, "quiz.html", {'quiz': quiz})


def quiz_data_view(request, myid):
    quiz = Quiz.objects.get(id=myid)

    # korabbi kerdesek torlese
    for q in quiz.get_questions():
        q.delete()

    print(quiz_data_view.__name__, f"{quiz=}")

    kerdesek_hozzaadasa(kerdesszam=3, quiz=quiz)

    questions = []
    for q in quiz.get_questions():  # a kviz objektumnak van egy get questions metodusa
        answers = []
        for a in q.get_answers():
            answers.append(a.content)
        questions.append({str(q): answers})

    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def save_quiz_view(request, myid):
    print(save_quiz_view.__name__, f"{myid=}")

    if is_ajax(request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        # print(data_)

        data_.pop('csrfmiddlewaretoken')

        for i, k in enumerate(data_.keys()):
            # print(f'{i}key: ', k)
            question = Question.objects.filter(content=k)[0]
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(id=myid)

        score = 0
        marks = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.content)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.content:
                        if a.correct:
                            score += 1
                            correct_answer = a.content
                    else:
                        if a.correct:
                            correct_answer = a.content

                marks.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                marks.append({str(q): 'not answered'})

        Marks_Of_User.objects.create(quiz=quiz, user=user, score=score)
        return JsonResponse({'passed': True, 'score': score, 'marks': marks})


def add_quiz(request):
    if request.method == "POST":
        kvizkeszito(
            ido=30,
            kerdesszam=0,
            kviznev="mindig random kerdes kviz",
            leiras="jo kviz lesz"
        )
        form = QuizForm(data=request.POST)
        if form.is_valid():
            # quiz = form.save(commit=False)
            # quiz.save()
            obj = form.instance
            return render(request, "index.html", {'obj': obj})
    else:
        form = QuizForm()
    return render(request, "add_quiz.html", {'form': form})


def kerdesbank_keszito(bolygojegyben=False, bolygohazban=False, hazurahazban=False):
    kerdesbank = []
    if bolygohazban:
        for i in BolygoHazban2.objects.all():
            kerdesbank.append({f"{i.haz}. ház {i.bolygo}": i.leiras})
    elif bolygojegyben:
        for i in BolygoJegyben2.objects.all():
            kerdesbank.append({f"{i.jegy} {i.bolygo}": i.adatok})
    elif hazurahazban:
        for i in HazUraHazban.objects.all():
            kerdesbank.append({f"{i.alap_haz}. ház ura {i.ura_melyik_hazban}. házban": i.tulajdonsagok["analogiak"]})
    else:
        print("NEM LETT MEGADVA KÉRDÉSBANK ANALOGIA")

    # [print(i, end="\n\n") for i in kerdesbank]

    return kerdesbank


def kvizkeszito(ido=10, kerdesszam=0, kviznev="", leiras=""):

    form = QuizForm()
    quiz = form.save(commit=False)
    quiz.time = ido
    quiz.number_of_questions = kerdesszam
    quiz.name = kviznev
    quiz.desc = leiras
    quiz.save()
    print("KVIZ ELMENTVE")



def kerdesek_hozzaadasa(kerdesszam, quiz):
    valasz_lehetosegek_szama_per_kerdes = 3
    kerdesbank = kerdesbank_keszito(bolygojegyben=True)
    for _ in range(kerdesszam):
        kerdes_szoveg, valaszlehetosegek = random_kerdes_generalas(kerdesbank, valasz_lehetosegek_szama_per_kerdes)

        kerdes_hozzaadas(
            kerdes_szoveg=kerdes_szoveg,
            kviz=quiz,
            valaszlehetosegek=valaszlehetosegek
        )


def random_kerdes_generalas(kerdesbank,valasz_lehetosegek_szama_per_kerdes):
    """
    kerdes_szövege : bj tulajdonság
    válasz: bj név
    """
    def randomszam(mennyi):
        return random.randint(0, mennyi)

    print("összes bolygó jegyben analógia: ", len(kerdesbank))
    osszes_valaszlehetoseg = set()
    uj_kerdesbank = []
    for i in kerdesbank:
        for bj_nev,bj_tul_ok in i.items():
            if sum([len(k) for k in bj_tul_ok.values()]) >= 1:
                osszes_valaszlehetoseg.add(bj_nev)
                for szempont,tul_leiras_ok in bj_tul_ok.items():
                    for tulajdonsag_kerdes in tul_leiras_ok:
                        uj_kerdesbank.append({f"{szempont}: {tulajdonsag_kerdes}": bj_nev})

    print("\nfennmaradó bj analógia: ",len(uj_kerdesbank))
    osszes_valaszlehetoseg= list(osszes_valaszlehetoseg)
    print(len(osszes_valaszlehetoseg), osszes_valaszlehetoseg)

    feltett_kerdes_alapanyag = uj_kerdesbank[randomszam(len(uj_kerdesbank))]

    kerdes_szoveg = str(feltett_kerdes_alapanyag)

    valaszlehetosegek = valaszlehetosegek_hozzaadasa(osszes_valaszlehetoseg, feltett_kerdes_alapanyag, randomszam,
                                 valasz_lehetosegek_szama_per_kerdes)

    print("talajdonsagok:", kerdes_szoveg)
    print("/////",valaszlehetosegek)

    return kerdes_szoveg, valaszlehetosegek


def valaszlehetosegek_hozzaadasa(osszes_valaszlehetoseg, random_analogia, randomszam,
                                 valasz_lehetosegek_szama_per_kerdes):
    # helyes válasz
    valaszlehetosegek = [{"szoveg": str(random_analogia.values().__str__()), "igazsagertek": True}]

    # helytelen válaszok
    while len(valaszlehetosegek) < valasz_lehetosegek_szama_per_kerdes:
        rossz_valasz = osszes_valaszlehetoseg[randomszam(len(osszes_valaszlehetoseg))]

        # ha a rossz valasz != jó válasz
        if rossz_valasz not in valaszlehetosegek:
            valaszlehetosegek.append({"szoveg": rossz_valasz, "igazsagertek": False})

    return valaszlehetosegek


def kerdes_generator(feltoltendo_adatok, kviz_adatok):
    bolygojegyben_kerdesbank = []
    opciok = set()
    for bj_analogia, bj_tul in feltoltendo_adatok.items():
        szempontok = bolygo_values["szempontok"]
        for jegy_nev, jegy_values in bj_tul.items():
            for szempont_nev, szempont_array in jegy_values.items():
                for analogia in szempont_array:
                    opciok.add("-".join([jegy_nev, bolygo_nev]))
                    if analogia != "" and szempont_nev != "munka":
                        bolygojegyben_kerdesbank.append({
                            "kerdes": str(szempont_nev) + ": " + str(analogia),
                            "valasz": "-".join([jegy_nev, bolygo_nev])
                        })
                    # print(,analogia,sep="-" )
    kerdesbank_meret = len(bolygojegyben_kerdesbank)
    # for i in bolygojegyben_kerdesbank:
    #     print(i)

    kerdesek = []
    import random

    for _ in range(int(kviz_adatok["kérdésszám"])):
        # print(kerdesek)
        kivalasztott_kerdes_valasz = bolygojegyben_kerdesbank[random.randint(0, kerdesbank_meret-1)]

        valasz_opciok = [
                {"opcio": kivalasztott_kerdes_valasz["valasz"], "helyes_e": "igaz"},
                {"opcio": bolygojegyben_kerdesbank[random.randint(0, kerdesbank_meret)]["valasz"], "helyes_e": "haims"},
                {"opcio": bolygojegyben_kerdesbank[random.randint(0, kerdesbank_meret)]["valasz"], "helyes_e": "haims"}
            ]
        random.shuffle(valasz_opciok)
        kerdesek.append({
            "kerdesnev": kivalasztott_kerdes_valasz["kerdes"],

            "valasz_opciok": valasz_opciok})
    print("kérdések")
    print(kerdesek)
    return kerdesek



def kerdes_hozzaadas(kerdes_szoveg, kviz, valaszlehetosegek):
    form = QuestionForm()
    # if form.is_valid():
    question = form.save(commit=False)
    question.content = kerdes_szoveg
    question.quiz = kviz

    question.save()
    print("KÉRDÉS HOZZAADVA")
    for valaszlehetoseg in valaszlehetosegek:

        valasz_lehetoseg_hozzaadas(
            valasz_szoveg=valaszlehetoseg["szoveg"],
            igazsagertek=valaszlehetoseg["igazsagertek"],
            kerdes_obj=question)

    print("VALASZ HOZZAADVA")


def add_question(request):
    questions = Question.objects.all()
    questions = Question.objects.filter().order_by('-id')
    #
    # for q in questions:
    #     print("question: ",q),
    #     for a in q.get_answers():
    #         a.content= "2"
    #         a.correct= True
    #
    # for q in questions:
    #     print("question: ",q),
    #     for a in q.get_answers():
    #         print(a)

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # if question.quiz == 1:
            #     question.content = 1 # todo
            question.save()

            return render(request, "add_question.html")
    else:
        form = QuestionForm()
        print("add_question", {'form': form, 'questions': questions})
    return render(request, "add_question.html", {'form': form, 'questions': questions})


#
# def add_answers(request,):
#     form = HoroszkopFormGyors()
#
#     if "megse" in request.POST:
#         return redirect(f"horoszkop_gyujtemeny")
#
#     if request.method == "POST":
#         form = HoroszkopFormGyors(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#
#             obj = set_bolygo_es_haz_objektumok(obj)
#             print(f'ASC-{obj.haz_1_id=}')
#             obj.save()
#             if 'ujabb_fevitel' in request.POST:
#                 return redirect(f"create-horoszkop")
#
#             elif "mentes_es_foolal" in request.POST:
#                 return redirect(f"horoszkop_gyujtemeny")
#
#     context = {'form': form}
#     return render(request, "create_templates/analogia_form.html", context)

def delete_question(request, myid):
    question = Question.objects.get(id=myid)
    if request.method == "POST":
        question.delete()
        return redirect('/add_question')
    return render(request, "delete_question.html", {'question': question})


def add_options(request, myid):
    kerdes = Question.objects.get(id=myid)
    # print("------------", question, question.quiz)
    QuestionFormSet = inlineformset_factory(Question, Answer, fields=('content', 'question'), extra=2)
    if request.method == "POST":
        formset = QuestionFormSet(request.POST, instance=kerdes)
        if formset.is_valid():

            adatok = [
                {"szöveg": "szöveg1",
                 "igazságérték": False
                 },
                {"szöveg": "szöveg2",
                 "igazságérték": False
                 },
                {"szöveg": "szöveg3",
                 "igazságérték": False
                 },
            ]

            for valasz in adatok:
                valasz_lehetoseg_hozzaadas(valasz_szoveg=valasz["szöveg"],
                                           igazsagertek=valasz["igazságérték"],
                                           kerdes_obj=kerdes)

            alert = True
            formset.save()
            return render(request, "add_options.html", {'alert': alert})
    else:
        formset = QuestionFormSet(instance=kerdes)
        # print("add_options", {'formset': [i for i in formset], 'question': kerdes})
    return render(request, "add_options.html", {'formset': formset, 'question': kerdes})


# def add_options(request, myid):
#     kerdes = Question.objects.get(id=myid)
#     # print("------------", question, question.quiz)
#     QuestionFormSet = inlineformset_factory(Question, Answer, fields=('content', 'question'), extra=2)
#     if request.method == "POST":
#         formset = QuestionFormSet(request.POST, instance=kerdes)
#         if formset.is_valid():
#
#             adatok = [
#                 {"szöveg": "szöveg1",
#                  "igazságérték": False
#                  },{"szöveg": "szöveg2",
#                  "igazságérték": False
#                  },{"szöveg": "szöveg3",
#                  "igazságérték": False
#                  },
#             ]
#
#             for valasz in adatok:
#                 valasz_lehetoseg_hozzaadas(valasz_szoveg=valasz["szöveg"],
#                                            igazsagertek=valasz["igazságérték"],
#                                            kerdes_obj=kerdes)
#
#             alert = True
#             formset.save()
#             return render(request, "add_options.html", {'alert': alert})
#     else:
#         formset = QuestionFormSet(instance=kerdes)
#         # print("add_options", {'formset': [i for i in formset], 'question': kerdes})
#     return render(request, "add_options.html", {'formset': formset, 'question': kerdes})


def valasz_lehetoseg_hozzaadas(valasz_szoveg, igazsagertek, kerdes_obj):
    Answer.objects.create(
        content=valasz_szoveg,
        correct=igazsagertek,
        question=kerdes_obj
    ).save()


def results(request):
    marks = Marks_Of_User.objects.all()
    return render(request, "results.html", {'marks': marks})


def delete_result(request, myid):
    marks = Marks_Of_User.objects.all()
    # for mark in marks:
    #     print(mark.id, mark.user)
    marks = Marks_Of_User.objects.get(id=myid)
    if request.method == "POST":
        marks.delete()
        return redirect('results')
    return render(request, "delete_result.html", {'marks': marks})
