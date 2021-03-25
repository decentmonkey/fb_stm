# В следующий раз, когда Моника идет заниматься фитнесом, срабатывает диалог Моники и Барди о том что
# они едут на фитнесс. Барди улыбается.

# После занятия фитнесом, Моника выходит, говоря Барди что Бетти осталась наедине с тренером.
# Барди улыбается

# Идет сцена занятия Бетти с тренером, где он лапает ее по разному.
# Барди подсматривает и снимает на телефон.
# Далее, тренер говорит что одежда мешает ей до конца выгнуть спинку. Снимает лифчик.
# Бетти без лифчика делает упражнения.
# Ноги все еще плохо гнутся. Тренер предлагает Бетти снять одежду и с низа.
# Бетти остается голая. Говорит что ей немного не комфортно.
# Продолжают заниматься.
# Затем тренер раздевается и говорит что Бетти надо немного энергии. Для этого предлагает заняться
# медитацией (сексом)
# Вариант выбора соглашаться или сказать что она замужем.
# Если согласилась, идет секс.


# В конце Барди, в зависимости от того согласилась Бетти или нет, произносит.
# Ну все, Бетти, ты попалась! Теперь ты узнаешь кто действительно хозяин в доме!

# Конец фитнеса.
# На улице Моника ничего не говорит
# Сцена меняется на дом, Барди в своей комнате.
# Моника говорит что стоит узнать как там Барди. Спать не лечь, пока не узнает.

label ep24_dialogues3_fitness1:
# В следующий раз, когда Моника идет заниматься фитнесом, срабатывает диалог Моники и Барди о том что
# они едут на фитнесс. Барди улыбается.

    return


label ep24_dialogues3_fitness2:
# После занятия фитнесом, Моника выходит, говоря Барди что Бетти осталась наедине с тренером.
# Барди улыбается

    return

label ep24_dialogues3_fitness3:
# Идет сцена занятия Бетти с тренером, где он лапает ее по разному.
# Барди подсматривает и снимает на телефон.
# Далее, тренер говорит что одежда мешает ей до конца выгнуть спинку. Снимает лифчик.
# Бетти без лифчика делает упражнения.
# Ноги все еще плохо гнутся. Тренер предлагает Бетти снять одежду и с низа.
# Бетти остается голая. Говорит что ей немного не комфортно.
# Продолжают заниматься.
# Затем тренер раздевается и говорит что Бетти надо немного энергии. Для этого предлагает заняться
# медитацией (сексом)
# Вариант выбора соглашаться или сказать что она замужем.
# Если согласилась, идет секс.

    # Занятие 1
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
#    music Loved_Up
    music Ready_and_Waiting
    img 10142
    with fadelong
    fitness_instructor "Бетти, расслабься."
    "Здесь только мы одни..."
    betty "Хорошо, я постараюсь..."
    img 10143
    fitness_instructor "Делай вот так, выгибай ногу сильнее."
    betty "Я стараюсь..."
    img 10144
    with fade
    fitness_instructor "Я помогу тебе, надо только немного поддержать..."
    img 10145
    betty "Вот так?"
    img 10146
    with fade
    fitness_instructor "Да, тебе надо держать корпус ровнее..."
    "Я помогу тебе..."
    # кладет руку на попу
#    img 10147
#    with diss
#    sound Jump2
#    w
#    img 10149
#    w
#    call photoshop_flash() from _call_photoshop_flash_82
#    w
    img 10148
    betty "Хорошо..."

    #Барди
#    music Sneaky_Snitch
#    img 10149
#    with fade
#    bardie "Мне надо продолжать следить за Бетти."
#    bardie "Уверен, что я могу увидеть больше!"
#    #

    ######
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    img 10249
    with fadelong
    music Loved_Up
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "В следующий раз мы выполним упражнения посложнее."
    betty "Хорошо..."
    return

label ep24_dialogues3_fitness3b:
    # Занятие 2
    # рука уже на попе
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Ready_and_Waiting
    img 10150
    with fadelong
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    img 10151
    fitness_instructor "Тебе надо больше выгибать спинку, постарайся..."
    img 10152
    with fade
    betty "Я пытаюсь, у меня не получается выгнуться сильнее..."

    music Loved_Up
    img 10153
    with fadelong
    fitness_instructor "У тебя очень обтягивающая форма."
    img 10154
    fitness_instructor "Она сковывает твои движения."

    img 10155
    with fadelong
    fitness_instructor "Попробуй снять свой верх."
    img 10156
    fitness_instructor "Увидишь, тебе сразу станет свободнее двигаться."
    img 10157
    with fade
    betty "Правда?"
    "Я немного смущаюсь?"

    img 10158
    with fade
    sound Jump1
    fitness_instructor "Бетти, я всего-лишь фитнесс тренер."
    fitness_instructor "Я желаю, чтобы ты добилась результатов."
    img 10159
    fitness_instructor "Доверься мне!"
    betty "Хорошо..."

    #Снимает лифчик
    sound snd_fabric1
    img 10160
    with fade
    w
    img 10161
    with fade
    w
    img 10162
    with fade
    w
