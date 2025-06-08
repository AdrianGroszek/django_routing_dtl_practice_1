from django.shortcuts import render

champions = [
    {
        "id": 1,
        "name": "ahri",
        "role": "Mage",
        "difficulty": "Medium",
        "image_url": "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Ahri_0.jpg",
        "description": "Ahri to lisia czarodziejka, która wykorzystuje magię do manipulowania emocjami swoich przeciwników. Jej urok sprawia, że wrogowie są bezbronni na chwilę, co pozwala jej ich szybko wyeliminować. Jest zwinna, potrafi przemieszczać się po polu walki dzięki swojej superumiejętności. Jej styl gry opiera się na precyzyjnych atakach i szybkim reagowaniu na sytuację na mapie."
    },
    {
        "id": 2,
        "name": "garen",
        "role": "Fighter",
        "difficulty": "Easy",
        "image_url": "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Garen_0.jpg",
        "description": "Garen to odważny wojownik z Demacii, znany z honoru i lojalności. Jego umiejętności czynią go niezwykle wytrzymałym w walce wręcz. Może wyciszać przeciwników i zadawać potężne obrażenia swoją legendarną sztyletową egzekucją. Idealny wybór dla graczy, którzy lubią proste, ale skuteczne podejście do walki."
    },
    {
        "id": 3,
        "name": "jinx",
        "role": "Marksman",
        "difficulty": "Medium",
        "image_url": "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Jinx_0.jpg",
        "description": "Jinx to nieobliczalna strzelczyni, która uwielbia chaos i eksplozje. Uzbrojona w arsenał śmiercionośnych broni, potrafi szybko zmieniać styl ataku między karabinem a rakietnicą. Jej obecność w grze sprawia, że walki drużynowe stają się nieprzewidywalne. Gdy zabije przeciwnika, wpada w szał, co pozwala jej przejąć kontrolę nad walką."
    },
    {
        "id": 4,
        "name": "leona",
        "role": "Tank",
        "difficulty": "Medium",
        "image_url": "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Leona_0.jpg",
        "description": "Leona to nieustraszona obrończyni Solari, władająca mocą słońca. Jej styl gry skupia się na inicjowaniu walk i chronieniu sojuszników. Potrafi ogłuszać wielu wrogów jednocześnie i wytrzymać ogromne ilości obrażeń. W połączeniu z odpowiednim wsparciem, stanowi trzon każdej drużyny."
    },
    {
        "id": 5,
        "name": "zed",
        "role": "Assassin",
        "difficulty": "Hard",
        "image_url": "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Zed_0.jpg",
        "description": "Zed to bezlitosny zabójca cieni, który uderza z zaskoczenia i znika, zanim przeciwnik zdąży zareagować. Wykorzystuje klony cienia do zadawania kombinacji ciosów i unikania niebezpieczeństwa. Jego gra opiera się na szybkich refleksach i precyzyjnych decyzjach. W rękach wprawionego gracza potrafi samodzielnie wygrywać walki."
    },
    {
        "id": 6,
        "name": "lux",
        "role": "Mage",
        "difficulty": "Easy",
        "image_url": "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Lux_0.jpg",
        "description": "Lux to czarodziejka światła, która potrafi rozświetlić pole bitwy potężnymi promieniami. Doskonale sprawdza się w kontrolowaniu tłumu i wspieraniu drużyny z bezpiecznej odległości. Jej ultimate potrafi zaskoczyć wrogów nawet z dużej odległości. Jest świetnym wyborem dla graczy, którzy lubią czystą magię i precyzyjne rzucanie umiejętności."
    },
    {
        "id": 7,
        "name": "thresh",
        "role": "Support",
        "difficulty": "Hard",
        "image_url": "https://ddragon.leagueoflegends.com/cdn/img/champion/loading/Thresh_0.jpg",
        "description": "Thresh to upiorny strażnik, który więzi dusze swoich ofiar w latarni. Jego styl gry opiera się na umiejętnym łapaniu wrogów i chronieniu sojuszników. Potrafi całkowicie zmienić przebieg walki jednym trafionym hakiem. Wymaga dobrej komunikacji i szybkiego podejmowania decyzji, ale nagradza za odwagę i pomysłowość."
    }
]

# Create your views here.


def starting_page(request):
    return render(request, 'lol_champs/index.html')


def champions_page(request):
    return render(request, 'lol_champs/champions.html', {
        'champions': champions
    })


def single_champion_page(request, champion):
    single_champion = next(
        (champ for champ in champions if champ['name'] == champion), None)
    return render(request, 'lol_champs/champion_details.html', {
        'champion': single_champion
    })
