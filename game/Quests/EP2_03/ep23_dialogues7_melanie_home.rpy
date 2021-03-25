# Дик и Мелани у нее дома

# Дик оглядывает комнату и говорит: Мелани, у вас такое уютное гнездышко. Вы имеете отличный вкус.
label ep23_dialogues7:

    # Мелани отвечает спасибо и предлагает Дику присесть.
    # И предлагает чай, вино или виски?
    # Дик говорит что хотел бы сразу взять номер того негодяя, потому что боится что потом может забыть.
    # Что при виде Мелани у него путаются мысли и он уже не может сосредоточиться.
    # Мелани говорит что да, конечно. И спрашивает не кажется-ли Мистеру Дику что здесь очень жарко.
    # Я пойду одену что-то более легкое, вы не возражаете если я отойду?
    # Дик говорит что конечно нет.
    music stop
    sound snd_car_engine
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(t_("У МЕЛАНИ ДОМА...")) from _call_textonblack_12
    scene black_screen
    with Dissolve(1)
    music ZigZag
    img 8964
    with fade
    dick "Мелани! У Вас такое уютное гнездышко!"
    img 8965
    dick "Вы имеете отличный вкус!"
    img 8966
    melanie "Спасибо, Мистер Дик..."
    img 8967
    with fade
    w
    img 8968
    w
    img 8969
    with Dissolve(0.5)
    w

    img 8970
    with fadelong
    melanie "Присаживайтесь, Мистер Дик."
    img 8971
    melanie "Давайте я Вас чем-нибудь угощу?"
    img 8972
    with fade
    melanie "Что Вы предпочитаете? Кофе, вино или виски?"
    img 8973
    dick "Мелани, я хотел бы сразу записать номер того негодяя."
    "Я боюсь что могу забыть потом."
    img 8974
    with fade
    dick "Мелани, при виде Вас у меня путаются мысли."
    img 8975
    with Dissolve(0.5)
    "Я даже сейчас уже не могу сосредоточиться...."
    img 8976
    with fade
    melanie "Да, конечно, Мистер Дик."
    img 8977
    with fadelong
    "Аххххх..."
    "Не кажется-ли Вам что здесь очень жарко?"
    img 8978
    with fade
    "Я пойду одену что-то более легкое."
    img 8979
    "Вы не возражаете если я отойду на минутку?"
    dick "Что Вы, Мелани? Конечно я не возражаю."
    music stop
    scene black_screen
    with Dissolve(1)
    pause 1.0

    # Мелани возвращается одетая в трусики и шубку.
    # Подходит к Дику и спрашивает нравится-ли Дику ее образ? Не слишком-ли он будет смущать Мистера Дика?
    # Дик просто в шоке.
    # Он, запинаясь, говорит Мелани что его не будет смущать.
    # Мелани открывает шубку, там грудь. А так?
    # Дик в шоке.
    # О Мелани! Я прошу Вас! Можно я сделаю несколько кадров? Я всегда мечтал об этом!
    # Дик, но у Вас нет камеры.
    # У меня есть телефон! Я могу сделать кадры на него!
    # Мелани говорит что она любит фотографироваться, как Мистер Дик уже, наверное, знает.
    # Но она любит хорошее качество фото.
    music Loved_Up
    img 8980
    with fadelong
    melanie "Мистер Дик, нравится-ли Вам мой образ?"
    img 8981
    with Dissolve(0.5)
    "Не слишком-ли он будет смущать Вас?"
    img 8982
    dick "..."
    img 8983
    dick "!!!"
    img 8984
    melanie "..."
    img 8985
    with fade
    dick "Ммм... Мелани..."
    dick "Нет... Этот образ... Не будет смущать меня..."
    img 8986
    with fadelong
    with hpunch
    melanie "А так?"
    sound Jump2
    img 8987
    dick "!!!"
    img 8988
    w
    img 8989
    with fade
    dick "..."
    img 8990
    with Dissolve(0.5)
    w
    img 8991
    dick "!!!"
    dick "О, Мелани!"
    "Я прошу Вас!"
    "Можно я сделаю несколько кадров?"
    "Я всегда мечтал об этом!"
    img 8992
    with fade
    melanie "Дик, но у Вас нет камеры."
    img 8993
    with Dissolve(0.5)
    dick "У меня есть телефон! Я могу сделать кадры на него!"
    img 8994
    with fade
    melanie "Мистер Дик, я люблю фотографироваться. Вы уже, наверное, это знаете."
    "Но я люблю хорошее качество фото."

    # Дик говорит что это будут самые лучшие фотографии для него! И никто их не увидит никогда!
    # Только Дик сможет оценивать красоту и качество сделанных фото!
    # Так что неважно на какую камеру они будут сделана, для Дика они будут лучшие, потому что
    # На них будет Мелани!
    # Хорошо, Мистер Дик. Вы знаете, мне незачем стесняться своей груди, но я бы не хотела чтобы мир увидел их раньше времени.
    # Дик отвечает что клянется, никто не увидит это. Только пожалуйста, пусть она даст возможность!
    # Мелани отвечает что хорошо, только трогать нельзя.
    # Дик отвечает что все будет как Мелани скажет ему!
    img 8995
    dick "Для меня это будут самые лучшие фото!"
    "Их больше никто никогда не увидит!"
    "Только я смогу оценивать их бесконечную красоту!"
    "И неважно на какую камеру они сделаны!"
    "Они лучшие, потому что на них будете Вы, Мелани!"
    img 8996
    melanie "Хорошо, Мистер Дик. Вы знаете, мне незачем стесняться своей груди."
    "Но я бы не хотела чтобы мир увидел ее раньше времени..."
    img 8997
    dick "Мелани! Я клянусь! Никто не увидит это!"
    "Только пожалуйста, дайте мне возможность!"
    img 8998
    with fade
    melanie "Хорошо, Мистер Дик. Но трогать нельзя..."
    img 8997
    dick "Мелани! Все будет так как скажете ВЫ!"

    music stop
    scene black_screen
    with Dissolve(1)
    pause 1.0
    # Начинается фотосессия Мелани с Диком.
    # Дика почти не видно, фото чисто с Мелани.
    # Вертятся везде по дому.
    # photo
    music Molten_Alloy
    img 8999
    with fadelong
    w
    call photoshop_flash() from _call_photoshop_flash_58
    w
    img 9000
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_59
    w
    img 9001
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_60
    w
    img 9002
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_61
    w
    img 9003
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_62
    w
    img 9004
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_63
    w
    img 9005
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_64
    w
    img 9006
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_65
    w
    img 9007
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_66
    w
    img 9008
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_67
    w
    img 9009
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_68
    w
    img 9010
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_69
    w
    img 9011
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_70
    w
    img 9012
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_71
    w
    img 9013
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_72
    w
    img 9014
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_73
    w
    img 9015
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_74
    w
    img 9016
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_75
    w
    img 9017
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_76
    w
    img 9018
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_77
    w
    img 9019
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_78
    w
    img 9020
    with fade
    melanie "Мистер Дик, Вам нравится?"
    dick "Мелани, я просто без ума!"
    melanie "Идите сюда..."
    img 9021 #nophoto
    with fade
    w
    melanie "Я разрешаю сделать Вам последний кадр..."

    if richHotelRestaurantDickOffended1 == True or dickWantFuckMelanie == True:
        $ notif(t_("Дик признавался что хочет Мелани"))
        img 9022 #nophoto
        with fade
        w
        img 9023
        with Dissolve(0.8)
        w
        call photoshop_flash() from _call_photoshop_flash_79
        w

    else:
        w
        call photoshop_flash() from _call_photoshop_flash_80
        w

    #end_photo


    # Дик садится на колени перед Мелани и говорит что он восхищается ей!
    music Continue_Life
    img 9024
    with fadelong
    dick "О, Мелани!"
    img 9025
    with Dissolve(0.5)
    w
    img 9026
    with Dissolve(0.5)
    w
    img 9027
    "Я восхищаюсь ВАМИ!"
    img 9028
    with fade
    melanie "..."
    # Сцена заканчивается.
    scene black_screen
    with Dissolve(1)
    music stop
    pause 2.0
    return
