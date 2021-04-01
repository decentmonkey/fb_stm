label gallery_1164:
#    pause 2
#    sound snd_phone2

#    secretary "Добрый день еще раз."

#    "Это секретарь Миссис Бакфетт."

#    "Вы можете поднятся."

#    "Она в своем кабинете ожидает вас."

#    $ entranceMonkeys = False

    music casualMusic
    pause 2
    sound snd_phone1
    pause 2
    sound snd_phone2

    img 1155
    steve "Да, Моника.
    Я тебя слушаю."

    img 1156
    m "Моника? Слушаю????"

    "ЭТО Я ТЕБЯ СЛУШАЮ, СТИВ!!!"

    "Мы с тобой договаривались об аренде!"

    "Секретарь сказала что платежа так и нет."

    "ГДЕ ОН???"

    steve "Моника."

    "Я все сделал как мы договаривались."

    "Может быть это банк задерживает?"

    sound snd_lift
    pause 4
#    $ renpy.pause(4, hard=True)
    sound highheels_run1
#    $ renpy.pause(2, hard=True)
    wc
    img 1159
    with fadelong

    m "Банк задерживает?"

    "Да, такое бывает."

    "Если денег завтра не будет, то я съезжу в банк проверю сама."

    steve "Конечно, Моника."

    "Ты можешь проверить."

    "Я тебя никогда не обманывал."

    img 1157
    m "Ты?"

    "Никогда не обманывал?"

    img 1158
    "ДА Я ЗНАЮ ТЕБЯ ОЧЕНЬ ХОРОШО!!!"

    menu:
        "Обозвать Стива.":
#            $ steveOffended1 = True
#            call bitch(2, "steve_offended1") from _call_bitch_38
            img 1160
            with fade
            m "ТЫ!!"

            "МЕШОК С ДЕРЬМОМ!!!"
            img 1161
            sound snd_gulp
            model1 "(испуганно сглатывает)"

            img 1162
            sound snd_gulp
            model2 "(испуганно сглатывает)"

        "Выразиться мягче.":
            m "Ты!
            Обманщик!"

    img 1163
    m "ТАК ЧТО НЕ ДУМАЙ ЧТО Я НЕ ПРОВЕРЮ!!!"

    "Разговор закончен."

    img 1164
    "НА СЕГОДНЯ!!!"

    img 1165
    with fade
    music All_Stars_Loop
    m "Так."

    "А это у нас еще кто?"

    menu:
        "Обозвать их мартышками.":
#            call bitch(2, "monkeys_offend1") from _call_bitch_39
#            $ monkeysOffended1 = True
            "А, это те две мартышки, которые стояли внизу?"
            img 1166
            sound snd_gulp
            model1 "(испуганно сглатывает)"

            img 1167
            sound snd_gulp
            model2 "(испуганно сглатывает)"

            img 1168
            m "И вы считаете что можете быть моделями?"

        "Начать разговор.":
#            $ monkeysOffended1 = False
            if entranceTalkedWithMonkeys == False:
#                call bitch(-1, "monkeys_offend1") from _call_bitch_40
                m "Я никогда вас не видела."
            else:
#                call bitch(-8, "monkeys_offend1") from _call_bitch_41
                m "Я видела вас внизу, вы мне нагрубили"
                img 1166
                sound snd_gulp
                model1 "(испуганно сглатывает)"

                img 1167
                sound snd_gulp
                model2 "(испуганно сглатывает)"
                m "Но я не держу обиды.
                Вы не знали с кем разговариваете."

            img 1168
            m "Итак, вы считаете что можете быть моделями?"



    img 1169
    model1 "Мэм."

    "Вообще-то да."

    "Мы хотим попробовать."

    model2 "Нам очень нужна работа."

    "Мы будем стараться."

    m "Хорошо."

    "Встаньте обе передо мной!"

    "И покажите что из себя представляете."

    img 1170
    model1 "Мэм..."

    "Вы собираетесь проводить кастинг с нами обеими одновременно?"

    model2 "Мэм."

    "Может быть есть возможность провести его по отдельности?"

    if monkeysOffended1 == True:
        m "У меня нет времени возиться с вами по отдельности."
    else:
        m "Ничего страшного, не стесняйтесь."

    m "Итак."

    m "Покажите что умеете."

    "Принимайте разные позы."

    "Привлеките внимание."

    model1 "Хорошо, Мэм."
    model2 "Хорошо, Мэм."

    img 1171
    w
    img 1172
    w
    img 1173
    w
    img 1174
    w
    img 1175
    w
    img 1176
    w
    img 1177
    w
    img 1178
    w
    img 1179
    w
    img 1180
    w
    img 1181
    w
    img 1182

    music casualMusic

    m "Стоп."

    "Стоп. Стоп."

    img 1183
    "Это никуда не годится."

    "Не вижу никакого эффекта."


#    $ subst_to_object("Teleport_Monica_Office_Secretary", "monica_office_monkey_exit_blocked")
#    $ monicaMonkeysStage = 1
#    $ monicaOfficeCabinetMonkeys = True
#    $ scene_transition = "Fade"
#    call refresh_scene() from _call_refresh_scene_13
#    return

#label monkeys_monica_office1_3:
    menu:
        "Они никуда не годятся, но я продолжу издеваться над ними.":
#            $ monkeysOffended2 = True
#            call bitch(2, "monkeys_offend2") from _call_bitch_42
            pass

        "Выгнать их":
            jump gallery_monkeys_monica_office1_get_out

    if monkeysOffended1 == True:
        "Возможно дело в ваших обносках."
    else:
        "Возможно дело в ваших вещах, что на вас одеты."

    "Снимите одежду."

    "До белья."

    model1 "Хорошо, Мэм."
    model2 "Хорошо, Мэм."

    sound snd_fabric1
    music All_Stars_Loop

    img 1184
    with fadelong

    img 1186
    w
    img 1187
    w
    img 1188
    w
    img 1185
    m "Обернитесь."

    img 1189
    w
    img 1190
    w
    img 1191
    w
    img 1192
    m "Хорошо."

    "Начинайте."

    img 1193
    w
    img 1194
    w
    img 1195
    w
    img 1196
    w
    img 1197

    m "Стоп."
    music:casualMusic

    img 1198
    w
    img 1199
    mt "Ну что это за убожество?"

    "Надо будет еще раз высказать секретарше неудовольствие по поводу тех кого она ко мне посылает."

    "Ну что это такое?"

    "Какие из них модели?"

    "Я бы таких даже уборщицами не взяла."

    "Вот такие люди."

    "Все пытаются куда-то подняться."
    "Чего-то добиться."

    "А сами они кто?"

    "Как они могут сравнивать себя с такими как Я?"

    "У каждого свое место в жизни."

    img 1200
    "Я богатая. Красивая."

    if monkeysOffended1 == True:
        "А они жалкие ничтожества."
    else:
        "А они маленькие людишки."

    "Корчатся сейчас передо мной.
    На что-то надеются."

    "Пора их выгнать."

    "Надо решить."

    if entranceTalkedWithMonkeys == True:
        mt "Хотя стой.
        Они же мне что-то сказали там внизу."

        "Хм.
        Неважно что они там говорили."

        "Важно то что сейчас они подчиняются мне."

        "Будут делать все что я скажу."

        "Потому что Я сверху, а они - снизу."

        img 1201
        "Мне нравится это использовать :)"

    music casualMusic
#    $ subst_to_object("Teleport_Monica_Office_Secretary", "monica_office_monkey_exit_blocked")
#    $ monicaMonkeysStage = 2
#    $ monicaOfficeCabinetMonkeysSuffix = "2"
#    $ monicaOfficeCabinetMonkeys = True
#    $ scene_transition = "Fade"
#    call refresh_scene() from _call_refresh_scene_14
#    return

#label monkeys_monica_office1_4:

    menu:
        "Заставить их полностью раздеться. Ха-ха!!!":
#            $ monkeysOffended3 = True
#            call bitch(8, "monkeys_offend3") from _call_bitch_43
            pass
        "Выгнать их":
            jump gallery_monkeys_monica_office1_get_out

    m "Девочки!"
    label gallery_1228:
    music casualMusic
    img 1198
    model1 "Да, Мэм."
    model2 "Да, Мэм."

    m "Вы знаете.
    Что-то в вас есть."

    "Для того чтобы все получилось, вам надо продолжать."

    model1 "Мэм, но что продолжать?"

    "Мы стараемся изо всех сил!"

    m "Все просто."

    "Снимите одежду."

    model2 "Мэм, но у нас и так снята одежда."

    m "Неужели?"

    "Раздевайтесь полностью."

    img 1202
    model1 "Мэм, но зачем..."
    model2 "Мэм, мы стесняемся..."

    img 1203
    m "Если вы не готовы раздеться, значит вы не готовы получить работу."

    "Мне надо увидеть полностью своих моделей."

    "Оценить их."

    "У меня ответственная работа."

    "Я возглавляю очень популярный журнал.
    С хорошей репутацией."

    "Мы профессионалы, поэтому требуется неукоснительно соблюдать качество."

    "Если вы готовы стать профессионалами, то должны делать все что я скажу..."

    img 1204
    "ИЛИ МОЖЕТЕ УХОДИТЬ!"

    img 1205
    w
    img 1206
    music RocknRoll_loop
    w
    img 1207
    w
    img 1208
    w
    img 1209
    w
    img 1210
    w
    img 1211
    m "Встать сюда."

    img 1212
    w
    img 1213
    w
    img 1214
    w
    img 1215
    w
    img 1216

    m "Встаньте спиной."

    img 1217
    w
    img 1218
    w
    img 1219
    w
    img 1220
    m "Нагнитесь сильнее."

    img 1221
    w
    img 1222
    w
    img 1223
    w
    img 1224
    m "Не поняла!"

    "Я, кажется, приказала раздеться."

    "Что это на тебе болтается?"

    "Что ты там прячешь??!"

    "Я должна знать моделей досконально!
    Вам нечего скрывать от меня!"

    "И положи руки на свой зад, как это сделала твоя подруга!"

    img 1225
    w
    img 1226
    w
    img 1227

    m "На четвереньки задом ко мне!"

    img 1228
    mt "Хорошо что моя секретарь не видит этого."

    "Ее высокоморальная душа не выдержала бы этого."

    "Но что поделать.
    Надо воспитывать таких как эти..."

    "Хи-хи."

    img 1229
    w
    img 1230
    w
    img 1231
    w
    img 1232
    w
    img 1235
    w
    img 1236
    w
    img 1237
    w
    img 1238
    w
    img 1239
    w
    img 1240
    w
    img 1241
    w
    img 1242
    w
    img 1243
    w
    img 1245
    w
    img 1246
    w

    mt "..."

    mt "Так, пора заканчивать этот цирк."

#
    img 1247
    music casualMusic
    m "ТАК СТОП."

    "СТОП. СТОП!"

    "Вставайте и одевайтесь!"

    sound snd_fabric1
    img 1248
    with fadelong
    model1 "Мэм, мы приняты?"

    img 1249
    m "Вы не подходите."

    "Можете уходить."

    img 1250
    model1 "Мэм, но как?"
    model2 "Мы думали мы Вам подходим?"

    "Все что мы здесь сейчас делали..."

    img 1251
    m "Вы проходили кастинг."

    "Вы его завалили."

    "До свидания."

    img 1252
    model1 "Мэм, но пожалуйста!"

    "Дайте нам шанс!"

    "Проведите с нами фотосессию, хотя бы одну!"

    model2 "Вы не должны так просто нас выгнать!"

#    $ subst_to_object("Teleport_Monica_Office_Secretary", "monica_office_monkey_exit_blocked")
#    $ monicaMonkeysStage = 3
#    $ monicaOfficeCabinetMonkeysSuffix = "1"
#    $ monicaOfficeCabinetMonkeys = True
#    $ scene_transition = "Fade"
#    call refresh_scene()
#    return

#label monkeys_monica_office1_5:

    img 1253
    m "Не должна так просто вас выгнать?"

    "Хорошо."

    "Кто вы?"

    "Откуда?"

    img 1254
    m "И почему я не должна вас выгнать?"

    img 1255
    model1 "У меня нет родителей.
    И никто мне не помогает."

    "Я учусь.
    Мне надо платить деньги за учебу."

    "Завтра последний день!"

    "Мне надо заработать хоть что-нибудь!"

    img 1256
    model2 "Я приехала издалека."

    "У меня нет денег."

    "И мне уже сегодня нечего есть."

    img 1257
    m "О Боже!"

    "Нечего есть..."

    "Нечем платить...."

    "Это все глупые аргументы, не достойные обсуждения в обществе, к которому я принадлежу."

    "Это принято обсуждать в ваших кругах."

    "Бедняков и неудачников."

    img 1258
    m "Вот вы хотите устроиться на работу."

    "А у вас проблемы."

    "Не знаю понимаете-ли вы или нет, но мне не нужны на работе люди с проблемами."

    "Независимо от вашего вида."

    "Если есть проблемы, значит нет работы."

    img 1259
    "Да и ваш вид."

    "Ну посмотрите на себя!"

    "Как вы с такими формами вообще могли придти на кастинг?"

    menu:
        "Показать им как выглядят настоящие модели.":
            m "..."

        "Прогнать их сейчас же!":
            jump gallery_monkeys_monica_office1_get_out_now


    img 1260
    "Знаете что?"

    "Я добрый человек."

    "Я дам вам кое-какие знания на будущее."

    "Я покажу вам как выглядят и ведут себя настоящие модели."

    img 1261
    "Идите в студию."

    jump monkeys_monica_photostudio1


label gallery_monkeys_monica_office1_get_out:

    if monicaMonkeysStageDropFlag == False:
        if monkeysOffended1 == True:
#            call bitch(2, "monkeys_offend_getout_1") from _call_bitch_44
            m "Знаете что, мартышки?!
            Вы мне не подходите!"
        else:
#            call bitch(1, "monkeys_offend_getout_1") from _call_bitch_45
            m "Нет, извините, но вы мне точно не подходите!"
    if monicaMonkeysStage == 2 and monicaMonkeysStageDropFlag == False:
        m "Одевайтесь."
        sound snd_fabric1
#        $ monicaMonkeysStageDropFlag = True
#        $ monicaOfficeCabinetMonkeysSuffix = "1"
#        $ scene_transition = "Fade_long"
#        $ autorun_to_object("monica_office_cabinet_table", "monkeys_monica_office1_get_out")
#        call refresh_scene() from _call_refresh_scene_15
#        return

    menu:
        "Показать им как выглядят настоящие модели.":
            m "Знаете что?"

            "Я добрый человек."

            "Я дам вам кое-какие знания на будущее."

            "Я покажу вам как выглядят и ведут себя настоящие модели."

            "Идите в студию."
            jump gallery_monkeys_monica_photostudio1

        "Прогнать их сейчас же!":
            jump gallery_monkeys_monica_office1_get_out_now
    return