#    img 10163
#    sound Jump2
#    bardie "!!!"

    img 10164
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_83
    w

    # Занимается без лифчика
    img 10165
    with fadelong
    fitness_instructor "Вот так, Бетти!"
    img 10166
    "Чувствуешь, как тебе стало свободнее двигаться?"
    "У тебя сразу получилось прогнуть спинку, как следует!"
    img 10167
    "Ты чувствуешь?"

    img 10168
    betty "Да, я действительно выгнулась гораздо сильнее..."

#    img 10173
#    w
    img 10169
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_84
    w
    img 10170
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_85
    w
    img 10171
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_86
    w
    img 10172
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_87
    w

#    #Барди
#    music Sneaky_Snitch
#    img 10173
#    with fade
#    bardie "Мне надо продолжать следить за Бетти."
#    bardie "Уверен, что я могу увидеть больше!"

    ############
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Loved_Up
    img 10250
    with fadelong
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "В следующий раз мы выполним упражнения посложнее."
    betty "Хорошо..."
    return

label ep24_dialogues3_fitness3c:

    # Занятие 3
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Ready_and_Waiting
    img 10174
    with fade
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "Ты помнишь что без верха у тебя лучше результаты."
    img 10175
    betty "Да, помню."
    img 10174
    with fade
    fitness_instructor "Пожалуйста, сними его."
    img 10175
    betty "Хорошо."

    #Бетти снова снимает лифчик
    music Loved_Up
    sound snd_fabric1
    img 10176
    with fade
    w
#    #Барди
#    img 10177
#    bardie "!!!"
    img 10178
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_88
    w
    img 10179
    with fadelong
    fitness_instructor "Молодец."
    fitness_instructor "Теперь тяни ножку, тяни сильнее..."
    img 10180
    betty "Я не могу, мне дальше никак..."
    fitness_instructor "Тебе больно, Бетти?"
    betty "Нет, мне уже не больно..."
    "Она... Она просто не гнется дальше и все..."
    img 10181
    betty "У меня не получается!"
    with diss
    img 10182
    with fade
    fitness_instructor "Бетти, я знаю что тебе мешает..."
    fitness_instructor "Я знаю что тебе мешает добиться лучших результатов..."
    img 10181
    betty "Что же?"
    img 10183
    with fade
    fitness_instructor "Твой низ, Бетти!"
    fitness_instructor "Он слишком обтягивает тебя, сковывает твои движения!"
    img 10184
    fitness_instructor "Твои связки могут позволить тебе сделать упражнение как надо."
    fitness_instructor "Но твоя одежда не позволяет тебе сделать это."
    img 10185
    with fade
    betty "Что же делать с этим?"
    img 10186
    fitness_instructor "Ты можешь снять с себя это, Бетти."
    betty "Но я... Стесняюсь..."
    img 10187
    with fadelong
    sound Jump1
    fitness_instructor "Бетти, я твой инструктор!"
    img 10188
    fitness_instructor "Я провожу персональные занятия с тобой."
    fitness_instructor "Я делаю это бесплатно, потому что вижу в тебе потенциал!"
    img 10189
    betty "Правда? У меня есть потенциал?"
    fitness_instructor "Да, Бетти!"
    fitness_instructor "Ты прекрасна!"
    img 10190
    with fade
    fitness_instructor "Доверься мне! Я лишь хочу чтобы у тебя получалось!"
    fitness_instructor "Я хочу чтобы ты была успешной!"
    img 10191
    with fade
    betty "Хорошо, только..."
    img 10192
    with diss
    betty "Я ведь правда не толстая?"
    img 10193
    with diss
    fitness_instructor "Бетти, ты прекрасна! Тебе не стоит стесняться своего тела!"
    img 10194
    with fade
    betty "Хорошо..."
    # Бетти раздевается полностью
    music Loved_Up2
    sound snd_fabric1
    img 10195
    with fadelong
    w
    img 10196
    with Dissolve(0.5)
    w
