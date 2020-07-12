# AutomationPractice
Sample test automation project using Page Object Pattern.

## Narzędzia i biblioteki
- Python 3.8 (język programowania)
- Selenium
- Pytest

## Konfiguracja i uruchomienie testów
Instrukcja dotyczy systemu Windows.

1. Instalacja JDK np. OpenJDK 13 GA z https://jdk.java.net/archive (rozpakowanie pobranego archiwum, dodanie katalogu `bin` do zmiennej środowiskowej Path).
2. Instalacja Python 3.8.3 (https://www.python.org/downloads/release/python-383) (w trakcie instalacji należy zaznaczyć opcję dodania do zmiennych środowiskowych oraz instalacji pip)
3. (Opcjonalnie) Instalacja IDE PyCharm w celu otwarcia plików źródłowych (https://www.jetbrains.com/pycharm/download)
4. Instalacja przeglądarki Chrome
5. Pobranie Chromedriver w wersji odpowiadającej zainstalowanej wersji przeglądarki Chrome (https://chromedriver.chromium.org/downloads), dodanie katalogu z Chromedriver do zmiennej środowiskowej Path
6. Sklonowanie repozytorium
7. Otwarcie głównego katalogu projektu w wierszu poleceń Windows (cmd.exe) i instalacja wymaganych modułów (w tym Selenium): `pip install -r requirements.txt`
8. (Opcjonalnie) Edycja pliku `execution_scripts\run_all_tests_chrome.bat` w celu dostosowania ścieżek katalogów na pliki wynikowe (raport wykonania testów, screenshoty w przypadku błędu)
9. Uruchomienie pliku `execution_scripts\run_all_tests_chrome.bat` - wykonanie wszystkich testów
10. Raport z wykonania testów powinien zostać wygenerowany w katalogu wskazanym w skrypice `run_all_tests_chrome.bat`; jeżeli nie dokonano zmian w kroku 8. jest to: `C:\Reports\AutomationPractice\report.html`

Uwaga: po wykonaniu instalacji i edycji zmiennych środowiskowych możliwa jest konieczność restartu systemu


## Strukura projektu
Framework składa się z następujących katalogów i plików głównego poziomu:
- `domain` - klasy reprezentujące fragmenty domeny testowanej aplikacji
- `execution_scripts` - skryty pozwalające na konfigurację uruchomienia i uruchomienie testów poza IDE 
- `helpers` - klasy pomocnicze związane z technicznymi zagadnieniami procesu wykonywania testów
- `pages` - klasy stron implementujące wzorzec Page Object Model
- `tests` - klasy testów
- `conftest.py` - plik zawierający elementy wykorzystywane przez bibliotekę Pytest; w przypadku aktualnego stanu projektu jest to "fixture" odpowiedzialny za zarządzanie cyklem życia (tworzeniem i zamykaniem) instancji klasy WebDrivera selenium w jednym miejscu (jest on następnie przekazywany jako parametr wszystkich metod testowych) oraz "hook" wpinający się w moment nieudanej próby wykonania testu przez bibliotekę Pytest w celu wykonania screenshota stanu strony w przeglądarce w momencie wystąpienia problemu
- `config.py` - plik z konfiguracją uruchomienia testów (automatycznie generowany w przypadk użycia skryptu z katalogu execution_scripts)
- `driver_config.py` - klasa konfigurująca instancję WebDrivera Selenium
- `urls.py` - zbiór adresów podstron wykorzystywanych w testach
- `credentials.py` - plik zawierający dane logowania, w przypadku rzeczywistych testów nie powinien być dodany do repozytorium


## Zastosowane wzorce projekowe i koncepty
Przygotowane testy opierają się o wykorzystanie wzorca Page Object Model. 

Proces wykonania pojedynczego testu typowo odbywa się w następujących krokach:
1. Uruchomienie wykonania testu
2. Dostarczenie skonfigurowanej instancji WebDrivera Chrome jako parametr metody testowej; jest to automatycznie wykonywane przez bilbiotekę Pytest na bazie przygotowanego "fixture" (szczegóły powyżej, w opisie pliku `conftest.py`)
3. Utworzenie instancji klasy implementującej wzorzec Page Object Model
4. Nawigacja do adresu testowanej podstrony
5. Wykonanie założonego scenariusza testu przy użyciu operacji udostępnionych przez klasy implementujące Page Object Model
6. Wykonanie asercji, weryfikujących założenia testu

W ramach implementacji testów starano się podążąć za głównym paradygmatem wzorca POM mówiącym o odseparowaniu operacji dostępnych z perspektywy użytkownika (i używaniu ich w metodach testowych) od technicznych zagadanień testu. Zgodnie z koncepem wzorca POM, jedynymi wartościami zwracanymi przez publiczne metody klas go implementujących są dane łatwo interpertowalne z poziomu użytkownika końcowego testowanego systemu (typy proste, lub obiekty domenowe) lub instancje innych klas implementujących POM (jeżeli następuje przejście do fragmentu systemu opisywanego przez inny Page Object). Publiczne metody klas implementujących POM nigdy nie zwracają elemenów bilbioteki Selenium. W samej wewnętrznej implementacji poszczególnych metod klas Page Object starano skupić się bezpośrednio na operowaniu na elementach strony, przenosząc techniczne aspekty realizacji do klas pomocnicznych.