label gallery_monkeys_monica_office1_get_out_now:

    if monkeysOffended1 == True:
#        call bitch(1, "monkeys_offend_getout_1") from _call_bitch_46
        m "Убирайтесь вон, сейчас же!"
    else:
        m "Пожалуйста, покиньте мой офис!
        У меня и так много работы!"

#    $ monicaOfficeDickIncomingCallPlanned = True
#    $ autorun_to_object("monica_office_cabinet_table", "dickIncomingCallDay1")
    sound highheels_run1
#    $ subst_to_object("Teleport_Monica_Office_Secretary", False)
#    $ monicaMonkeysStage = 3
#    $ monicaOfficeCabinetMonkeysSuffix = "1"
#    $ monicaOfficeCabinetMonkeys = False
#    $ photoStudioOpened = True
#    $ photostudioEmpty = True
#    $ scene_transition = "Fade_long"
#    $ add_objective("go_work", _("Продолжить работать"), c_green, 20)
#    $ autorun_to_object("monica_office_photostudio", "monica_office_photostudio_autorun_monica_day_1")
#    call refresh_scene() from _call_refresh_scene_16
#    return


label gallery_monkeys_monica_photostudio1:
#    music casualMusic
#    $ melaniePhotoShotProcessed = True

#    show screen notify(_("Кастинг модели убежали в фотостудию..."))
#    $ photoStudioOpened = True
    sound highheels_run1
#    music casualMusic
#    $ subst_to_object("Teleport_Monica_Office_Secretary", False)
#    $ monicaMonkeysStage = 3
#    $ monicaOfficeCabinetMonkeysSuffix = "1"
#    $ monicaOfficeCabinetMonkeys = False
#    $ photoStudioOpened = True
#    $ scene_transition = "Fade_long"
#    $ add_objective("go_photostudio", _("Идти в фотостудию"), c_green, 20)
#    $ autorun_to_object("monica_office_photostudio", "monica_office_photostudio_autorun_monica_day_1")
#    call refresh_scene() from _call_refresh_scene_17
#    return

    label gallery_1272:
#    $ remove_objective("go_photostudio")
#    $ monkeysSeenMelanie = True

    music ZigZag

    img 1262
    img 1263
    alex_photograph "Добрый день, Мэм!"
    img 1264

    melanie "Здравствуйте, Миссис Бакфетт!
    Вы сегодня отлично выглядите!"

    img 1265
    m "Спасибо, Мелани.
    Ты, в целом тоже ничего."

    "Хотя до меня тебе, конечно, далеко."

    img 1266
    melanie "Мэм, конечно!"

    "Вы просто идеал красоты!"

    img 1267
    "Вы так хорошо смотритесь на обложке нового журнала!"

    img 1268
    "Вам завидуют все модели!"

    img 1269
    m "Еще бы."

    "Но к делу."

    img 1270
    "Алекс, Мелани.
    Покажите этим двум школьницам как снимаются настоящие фотомодели."

    img 1271
    alex_photograph "Конечно, Мэм!
    Мы как раз проводим фотосессию!"

    "Мелани, ты готова?"

    img 1272
    melanie "Конечно, Алекс!"

    img 1273
    alex_photograph "Тогда начинаем!"

    music Molten_Alloy
    "Мотор!"

    img black_screen
    with Dissolve(1.0)

    img 1274
    call photoshop_flash()
    w
    img 1275
    call photoshop_flash()
    w
    img 1276
    call photoshop_flash()
    w
    img 1277
    call photoshop_flash()
    w
    img 1278
    call photoshop_flash()
    w
    img 1279
    call photoshop_flash()
    w
    img 1280
    call photoshop_flash()
    w
    img 1281
    call photoshop_flash()
    w
    img 1282
    call photoshop_flash()
    w
    img 1283
    call photoshop_flash()
    w
    img 1284
    w
    img 1285
    call photoshop_flash()
    w
    img 1286
    call photoshop_flash()
    w
    img 1287
    call photoshop_flash()
    w
    img 1288
    call photoshop_flash()
    w
    img 1289
    call photoshop_flash()
    w
    img 1290
    call photoshop_flash()
    w
    img 1291
    call photoshop_flash()
    w
    img 1292
    call photoshop_flash()
    w
    img 1293
    call photoshop_flash()
    w
    img 1294
    call photoshop_flash()
    w
    img 1295
    call photoshop_flash()
    w
    img 1296
    w
    img 1297
    call photoshop_flash()
    w
    img 1298
    call photoshop_flash()
    w
    img 1299
    call photoshop_flash()
    w
    img 1300
    call photoshop_flash()
    w
    img 1301
    call photoshop_flash()
    w
    img 1302
    call photoshop_flash()
    w
    img 1303
    w
    img 1304
    call photoshop_flash()
    w
    img 1305
    w
    img 1306

    m "Довольно"


    music casualMusic
    img 1307
    melanie "Мэм, вам понравилось?"

    menu:
        "Сделать Мелани замечание.":
#            $ melanieOffended1 = True
#            call bitch(2, "melanie_offended1") from _call_bitch_47
            img 1308
            m "В целом неплохо, Мелани."

            "Я смотрю ты поправилась немного."

            "Следи за собой, пожалуйста."

            "На твое место много желающих."

            img 1309

            melanie "Конечно, Мэм!"

            "Я буду стараться лучше!"

        "Сказать что понравилось.":
#            $ melanieOffended1 = False
#            call bitch(-2, "melanie_offended1") from _call_bitch_48
            img 1308
            m "Ты молодец, Мелани.
            Ты выглядишь просто потрясающе!"

            img 1309
            melanie "Спасибо, Мэм!
            Мне очень приятно!"

    img 1310
    m "Алекс."
    img 1311
    alex_photograph "Да, Мэм!"

    img 1310
    alex_photograph "В целом ты неплохо работаешь, но..."

    img 1311
    alex_photograph "Да, Мэм?"

    img 1310
    m "Я уже упоминала тебе как-то про это."

    "Ты берешь слишком откровенные и эротичные кадры."

    "У них, конечно, есть своя аудитория."

    "Но у нас приличный журнал.
    И некоторые ракурсы выглядят неподобающе."

    menu:
        "Сказать что он будет уволен если ослушается":
#            call bitch(2, "alexphotograph_offended1") from _call_bitch_49
#            $ alexPhotographOffended1 = True
            img 1312
            m "Если ты, все-же, не перестанешь этого делать, то лишишся работы."

            "Ты меня понял, Алекс?"

            img 1311
            alex_photograph "Да, Мэм!"
            "Я Вас понял!"

            img 1312
            m "И?"

            img 1311
            alex_photograph "Такого больше не повторится, Мэм!"

            "Я клянусь!
            Все будет так как скажет мой Босс!"

            img 1312
            m "А кто Босс?"

            img 1313
            alex_photograph "Конечно Вы, Мэм!"


        "Попросить его войти в мое положение.":
#            call bitch(-2, "alexphotograph_offended1") from _call_bitch_50
#            $ alexPhotographOffended1 = False
            m "Алекс, я знаю что ты лучший фотограф, которого я только могу найти."
            "Но, пожалуйста, войди в мое положение
            На кону репутация журнала."
            img 1311
            alex_photograph "Мэм, я обещаю что исправлюсь!"

            "Больше никаких откровенных ракурсов."

    img 1314
    m "Хорошо.
    Вы свободны."

#    $ melanieAlexBeforePhotoshoot = False
#    $ melanieAlexAfterPhotoshoot = True

    img 1315
    with fadelong
    m "Ну что, вы все поняли?"

    img 1316
    model1 "Да, нам все понятно."

    model2 "Мэм, но может все-таки?"

    menu:
        "Я СКАЗАЛА БЫСТРО ВОН ОТСЮДА! МАЛЯВКИ!!!":
#            $ monkeysOffended4 = True
#            call bitch(2, "monkeys_offend4") from _call_bitch_51

            img 1317
            m "ТАК."

            "БЫСТРО ВОН ОТСЮДА!"

            "МОЕ ТЕРПЕНИЕ ЗАКОНЧИЛОСЬ!"

            "ВОН!!!!"


        "Мое решение окончательно. Мне очень жаль что так вышло.":
#            $ monkeysOffended4 = True
#            call bitch(-2, "monkeys_offend4") from _call_bitch_52
            img 1315
            "Мое решение окончательно.
            Мне очень жаль что так вышло."
            img 1316
            model1 "Да, Мэм.
            Мы понимаем.
            До свидания."

#    $ monicaOfficeDickIncomingCallPlanned = True
#    $ autorun_to_object("monica_office_cabinet_table", "dickIncomingCallDay1")
    sound highheels_run1
#    $ add_objective("go_work", _("Продолжить работать в своем офисе"), c_green, 20)
#    $ scene_transition = "Fade_long"
#    call refresh_scene() from _call_refresh_scene_18
    return

label gallery_1837:
    music RnB4_100
    img 1835
    with fadelong
    secretary "Миссис Бакфетт."

    "Пожалуйста, Ваш чай."

    img 1836
    m "Спасибо, моя дорогая."

    img 1837
    secretary "У Вас сегодня было много дел?"

    img 1838
    m "Да."

    "Ты не представляешь какие люди меня окружают."

    "Вокруг все лжецы и обманщики."

    img 1839
    secretary "..."

    img 1840
    m "Я была сегодня у Стива."
    "Представляешь, у него там работают девушки, которые явно не соответствуют занимаемым должностям."
    "Я определенно уверена в том каким способом они получили эти должности."

    img 1841
    secretary "Ох, Миссис Бакфетт."

    "Я ничуть не удивлена."

    "В наше время старые моральные ценности почти ничего не значат."

    "Я всю жизнь прожила следуя строгим моральным принципам."

    "И проживу оставшуюся так же."

    "Я добилась своей должности работая день и ночь."

    "Без устали."

    img 1842
    "Я бы никогда не позволила себе переступить моральную черту."

    "И получить должность за счет близости с чужим мужчиной."

    img 1843
    "..."

    "....."

    img 1844
    "Я бы никогда и ни за что не разделась ни перед кем."

    img 1845
    with dissolve
    "Если честно, Миссис Бакфетт."
    "Я даже осуждаю то что происходит у нас в студии."

    img 1846
    "Этот Алекс."

    "Ваш фотограф."

    "У меня такое чувство, что его интересует не тонкая женская красота."

    "А интересуют интимные места и позы."

    "Дай ему волю, он бы превратил наш журнал в порнографический."

    img 1847
    m "Да, моя дорогая."

    "Я знаю."

    if alexPhotographOffended1 == True:

        "Я вчера сделала ему замечание."

        "Если еще раз заметишь что-то подобное, то скажи мне."

        img 1848
        "Я сразу уволю его."
    else:
        m "Дорогая, это лучший фотограф, которого можно найти за деньги."
        "Однако он пообещал мне что будет внимательнее следить за своим поведением."
        "Так что приглядывай за ним."

    img 1849
    secretary "Хорошо, Миссис Бакфетт."

    "Я прослежу за ним."

    img 1850
    m "Спасибо, моя дорогая."

    "Без тебя я бы не справилась с нашей компанией."

    img 1851
    secretary "Миссис Бакфетт."

    img 1852
    "Я всегда буду Вам верна."

    img 1853
    m "Спасибо, моя дорогая."

    "А я обещаю тебе что мы никогда не скатимся во что-то неприличное."

    "Хотя, ты знаешь."

    "Сейчас весь мир скатывается в непотребство."

    img 1854
    "Но мы будем держать свой курс!"

    img 1855
    secretary "Спасибо, Миссис Бакфетт!"

    "Я бы не смогла работать в компании, где не ценят высокую мораль!"

    img 1856
    m "Вкусный чай."

    "Спасибо!"

    secretary "Всегда пожалуйста, Миссис Бакфетт!"

    m "Хорошо, можешь идти."

    "Мне надо позвонить Дику."

    secretary "..."

    img 1858
    with fadelong
    m "..."

    music Stealth_Groover
    "Так, а где мой телефон?"

    img 1859
    "Здесь его нет."

    img 1860
    "И здесь тоже."

    "..."

    "Хм..."

    img 1861
    "Куда я его дела?"

    "..."

    "Моя дорогая, я куда-то дела свой телефон."

    "Может я выронила его где-то здесь."

    "Поищи, пожалуйста!"

    music Jazz_club1_130
    img 1862
    secretary "Да, Миссис Бакфетт!"

    "Я его найду!!"

#    menu:
#        "Искать телефон.":
#            pass
#        "Показать подсказку.":
#            img help1_16
#            with fadelong
#            help "Телефон на полу при входе в офис..."

#    call question_helper_enable("question_office_tea_lost_phone") from _call_question_helper_enable_7
#    $ monicaOfficeDay2TeaPlanned = False
#    $ remove_objective("tea_with_secretary")
#    $ add_objective("find_phone", _("Найти телефон!"), c_orange, 20)

#    sound highheels_run1
#    show screen notify(_("Секретарша убежала искать телефон..."))

#    $ monicaOfficeDay2PhoneLost = True
#    $ autorun_to_object("monica_office_secretary", "monica_office_tea_secretary_searching_phone")
#    call refresh_scene_fade() from _call_refresh_scene_fade_204
    return

label gallery_2831:
    music Groove2_85
