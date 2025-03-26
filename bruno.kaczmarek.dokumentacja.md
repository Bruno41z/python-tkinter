# Dokumentacja Testów Jednostkowych w C# dla Aplikacji WPF (XAML)

### Cel zadania
Celem dokumentacji jest opisanie procesu pisania testów jednostkowych dla aplikacji desktopowej WPF (Windows Presentation Foundation) napisanej w języku C#, przy użyciu frameworka xUnit.

---

## 1. **Wstęp**

### Czym są testy jednostkowe i dlaczego są ważne?
Testy jednostkowe polegają na testowaniu pojedynczych jednostek kodu (np. metod, funkcji) w izolacji. Są istotne, ponieważ:
- Umożliwiają wczesne wykrycie błędów.
- Zwiększają jakość kodu i wspierają refaktoryzację.
- Pomagają w utrzymaniu aplikacji na dłuższą metę.

### Opis frameworka xUnit i jego zastosowania w testowaniu aplikacji WPF
xUnit to popularny framework do testów jednostkowych w C#. Umożliwia łatwe pisanie testów, oferując asercje, uruchamianie testów oraz generowanie raportów. W aplikacjach WPF xUnit może być używane do testowania logiki biznesowej i sprawdzania poprawności reakcji na zmiany w interfejsie użytkownika.

---

## 2. **Tworzenie projektu testowego**

### Jak dodać nowy projekt testowy w Visual Studio?
1. Otwórz **Visual Studio**.
2. Kliknij **File > New > Project**.
3. Wybierz **xUnit Test Project**.
4. Ustaw projekt testowy w tej samej solucji, co główny projekt WPF.

### Konfiguracja frameworka testowego i dodanie referencji do głównego projektu
1. Kliknij prawym przyciskiem myszy na projekt testowy.
2. Wybierz **Add > Reference**, a następnie zaznacz główny projekt WPF.

---

## 3. **Instalacja niezbędnych bibliotek**

Aby zainstalować xUnit i wymagane pakiety, użyj poniższych komend:
```bash
dotnet add package xunit
dotnet add package xunit.runner.visualstudio
dotnet add package Microsoft.NET.Test.Sdk
```bash

## 4. **Uruchamianie testów**
W Visual Studio
Otwórz Test Explorer (Test > Windows > Test Explorer).

Uruchom testy klikając na Run All.

###Z terminala
Uruchom testy używając komendy:
**dotnet test**