#    img 10197
#    with fade
#    bardie "..." #Улыбается
    img 10198
    with Dissolve(0.5)
    w
    call photoshop_flash() from _call_photoshop_flash_89
    w
    img 10199
    w
    img 10200
    with diss
    w
    img 10201
    with Dissolve(0.5)
    w
    img 10202
    with Dissolve(0.5)
    w
    call photoshop_flash() from _call_photoshop_flash_90
    w
    img 10203
    with fade
    betty "Так хорошо?"
    call photoshop_flash() from _call_photoshop_flash_91
    w
    fitness_instructor "Да, Бетти. Давай продолжим."
    img 10204
    with fadelong
    #Занимается обнаженной
    fitness_instructor "Вот так, Бетти!"
    img 10205
    fitness_instructor "У тебя получается, ты чувствуешь?"
    img 10206
    with fade
    betty "Да, я правда смогла поднять ногу выше..."
    call photoshop_flash() from _call_photoshop_flash_92
    w
    img 10207
    with diss
    fitness_instructor "Отлично!"
    fitness_instructor "Ты чувствуешь себя свободной?"
    img 10208
    with diss
    betty "Да..."
    call photoshop_flash() from _call_photoshop_flash_93
    w

    img 10209
    fitness_instructor "Тебе комортно, ты больше не стесняешься меня?"
    img 10210
    betty "Да, мне очень комфортно..."

    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Loved_Up
    img 10211
    with fadelong
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "В следующий раз мы выполним упражнения посложнее."
    return

label ep24_dialogues3_fitness3d:
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 1.0
    music Ready_and_Waiting
    # Занятие 4
    img 10212
    with fadelong
    fitness_instructor "Хорошо, Бетти, молодец."
    fitness_instructor "У тебя уже лучше получается."
    fitness_instructor "Ты помнишь что одежда сковывает тебя?"
    img 10213
    betty "Да, помню..."
    img 10214
    fitness_instructor "Если ты хочешь, ты можешь снять ее."
    fitness_instructor "Тогда мы сможем достичь большего прогресса."
    img 10213
    betty "Хорошо..."
    #Снимает одежду

    sound snd_fabric1
    music Loved_Up
    img 10215
    with fade
    w
#    img 10216
#    with fade
#    w
    img 10217
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_94
    w
    img 10218
    with diss
#    sound kiss2
    w
    call photoshop_flash() from _call_photoshop_flash_95
    w
    img 10219
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_96
    w
    img 10220
    with diss
    w
    call photoshop_flash() from _call_photoshop_flash_97
    w
    img 10221
    with fade
    w
    call photoshop_flash() from _call_photoshop_flash_98
    w
    sound snd_fabric1
    img 10223
    with fade
    w
    img 10222
    with fade
    w
    img 10224
    with fade
    w
#    #Барди
#    img 10225
#    w
#    call photoshop_flash() from _call_photoshop_flash_99
#    w


    img 10226
    with fadelong
    fitness_instructor "Теперь тянись, тянись как можешь..."
    betty "..."
    img 10227
    with fade
    fitness_instructor "Вот так, хорошо..."
    fitness_instructor "Давай, ты можешь еще, я знаю."
    img 10228
    betty "Мне никак!"
    betty "Я стараюсь!"
    img 10229
    fitness_instructor "Бетти, ты слишком напряжена, ты чувствуешь это?"
    betty "Да, я чувствую..."
    fitness_instructor "Тебе надо расслабиться, Бетти."
    img 10230
    betty "Но как это сделать?"
    betty "Я волнуюсь, я хочу чтобы у меня получалось..."
    img 10231
    with fade
    fitness_instructor "Тебе нужно пройти сеанс медитации, Бетти."
    fitness_instructor "Тогда ты сможешь расслабиться и у тебя все получится."
    img 10230
    betty "Но как? Я не умею медитировать."
    img 10231
    fitness_instructor "Хочешь чтобы я показал тебе как это надо делать?"
    img 10232
    betty "Да, очень хочу..."

    # тренер встает и раздевается
    music Loved_Up2
    sound snd_fabric1
    img 10234
    with fadelong
    w
    fitness_instructor "Я буду твоим проводником, Бетти."
    img 10233
    fitness_instructor "Твоим проводником на пути к достижению душевного равновесия."
    # обнимает Бетти и лапает за попу
    img 10235
    with fade
    sound Jump1
    fitness_instructor "Я проведу тебя через весь путь."
    img 10236
    with diss
    sound Jump2
    fitness_instructor "Ты поймешь что такое настоящий Дзен..."
    call photoshop_flash() from _call_photoshop_flash_100
    w

