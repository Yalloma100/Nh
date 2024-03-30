
# ----------------------------
from googletrans import Translator, LANGUAGES


def detect_language(text):
    translator = Translator()
    detection = translator.detect(text)
    return detection.lang


def text_translator(text, src=None, dest='en'):
    if not src:
        src = detect_language(text)

    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)

        return translation.text
    except Exception as ex:
        return ex


def main():
    prompt = "Hola"
    detected_lang = detect_language(prompt)
    print(f"Виявлена мова: {LANGUAGES[detected_lang]}")
    translated_text = text_translator(prompt, src=detected_lang)
    print(f"Переклад на українську: {translated_text}")


if name == "main":
    main()
