# Horse clicker
Jest to projekt, który został stworzony, aby zaoszczędzić trochę czasu na nudnych czynnościach wykonywanych w grze howrse. Polega on na podstawowej opiece nad końmi, wykorzystując do tego rozpoznawanie elementów na ekranie.

## Spis treści
1. Technologie.
2. Funkcje programu.
3. Przykład działania programu.
4. Czym jest howrse?
5. Plany na rozwój projektu.

## 1. Technologie.
Język programowania użyty w programie:
 - Python 3.10
 
Biblioteki i frameworki użyte w programie:
 - pyautogui
 - opencv-python
 - pillow
 - time
 - random
 - os
 - sys
 - datetime
 - pyshortcuts
 - flask (tylko test)
 - pytesseract (tylko test)
 - tesseract (tylko test)
 - tesseract-ocr (tylko test)
 
 
 ## 2. Funkcje programu.
 Program ma przede wszystkim za zadanie wykonać kilka podstawowych czynności związanych z zajmowaniem się końmi.
 Są to kolejno: rejestracja do ośrodka, nakarmienie, oporządzenie, położenie spać oraz przejście do następnego konia.
 
 Każda z funkcji ma za zadanie rozpoznać, czy na stronie, którą mamy otworzoną, znajduje się obrazek przedstawiający jedno z zadań, którą ma wykonać program. Przykładowo może znaleźć, czy koń został nakarmiony. Jeśli nie jest nakarmiony, clicker go nakarmi, jak jest, to przejdzie do dalszych czynności.
 
 Oprócz podstawowych funkcji wymienionych wyżej, Horse clicker może wrócić do oporządzania po śmierci jednego z koni. Oprócz tego na początku można wybrać parę opcji, które odpowiadają za to, jak program ma dokładnie działać - są to: ilość koni do oporządzenia, posiadanie konta VIP - jest to uprzywilejowane konto w tej grze - oraz czy chcemy, by konie były kładzone spać (jest to związane z tym, że niektórzy gracze posiadają specjalnego konia, który kładzie spać konie po oporządzeniu go, wtedy funkcja sleep nie jest już potrzebna.)
 
 ## 3. Przykład działania programu.
 ![horse-clicker](https://github.com/Halcik/Horse-clicker/assets/45713520/57793092-19f2-4d60-9e52-303ff0fb7a55)

 
 ## 4. Czym jest howrse?
 Howrse to jedna z wielu gier, które są dostępne dla milionów graczy w Internecie. Jest to gra przeglądarkowa, która polega na opiece nad własnymi końmi, prowadzeniu ośrodka jeździeckiego oraz rozwijaniu ras koni.
 ### Czy używanie tego clickera jest bezpieczne?
 To coś, co chciałabym zaznaczyć na starcie. Używanie go jest tylko i wyłącznie na własną odpowiedzialność. Programy takiego typu są niedozwolone w grze, a gracze, którzy zostaną przyłapani na ich użytkowaniu, są banowani.
 
 ## 5. Plany na rozwój projektu.
 Jest to projekt, który ciągle się rozwija. Mam do niego jeszcze sporo planów.
 Rzeczy, które planuję dodać lub poprawić w najbliższych miesiącach:
   - stworzenie strony działającej tylko na lokalnym komputerze, która ułatwiłaby obsługę programu (planowane połączenie flaska i formularzy). Służyłoby to do wybierania początkowej konfiguracji w programie - *w trakcie tworzenia*
  - wgrywanie zdjęć przycisków w razie niezgodności
  - udoskonalanie karmienia bez specjalnego konta VIP
  - ogarnianie wielu kont bez konieczności włączania od nowa programu
  - wysyłanie gdzieś powiadomienia lub odtworzenie dźwięku, by wiedzieć o skończeniu działania programu.
 
 
