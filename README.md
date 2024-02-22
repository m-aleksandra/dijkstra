# Wizualizacja algorytmu Dijkstry z wykorzystaniem kopca

Projekt implementuje wizualizację algorytmu Dijkstry, wykorzystując kopiec do efektywnego znajdowania najkrótszej ścieżki w grafie.

## Klasa Dijkstra

### `__init__(self, G, pos, src)`
Konstruktor klasy przyjmuje trzy argumenty:
- `G`: Graf, na którym będzie wykonywany algorytm Dijkstry, reprezentowany przez obiekt `networkx.Graph`.
- `pos`: Pozycje wierzchołków grafu, używane do ich wizualizacji. Może być to słownik zdefiniowany przez użytkownika lub wynik funkcji `networkx` do rozmieszczania wierzchołków, np. `networkx.spring_layout(G)`.
- `src`: Wierzchołek startowy algorytmu Dijkstry.

### `_dijkstra_step(self) -> bool`
Metoda wykonująca pojedynczy krok algorytmu Dijkstry. Zwraca `True`, jeśli algorytm może kontynuować, lub `False`, gdy kolejka priorytetowa jest pusta, co oznacza zakończenie algorytmu.

### `animate(self, i) -> None`
Metoda wywoływana na każdym kroku animacji, odpowiedzialna za aktualizację wizualizacji grafu. Koloruje wierzchołki i krawędzie w zależności od ich statusu w algorytmie (np. wierzchołek aktualnie przetwarzany jest zielony, odwiedzone są niebieskie).

### `dijkstra(self, visualise=True) -> int`
Metoda uruchamiająca algorytm Dijkstry. Jeśli `visualise` jest ustawione na `True`, algorytm jest wizualizowany. Zwraca słownik odległości od wierzchołka startowego do pozostałych wierzchołków.

### `recreate_path(self, target, visualise=True) -> List[int]`
Metoda odtwarzająca i wizualizująca najkrótszą ścieżkę od wierzchołka startowego do wierzchołka docelowego `target`. Gdy `visualise=True` koloruje ścieżkę i odpowiednie krawędzie, aby zaznaczyć wyznaczoną trasę. Zwraca listę ze ścieżką.

## Klasa PriorityQueue

### `__init__(self)`
Konstruktor klasy inicjalizuje pustą listę `heap`, która będzie przechowywać krotki `(dystans, wierzchołek)`. Dystans jest wykorzystywany jako klucz do ustalania priorytetu w kopcu.

### `empty(self) -> bool`
Metoda zwraca `True`, jeśli kopiec jest pusty, w przeciwnym razie zwraca `False`. Umożliwia sprawdzenie, czy w kolejce priorytetowej są jeszcze jakieś elementy.

### Metody pomocnicze
- `_parent(self, i) -> int`
- `_left_child(self, i) -> int`
- `_right_child(self, i) -> int`
- `_swap(self, i, j) -> None`
- `_heapify_up(self) -> None`
- `_heapify_down(self) -> None`

### `push(self, item) -> None`
Dodaje nowy element `item` do kopca i przywraca jego własności kopca minimalnego za pomocą metody `_heapify_up`.

### `pop(self) -> tuple`
Usuwa i zwraca element z kopca o najniższym priorytecie (najmniejszym dystansie). Przed zwróceniem elementu, metoda przywraca własności kopca za pomocą metody `_heapify_down`.

## Uruchomienie
Wymagane jest zainstalowanie bibliotek `matplotlib` oraz `networkx`. Następnie wystarczy uruchomić plik `run.py`. Dwa przykłady grafów są stworzone w pliku `graph_examples.py` i importowane do `run.py`.

![Zrzut ekranu 2024-02-21 235455](https://github.com/m-aleksandra/dijkstra/assets/100863656/7e8c76f1-5274-4282-9d57-2fa8ea83e0d4)