#    if dickOfficeSecretaryTalkedFlag1 == False:
#        $ dickOfficeSecretaryTalkedFlag1 = True
    img 2829
    with fadelong
    dick_secretary "Здравстуйте, Мэм!"
    "Куда это Вы собрались?"
    img 2830
    m "В смысле куда я собралась?"
    "Я иду к Дику!"
    img 2831
    dick_secretary "Мэм."
    "Как Ваше имя?"
    img 2832
    with fade
    w
    img 2833
    with fade
    w
    img 2834
    with fade
    w
    img 2835
    with fade
    w
    img 2836
    with fade
    w
    img 2837
    with fade
    w
    img 2838
    with fade
    w
    img 2839
    with fade
    w
    img 2840
    with fade
    w
    img 2841
    with fade
    m "Меня зовут Моника Бакфетт!"
    "И ты, дорогуша, должна бы знать это!"
    "Твоя предшественница знала это прекрасно!"
    img 2842
    "И, не знаю куда она делась, но если ты не хочешь последовать за ней, то лучше запомни меня!"
    img 2843
    dick_secretary "Мэм."
    "Я сейчас проверю в списке встреч и сообщу Вам о результате."
    img 2844
    m "Что за бюрократия?"
    "Ну проверяй!"
    img 2845
    m "..."
    dick_secretary "..."
    img 2846
    m "..."
    dick_secretary "..."
    img 2847
    music Power_Bots_Loop
    dick_secretary "Мэм."
    "Вас нет в списке людей, с которыми у Мистера Дика назначена встреча."
    m "И что это значит?"
    dick_secretary "Вы не можете пройти, Мэм."
    img 2848
    m "Ты соображаешь что говоришь?"
    "Что это за список?"
    "Я не его деловой партнер, а его друг!"
    "Очень даже близкий!"
    "Даже более чем!"
    img 2849
    music Groove2_85
    dick_secretary "Хм.."
    "Мэм."
    "Насколько знаю, у Мистера Дика уже есть близкий друг."
    img 2850
    mt "Это она имеет ввиду себя что-ли?"
    "Очередная дешевая давалка!"
    img 2852
    dick_secretary "Мэм."
    "Хорошо."
    "Я сейчас проверю список друзей Мистера Дика."
    img 2851
    m "Давай! Смотри быстрее!"
    img 2853
    dick_secretary "..."
    m "..."
    img 2854
    dick_secretary "..."
    m "..."
    img 2855
    music Power_Bots_Loop
    dick_secretary "Мэм."
    "Вы не числитесь среди друзей Мистера Дика."
    "Мне очень жаль."
    img 2856
    m "ЧТО???"
    "Да как ты смеешь!"
    "Малявка!"
    "Быстро пусти меня к Дику!"
    "Или я сама туда зайду, БЕЗ ТВОЕГО РАЗРЕШЕНИЯ!"
    img 2857
    music Groove2_85
    dick_secretary "Мэм."
    "В любом случае Мистера Дика сейчас нет."
    "Он уехал по каким-то важным делам."
    img 2858
    m "По каким это?"
    img 2859
    dick_secretary "Я не знаю, Мэм."
    "Дела Мистера Дика очень серьезные и приватные и никого не касаются."
    img 2860
    mt "Знаю я какие у него обычно серьезные дела..."
    img 2861
    "Свяжитесь с Мистером Диком и передайте что его ждет Моника Бакфетт."
    img 2862
    dick_secretary "Мэм."
    "Мистер Дик просил его не беспокоить."
    "Я не буду нарушать его приказ."
    img 2863
    m "Что значит нарушать?"
    "Мы с ним друзья, он будет рад тому что я здесь."
    img 2864
    dick_secretary "Мэм."
    "Если вы друзья, то может быть вы сами позвоните ему?"
    img 2865
    music Power_Bots_Loop
    mt "ЧЕРТ!"
    mt "Я НЕ ПОМНЮ ЕГО НОМЕР! ОН БЫЛ В ТЕЛЕФОНЕ!"
    "А если я начну его спрашивать у этой дуры, то она точно его не даст."
    img 2866
    music Groove2_85
    m "Скажите, Мистер Дик когда вернется?"
    img 2867
    dick_secretary "Я точно не знаю, Мэм."
    "Вы можете подождать."
    img 2868
    m "Хорошо, я подожду в его кабинете."
    img 2869
    dick_secretary "Это исключено, Мэм."
    "Туда имеет доступ только Мистер Дик."
    img 2870
    m "А где мне тогда ждать?"
    img 2871
    dick_secretary "Вы можете присесть где Вам будет удобно, Мэм."
    img 2872
    m "Хорошо, я подожду его."

#    $ dickOfficeSecretaryMonicaStage = 1
#    $ remove_objective("dick_search")
#    $ add_objective("wait_dick", _("Дождаться Дика"), c_orange, 5)
#    $ add_objective("wait_dick_chair", _("Подождать Дика в удобном кресле"), c_green, 6)
#    $ autorun_to_object("dick_office_hall1", "afterJail_Day2_DickOffice_Secretary_dialogue3")
#    call refresh_scene_fade() from _call_refresh_scene_fade_147
    return

label gallery_3064:
    music Groove2_85
    sound highheels_run1
    img 3057
    with fadelong
    mt "Долбаные каблуки!"
    "Мне жмут!"

    img 3058
    with fade
    w
    img 3059
    with fade
    w
    img 3060
    with fade
    w
    img 3061
    with fade
    m "Здравстуйте, Мэм!"

    img 3062
    with fade
    w
    img 3063
    with fade
    m "Я пришла к Дику."

    img 3064
    with fade
    w
    img 3065
    with fade
    m "Надеюсь он у себя, наконец-то!!!"

    img 3066
    with fade
    sound snd_woman_laugh
    w

    img 3067
    sound snd_woman_laugh2
    w

    img 3068
    with fade
    m "?????"

    img 3069
    w
    img 3070
    dick_secretary "Прошу прощения..."
    "Напомните кто вы Мистеру Дику?"
    img 3071
    m "Я его близкий друг!"
    "Даже больше!"
    img 3072
    dick_secretary "У Мистера Дика есть такие друзья?"
    music Pyro_Flow
    img 3073
    m "Не ваше дело какие у него друзья!"
    "Я пришла к нему!"
    "Впустите меня немедленно!"
    img 3074
    dick_secretary "Прошу прощения, но я вынуждена отказать в посещении Мистера Дика."
    "Он доверяет мне первоначальную фильтрацию посетителей."
    img 3075
    "И я считаю вам не следует его беспокоить."
    img 3076
    with fadelong
    m "Я НЕ СОБИРАЮСЬ СЛУШАТЬСЯ ТВОИХ РЕШЕНИЙ!"
    "ТЫ!!!"
    "СТЕРВА!!!"
    img 3077
    with fadelong
    m "..."
    img 3078
    "ДИК!!!"
    "ДИК, ТЫ ТАМ???"

#    $ subst_to_object("Teleport_Hall", "dickAfterJail_secretary_dialogue2a")

#    call change_scene("dick_office_secretary") from _call_change_scene_259
#    return

#label dickAfterJail_secretary_dialogue2:
    sound highheels_run2
    img 3079
    with fadelong
    mt "Мне плевать что эта сучка говорит."
    "Я силой ворвусь к нему!"
    img 3080
    with fade
    dick_secretary "СТОЙТЕ!!!"
    "ВАМ НЕЛЬЗЯ ТУДА!!!"

#    $ remove_objective("go_dick")
#    $ autorun_to_object("dick_office_cabinet", "dickAfterJail_secretary_dialogue2b")
#    $ subst_to_object("Teleport_Hall", False)
#    call change_scene("dick_office_cabinet") from _call_change_scene_260
    return

label gallery_3085:
    music Groove2_85
    img 3081
    with fadelong
    dick "Моника!!!"
    "Здравствуй!"
    "Какая встреча!"

    sound highheels_run1
    img black_screen
    with Dissolve(1)
    $ renpy.pause(1.0)
    music Power_Bots_Loop
    img 3082
    with fadelong
    dick_secretary "Мистер Дик!"
    img 3083
    "К Вам вломилась какая-то проститутка!"
    img 3084
    "Я ее не пускала, но она!.."
#    $ dickOfficeCabinetStage = 1
#    call refresh_scene_fade() from _call_refresh_scene_fade_172
#    return

#label dickAfterJail_secretary_dialogue4:
    img 3085
    with fadelong
    m "КТО Я????"
    img 3086
    with hpunch
    m "АХ ТЫ ТВАРЬ!!!"
    img 3087
    music Groove2_85
    dick "Успокойтесь, девочки."
    "Все хорошо."
    "Это Моника, мой хороший друг."
    img 3088
    "Пусть она останется."
    "Я рад ее видеть."

#    img 3090
    # render
    # секретарша уходит из кабинета не показывая жопу!
    dick_secretary "Хорошо, Мистер Дик."

#    img 3089
#    img 3091
    mt "Сучка!!!"

#    music Groove2_85
#    $ dickOfficeCabinetStage = 2
#    call refresh_scene_fade() from _call_refresh_scene_fade_173
    return

label gallery_1742:
    music Pyro_Flow
    img 1686
    with fadelong
    w
    img 1687
    w
    img 1688
    jane "Здравствуйте, Миссис Бакфетт!"

    img 1689
    "Чем могу Вам помочь?"

    img 1690
    m "Аааа..."
    "Джейн."
    "Мелкая подлиза."

    img 1691
    "Я смотрю ты уже пролезла в секретари Стива?"
    "Это тебя повысили или понизили, А?"
    "И как ты здесь оказалась?"

    img 1692
    "Через его член?"

    img 1693
    jane "Миссис Бакфетт!"

    img 1694
    m "Молчать!"
    "И встань когда с тобой разговаривает твой Босс!"

    img 1695
    jane "Но Мэм!"
    "Мой Босс Стив."

    img 1696
    m "Стив моя шестерка."
    "Через меня идут все деньги его компании!"

    img 1697
    "Так что я твой Босс, ку-кол-ка!!"

    img 1698
    "Встать!"

    img 1699
    "..."

    img 1700
    "Так-то лучше."

    img 1701
    "Это что у тебя за дресс код?"

    img 1702
    w
    img 1703
    w
    img 1704
    "Одета как проститутка!"

    img 1705
    "Что это вообще за место?"
    "Это фирма моего младшего партнера или публичный дом?"
    img 1706
    "..."
    "Что молчишь?"
    "Быстро отвечать!"

    img 1707
    jane "Это солидная фирма, Мэм...."
    img 1706
    m "А почему тогда здесь проститутки?"
    "Я всегда считала что проституткам место в борделе, а не в солидной фирме."

    img 1708
    "Как ты считаешь, Джейн?"

    img 1709
    jane "Да, Мэм."
    "Проституткам не место в солидной фирме."

    img 1710
    m "Да?"
    "И почему-же тогда ты здесь находишься?"

    img 1711
    jane "Мэм."
    "Я исправлюсь."
    "В следующий раз Вы меня увидите в строгом деловом костюме."

    img 1712
    m "В следующий раз??"
    "У тебя 30 секунд!"

    img 1713
    "Иначе в следующий раз я тебя здесь уже не увижу!"

    img 1714
    jane "Но Мэм."
    "У меня нет с собой другой одежды."

    img 1715
    m "Почему меня это должно волновать?"

    sound highheels_run2
    music Hidden_Agenda
    img 1716
    with fadelong
    tiffany "Джейн."

    img 1717
    "Какие планы после работы?"

    img 1718
    "Может сходим в клуб?..."

    img 1719
    w
    img 1720
    jane "Чшшш! Тихо!"

    img 1721
    w
    img 1722
    w
    music Pyro_Flow
    img 1723
    w
    img 1724
    w
    img 1725
    tiffany "..."

    img 1726
    "ОЙ!"

    img 1727
    "Миссис Бакфетт!"

    "Здравствуйте!"

    img 1728
    m "Оооо!"
    "А это кто у нас?"

    img 1729
    "Судя по внешнему виду, это напарница по ремеслу!"

    img 1730
    "Что девочки, вместе ходите сниматься в клуб?"

    img 1731
    tiffany "Мэм, я просто зашла..."

    img 1732
    "Передать документы..."

    sound highheels_run2
    img 1733
    "Я уже ухожу..."

    img 1734
    with fade
    w
    img 1735
    with fade
    w
    img 1736
    with fade
    w
    img 1737
    with fade
    w
    img 1738
    with fade
    w
    img 1739
    with fade
    w
    img 1740
    with fade
    w
    img 1741
    with fade
    w
    img 1742
    m "Стоять!!!"

    img 1743
    "Быстро назад!!!"

    sound highheels_short_walk
    img 1744
    "Как тебя зовут?"

    img 1745
    tiffany "Мое имя Тиффани, Мэм."

    img 1746
    m "Что-то я тебя не помню."

    "Давно ты здесь работаешь?"

    img 1747
    tiffany "Третий месяц, Мэм."

    img 1748
    m "И что ты здесь делаешь?"

    "Почему ты уже входишь практически в кабинет к Стиву?"

    img 1749
    "У тебя какие-то особые таланты, А?"

    "Почему ты так быстро поднялась по каръерной лестнице??"

    img 1750
    tiffany "Мэм."

    "У меня хорошее образование и отличное резюме."

    img 1751
    m "А мне сдается единственный быстрый социальный лифт в этой компании -"

    img 1752
    "- Это член Стива!"

    img 1753
    "..."

    img 1754
    "Развел проституток!"

    "Я наведу здесь порядок, не переживайте!"

    img 1755
    tiffany "Мэм..."

    img 1756
    m "Посмотри на себя!"

    "В чем ты одета!"

    img 1757
    m "Все."

    menu:
        "Вас обеих здесь больше не будет.":
#            $ steveSecretaryFireOffended = True
#            call bitch(1, "steve_secretaryjane_fireoffended") from _call_bitch_86
            img 1758
            "Вас обеих здесь больше не будет."
            img 1759
            m "А теперь быстро вышла отсюда!"

            img 1760
            "Я пойду надирать задницу вашему Боссу!"

        "Я пойду надирать задницу вашему Боссу!":
            img 1759
            m "А теперь быстро вышла отсюда!"
            img 1760
            "Я пойду надирать задницу вашему Боссу!"


#    $ steveSecretaryOffended = True
    return

label gallery_1769:
#    $ remove_objective("catch_steve")
    music Pyro_Flow
    img 1761
    with fadelong
    w
    img 1762
    with fade
    w
    img 1763
    with fade
    w
    img 1764
    with fade
    m "Ага!"
    "Попался."
    "Мешок с дерьмом!"

    img 1765
    steve "Моника, я..."

    img 1766
    "Я все объясню..."

    img 1767
    m "Брысь из моего кресла!"

    img 1768
    "Живо!"

#    call change_scene("steve_office_office_table", "Fade_long") from _call_change_scene_100

#    return

#label steve1_steve_talk2:
    img 1769
    with fade
    steve "Моника..."
    "Я все объясню..."

    img 1770
    m "Я тебя слушаю, Стив!"

    img 1771
    steve "Моника, я..."
    "В общем..."
    "В общем у нас финансовые трудности."
    "И нам сложно выполнить то о чем мы договорились."
    "О взятии в аренду половины этажа в твоем тауере."

#    $ steveOfficeSteveTableStateTalk = 1
#    return

#label steve1_steve_talk3:
    img 1772
    with fade
    m "Уже половины?"
    "Стив."
    "Речь шла о целом этаже."
    "Откуда половина?"

    img 1773
    steve "..."

    m "..."

    img 1774
    "Стив?"

    img 1775
    steve "Да."

    img 1776
    m "Стив."
    "Почему ты прятался от меня?"
    "Ты меня не уважаешь?"
    "А, Стив?"
    "Ответь-ка мне?"

    img 1777
    with dissolve
    "Ты ведь знаешь что я щелчком пальцев могу перекрыть тебе кислород."

    img 1778
    steve "Да, Моника."
    "Я знаю..."
    "..."
    "......"

    "Моника."

    "Я..."
    "Я......"

    "Я просто..."

    img 1779
    m "Что ты просто, Стив?"

    img 1780
    steve "Моника!"
    "Я боялся тебя!"
    "Я трус!"

#    $ steveOfficeSteveTableStateTalk = 2
#    return

