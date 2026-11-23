# Документация Geometric Lib Tests

## Общее описание

**Geometric Lib** — лабораторная работа на Python для вычисления площади и периметра геометрических фигур.

Каждая фигура описана в отдельном модуле. Функции принимают числовые параметры и возвращают результат вычислений. Работа функций проверяется unit-тестами на `unittest`.

**Поддерживаемые фигуры:**

- Круг — `circle.py`
- Квадрат — `square.py`
- Прямоугольник — `rectangle.py`
- Треугольник — `triangle.py`

---

## Math formulas

### Area

- **Circle:** S = πR²
- **Rectangle:** S = ab
- **Square:** S = a²
- **Triangle:** S = ah / 2

### Perimeter

- **Circle:** P = 2πR
- **Rectangle:** P = 2a + 2b
- **Square:** P = 4a
- **Triangle:** P = a + b + c

---

## Описание функций

### circle.py

| Функция | Параметры | Результат |
|---|---|---|
| `area(r)` | `r` — радиус | площадь круга |
| `perimeter(r)` | `r` — радиус | длина окружности |

```python
import circle
circle.area(2)       # 12.566370614359172
circle.perimeter(2)  # 12.566370614359172
```

### square.py

| Функция | Параметры | Результат |
|---|---|---|
| `area(a)` | `a` — сторона | площадь квадрата |
| `perimeter(a)` | `a` — сторона | периметр квадрата |

```python
import square
square.area(3)       # 9
square.perimeter(3)  # 12
```

### rectangle.py

| Функция | Параметры | Результат |
|---|---|---|
| `area(a, b)` | `a`, `b` — стороны | площадь прямоугольника |
| `perimeter(a, b)` | `a`, `b` — стороны | периметр прямоугольника |

```python
import rectangle
rectangle.area(2, 3)       # 6
rectangle.perimeter(2, 3)  # 10
```

### triangle.py

| Функция | Параметры | Результат |
|---|---|---|
| `area(a, h)` | `a` — основание, `h` — высота | площадь треугольника |
| `perimeter(a, b, c)` | `a`, `b`, `c` — стороны | периметр треугольника |

```python
import triangle
triangle.area(4, 3)          # 6.0
triangle.perimeter(3, 4, 5)  # 12
```

---

## 🧪 Тестирование

Тесты написаны на стандартном модуле **unittest**, внешние зависимости не нужны.

| Файл тестов | Класс | Кол-во тестов | Проверяемые случаи |
|---|---|:---:|---|
| `test_circle.py` | `CircleTestCase` | 7 | нулевой радиус, r = 1, r = 2, дробный радиус |
| `test_rectangle.py` | `RectangleTestCase` | 7 | нулевая сторона, равные и разные стороны, дробные значения |
| `test_square.py` | `SquareTestCase` | 6 | нулевая сторона, целая и дробная сторона |
| `test_triangle.py` | `TriangleTestCase` | 6 | нулевая высота, дробный результат, прямоугольный и равносторонний треугольники |
| **Итого** | | **26** | |

**Запуск всех тестов:**

```bash
python3 -m unittest -v
```

**Запуск тестов одной фигуры:**

```bash
python3 -m unittest test_rectangle.py
```

**Ожидаемый результат:**

```
Ran 26 tests in 0.001s

OK
```

---

## История изменений

| Хеш коммита | Описание |
|---|---|
| 7e31201 | Add unit tests |
| a438e37 | Add geometry modules |