#    img 10238
#    bardie "!!!" #довольный фоткает
    img 10236
    w
#    img 10237
#    w
#    call photoshop_flash() from _call_photoshop_flash_101
#    w

    img 10239
    with fade
    fitness_instructor "Ты хочешь этого?"
#    img 10240
#    with fade
    menu:
        "Да, я очень хочу...":
            pass
        "Я хочу, но не таким путем. Я замужем!":
            music Groove2_85
            img 10241
            with fade
            betty "Я хочу, но не таким путем. Я замужем!"
            betty "А это выглядит как измена!"
            img 10242
            fitness_instructor "..."
            img 10243
            with fade
            betty "Я оденусь и мы продолжим."
            betty "Я уверена, что смогу добиться успеха не прибегая к медитациям..."
            fitness_instructor "Хорошо, Бетти..."
            $ questHelp("house_13", False)
            $ questHelp("fitness_2", False)
            return False
    $ bettyInstructorSex1 = True

    img 10244
    with fade
    w
    img 10245
    with fade
    w
    img 10246
    with diss
    betty "Да, я очень хочу..."
    img 10247
    with fadelong
    fitness_instructor "Тогда начнем!"
    img 10248
    fitness_instructor "Расслабься и чувствуй меня!"

    #идет секс
    music stop
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_1 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_1.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_1
    show screen camera_record_screen()
    fitness_instructor "Чувствуй меня, следуй за мной!"
    betty "Да! Хорошо!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_2 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_2.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_2
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_3 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_3.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_3
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_4 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_4.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_5 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_5.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_5
    fitness_instructor "Ты чувствуешь меня?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_6 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_6.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_6
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_1.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_1_7 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_1_7.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_1_7
    wclean

    music stop
    img black_screen
    hide screen camera_record_screen
    with Dissolve(1.0)
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_1 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_1.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_1
    show screen camera_record_screen()
    with fadelong
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_2 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_2.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_2
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_3 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_3.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_3
    fitness_instructor "Ты чувствуешь как тебя заполняет энергия равновесия?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_4 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_4.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_5 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_5.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_5
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_6 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_6.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_6
    fitness_instructor "Ты чувствуешь прилив энергетических сил?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_7 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_7.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_7
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_8 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_8.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_8
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_9 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_9.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_9
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.5)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_2.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_2_10 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_2_10.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_2_10
    wclean


#############

    music stop
    img black_screen
    hide screen camera_record_screen
    with Dissolve(1.0)
    pause 1.0
    stop music
    play music "Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_1 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_1.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_1
    show screen camera_record_screen()
    with fadelong
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_2 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_2.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_2
    fitness_instructor "Ты следуешь за мной по дороге к Дзен?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_3 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_3.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_3
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_4 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_4.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_4
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_5 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_5.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_5
    fitness_instructor "Тебе нравится эта медитация?"
    betty "Да!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_6 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_6.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_6
    fitness_instructor "Очень нравится?"
    betty "Да, очень!"
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_7 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_7.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_7
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_8 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_8.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_8
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_9 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_9.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_9
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_10 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_10.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_10
    wclean
    stop music
    play music "<from " + str((rand(1,6)*1.166)) + " loop 0.0>Sounds/audio_Fitness_Instructor_Betty_Sex_3.mp3"
    scene black
    image videov_Fitness_Instructor_Betty_Sex_3_11 = Movie(play="video/v_Fitness_Instructor_Betty_Sex_3_11.mkv", fps=30)
    show videov_Fitness_Instructor_Betty_Sex_3_11
    wclean

    hide screen camera_record_screen
######
    music stop
    music Power_Bots_Loop
    call ep24_dialogues3_fitness4() from _call_ep24_dialogues3_fitness4
    music stop
    img black_screen
    with Dissolve(1.0)
    pause 2.0

    return


label ep24_dialogues3_fitness4:
    return


label ep24_dialogues3_fitness5:
    return

label ep24_dialogues3_fitness6:
    # После этого, при выходе из фитнесса Моника делает комментарий что Бетти что, продолжает трахаться
    # с тренером после того что было?
    mt "Я не понимаю..."
    "Эта Бетти что, продолжает трахаться с тренером?!"
    "После того что было?!"
    return











#