#label steve1_steve_talk4:
    img 1781
    m "Ахахаха!"
    "Хахахаха!"
    "Ну ты рассмешил меня."
    "Я знаю Стив."

    img 1782
    "Знаю что ты трусливый слизняк."

    img 1783
    "Но ты оказывается умеешь быть смелым."
    "У тебя хватило смелости сказать мне правду."

    img 1784
    steve "..."

    img 1785
    m "Хорошо."
    "Ты растопил мою решимость убрать тебя."
    "Поднял мне настроение."

    img 1786
    steve "..."

    img 1787
    m "Итак."
    "Что там у нас с арендой?"
    "Ты понимаешь что этот этаж сейчас пустует?"
    "Мне не нужны пустующие площади."
    "Меня не беспокоят деньги."

    img 1788
    "Пустующие площади вредно для репутации, Стив."
    "Ты понимаешь?"

    img 1789
    steve "Да, Моника."
    "Я понимаю."
    "Смотри."
    "Я предлагаю переделать наш годовой бюджет."
    "Для этого надо согласовать с твоей компанией."
    "У нас освободятся средства."
    "Мы закроем несколько сделок, которые висят."

    img 1790
    "У нас появится солидная прибыль."
    "И мы снимем половину этажа за 200.000 долларов."

    img 1791
    m "За 500.000 долларов, Стив."

    "Половина этажа."

    "Аренда."

    "600.000 за целый."

    img 1792
    steve "400.000 долларов за целый этаж аренды."

    img 1793
    m "500.000 за целый этаж."

    img 1794
    steve "250.000 за половину."

    img 1795
    m "За половину 350.000 долларов."

    img 1796
    steve "350.000 за целый."

    img 1797
    m "За целый 450.000."

    img 1798
    steve "Тогда за половину 300.000."

    img 1799
    m "370.000 за целый."

    img 1800
    steve "Хорошо."

    "Я согласен."

    img 1801
    menu:
        "И еще уволить этих двух сучек на входе к тебе.":
            m "И еще уволить этих двух сучек на входе к тебе."

    sound highheels_run2
    img 1802
    with fade
    m "Стив."
    "Что там за шум?"
    img 1803
    with fadelong
    steve "Тут никого нет."

#    $ steveOfficeSteveTableStateTalk = 3
#    $ steveOfficeSteveTableState = 1
#    return
#label steve1_steve_talk5:

    img 1804
    with fade
    steve "Моника, кого ты имеешь ввиду уволить?"
    "Каких двух сучек?"

    img 1805
    m "Одна твоя секретарь Джейн."

    steve "А вторая?"

    m "Вторая какая-то миловидная стерва."
    "Как ее зовут?.."

    "..."

    "....."
    img 1806
    "Тиффани!"

    "Кстати, чем она вообще занимается?"

    img 1807
    steve "Она обрабатывает отчеты."
    "Моника.
    Что она тебе сделала?"

    img 1808
    steve "Стив."

    "За 370.000 долларов ты не должен задавать вопросы."

    img 1809
    steve "Но Моника, в нашей компании трудятся только высокоморальные люди."

    "Тут никто не позволяет себе лишнего."

    img 1810
    m "Не ври мне, Стив."

    "Что одна что другая попали сюда через твой член."

    img 1811
    img 1812
    steve "Моника, я клянусь тебе!"

    "Могу поклясться своей мамой!"

    "Мамма-миа!"

    "У меня нет близости ни с одной из этих невинных девушек!"

    img 1813
    m "450.000 долларов."

    img 1814
    steve "Хорошо, Моника."

    "Я понял."

    "350.000 и я увольняю Тиффани и Джейн."

    img 1815
    m "Ладно, пусть будет по твоему."

    img 1816
    menu:
        "Если ты мне солгал, то ты отсосешь у собаки.":
#            $ monicaSteveDogOffended = True
            m "Но я запомню твою клятву."


#            call bitch(4, "steve_dog_offend") from _call_bitch_89
            "Если ты мне солгал, то ты отсосешь у собаки."

            img 1817
            steve "Моника!"

            "Ты что?"

            "Что ты такое говоришь?"

            img 1818
            m "Ничего."

            "Просто придумала самое омерзительное наказание за твою ложь."

            "Так ты согласен?"

            img 1819
            "Ведь если ты невиновен, тебе нечего бояться?"

            img 1820
            with fadelong
            steve "Хорошо, Моника."

            "Я согласен."

        "Но я запомню твою клятву.":
            m "Но я запомню твою клятву."
            img 1820
            with fadelong
            steve "Хорошо, Моника."


    img 1821
    m "Вот и все."

    "Ну..."

    "Я пошла."

    img 1822
    with fadelong
    m "Я разрешаю тебе пока посидеть в моем кресле, Стив."

    steve "Спасибо, Моника."

#    $ add_objective("goto_office_for_tea", _("Ехать в свой офис"), c_green, 20)
#    $ autorun_to_object("street_steve_office", "steve1_end_monica_thinking")
#    $ autorun_to_object("monica_office_entrance", "steve1_scene1_1")
#    $ steveOfficeSteveTableStateTalk = 4
#    $ steveOfficeSteveState = 2
    return

label gallery_4899: #разговор с Джейн и Тиффани

    music Hidden_Agenda
    call textonblack(_("ТЕМ ВРЕМЕНЕМ..."))
    img black_screen
    with Dissolve(1)
