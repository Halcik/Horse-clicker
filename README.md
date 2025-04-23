# 🐴 Horse Clicker

**Horse Clicker** to narzędzie automatyzujące powtarzalne czynności w grze **Howrse**, takie jak karmienie koni czy zapisy do ośrodka. Program działa na zasadzie "clickera", wykorzystując rozpoznawanie elementów na ekranie.

> ⚠️ **Uwaga:** Użycie programu odbywa się **na własną odpowiedzialność**. Automatyzacja jest zabroniona przez regulamin gry Howrse i może skutkować **banem konta**. 

> ❌ **Projekt nie jest już rozwijany ani wspierany.** Udostępniam go wyłącznie jako inspirację.

---

## 🔧 Technologie

**Język programowania:**  
- Python 3.11

**Moduły zewnętrzne:**  
- `pyautogui` – znajdowanie obrazów i automatyzacja kliknięć  
- `pyshortcuts` – tworzenie skrótu do programu 
- *(testowo)*: `pillow`, `flask`, `pytesseract`

**Moduły standardowe:**  
- `time`, `random`, `os`, `sys`, `datetime`

---

## ▶️ Jak uruchomić

Są dwie opcje, by to zrobić:

### 1. Przez `settings.py`  
Tworzy skrót na pulpicie i instaluje wymagane moduły:
```bash
python settings.py
```

### 2. Ręcznie:
Zainstaluj moduły:
```bash
pip install -r requirements.txt
```
> ⚠️ **Uwaga:** Nie zaleca się ręcznej instalacji modułów.  
> Program korzysta ze specyficznej wersji `pyscreeze` (sprzed wprowadzenia błędu przy braku dopasowania obrazu).  
> Aby uniknąć problemów, użyj `settings.py` lub zainstaluj moduły zgodnie z `requirements.txt`.


Następnie uruchom:
```bash
python main.py
```

**Uwaga:**  
- W przeglądarce musi być otwarta karta z **dowolnym koniem w gospodarstwie** - program działa w obrębie jednego gospodarstwa.  
- Po uruchomieniu w konsoli pojawią się pytania: liczba koni, VIP, czy kłaść spać. Te dane mogą zostać zapisane w pliku `account_setting.txt`.

---

## 🌐 Wersja testowa (webowa)

Możesz testowo uruchomić wersję lokalną z interfejsem przeglądarkowym:

```bash
python app.py
```

Uruchomi to prostą stronę (Flask) do konfiguracji działania programu.

---

## 🐎 Funkcje

Program automatyzuje:
- Rejestrację do ośrodka
- Karmienie
- Oporządzanie
- Kładzenie konia spać
- Przejście do kolejnego konia

Dodatki:
- Obsługa kont VIP i koni automatycznie usypiających
- Wznowienie działania po śmierci konia
- Zapis konfiguracji w `account_setting.txt`

---

## 🧩 Problemy z rozpoznawaniem obrazków?

Program **nie obsługuje skalowania strony**, więc:
- gra musi być ustawiona w takiej samej rozdzielczości jak podczas testów,
- jeśli coś nie działa, **można podmienić obrazki** w folderze `Image` – są to pliki `.jpg`.

---

## 🖼️ Przykład działania

![horse-clicker](https://github.com/Halcik/Horse-clicker/assets/45713520/57793092-19f2-4d60-9e52-303ff0fb7a55)

---

## O grze Howrse

**Howrse** to przeglądarkowa gra online, w której gracze opiekują się końmi, prowadzą ośrodek i hodują konie różnych ras.

---

## 💤 Stan projektu

Projekt nie jest już rozwijany. Może służyć jako:
- przykład automatyzacji GUI,
- inspiracja do własnych projektów.
