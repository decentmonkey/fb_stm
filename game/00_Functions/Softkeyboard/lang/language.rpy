init -1000 python:
    # 言語とフォントの定義
    # Language & Font definitions
    langs = ["en"]
    ml_langs = {}
    ml_langs["en"] = "{font=DejaVuSans.ttf}English{/font}"
#    ml_langs["jp"] = "{font=lang/jp/VL-PGothic-Regular.ttf}日本語{/font}"

    def ml_GetLangName(lang):
        return ml_langs[lang]

    def ml_ChangeLang(newLang):
        persistent.lang = newLang
        lang = newLang

label language_picker:
scene black

#EOF