#    img
#    with fadelong
    # Джейн заходит ко Стиву
    img 4854
    w
    img 4855
    w
    img 4856
    jane "Стив!"
    img 4857
    steve "О, моя милая Джейн!"
    "Хорошо что ты зашла."
    img 4858
    jane "Стив, скажи, что это значит?"
    img 4859
    steve "Джейн, что ты имеешь ввиду?"
    img 4860
    jane "Эта Бакфетт, она унизила меня только что."
    img 4861
    steve "..."
    img 4862
    jane "Более того, я думаю она собирается уволить меня."
    img 4863
    "Она ведь говорила об этом с тобой, Стив?"
    img 4864
    steve "Нет, Джейн, она не говорила об этом. Наоборот, она хорошо отзывалась о тебе!"
    img 4865
    jane "Стив, ты мне врешь! Я все слышала!"
    img 4866
    steve "Ты подслушивала?"
    img 4867
    jane "Стив, мы находимся в таких отношениях, когда я имею право следить за тем что происходит!"
    img 4868
    steve "Ты про что, Джейн?"
    img 4869
    with fadelong
    jane "Про наши планы! Надеюсь ты не забыл?!"
    img 4870
    steve "Планы?"
    img 4871
    jane "Да, Стив! Наши планы!"
    img 4872
    "Не забудь, какие документы проходят через меня."
    img 4873
    "Я же вижу все твои темные делишки! И на многих документах стоят мои подписи, как секретаря!"
    img 4874
    "И если тебя возьмут за мягкое место, Стив, то могут взять и меня."
    img 4875
    "А, зная тебя, я не удивлюсь, если стану козлом отпущения!"
    img 4876
    "Потому если ты хочешь чтобы все дальше шло как идет."
    img 4877
    "Чтобы я закрывала глаза на твои делишки. Чтобы я ходила при тебе как проститутка. И все остальное."
    img 4878
    "И никакая Бакфетт или другая сучка не смогла бы уволить меня!"
    img 4879
    "То давай поженимся, как и собирались. Наши отношения станут законными и отвечать, если что, будешь за все ты."
    img 4880
    steve "Прибыль тоже будет общая. Да, Джейн?"
    "Как и доля в компании..."
    img 4881
    jane "Конечно, Стив!" #ехидно улыбается
    img 4880
    steve "..."
    img 4882
    jane "..."
    img 4883
    with fadelong
    jane "Ты передумал, милый? Ты меня больше не любишь?"
    img 4884
    jane "Ты уже не хочешь жениться на мне?"
    img 4885
    with fadelong
    steve "Что ты, Джейн! Я тебя очень люблю! Иди ко мне моя малышка."
    img 4886
    "Дай я поцелую тебя..."
    img 4887
    w
    img 4888
    w
    img 4889
    w
    sound snd_fabric1
    img 4890
    with fadelong
    w
    img 4891
    steve "Малышка, поцелуй меня скорее, закрепим наш союз..."
    img 4892
    w
    img 4893
    w
    img 4894
    w
    img 4896
    with fadelong
    w
    img 4895
    music Loved_up
    jane "Хорошо, милый..."

    img 4896
    w
    img 4897
    w
    img 4898
    w
    img 4899
    w
    img 4900
    w
    img 4901
    w
    #video


    # делает минет
    img 4903
    steve "Мммм.. даа.."
    scene black
    image videoSteve_Jane_Blowjob_1_1 = Movie(play="video/Steve_Jane_Blowjob_1_1.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_1
    wclean
    img 4904
    w
    scene black
    image videoSteve_Jane_Blowjob_1_2 = Movie(play="video/Steve_Jane_Blowjob_1_2.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_2
    wclean
    img 4905
    w
    scene black
    image videoSteve_Jane_Blowjob_1_3 = Movie(play="video/Steve_Jane_Blowjob_1_3.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_3
    wclean
    img 4906
    "Вот так, давай... соси..."
    scene black
    image videoSteve_Jane_Blowjob_1_4 = Movie(play="video/Steve_Jane_Blowjob_1_4.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_4
    wclean
    img 4907
    w
    scene black
    image videoSteve_Jane_Blowjob_1_5 = Movie(play="video/Steve_Jane_Blowjob_1_5.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_5
    wclean
    img 4908
    "Соси... свою долю в компании... давай..."
    scene black
    image videoSteve_Jane_Blowjob_1_6 = Movie(play="video/Steve_Jane_Blowjob_1_6.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_6
    wclean
    img 4909
    w
    scene black
    image videoSteve_Jane_Blowjob_1_7 = Movie(play="video/Steve_Jane_Blowjob_1_7.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_7
    wclean
    scene black
    image videoSteve_Jane_Blowjob_1_8 = Movie(play="video/Steve_Jane_Blowjob_1_8.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_8
    wclean
    scene black
    image videoSteve_Jane_Blowjob_1_9 = Movie(play="video/Steve_Jane_Blowjob_1_9.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_9
    wclean
    img 4910
    "Вот так... дааа..."
    scene black
    image videoSteve_Jane_Blowjob_1_10 = Movie(play="video/Steve_Jane_Blowjob_1_10.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_10
    wclean
    scene black
    image videoSteve_Jane_Blowjob_1_11 = Movie(play="video/Steve_Jane_Blowjob_1_11.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_11
    wclean

    img 4911
    w

    # заходит Тиффани
    music Groove2_85
    img 4912
    with fadelong
    w
    img 4913
    tiffany "Ой!"
    img 4914
    w
    img 4915
    "Мистер Стив! Простите!"
    "Я зашла передать документы..."
    img 4916
    w
    img 4917
    jane "Упс!"
    img 4918
    steve "Тиффани, обожди минуту."
    img 4919
    "Я сейчас освобожусь."
    img 4920
    tiffany "Хорошо, Мистер Стив!"
    "Я подожду у рабочего стола Джейн."
    sound snd_fabric1
    img 4922
    with fadelong
    jane "..." #встает и вытирает лицо
    img 4921
    jane "Стив. Я давно хотела спросить тебя."
    img 4923
    steve "Да, милая, можешь спрашивать все что хочешь. Мы уже почти семья."
    img 4924
    jane "Почему Тиффани так одета. Это мне что-то напоминает про твои ко мне просьбы."
    img 4925
    steve "Я не знаю, Джейн!" #мутный и хитрый
    img 4926
    jane "Ты не знаешь?"
    img 4927
    steve "Нет, она же твоя подружка. Я думал ты знаешь..."
    img 4928
    w
    img 4929
    jane "Ты не просил ее этого делать, правда ведь Стив?" #пристально смотрит
    img 4930
    steve "Конечно нет, Джейн! Ты же знаешь что для меня есть только ты!"
    img 4931
    "Может быть Тиффани сама флиртует со мной... Но я даже не смотрю на нее, Джейн!"
    img 4932
    "Может быть она завидует тебе, пытается равняться на тебя."
    "Начинает подражать..."
    img 4933
    music Loved_up
    "Но это бесполезно, ты ведь знаешь меня!"
    img 4934
    w
    img 4935
    w
    img 4936
    w
    img 4937
    w
    img 4938
    w
    img 4939
    jane "Чмок!"
    img 4940
    jane "Хорошо, милый. Я пошла."
    img 4941
    "Сегодня я поеду подбирать свадебное платье. А от тебя я жду даты свадьбы, решай это скорее!"
    steve "Да, милая, конечно!"
    img 4942
    w

    #jane уходит

    #fade
    #разговор у стола джейн и тиффани
    music Indo_Rock
    img 4943
    with fadelong
    w
    img 4944
    with fade
    w
    img 4945
    w
    img 4946
    w
    img 4947
    tiffany "О, Джейн! Вы закончили со Стивом! Я могу войти?"
    img 4948
    jane "Да, Тиффани, можешь заходить."
    img 4949
    "Я сегодня не поеду с тобой в клуб. Мне надо выбирать свадебное платье."
    img 4950
    "Присоединишься ко мне?"
    img 4951
    tiffany "Джейн, конечно! Я очень рада за вас!"
    img 4952
    "Я с удовольствием присоединюсь к тебе! Ты моя лучшая подруга!"
    img 4953
    "Как я могу пропустить такое мероприятие, как выбор подвенечного платья!"
    img 4954
    jane "Хорошо, Тиффани, уже почти конец рабочего дня."
    "Как освободишься, скажи мне. Я уже свободна."
    img 4955
    tiffany "Хорошо, Джейн! Чмоки!"

    #заходит ко стиву, стив сидит за столом на что-то отвлечен
    label gallery_5002:
    music Hidden_Agenda
    img 4956
    with fadelong
    w
    img 4957
    with fade
    w
    img 4958
    with fade
    tiffany "Мистер Стив!"
    img 4959
    steve "Да, Джейн? Ты хотела передать документы?"
    img 4960
    tiffany "Мистер Свит! На самом деле я пришла поговорить с вами о Миссис Бакфетт!"
    img 4961
    steve "Я тебя слушаю, говори."
    img 4962
    tiffany "Она собирается уволить меня!"
    "Она мне практически так и сказала!"
    img 4963
    steve "Она сказала именно так? Но за что?"
    ##
    if steveSecretaryFireOffended == True:
        img 4962
        tiffany "Да, сказала именно так!"
    else:
        img 4962
        tiffany "Не совсем так, но она намекала на это!"
    img 4964
    steve "За что она хочет уволить тебя?"
    img 4965
    tiffany "За мой внешний вид!"
    img 4966
    steve "?" #глупое лицо, косит под дурачка, улыбается и разводит руками
    img 4967
    tiffany "Мистер Стив! Это вы заставляете меня носить это!"
    img 4968
    #стив встает и подходит сбоку к Тиффани
    steve "Тиффани, моя хорошая. Я ведь не приказывал тебе этого делать, я поднял тебе зарплату и ты решила меня отблагодарить..."
    "Разве нет?"
    img 4969
    tiffany "Мистер Стив! Вы недвусмысленно намекнули мне о том, благодаря чему запрплата будет повышена." #лисичка
    img 4970
    "И вы повысили ее после того как я выполнила ваши намеки."
    img 4971
    "А теперь из-за этого я могу лишиться работы!"
    img 4972
    steve "..."
    img 4973
    "Мистер Стив! Вы знаете, что с таким резюме как у меня, я смогу устроиться в любую компанию, где будет дальнейший карьерный рост!"
    img 4974
    steve "..."
    img 4975
    steve "О да! Тиффани!" #лапает за попу
    sound Jump2
    img 4976
    with fadelong
    w
    img 4977
    with fade
    w
    img 4978
    "С таким резюме у тебя открыты все дороги... И в этой компании тоже..."
    img 4979
    tiffany "И в этой компании тоже?"
    img 4980
    steve "Да, Тиффани... Я давно напоминал тебе о повышении.." #продолжает лапать
    img 4981
    w
    img 4982
    steve "Не знаю почему ты говоришь мне каждый раз слово НЕТ..."
    img 4983
    music Groove2_85
    tiffany "Потому что вы женитесь на Джейн."
    "А у меня есть моральные принципы, которые запрещают мне делать то что вы просите в данных обстоятельствах."
    img 4984
    with fadelong
    steve "Женюсь?? Кто тебе сказал это?"
    tiffany "Мне сказала это Джейн."
    #стив ошарашен
    img 4985
    steve "..."
    img 4986
    tiffany "Ведь это правда?"
    img 4987
    steve "Тиффани.. я... у нас правда есть кое-какие планы с Джейн... но..."
    img 4988
    tiffany "???"
    img 4989
    music Hidden_Agenda
    steve "Тиффани, ты такая красивая!"
    sound Jump2
    img 4990
    "Знала бы ты как я хочу тебя!" #снова лапает ее
    img 4991
    tiffany "Больше чем Джейн?"
    img 4992
    steve "Конечно больше! Раздевайся скорее!" #лапает
    img 4993
    tiffany "Хорошо, но при одном условии!"
    sound snd_fabric1
    img 4994
    with fadelong
    w
    img 4995
    steve "Проси все что хочешь, я не могу удержаться. Я тебя возьму прямо здесь! Любимая Тиффани!" #стив стоит с опущенными штанами с членом
    img 4996
    tiffany "Вы поднимаете мне зарплату в два раза..." #тиффани поворачивается к нему
    steve "Хорошо, Тиффани! Скорее, возьми его!"
    img 4997
    w
    img 4998
    w
    img 4999
    tiffany "Вы защищаете меня от этой сучки, Бакфетт!"
    img 5000
    steve "Хорошо, Тиффани, я договорюсь с ней. Она не тронет тебя."
    img 5001
    "Скорее возьми его в ротик!"
    img 5002
    music Groove2_85
    tiffany "И последнее..." #берет его за член
    img 5003
    w
    img 5004
    w
    img 5005
    w
    img 5006
    tiffany "И последнее..." #берет его за член
    img 5007
    w
    img 5008
    "Я занимаю место Джейн..."
    img 5009
    steve "..." #ошарашен
    img 5010
    tiffany "Подумайте, Мистер Стив..."
    img 5013
    w
    img 5011
    tiffany "Можете не торопиться!" #щелкает его по члену
    img 5012
    with dissolve
    w
    img 5014
    with fade
    w
    img 5015
    with fade
    w
    img 5016
    with fade
    w
    img 5017
    with fade
    w
    img 5018
    with fade
    w
    img 5019
    with fade
    w
    img 5020
    with fade
    w
    img 5021
    with fade
    w
    img 5022
    steve "..."
    #тиффани сексуально уходит
    #стив смотрит ей вслед со смущением и злостью

    #fade
    #тиффани и джейн у стола джейн
    img 5023
    music Indo_Rock
    with fadelong
    jane "Ты передала документы? Все хорошо?"
    img 5024
    w
    img 5025
    tiffany "Да, Джейн!" #улыбается веселая
    "Я свободна на сегодня!"
    img 5026
    "Поехали скорее выбирать тебе платье!"
    img 5027
    jane "Хорошо, Тиффани. Я сейчас сообщу Боссу и особожусь. Жди меня внизу!"
    img 5028
    tiffany "Хорошо, Джейн! Поторопись! Мне показалось что Босс сегодня немного злой."
    img 5029
    jane "Я не боюсь его злости, Тиффани. Я знаю подход к нему!"
    img 5030
    tiffany "О, Джейн! Конечно! Ты моя лучшая подруга."
    img 5031
    jane "Ты тоже моя лучшая подруга, Тиффани! Увидимся через 10 минут!"
    img 5032
    tiffany "Пока! Чмоки!"
    label gallery_5044:
    music Indo_Rock
    #fade
    #выходит Стив
    img 5033
    with fadelong
    jane "Стив, я уже все закончила, так что я пойду. Мы с Тиффани поедем выбирать мне свадебное платье."
    img 5034
    steve "Конечно, Джейн! Ты сейчас пойдешь."
    img 5035
    jane "Стив! Что ты делаешь???"
    img 5036
    w
    img 5037
    with dissolve
    w
    img 5038
    w
    img 5039
    with fade
    jane "Стив! Что ты делаешь???"
    img 5040
    steve "Проверка соблюдения дресс-кода!"
    img 5041
    w
    img 5042
    w
    img 5043
    w
    img 5044
    jane "Я все соблюдаю, Стив!"
    img 5045
    jane "Стив! Мне надо идти! Я тороплюсь!"
    steve "Конечно, Джейн! Ты сейчас пойдешь."
    #хватает ее, поднимает и поворачивает руками на стол
    img 5046
    "Но прежде ты исполнишь супружеский долг!"
    menu:
        "Ахххх..":
            img 5049
            jane "Ахххх.."
            # секс стива и джейн
            img 5048
            w
            img 5050
            jane "Нет, Стив! Он слишком большой!"
            img 5051
            jane "Только после свадьбы!"

            #video
            scene black
            image videoSteve_Jane_Sex_1_1 = Movie(play="video/Steve_Jane_Sex_1_1.mp4", fps=30)
            show videoSteve_Jane_Sex_1_1
            wclean
            scene black
            image videoSteve_Jane_Sex_1_2 = Movie(play="video/Steve_Jane_Sex_1_2.mp4", fps=30)
            show videoSteve_Jane_Sex_1_2
            wclean
            scene black
            image videoSteve_Jane_Sex_1_3 = Movie(play="video/Steve_Jane_Sex_1_3.mp4", fps=30)
            show videoSteve_Jane_Sex_1_3
            wclean
            scene black
            image videoSteve_Jane_Sex_1_4 = Movie(play="video/Steve_Jane_Sex_1_4.mp4", fps=30)
            show videoSteve_Jane_Sex_1_4
            wclean
            scene black
            image videoSteve_Jane_Sex_1_5 = Movie(play="video/Steve_Jane_Sex_1_5.mp4", fps=30)
            show videoSteve_Jane_Sex_1_5
            wclean
            scene black
            image videoSteve_Jane_Sex_1_6 = Movie(play="video/Steve_Jane_Sex_1_6.mp4", fps=30)
            show videoSteve_Jane_Sex_1_6
            wclean
            scene black
            image videoSteve_Jane_Sex_1_7 = Movie(play="video/Steve_Jane_Sex_1_7.mp4", fps=30)
            show videoSteve_Jane_Sex_1_7
            wclean
            scene black
            image videoSteve_Jane_Sex_1_8 = Movie(play="video/Steve_Jane_Sex_1_8.mp4", fps=30)
            show videoSteve_Jane_Sex_1_8
            wclean
            scene black
            image videoSteve_Jane_Sex_1_9 = Movie(play="video/Steve_Jane_Sex_1_9.mp4", fps=30)
            show videoSteve_Jane_Sex_1_9
            wclean
            scene black
            image videoSteve_Jane_Sex_1_10 = Movie(play="video/Steve_Jane_Sex_1_10.mp4", fps=30)
            show videoSteve_Jane_Sex_1_10
            wclean
            scene black
            image videoSteve_Jane_Sex_1_11 = Movie(play="video/Steve_Jane_Sex_1_11.mp4", fps=30)
            show videoSteve_Jane_Sex_1_11
            wclean


            img 5052
            steve "АААааррргххх!!!"
            img 5053
            steve "Аааааа!!!"
            img 5054
            jane "Нет, Стив! Не в меня!!!"
            steve "АААааррргххх!!!"
            img 5055
            with fadelong
            steve "Все, детка!"
            img 5056
            steve "Можешь идти!"
            img 5057
            w
            img 5058
            steve "Рабочий день закончен..."

        "Только после свадьбы, Стив!":
            img 5047
            jane "Только после свадьбы, Стив!"

#    call refresh_scene_fade() from _call_refresh_scene_fade_9
#    music Mandeville
    return

label gallery_4347:
    music Loved_up
    img 4288
    w
    img 4289
    w
    img 4290
    w
    img 4291
    w
    img 4292
    w
    img 4293
    w
    img 4294
    w
    img 4295
    w
    img 4343
    w
#    $ dressFitOwnDressDressedOut = True
    menu:
        "Полюбоваться собой в зеркало.":
            img 4344
            w
            img 4345
            dick "Вау!!!"
            img 4346
            w
            img 4347
            w
            img 4348
            w
        "Не заниматься ерундой":
            pass
#    music casualMusic
#    $ scene_transition = "Fade"
#    call refresh_scene() from _call_refresh_scene_30
    return

label gallery_4366:
    music Loved_up
    img 4349
    with fadelong
    w
    img 4350
    w
    sound snd_fabric1
    stop music fadeout 1.0
    img 4351
    m "Упс!!!"
    img 4352
    music Molten_Alloy
    m "Что там?"
    img 4353
    with dissolve
    m "Мои трусики!
    Дьявол!"
    m "Я поспешила надеть это дурацкое платье и зацепила им за трусики!!!"
    img 4355
    w
    img 4356
    w
    img 4304
    dick "ОГО!!!"
    img 4357
    w
    img 4358
    m "Дьявол!
    Я запуталась в этом платье!"
    "Ничего! Сейчас я дотянусь!"
    menu:
        "Дотянуться аккуратно.":
            img 4359
            with fadelong
            w
            img 4360
            w
            music casualMusic
            img 4368
            m "Все, инцидент исчерпан!"

        "Дотянуться резко. Я что, собираюсь тут вечно стоять без трусиков???":
            img 4361
            with fadelong
            m "Дурацкое платье! Я запуталась!"
            img 4362
            m "Надо потянуться еще посильнее..."
            img 4304
            dick "Вот это да!!! У нее грудь и правда на миллиард долларов!"

            img 4359
            w
            img 4360
            w
            img 4363
            m "Так-то лучше."
            m "Все, инцидент исчерпан!"
            img 4364
            m "ЧТООООО????"
            m "Дьявол!
            Из-за того что я сильно потянулась, это дурацкое платье сползло с моей груди!"
            img 4365
            w
            img 4366
            w
            music casualMusic
            img 4367
            w
            img 4368
            w
    return

label gallery_1382:
    music Marty_Gots_a_Plan
    img 1376
    with fadelong
    m "Дик."
    dick "Да, дорогая."

    menu:
        "Дик. Зачем ты подглядывал за мной?":
#            $ dickClothShopOffended1 = True
#            call bitch(5, "dick_cloth_shop_peeping_dialogue1") from _call_bitch_96
            m "Дик.
            Скажи."

            m "Зачем ты подглядывал за мной?"

            img 1377
            dick "Дорогая, я уже говорил."
            "Я хотел проверить все-ли у тебя в порядке."
            img 1378
            m "Дик, не ври мне."
            "Я прекрасно понимаю что у тебя на уме."
            "Можно задать вопрос, а ты честно ответишь на него."

            img 1377
            dick "Конечно..."

            img 1379
            m "Ты ведь хочешь переспать со мной?"
            "Верно?"
            img 1377
            dick "Моника... Я..."
            img 1379
            m "Не увиливай, скажи прямо да или нет."

            img 1380
            dick "Ну, вообще-то, да."

            music casualMusic
            menu:
                "Дик, ты же уродливый. Посмотри на себя.":
#                    $ dickClothShopOffended2 = True
#                    call bitch(5, "dick_cloth_shop_peeping_dialogue2") from _call_bitch_97
                    img 1381
                    m "О Боже, Дик, Дик."
                    "Ну посмотри на себя."
                    "Ты жирный и уродливый."
                    "Как вообще ты себе представляешь что такая девушка как я будет заниматься с тобой этим?"

                    img 1382
                    m "Посмотри на свой уродливый галстук!"

                    img 1383
                    m "Где твой вкус?"
                    "Мы общаемся только потому что ты решаешь мои дела."

                "Дик, это невозможно.":
                    img 1389
                    m "Ты считаешь что я буду спать с мужчиной у которго такой смешной галстук?"
                    "Да, Дик?"

            img 1384
            dick "Моника.. Я..."

            img 1385
            m "Ты знаешь, Дик, что вообще-то я замужем."
            "Ты ведь знаешь это?"

            img 1380
            dick "Да..."
            img 1385
            m "И это тебя не смущает?"

            img 1386
            m "А ты знаешь что я вообще не люблю секс?"
            "Я не понимаю что в нем вообще такого."
            "Это любят только мужчины."

            img 1387
            m "Мы с мужем занимались этим всего пару раз за все время."

            img 1388
            m "И то только тогда, когда мне что-то было от него нужно."
            "..."
            "..."

            img 1389
            m "Что молчишь?"

            img 1390
            dick "Моника, дорогая."
            "Скажи, мой вес это правда проблема?"
            "Я могу пойти заниматься в спортзал и ...."

            img 1391
            m "Да, Дик!"
            "Это проблема!"
            "И, пока ты это не решишь, в любом случае это будет оставаться проблемой."

            img 1389
            m "А ты ведь знаешь что мне не нужны люди с проблемами."
            "..."

            img 1392
            m "И вообще, как я уже сказала."
            "Мне секс неинтересен."
            "Ни с тобой, ни с кем-либо еще."
            "И на этом закроем эту тему раз и навсегда."

            img 1393
            dick "Хорошо, Моника."
            "Как скажешь."
            "Давай я заплачу за платье?"

            menu:
                "Я сама могу о себе позаботиться.":
#                    $ dickClothShopOffended3 = True
#                    call bitch(1, "dick_cloth_shop_peeping_dialogue3") from _call_bitch_98
#                    $ dressMonicaPaid = True
                    img 1392
                    m "Я сама могу о себе позаботиться."
                "Если тебе это так нужно, то плати.":
                    img 1391
                    m "Если тебе это так нужно, то плати."
                    "Но учти что твои деньги мне не нужны.
                    У меня их гораздо больше чем у тебя!"
                    img 1393
                    dick "Да, Моника, я знаю..."


        "У тебя смешной галстук, Дик!":
            label gallery_1389:
            music Marty_Gots_a_Plan
            img 1389
            m "У тебя смешной галстук, Дик!"
            img 1383
            dick "Моника.. Я..."
            img 1384
            dick "Ты так правда считаешь? Он смешной?"
            m "Да, Дик! Определенно!"
            img 1391
            "Тебе нужен кто-то кто купит тебе новый галстук!"
            music casualMusic
            img 1385
            "И это определнно буду не я!"
            dick "Да, Моника, я понимаю..."
            "Конечно."
            "Пойдем я оплачу тебе платье?"

            menu:
                "Я сама могу о себе позаботиться.":
#                    $ dickClothShopOffended3 = True
#                    call bitch(1, "dick_cloth_shop_peeping_dialogue3") from _call_bitch_99
#                    $ dressMonicaPaid = True
                    img 1392
                    m "Я сама могу о себе позаботиться."
                "Если тебе это так нужно, то плати.":
                    img 1391
                    m "Если тебе это так нужно, то плати."
                    "Но учти что твои деньги мне не нужны.
                    У меня их гораздо больше чем у тебя!"
                    img 1393
                    dick "Да, Моника, я знаю..."
    return

label gallery_1915:
    music casualMusic
    img 1913
    with fadelong
    cashier "Добрый вечер, Мэм!"
    "Вы решили еще что-нибудь подобрать?"
    "Рады видеть Вас!"

    img 1914
    music Pyro_Flow
    m "Я не собираюсь подбирать что-то еще в вашей дыре."

    img 1915
    "Я возвращаю вчерашнее платье."
    "Оно жуткое."

    img 1916
    cashier "Но Мэм."

    "Оно Вам прекрасно подходит."

    "На нем нет никаких дефектов."

    "Его нет нужды возвращать назад."

    img 1917
    m "Я не ношу такие дешевые платья."
    "Пусть оно дальше висит в вашем дешевом магазине."
    "И его купит какая-нибудь дура, у которой нет денег на нормальные вещи."

    img 1918
    "Так что возьмите его по хорошему и не тратьте мое время."
    "Иначе пожалеете."

    img 1919
    cashier "Мэм."
    "Как хотите, но..."

    menu:
        "Никаких НО, сучка!!":
#            $ clothShopCashierOffended3ReturnDress = True
            img 1920
            m "Никаких НО!!"

#            call bitch(3, "clothShopCashierOffended3ReturnDress") from _call_bitch_82
            img 1921
            "Если ты сучка еще раз мне скажешь НО или будешь возражать мне, то я тебя засужу и закрою твой магазин к чертовой матери!"

            img 1922
            "ПОНЯТНО??"

            img 1923
            cashier "Хорошо, Мэм."

            img 1924
            w
        "Просто вернуть платье вежливо...":
#            $ clothShopCashierOffended3ReturnDress = False
            music Stealth_Groover
            img 1917
            m "Девушка, я знаю свои права как потребителя."
#            call bitch(-3, "clothShopCashierOffended3ReturnDress") from _call_bitch_83
            "Просто возьмите это платье, мне не нужны деньги за него."
            "Это мои принципы, вы понимаете?"
            img 1919
            cashier "Да, я понимаю, конечно."
            "Спасибо, Мэм!"

#    $ remove_inventory("shop_dress_eveningdress", 1, True)
#    $ clothShopCashierTalkStage = 1
#    call refresh_scene_fade() from _call_refresh_scene_fade_12
#    music Stealth_Groover
#    $ remove_objective("return_dress")
#    $ add_objective("return_to_home", _("Ехать домой"), c_green, 20)
    #$ drivingPlacePlannedArray["House"] = "dress_return_drive3"
#    $ dressReturnDialoguePlanned = True
#    $ returnDressInProgress = False
    return

label gallery_5845:
    scene black_screen
    with Dissolve(1)
    stop music fadeout 1.0
    call textonblack(_("ТЕМ ВРЕМЕНЕМ..."))
    scene black_screen
    with Dissolve(1)
    music Hidden_Agenda
#    $ clothShopCashierFirstNightOffended = False

    img 5826
    with fadelong
    cashier "Конец рабочего дня, я закрыла магазин."
    "Можно идти домой."
    if clothShopCashierFirstNightOffended == True:
        img 5827
        cashier "Вот же эта сучка сегодня!"
        "Какой уже раз она меня оскорбляет?!"
        img 5828
        "Долго мне терпеть подобных клиентов?"
        img 5829
        "Я знаю что бы я сделала с ней!"
        img 5830
        "Я слишком напряжена..."
        "Мне надо расслабиться..."
        menu:
            "Расслабиться...":
                pass
            "Идти домой.":
                return
        music Loved_up
        img 5831
        with fadelong
        "Здесь она лежала?"

        img 5832
        w
        img 5833
        with fade
        w
        img 5834
        w
        img 5835
        w
        img 5836
        w
        img 5837
        w
        img 5838
        w
        img 5839
        w
        img 5840
        "Так гораздо свободнее!"
        img 5841
        with fade
        w
        img 5842
        "Почему бы мне тоже не расслабиться здесь?"
        img 5843
        w
        #video start
        img 5844
        w
        scene black
        image videoClothShopTrader_Masturbation_1_1 = Movie(play="video/ClothShopTrader_Masturbation_1_1.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_1
        wclean
        img 5845
        w
        scene black
        image videoClothShopTrader_Masturbation_1_2 = Movie(play="video/ClothShopTrader_Masturbation_1_2.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_2
        wclean
        img 5846
        w
        "ДА.. АААААА!!!!"
        img 5847
        w
        scene black
        image videoClothShopTrader_Masturbation_1_3 = Movie(play="video/ClothShopTrader_Masturbation_1_3.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_3
        wclean
        img 5848
        w
        scene black
        image videoClothShopTrader_Masturbation_1_4 = Movie(play="video/ClothShopTrader_Masturbation_1_4.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_4
        wclean
        img 5849
        w
        scene black
        image videoClothShopTrader_Masturbation_1_5 = Movie(play="video/ClothShopTrader_Masturbation_1_5.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_5
        wclean
        img 5850
        "ДА!"
        w
        img 5851
        w
        scene black
        image videoClothShopTrader_Masturbation_1_6 = Movie(play="video/ClothShopTrader_Masturbation_1_6.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_6
        wclean
        img 5852
        w
        "МММММММ!"
        img 5853
        w
        img 5854
        w
        #video end
        music Hidden_Agenda
        img 5855
        with fadelong
        "Нет, мне так не расслабиться."
#        img 5856
#        with fade
        img 5857
        with fade
        "Где там моя игрушка?"
        img 5858
        with fade
        w
        img 5859
        "Так, куда я ее положила?"
        img 5860
        with fade
        "Черт! Я же ее унесла!"
        "Так, а это что?"
        img 5861
        with fade
        "Ага! Платье этой сучки!"
        "Значит она ходила на свидание в нем?!"
        img 5862
        with fade
        w
        img 5863
        "Хммм..."
        img 5864
        "У меня есть идея..."
        img 5865
        "Ну-ка снимай с себя все!"
        sound snd_fabric1
        img 5866
        with fade
        "Так-то лучше!"
        sound snd_fabric1
        "Обожаю девочек..."
        img 5867
        with fade
        w
        img 5868
        "Вылитая сучка!"
        img 5869
        with fade
        "Мэм! Пройдемте со мной!"
        img 5870
        with fade
        "Вот так, да."
        img 5871
        "Разрешите я на вас присяду?"
        #video start
        music Loved_Up2
        img 5872
        with fade
        "Да!"
        img 5873
        "Покупатель? Вы не довольны?"
        img 5874
        "Вам не понравилось это платье?"
        img 5875
        w
        img 5876
        "На, получай!"
        scene black
        image videoClothShopTrader_Masturbation_2_1 = Movie(play="video/ClothShopTrader_Masturbation_2_1.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_1
        wclean
        scene black
        image videoClothShopTrader_Masturbation_2_2 = Movie(play="video/ClothShopTrader_Masturbation_2_2.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_2
        wclean
        scene black
        image videoClothShopTrader_Masturbation_2_3 = Movie(play="video/ClothShopTrader_Masturbation_2_3.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_3
        wclean
        img 5877
        "Нравится?"
        scene black
        image videoClothShopTrader_Masturbation_2_4 = Movie(play="video/ClothShopTrader_Masturbation_2_4.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_4
        wclean
        scene black
        image videoClothShopTrader_Masturbation_2_5 = Movie(play="video/ClothShopTrader_Masturbation_2_5.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_5
        wclean
        scene black
        image videoClothShopTrader_Masturbation_2_6 = Movie(play="video/ClothShopTrader_Masturbation_2_6.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_6
        wclean
        img 5878
        "Еще!"
        img 5879
        "На, сучка!"
        img 5880
        w
        scene black
        image videoClothShopTrader_Masturbation_2_7 = Movie(play="video/ClothShopTrader_Masturbation_2_7.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_7
        wclean
        img 5881
        "Будешь знать как грубить мне!"
        img 5882
        w
        scene black
        image videoClothShopTrader_Masturbation_2_8 = Movie(play="video/ClothShopTrader_Masturbation_2_8.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_8
        wclean
        #video end
        img black_screen
        with Dissolve(0.5)
        music Turbo_Tornado
        #video start
        img 5883
        with fadelong
        "Как я возбуждена!"
        w
        img 5884
        w
        scene black
        image videoClothShopTrader_Masturbation_3_1 = Movie(play="video/ClothShopTrader_Masturbation_3_1.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_1
        wclean
        img 5885
        w
        img 5886
        w
        "ААааааахххх!!!!"
        scene black
        image videoClothShopTrader_Masturbation_3_2 = Movie(play="video/ClothShopTrader_Masturbation_3_2.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_2
        wclean
        img 5887
        w
        img 5888
        w
        scene black
        image videoClothShopTrader_Masturbation_3_3 = Movie(play="video/ClothShopTrader_Masturbation_3_3.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_3
        wclean
        img 5889
        w
        scene black
        image videoClothShopTrader_Masturbation_3_4 = Movie(play="video/ClothShopTrader_Masturbation_3_4.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_4
        wclean
        img 5890
        w
        scene black
        image videoClothShopTrader_Masturbation_3_5 = Movie(play="video/ClothShopTrader_Masturbation_3_5.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_5
        wclean
        img 5891
        w
        img 5892
        "Аааааааа!!!!"
        scene black
        image videoClothShopTrader_Masturbation_3_6 = Movie(play="video/ClothShopTrader_Masturbation_3_6.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_6
        wclean
        img 5893
        "Аааааааа!!!!"
        img 5894
        "Какой кайф!!!"
        "Вот теперь я кончила..."
        return

#        "Вот так, да."
#        "Покупатель? Вы не довольны?"
#        "На, получай!"
#        "Нравится?"
#        "Еще!"
#        "На, сучка!"
#        "Эх... как бы я хотела чтобы здесь было ее лицо!"
#        "На, получай!"
#        "Будешь знать как грубить мне!"

    else:
        img 5826
        "..."
        "Какая вежливая покупательница..."
        "Обычно все богачи грубят, но не она..."
        img 5829
        with fade
        "Здесь она спала, говорит?"
        img 5830
        "Хм... жаль меня не было здесь...."
        img 5831
        "Обожаю девочек..."
        img 5832
        "Я слишком напряжена..."
        "Мне надо расслабиться..."
        menu:
            "Расслабиться...":
                pass
            "Идти домой.":
                return
        music Loved_up
        img 5833
        with fade
        w
        img 5834
        w
        img 5835
        w
        img 5836
        w
        img 5837
        w
        img 5838
        w
        img 5839
        w
        img 5840
        "Так гораздо свободнее!"
        img 5841
        w
        img 5842
        "Если она такая добрая и не хочет обидеть меня тем что вернула платье..."
        img 5843
        w
        img 5844
        "Я бы могла дать ей полизать свою киску."
        "Это бы компенсировало все..."
        #video start
        img 5845
        "Да... вы так вежливы..."
        scene black
        image videoClothShopTrader_Masturbation_1_1 = Movie(play="video/ClothShopTrader_Masturbation_1_1.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_1
        wclean
        img 5846
        "Пожалуйста, лижите полевее..."
        scene black
        image videoClothShopTrader_Masturbation_1_2 = Movie(play="video/ClothShopTrader_Masturbation_1_2.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_2
        wclean
        img 5847
        "Да, вот так..."
        scene black
        image videoClothShopTrader_Masturbation_1_3 = Movie(play="video/ClothShopTrader_Masturbation_1_3.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_3
        wclean
        img 5848
        w
        scene black
        image videoClothShopTrader_Masturbation_1_4 = Movie(play="video/ClothShopTrader_Masturbation_1_4.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_4
        wclean
        img 5849
        w
        scene black
        image videoClothShopTrader_Masturbation_1_5 = Movie(play="video/ClothShopTrader_Masturbation_1_5.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_5
        wclean
        img 5850
        "Теперь повыше, да!"
        img 5851
        "Вот так!"
        img 5852
        w
        scene black
        image videoClothShopTrader_Masturbation_1_6 = Movie(play="video/ClothShopTrader_Masturbation_1_6.mp4", fps=30)
        show videoClothShopTrader_Masturbation_1_6
        wclean
        "МММММММ!"
        img 5853
        "ДА!"
        img 5854
        w
        #video end

        music Hidden_Agenda
        img 5855
        with fadelong
        "Нет, мне так не расслабиться."
        img 5856
        with fade
        "Где там моя игрушка?"
        img 5857
        with fade
        w
        img 5858
        with fade
        w
        img 5859
        "Так, куда я ее положила?"
        img 5860
        with fade
        "Черт! Я же ее унесла!"
        "Так, а это что?"
        img 5861
        with fade
        "Ага! Платье этой покупательныцы!"
        "Значит она ходила на свидание в нем?!"
        img 5862
        with fade
        w
        img 5863
        "Хммм..."
        img 5864
        "У меня есть идея..."
        img 5865
        "Ну-ка снимай с себя все!"
        sound snd_fabric1
        img 5866
        with fade
        "Так-то лучше!"
        sound snd_fabric1
        "Обожаю девочек..."
        img 5867
        with fade
        w
        img 5868
        "Представлю что это она!..."
        img 5869
        with fade
        "Мэм! Пройдемте со мной!"
        img 5870
        with fade
        "Вот так, да."

        img 5871
        "Мэм. Разрешите мне присесть?"
        "Вы не против?"
        #video start
        music Loved_Up2
        img 5872
        with fade
        "Спасибо, Мэм! Вы очень любезны!"
        scene black
        image videoClothShopTrader_Masturbation_2_1 = Movie(play="video/ClothShopTrader_Masturbation_2_1.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_1
        wclean
        img 5873
        w
        scene black
        image videoClothShopTrader_Masturbation_2_2 = Movie(play="video/ClothShopTrader_Masturbation_2_2.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_2
        wclean
        img 5874
        w
        scene black
        image videoClothShopTrader_Masturbation_2_3 = Movie(play="video/ClothShopTrader_Masturbation_2_3.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_3
        wclean
        img 5875
        w
        scene black
        image videoClothShopTrader_Masturbation_2_4 = Movie(play="video/ClothShopTrader_Masturbation_2_4.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_4
        wclean
        img 5876
        w
        "Мэм, посмотрите еще. У нас большой ассортимент."
        img 5877
        w
        scene black
        image videoClothShopTrader_Masturbation_2_5 = Movie(play="video/ClothShopTrader_Masturbation_2_5.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_5
        wclean
        img 5878
        "Мэм, пожалуйста, не уходите. Я еще не закончила обслуживать вас."
        img 5879
        w
        scene black
        image videoClothShopTrader_Masturbation_2_6 = Movie(play="video/ClothShopTrader_Masturbation_2_6.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_6
        wclean
        img 5880
        w
        scene black
        image videoClothShopTrader_Masturbation_2_7 = Movie(play="video/ClothShopTrader_Masturbation_2_7.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_7
        wclean
        img 5881
        w
        scene black
        image videoClothShopTrader_Masturbation_2_8 = Movie(play="video/ClothShopTrader_Masturbation_2_8.mp4", fps=30)
        show videoClothShopTrader_Masturbation_2_8
        wclean
        img 5882
        w
        #video end
        img black_screen
        with Dissolve(0.5)
        music Turbo_Tornado
        #video start
        img 5883
        with fadelong
        "Как я возбуждена!"
        w
        scene black
        image videoClothShopTrader_Masturbation_3_1 = Movie(play="video/ClothShopTrader_Masturbation_3_1.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_1
        wclean
        img 5884
        w
        img 5885
        w
        scene black
        image videoClothShopTrader_Masturbation_3_2 = Movie(play="video/ClothShopTrader_Masturbation_3_2.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_2
        wclean
        img 5886
        w
        "ААааааахххх!!!!"
        img 5887
        w
        img 5888
        "Мэм! Вам удобно?"
        scene black
        image videoClothShopTrader_Masturbation_3_3 = Movie(play="video/ClothShopTrader_Masturbation_3_3.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_3
        wclean
        img 5889
        "Да, конечно, пожалуйста."
        "Всегда к вашим услугам."
        img 5890
        w
        scene black
        image videoClothShopTrader_Masturbation_3_4 = Movie(play="video/ClothShopTrader_Masturbation_3_4.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_4
        wclean
        img 5891
        w
        scene black
        image videoClothShopTrader_Masturbation_3_5 = Movie(play="video/ClothShopTrader_Masturbation_3_5.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_5
        wclean
        scene black
        image videoClothShopTrader_Masturbation_3_6 = Movie(play="video/ClothShopTrader_Masturbation_3_6.mp4", fps=30)
        show videoClothShopTrader_Masturbation_3_6
        wclean
        img 5892
        "Аааааааа!!!!"
        img 5893
        w
        img 5894
        "Какой кайф!!!"
        "Вот теперь я кончила..."
        return
    return

label gallery_2789:
#    img 2781
#    with fadelong
#    mt "Тоже не очень..."
    music RnB4_100
    img 2782
    mt "Я не могу больше ничего искать."
    "Я столько искала за день!"
    "Избегала пол города вдоль и поперек!"
    "Я столько дней толком ни ела и не спала!"
    img 2783
    "Мне себя так жаль!"
    "Я бедняжка!"
    img 2784
    music Pyro_Flow
    "Но я обязательно решу все свои проблемы и отомщу всем!"
    "ВЫ СЛЫШИТЕ!!!"
    "Я ОТОМЩУ ВСЕМ ВАМ!!!"
    "И ЭТОЙ ПРОДАВЩИЦЕ, ОТ КОТОРОЙ МНЕ ПРИШЛОСЬ ПРЯТАТЬСЯ!"
    img 2785
    "МНЕ!!!"
    "Я!!!"
    "Моника Бакфетт!!!"
    "И мне прятаться от какой-то продавщицы!"
    img 2786
#    music RnB4_100
    "Лучше не буду об этом думать."
    "Когда я обо всем этом начинаю думать, то мои мысли постепенно приходят к Маркусу."
    music Power_Bots_Loop
    img 2787
    "И его словам."
    "Что меня ждет."
    "Тогда меня начинает охватывать ужас."
    img 2788
    "Все, Моника!"
    "Хватит!"
    "Я валюсь с ног."
    music I_Feel_You
    img 2789
    with fadelong
    "Пожалуй я устроюсь поудобнее."
    img 2790
    with fadelong
    "Вот так."
    img 2791
    with fadelong
    "Все, я сплю..."
    "Пфффффф...."
    "..."
    "...."
    "....."

    scene black_screen
    with Dissolve(1)
    call textonblack_long("УТРО")
    scene black_screen
    with Dissolve(1)
#    $ changeDayTime("day")

#    $ rain = True
#    $ rainIntencity = 1
#    $ lightning = False

    img 2792
    with fadelong
    music Power_Bots_Loop
    cashier "КТО ВЫ???"
    "ЧТО ВЫ ТУТ ДЕЛАЕТЕ???"
    "ВЫ ВОР???"
    "!!!"
    img 2793
    m "Я..."
    "Ээээ..."
    img 2794
    mt "Где я?"
    "Это магазин?"
    "Что я делаю здесь?"
    img 2795
    cashier "Я ЕЩЕ РАЗ СПРАШИВАЮ, ЧТО ВЫ ЗДЕСЬ ДЕЛАЕТЕ!!!"
    img 2796
    mt "Что я делаю в магазине?"
    "Где Юлия?"
    "..."
    img 2797
    music Groove2_85
    mt "О БОЖЕ!!!"
    "Я ВСЕ ВСПОМНИЛА!!!"
    "Я проспала!"
    "Мне надо было проснуться раньше и тихо уйти."
    "Но я так устала!"
    "У меня не было сил."
    "Я отключилась и проспала до утра."
    "Пришла продавец и нашла меня!"
    "Спящую в примерочной!"
    "Какой позор, Моника!"
    "Как же ты вляпалась во все это?"
    img 2798
    music Power_Bots_Loop
    cashier "Я ВЫЗЫВАЮ ПОЛИЦИЮ!"
    img 2799
    mt "Что?"
    "Полицию?"
    "О БОЖЕ!!!"
    "Мне нельзя в полицию!!!"
    "Что же делать?"
    "..."
    img 2800
    music Groove2_85
    mt "Так, Моника. Стоп."
    "Да, ты заснула в примерочной."
    "Но с тобой говорит какая-то жалкая продавец."
    "А ты девушка с обложки модного журнала."
    "В платье, которое стоит дороже, чем все что есть в этом магазине."

# clothShopCashierOffended2 = False #Общаться с продавцом грубо. при покупке
# clothShopCashierOffended3ReturnDress = False # возвращение платья
    if clothShopCashierOffended2 == True or clothShopCashierOffended3ReturnDress == True:
        "И какая-то мелюзга на меня смеет кричать???"
    else:
        "И на меня кричит продавец, к которому я отнеслась по человечески?"
        "Была добра к ней."

    label gallery_after_jail_cloth_shop_cashier9_menuloop1:
        menu:
            "Полиция придется как раз кстати! Ты, сучка!":
                label gallery_2815:
#                $ clothShopCashierFirstNightOffended = True
                music Pyro_Flow;
                img 2801
                m "Кто вы?"
                img 2802
                cashier "Кто я?"
                "Я продавец в этом магазине!"
                "А кто вы?"
                "И что вы здесь делаете???"
                img 2803
                "Я вызываю полицию!"
                img 2804
                m "Вызывай!"
                "Давай!"
                "Попробуй!"
                "Полиция придется как раз кстати!"
                "Давай!"


                stop music fadeout 0.2
                sound highheels_run2
                img black_screen
                with fadelong
                $ renpy.pause(0.3)

                music Pyro_Flow
                img 2805
                with fadelong
                cashier "Почему вы на меня кричите?"
                img 2806
                m "Почему я кричу?"
                "Ты!!!"
                "Отвечай!"
                "Ты вчера работала???"
                img 2807
                cashier "Да, я. А что?"
                img 2808
                m "Отлично!"
                "Вызывай полицию."
                "Я напишу заявление!"
                img 2809
                cashier "Какое заявление?"
                img 2810
                m "Я вчера вечером пришла в этот чертов магазин, чтобы посмотреть себе гардероб."
                "Выбрала вещь."
                "Зашла в примерочную."
                "Потом мне видимо стало плохо."
                "И я потеряла сознание."
                img 2811
                "А ты!"
                "МЕЛКАЯ СУЧКА!!!"
#                call bitch(5, "clothShopCashierFirstNightOffended") from _call_bitch_113

                stop music fadeout 0.2
                sound highheels_run2
                img black_screen
                with fadelong
                $ renpy.pause(0.3)
                music Pyro_Flow

                img 2812
                m "Ты!"
                "Сучка!"
                "Даже не заметила меня!"
                "И не оказала мне помощь!"
                "Не вызвала медиков!"
                img 2813
                "У тебя!"
                "В твоем магазине всю ночь пролежал человек!"
                "Без сознания!!!"
                "А если бы я умерла!!"
                img 2814
                cashier "Мэм."
                "Прошу прощения, я..."
                img 2815
                m "ЧТО? ТЫ???"
                "Если ты сейчас же не извинишься передо мной, мелкая тварь!"
                "То я засужу тебя с твоим магазином!"
                "Вы будете до конца дней платить по моим искам!"
                "Ясно тебе!!!"
                "Ты вообще знаешь кто я такая???"
                cashier "Мэм."
                "Я..."
                img 2816
                with fade
                m "Быстро извинилась передо мной!"
                img 2817
                cashier "Мэм."
                "Я извиняюсь перед Вами от своего имени и от имени магазина."
                "Впредь обещаю что мы будем более внимательными к посетителям."
                "И такой ситуации больше не повторится."
                img 2818
                "Пожалуйста, простите нас!"
                img 2819
                m "То-то же!"
                "Запомни мою доброту!"
                "Но учти!"
                "Что я прощаю только один раз!"
                "На второй моего великодушия точно не хватит!"
                img 2820
                cashier "Мэм."
                "Прошу прощения еще раз..."

            "В этом нет необходимости. Я всего-лишь клиент." if clothShopCashierOffended2 == False and clothShopCashierOffended3ReturnDress == False:
#                $ clothShopCashierFirstNightOffended = False
#                call bitch(-5, "clothShopCashierFirstNightOffended") from _call_bitch_114
                music Stealth_Groover
                #render+
                #Моника вежливо говорит с продавщицей в магазине с утра
                img 2801
                m "Кто вы?"
                img 2802
                cashier "Кто я?"
                "Я продавец в этом магазине!"
                "А кто вы?"
                "И что вы здесь делаете???"
                img 2803
                "Я вызываю полицию!"
                img 5638
                m "В этом нет необходимости."
                img 5639
                cashier "Почему?"
                img 5640
                m "Потому что я не вор."
                img 5641
                "Посмотрите на меня, Вы меня не узнаете?"
                img 5642
                cashier "Вы... кажется я Вас уже видела..."
                img 5643
                m "Да, я недавно посещала ваш магазин. С обстоятельным джентельменом."
                "Я ваш особый клиент!"
                img 5644
                cashier "Да, я помню, но Вы вернули платье..."
                m "Да, формальности, но зато я относилась к Вам вежливо, разве Вы не помните?"
                img 5645
                cashier "Да, Мэм."
                "Я помню. Спасибо за вежливость."
                "..."
                "Мэм, но что Вы здесь делаете?"
                img 5646
                m "Я пришла сюда примерить другое платье вчера."
                "Мне было жаль что я вернула вам то платье."
                "Меня немного терзало чувство вины и..."
                img 5647
                cashier "Спасибо, Мэм!"
                img 5648
                m "Да, и я, по всей видимости, потеряла сознание прямо в примерочной."
                "Не знаю как это случилось, но я очнулась прямо сейчас перед вами."
                "Наверное это из-за похудения."
                "У меня очень строгая диета, вы, наверное, понимаете меня..."
                img 5649
                cashier "Да, я понимаю Вас, Мэм!"
                "Я действительно не проверяла примерочную вчера перед уходом."
                img 5650
                "Это моя вина. Я должна была обнаружить вас!"
                "И оказать помощь!"
                img 5651
                "Простите меня!"
                img 5652
                m "Ничего страшного, я не в обиде на вас."
                "В следующий раз будьте внимательны."
                img 5653
                cashier "Да, Мэм! Конечно!"
                img 5654
                cashier "..."
                img 5655
                "Мэм... А Вы будете покупать другое платье, как хотели?"
                img 5656
                mt "Хм... Какое другое платье???"
                "Моника, у тебя сейчас другие проблемы!!!"
                "КАКОЕ К ЧЕРТУ ПЛАТЬЕ!!!"
                img 5657
                m "Хм... Видите-ли."
                "Я себя неважно чувствую."
                img 5658
                "У меня уже нет настроения для покупок."
                "Может быть в следующий раз."
                img 5659
                cashier "Конечно, Мэм!"
                "До свидания!"
                m "До свидания..."

            "В этом нет необходимости. Я всего-лишь клиент. (disabled)" if clothShopCashierOffended2 == True or clothShopCashierOffended3ReturnDress == True:
                jump gallery_after_jail_cloth_shop_cashier9_menuloop1

        img 2821
        with fadelong
        mt "Надо идти к Дику."
        "Надо быстрее закончить этот кошмар!"
#        $ remove_objective("look_dressroom")
#        $ remove_objective("find_sleep")
#        $ add_objective("dick_search", _("Идти к Дику в офис."), c_blue, 5)
#        $ autorun_to_object("street_cloth_shop_s2", "afterJailDay2_clothShopStreet1")

#        $ s2ClothShopStage = 4
#        $ clothShopCashierTalkStage = 2
#        $ clothShopCashierAtCashDesk = True
#        $ gameSubStage = 1
#        call change_scene("cloth_shop_view1_s2", "Fade", False) from _call_change_scene_188

#    scene black_screen
#    with Dissolve(1)
#    call textonblack_long("The End of V0.4\nYou could support me on Patreon if you like the game :)")
#    scene black_screen
#    with Dissolve(1)
#    $ renpy.full_restart(transition=Fade(1.0, 1.0, 1.0))
    return

label gallery_1422:
    music casualMusic
    img 1422
    m "Дик."
#    call bitch(3, "waitressMonicaOffended1") from _call_bitch_120
#    $ waitressMonicaOffended1 = True
    "Меня утомила эта стерва."
    img 1423
    dick "..."

    img 1424
    m "Девушка!"
    "То что вы скоро закрываетесь."
    "Это очень плохо."
    "Вам следовало бы работать когда приходят такие гости как мы."
    img 1425
    waitress "Мэм."
    "Прошу прощения."
    "Но это не в моей компетенции."
    img 1426
    m "Конечно не в твоей."
    "В компетенцию официантки вообще ничего не входит."
    "Только приносить еду, которую она даже не готовит."
    "Потому что не умеет."
    "А также в компетенции убирать объедки."
    "Большего от тебя никто не ждет."

    "..."
    img 1427
    m "Дик!"
    dick "Да, дорогая."
    m "Давай уйдем отсюда."
    "Мне не нравится это место."
    "Но ваш заказ уже готов."
    img 1428
    dick "Хорошо, дорогая."
    "Как скажешь."
    "Можем уйти."
    img 1429
    m "Да, и я запрещаю тебе платить."
    img 1431
    w
    menu:
        "Уволь эту дуру.":
            img 1430
            m "А, и еще."
            "Дик."
            img 1432
            dick "Да, дорогая."
            img 1433
#            call bitch(5, "waitressMonicaFired") from _call_bitch_121
#            $ waitressMonicaFired = True
            m "Уволь эту дуру."

            "В следующий раз, когда мы придем."
            "Ее здесь не должно быть."
            img 1434
            dick "Хорошо, дорогая."
            "Как скажешь. (улыбается)"

            img 1435
            waitress "Про что это они???"
            "Да как они смеют?"
            img 1436
            m "Пойдем, Дик!"
            dick "Пойдем, дорогая."

        "Пойдем, Дик!":
            img 4689
            m "Пойдем, Дик!"
            dick "Пойдем, дорогая."
    return

label gallery_4690:
    music Last_Kiss_Goodnight
    img 4672
    m "Уже правда так поздно?"
    waitress "Да, Мэм."
    img 4673
    "Если честно, ресторан давно закрыт."
    m "Значит по этой причине мы сидим здесь одни?"
    waitress "Да, Мэм.
    Гостей уже не пускают сюда.
    Для вас сделано исключение."
    "Простите что напомнила вам о времени.
    Больше такого не повторится."
    "Я сейчас же принесу Ваш заказ."
#    call bitch(-3, "waitressMonicaOffended1") from _call_bitch_122
    img 4671
    m "Не стоит беспокоиться.
    Мы уже уходим."
    "Я не люблю сидеть в пустых ресторанах."
    img 4675
    m "Дик, ты не против если мы пойдем?"
    dick "Аэээмм.. Нет, Моника, я не против..."
    menu:
        "Оставить чаевые...":
            img 4670
            m "Девушка!"
            "Судя по вашему виду, вы, наверное, работали с самого утра?"
            waitress "Да, Мэм.
            У меня уже неделю не было выходных."
            "Уже поздно и мне завтра снова на работу с самого утра."
            img 4676
            m "Ясно."
            "Деточка, видишь-ли, я пытаюсь доказать всем что я добрая и что я не тиран."
            img 4675
            "Я ведь не тиран, Дик?"
            dick "Нет, Моника!
            Конечно нет!"
#            call bitch(-5, "waitressMonicaTips") from _call_bitch_123
#            $ waitressMonicaTips = True
            img 4670
            m "Вот. Поэтому этот мужчина с радостью оставит Вам в качестве чаевых ваш месячный оклад."
            img 4678
            m "Дик, ты ведь сделаешь это?"
            img 1432
            dick "(Дик поперхнулся)
            Эгхммм... Моника..."
            m "..."
            dick "Конечно, с радостью.
            Я думаю эта девушка заслуживает поощрения."
            img 4675
            m "То-то же."
            img 4691
            m "Пойдем, Дик!"
            dick "Пойдем, дорогая."

        "Уйти...":
            img 4690
            m "Пойдем, Дик!"
            dick "Пойдем, дорогая."
    return

label gallery_2684:
    music Stealth_Groover
    img 2658
    with fadelong
    reception "Здравствуйте, Мэм!"
    img 2659
    m "Здравствуйте."
    "Я хочу переночевать в этом месте."
    img 2660
    reception "Конечно, Мэм!"
    "Добро пожаловать!"
    "У нас лучший отель в городе!"
    img 2661
    m "Вот и посмотрим какой он."
    "Внешне он не выглядит лучшим."
    img 2662
    "Я уже вижу много недостатков."

    img 2663
    reception "Да, Мэм!"
    "Я понимаю."
    "Судя по Вам, Вы искушены в хороших отелях."
    "Вы, наверное, много где бывали и ..."
    img 2664
    m "Да, я много где бывала."
    "И хватит об этом!"
    "Давайте быстрее заселяйте меня!"
    "Не испытывайте моего терпения!"
    img 2665
    reception "... и мы стараемся держать уровень.."
    "Гхм.."
    img 2666
    "Мэм."
    "Да, конечно."
    "Сейчас мы Вас оформим."
    "Чем Вы будете платить?"
    "Наличными или картой?"

    img 2667
    with hpunch
    music Groove2_85
    m "Ээээээ.."
    "Ммммм.."
    img 2668
    music Power_Bots_Loop
    mt "!!!!!!!!!!!!!!!!"
    "У меня же нет денег!!!"
    img 2669
    "Черт!"
    "Черт, черт, черт!!!"
    "У меня все забрали в полиции!"

    img 2670
    music Groove2_85
    mt "Это совершенно не знакомое мне чувство!"
    "Я никогда не сталкивалась с проблемой того что на что-то нет денег."
    img 2671
    "Это стресс."
    "Мне надо будет походить к психотерапевту, поделать расслабляющие массажи и СПА."
    "..."
    img 2672
    "Но что сейчас-то делать?"
    img 2673
    with fade
    m "Видите-ли."
    "Дело в том что я только что из аэропорта."
    "Там произошла задержка багажа."
    "И мне привезут его утром."
    "Потому оплату я внесу во время утреннего завтрака."
    img 2674
    mt "С утра что-нибудь придумаю!"
    "А сейчас я мечтаю о нормальной постели!"
    "Мягкой и теплой!"
    img 2675
    "И еда!!!"
    "Я хочу есть!"
    img 2676
    reception "Мэм."
    "Я даже не знаю...."
    img 2677
    music Pyro_Flow
    m "Послушайте."
    "Взгляните на меня."
    "Вы считаете что у меня нет денег на вашу дыру?"
    img 2678
    reception "Нет, Мэм."
    "Конечно."
    "Вы выглядите очень респектабельно..."
    img 2679
    m "И вы собираетесь мне отказать?"
    img 2680
    "Вы в курсе какие рейтинги у моего аккаунта в сервисах размещения?"
    img 2681
    "Если вы откажете мне, то я красочно опишу эту ситуацию!"
    img 2682
    "Другие отели готовы будут бесплатно забрать меня отсюда на такси, лишь бы я осталась у них!"
    img 2683
    "И оставила хороший отзыв!"
    img 2684
    "В котором, кстати, могу упомянуть грамотного сотрудника рецепшина."
    img 2685
    "Который заслуживает повышения по службе!"
    img 2686
    reception "Мэм, спасибо, но..."
    "..."
    img 2687
    m "..."
    music Groove2_85
    img 2688
    reception "Хорошо, Мэм!"
    "Я заселю Вас под свою ответственность."
    img 2689
    m "Сразу бы так!"
    img 2690
    music Groove2_85
    reception "Мэм."
    "Пожалуйста, Ваши документы."
    img 2691
    reception "..."
    img 2692
    m "..."
    img 2693
    reception "..."
    img 2694
    m "..."
    img 2695
    reception "Мэм?"
    img 2696
    with fade
    music Power_Bots_Loop
    mt "О Боже!"
    "Я совсем забыла!"
    "У меня же нет документов с собой!"
    img 2697
    "Более того, у меня нет вообще никаких!"
    "НИКАКИХ!!!!!"
    "О БОЖЕ!!!"
    "..."
    img 2698
    music Groove2_85
    mt "Моника!"
    "Не вешай нос!"
    "Ты выбралась из такого кошмара не для этого!"
    "Ты выпутаешься из всего этого!"
    img 2699
    "И будешь на обложке своего журнала!"
    "Блестая женской красотой."
    "..."
    img 2700
    "А не на обложке с каким-то питомцем, который в меня входит..."
    img 2701
    music Power_Bots_Loop
    mt "О БОЖЕ!!!"
    "Я не могу об этом думать!"
    "Я не буду думать об этом!"
    "Эти мысли вселяют в меня ужас!"
    img 2702
    mt "..."
    img 2703
    music Groove2_85
    reception "Мэм?"
    "Вы себя хорошо чувствуете?"
    img 2704
    m "Да, все в порядке."
    img 2705
    reception "Ваши документы, Мэм?"
    img 2706
    m "Видите-ли..."
    "Мои документы тоже были в том чемодане, который должны привезти..."
    img 2707
    "И я... ээээ..."
    img 2708
    reception "Мэм."
    "Откуда был Ваш рейс?"
    img 2709
    m "Из Парижа."
    img 2710
    reception "Значит Вы проходили пограничный контроль?"
    img 2711
    m "Ээээ... ддда..."
    img 2712
    reception "А как Вы могли пройти его без документов, Мэм?"
    "Если они были в Вашем чемодане."
    img 2711
    m "..."
    img 2713
    "Да, вы правы."
    "Они были не в чемодане."
    "Я сказала вам так чтобы упростить ситуацию."
    "Они были в сумочке, которую я забыла в такси и..."
    img 2714
    with hpunch
    reception "Мэм, Вы приехали на такси?"
    img 2715
    m "Ну конечно на такси!"
    "А как же еще???"
    img 2716
    reception "Мэм."
    "У меня здесь камеры наблюдения."
    "Я видела как Вы подходили к отелю."
    "Вы шли пешком под дождем."
    img 2717
    with fade
    music Power_Bots_Loop
    m "..."
    mt "!!!!!!"
    img 2718
    reception "????"
    "Мэм?"
    "Вы точно приехали на такси?"
    "Вы говорите правду?"
    img 2719
    stop music fadeout 1.0
    m "Я..."
    "Я... Конечно...."
    img 2720
    music Pyro_Flow
    "Конечно я говорю правду!"
    "Как Вы смели сомневаться в этом!!!"
    "Жалкий сотрудник рецепшина!"
    "Какого-то задрипанного отеля!"
    img 2721
    music Groove2_85
    reception "Мэм."
    "Я знаю что Вы говорите неправду."
    "На моих камерах точно видно что Вы не приехали на такси."
    "Смею предположить что и все остальное что Вы говорили - это тоже неправда."
    "Я вынуждена отказать Вам в заселении."
    img 2722
    music Pyro_Flow
    m "ЧТО???"
    "АХ ТЫ МЕРЗКАЯ ТВАРЬ!!!"
    img 2724
    "Я УВОЛЮ ТЕБЯ!!!"
    "Я ТЕБЯ УНИЧТОЖУ!!!"
    img 2723
    "МЕЛКИЙ ПАРАЗИТ!!!"
    "НИКЧЕМНЫЙ! БЕСПОЛЕЗНЫЙ!"
    "ПАРАЗИТ!!!"
    img 2725
    music Groove2_85
    reception "..."
    "Мэм."
    "Знаете что."
    "Ваше поведение."
    "Ваши истории."
    "Мелкий уровень лжи, который легко обличается."
    "Вы непохожи на леди."

    img 2726
    "Вы больше похожи на шлюху."
    "Именно они, когда приходят, так себя ведут."
    if jailCageBlackmailMonicaSaidSheIsAWhore == True:
        img 5624
        w
        music prison_yell_music
        img black_screen
        with Dissolve(1)
        # хорошая шлюха
        img 5430
        with fade
        m "Я хорошая шлюха..."
        img 5432
        with fade
        prisoner1 "Громче! Мы не слышим!"
        m "Я хорошая шлюха!"
        img 5436
        with fadelong
        prisoner1 "Громче! Громко и ясно!"
        m "Я ХОРОШАЯ ШЛЮХА!!!"
        img black_screen
        with Dissolve(1)
        music Groove2_85
        img 5624
        with fade
        w

    img 2727
    with fadelong

    reception "А шлюхам у нас вход запрещен."
    img 2728
    reception "Единственное что меня смущает - это Ваше платье."
    img 2729
    "Оно дорогое, но неизвестно где Вы его взяли."
    img 2730
    music Pyro_Flow
    m "ЧТО???"
    "ДА КАК ТЫ СМЕЕШЬ ТАК СО МНОЙ РАЗГОВАРИВАТЬ!!!"
    "ПОЗОВИ СВОЕГО БОССА!!!"
    img 2731
    music Groove2_85
    reception "Мэм."
    "Сейчас в здании за старшую нахожусь я."
    "Я могу дать Вам телефон своего начальника и завтра Вы с ним свяжетесь."
    "Однако в заселении я Вам отказываю."
    img 2732
    music Pyro_Flow
    m "Я СЕЙЧАС ПОЗВОНЮ ТВОЕМУ БОССУ!!!"
    "Я РАЗБУЖУ ЕГО!!!"
    "МЕЛКОГО ЗАСРАНЦА!!!"
    "КОТОРЫЙ ДЕРЖИТ НА РАБОТЕ ТАКИХ НЕРАДИВЫХ СУЧЕК!"
    img 2733
    music Groove2_85
    reception "Мэм."
    "Мне неинтересно как меня оскорбляет какая-то шлюха."

    img 2734
    music Pyro_Flow
    m "ДАВАЙ НОМЕР!!!"
    "СЕЙЧАС ЖЕ!!!"
    "Я ПОКАЖУ ТЕБЕ КТО ИЗ НАС ШЛЮХА!!!"
    img 2735
    music Groove2_85
    reception "Мэм."
    "Пожалуйста."
    "Возьмите его визитку."
    img 2736
    music Pyro_Flow
    m "НУ ВСЕ!!!"
    "ДЕРЖИСЬ!!!"
    "Я ЗВОНЮ ЕМУ!!!"
    img 2737
    "..."
    "Сейчас!"
    "..."
    "Уже почти набираю!!!"
    img 2738
    music Power_Bots_Loop
    mt "ЧЕРТ!!!"
    "ГДЕ МОЙ ТЕЛЕФОН???"
    img 2739
    "ОН ОСТАЛСЯ В ПОЛИЦИИ!!!"
    "ДЬЯВОЛ!!!"
    img 2740
    music Pyro_Flow
    m "Давай телефон сюда!"
    "Быстро!"
    img 2741
    reception "Мэм."
    "Служебный телефон может использоваться только для рабочих звонков."
    img 2742
    m "!!!!!!"
    "..."
    img 2743
    "!!!!!!!!"
    "..."
    "..."
    img 2744
    m "Я уйду!"
    "И напишу жалобу!"
    img 2745
    "Ты пожалеешь об этом!"
    img 2746
    music Groove2_85
    reception "Мэм."
    "Всегда рады видеть Вас!"
#    $ hotelVisited = True
#    $ richHotelReceptionistMode = 2
#    if dickSearch == True and homeVisited == True and hotelVisited == True:
#        $ s2ClothShopStage = 1

#    call refresh_scene_fade() from _call_refresh_scene_fade_95
    return
