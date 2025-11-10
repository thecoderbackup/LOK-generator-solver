# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
L L O K K K
L O K L K L
L K K O O O
K L O K J O
O L O K L K
L K O K L K
```

## Solution

```
L L O K K K
L O K L K L
L K K O O O
K L O K J O
O L O K L K
L K O K L K
```

### Step 1

Start: (3, 1), End: (3, 3), Sacrifice: (0, 4)

```
L L O K # K
L O K L K L
L K K O O O
K # # # J O
O L O K L K
L K O K L K
```

### Step 2

Start: (0, 1), End: (0, 3), Sacrifice: (3, 5)

```
L # # # # K
L O K L K L
L K K O O O
K # # # J #
O L O K L K
L K O K L K
```

### Step 3

Start: (4, 1), End: (4, 3), Sacrifice: (0, 5)

```
L # # # # #
L O K L K L
L K K O O O
K # # # J #
O # # # L K
L K O K L K
```

### Step 4

Start: (3, 0), End: (5, 0), Sacrifice: (4, 5)

```
L # # # # #
L O K L K L
L K K O O O
# # # # J #
# # # # L #
# K O K L K
```

### Step 5

Start: (1, 3), End: (5, 3), Sacrifice: (2, 2)

```
L # # # # #
L O K # K L
L K # # O O
# # # # J #
# # # # L #
# K O # L K
```

### Step 6

Start: (5, 1), End: (5, 4), Sacrifice: (3, 4)

```
L # # # # #
L O K # K L
L K # # O O
# # # # # #
# # # # L #
# # # # # K
```

### Step 7

Start: (1, 0), End: (1, 2), Sacrifice: (2, 1)

```
L # # # # #
# # # # K L
L # # # O O
# # # # # #
# # # # L #
# # # # # K
```

### Step 8

Start: (1, 5), End: (5, 5), Sacrifice: (0, 0)

```
# # # # # #
# # # # K #
L # # # O #
# # # # # #
# # # # L #
# # # # # #
```

### Step 9

Start: (1, 4), End: (4, 4), Sacrifice: (2, 0)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 2

## Generated Puzzle

```
# L L O K
J O K L J
K K K O L
O L O L O
L L L K K
```

## Solution

```
# L L O K
J O K L J
K K K O L
O L O L O
L L L K K
```

### Step 1

Start: (2, 4), End: (4, 4), Sacrifice: (4, 1)

```
# L L O K
J O K L J
K K K O #
O L O L #
L # L K #
```

### Step 2

Start: (0, 1), End: (2, 1), Sacrifice: (1, 4)

```
# # L O K
J # K L #
K # K O #
O L O L #
L # L K #
```

### Step 3

Start: (0, 2), End: (0, 4), Sacrifice: (1, 0)

```
# # # # #
# # K L #
K # K O #
O L O L #
L # L K #
```

### Step 4

Start: (2, 2), End: (4, 2), Sacrifice: (3, 3)

```
# # # # #
# # K L #
K # # O #
O L # # #
L # # K #
```

### Step 5

Start: (1, 3), End: (4, 3), Sacrifice: (3, 1)

```
# # # # #
# # K # #
K # # # #
O # # # #
L # # # #
```

### Step 6

Start: (2, 0), End: (4, 0), Sacrifice: (1, 2)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 3

## Generated Puzzle

```
L O K K #
K O L O L
O L K L O
L O O K K
K K O L O
```

## Solution

```
L O K K #
K O L O L
O L K L O
L O O K K
K K O L O
```

### Step 1

Start: (1, 4), End: (3, 4), Sacrifice: (2, 2)

```
L O K K #
K O L O #
O L # L #
L O O K #
K K O L O
```

### Step 2

Start: (1, 0), End: (1, 2), Sacrifice: (2, 3)

```
L O K K #
# # # O #
O L # # #
L O O K #
K K O L O
```

### Step 3

Start: (2, 1), End: (4, 1), Sacrifice: (2, 0)

```
L O K K #
# # # O #
# # # # #
L # O K #
K # O L O
```

### Step 4

Start: (3, 0), End: (3, 3), Sacrifice: (0, 2)

```
L O # K #
# # # O #
# # # # #
# # # # #
K # O L O
```

### Step 5

Start: (0, 0), End: (0, 3), Sacrifice: (4, 4)

```
# # # # #
# # # O #
# # # # #
# # # # #
K # O L #
```

### Step 6

Start: (4, 0), End: (4, 3), Sacrifice: (1, 3)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 4

## Generated Puzzle

```
L L O K K
L K O L O
# L L K L
O O O O L
L K K L O
```

## Solution

```
L L O K K
L K O L O
# L L K L
O O O O L
L K K L O
```

### Step 1

Start: (2, 3), End: (4, 3), Sacrifice: (4, 4)

```
L L O K K
L K O L O
# L L # L
O O O # L
L K K # #
```

### Step 2

Start: (2, 2), End: (4, 2), Sacrifice: (0, 1)

```
L # O K K
L K O L O
# L # # L
O O # # L
L K # # #
```

### Step 3

Start: (1, 1), End: (1, 3), Sacrifice: (2, 4)

```
L # O K K
L # # # O
# L # # #
O O # # L
L K # # #
```

### Step 4

Start: (2, 1), End: (4, 1), Sacrifice: (1, 0)

```
L # O K K
# # # # O
# # # # #
O # # # L
L # # # #
```

### Step 5

Start: (0, 4), End: (3, 4), Sacrifice: (4, 0)

```
L # O K #
# # # # #
# # # # #
O # # # #
# # # # #
```

### Step 6

Start: (0, 0), End: (0, 3), Sacrifice: (3, 0)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 5

## Generated Puzzle

```
K K K O L J
O L O O O K
L K L K L L
K O L L K O
K L L O O K
L O K K K L
```

## Solution

```
K K K O L J
O L O O O K
L K L K L L
K O L L K O
K L L O O K
L O K K K L
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (3, 4)

```
K K K O L J
O L O O O K
L K L K L L
# # # L # O
K L L O O K
L O K K K L
```

### Step 2

Start: (0, 0), End: (2, 0), Sacrifice: (0, 5)

```
# K K O L #
# L O O O K
# K L K L L
# # # L # O
K L L O O K
L O K K K L
```

### Step 3

Start: (2, 5), End: (4, 5), Sacrifice: (2, 2)

```
# K K O L #
# L O O O K
# K # K L #
# # # L # #
K L L O O #
L O K K K L
```

### Step 4

Start: (5, 0), End: (5, 2), Sacrifice: (1, 3)

```
# K K O L #
# L O # O K
# K # K L #
# # # L # #
K L L O O #
# # # K K L
```

### Step 5

Start: (2, 4), End: (5, 4), Sacrifice: (5, 5)

```
# K K O L #
# L O # O K
# K # K # #
# # # L # #
K L L O # #
# # # K # #
```

### Step 6

Start: (3, 3), End: (5, 3), Sacrifice: (2, 1)

```
# K K O L #
# L O # O K
# # # K # #
# # # # # #
K L L # # #
# # # # # #
```

### Step 7

Start: (0, 2), End: (4, 2), Sacrifice: (4, 1)

```
# K # O L #
# L # # O K
# # # K # #
# # # # # #
K # # # # #
# # # # # #
```

### Step 8

Start: (1, 1), End: (1, 5), Sacrifice: (4, 0)

```
# K # O L #
# # # # # #
# # # K # #
# # # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 1), End: (0, 4), Sacrifice: (2, 3)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 6

## Generated Puzzle

```
L O K L O J L
K O L L L O K
L K O O O L O
K O L K K K K
O K O K J L O
L O K O K O K
K # J L O L J
```

## Solution

```
L O K L O J L
K O L L L O K
L K O O O L O
K O L K K K K
O K O K J L O
L O K O K O K
K # J L O L J
```

### Step 1

Start: (5, 0), End: (5, 2), Sacrifice: (3, 6)

```
L O K L O J L
K O L L L O K
L K O O O L O
K O L K K K #
O K O K J L O
# # # O K O K
K # J L O L J
```

### Step 2

Start: (3, 0), End: (3, 2), Sacrifice: (3, 3)

```
L O K L O J L
K O L L L O K
L K O O O L O
# # # # K K #
O K O K J L O
# # # O K O K
K # J L O L J
```

### Step 3

Start: (1, 0), End: (1, 2), Sacrifice: (6, 4)

```
L O K L O J L
# # # L L O K
L K O O O L O
# # # # K K #
O K O K J L O
# # # O K O K
K # J L # L J
```

### Step 4

Start: (4, 3), End: (6, 3), Sacrifice: (6, 6)

```
L O K L O J L
# # # L L O K
L K O O O L O
# # # # K K #
O K O # J L O
# # # # K O K
K # J # # L #
```

### Step 5

Start: (2, 0), End: (6, 0), Sacrifice: (4, 4)

```
L O K L O J L
# # # L L O K
# K O O O L O
# # # # K K #
# K O # # L O
# # # # K O K
# # J # # L #
```

### Step 6

Start: (1, 4), End: (3, 4), Sacrifice: (2, 3)

```
L O K L O J L
# # # L # O K
# K O # # L O
# # # # # K #
# K O # # L O
# # # # K O K
# # J # # L #
```

### Step 7

Start: (2, 1), End: (2, 5), Sacrifice: (6, 2)

```
L O K L O J L
# # # L # O K
# # # # # # O
# # # # # K #
# K O # # L O
# # # # K O K
# # # # # L #
```

### Step 8

Start: (0, 0), End: (0, 2), Sacrifice: (0, 5)

```
# # # L O # L
# # # L # O K
# # # # # # O
# # # # # K #
# K O # # L O
# # # # K O K
# # # # # L #
```

### Step 9

Start: (1, 3), End: (1, 6), Sacrifice: (0, 3)

```
# # # # O # L
# # # # # # #
# # # # # # O
# # # # # K #
# K O # # L O
# # # # K O K
# # # # # L #
```

### Step 10

Start: (4, 1), End: (4, 5), Sacrifice: (2, 6)

```
# # # # O # L
# # # # # # #
# # # # # # #
# # # # # K #
# # # # # # O
# # # # K O K
# # # # # L #
```

### Step 11

Start: (3, 5), End: (6, 5), Sacrifice: (5, 4)

```
# # # # O # L
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # O
# # # # # # K
# # # # # # #
```

### Step 12

Start: (0, 6), End: (5, 6), Sacrifice: (0, 4)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

---

# Puzzle 7

## Generated Puzzle

```
O L L O K L
J O L K O L
L O K O L O
K O L L L L
L K O O O K
K K K K K J
```

## Solution

```
O L L O K L
J O L K O L
L O K O L O
K O L L L L
L K O O O K
K K K K K J
```

### Step 1

Start: (3, 4), End: (5, 4), Sacrifice: (4, 0)

```
O L L O K L
J O L K O L
L O K O L O
K O L L # L
# K O O # K
K K K K # J
```

### Step 2

Start: (3, 3), End: (5, 3), Sacrifice: (5, 5)

```
O L L O K L
J O L K O L
L O K O L O
K O L # # L
# K O # # K
K K K # # #
```

### Step 3

Start: (0, 2), End: (0, 4), Sacrifice: (5, 1)

```
O L # # # L
J O L K O L
L O K O L O
K O L # # L
# K O # # K
K # K # # #
```

### Step 4

Start: (1, 3), End: (1, 5), Sacrifice: (3, 5)

```
O L # # # L
J O L # # #
L O K O L O
K O L # # #
# K O # # K
K # K # # #
```

### Step 5

Start: (2, 0), End: (2, 2), Sacrifice: (0, 0)

```
# L # # # L
J O L # # #
# # # O L O
K O L # # #
# K O # # K
K # K # # #
```

### Step 6

Start: (3, 0), End: (3, 2), Sacrifice: (1, 0)

```
# L # # # L
# O L # # #
# # # O L O
# # # # # #
# K O # # K
K # K # # #
```

### Step 7

Start: (0, 1), End: (4, 1), Sacrifice: (2, 4)

```
# # # # # L
# # L # # #
# # # O # O
# # # # # #
# # O # # K
K # K # # #
```

### Step 8

Start: (1, 2), End: (5, 2), Sacrifice: (2, 3)

```
# # # # # L
# # # # # #
# # # # # O
# # # # # #
# # # # # K
K # # # # #
```

### Step 9

Start: (0, 5), End: (4, 5), Sacrifice: (5, 0)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 8

## Generated Puzzle

```
K O L K O L
K K L O O L
K O O L J K
K L K O L J
O K K L O K
L K K L O L
```

## Solution

```
K O L K O L
K K L O O L
K O O L J K
K L K O L J
O K K L O K
L K K L O L
```

### Step 1

Start: (3, 2), End: (3, 4), Sacrifice: (4, 1)

```
K O L K O L
K K L O O L
K O O L J K
K L # # # J
O # K L O K
L K K L O L
```

### Step 2

Start: (0, 3), End: (0, 5), Sacrifice: (1, 1)

```
K O L # # #
K # L O O L
K O O L J K
K L # # # J
O # K L O K
L K K L O L
```

### Step 3

Start: (3, 0), End: (5, 0), Sacrifice: (4, 2)

```
K O L # # #
K # L O O L
K O O L J K
# L # # # J
# # # L O K
# K K L O L
```

### Step 4

Start: (1, 2), End: (5, 2), Sacrifice: (3, 1)

```
K O L # # #
K # # O O L
K O # L J K
# # # # # J
# # # L O K
# K # L O L
```

### Step 5

Start: (4, 3), End: (4, 5), Sacrifice: (5, 3)

```
K O L # # #
K # # O O L
K O # L J K
# # # # # J
# # # # # #
# K # # O L
```

### Step 6

Start: (5, 1), End: (5, 5), Sacrifice: (2, 5)

```
K O L # # #
K # # O O L
K O # L J #
# # # # # J
# # # # # #
# # # # # #
```

### Step 7

Start: (2, 0), End: (2, 3), Sacrifice: (1, 4)

```
K O L # # #
K # # O # L
# # # # J #
# # # # # J
# # # # # #
# # # # # #
```

### Step 8

Start: (1, 0), End: (1, 5), Sacrifice: (2, 4)

```
K O L # # #
# # # # # #
# # # # # #
# # # # # J
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 0), End: (0, 2), Sacrifice: (3, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 9

## Generated Puzzle

```
L O K L L L
K K O L L O
K L O L O L
O O O K K K
L K O O L K
L K O K L L
```

## Solution

```
L O K L L L
K K O L L O
K L O L O L
O O O K K K
L K O O L K
L K O K L L
```

### Step 1

Start: (1, 1), End: (1, 3), Sacrifice: (3, 3)

```
L O K L L L
K # # # L O
K L O L O L
O O O # K K
L K O O L K
L K O K L L
```

### Step 2

Start: (2, 3), End: (5, 3), Sacrifice: (2, 5)

```
L O K L L L
K # # # L O
K L O # O #
O O O # K K
L K O # L K
L K O # L L
```

### Step 3

Start: (0, 0), End: (0, 2), Sacrifice: (2, 0)

```
# # # L L L
K # # # L O
# L O # O #
O O O # K K
L K O # L K
L K O # L L
```

### Step 4

Start: (2, 1), End: (4, 1), Sacrifice: (4, 4)

```
# # # L L L
K # # # L O
# # O # O #
O # O # K K
L # O # # K
L K O # L L
```

### Step 5

Start: (0, 5), End: (3, 5), Sacrifice: (3, 2)

```
# # # L L #
K # # # L #
# # O # O #
O # # # K #
L # O # # K
L K O # L L
```

### Step 6

Start: (4, 0), End: (4, 5), Sacrifice: (5, 5)

```
# # # L L #
K # # # L #
# # O # O #
O # # # K #
# # # # # #
L K O # L #
```

### Step 7

Start: (5, 1), End: (5, 4), Sacrifice: (0, 4)

```
# # # L # #
K # # # L #
# # O # O #
O # # # K #
# # # # # #
L # # # # #
```

### Step 8

Start: (1, 0), End: (5, 0), Sacrifice: (0, 3)

```
# # # # # #
# # # # L #
# # O # O #
# # # # K #
# # # # # #
# # # # # #
```

### Step 9

Start: (1, 4), End: (3, 4), Sacrifice: (2, 2)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 10

## Generated Puzzle

```
K K L O K
L O K L K
O J L O O
L J O K L
L # K K O
```

## Solution

```
K K L O K
L O K L K
O J L O O
L J O K L
L # K K O
```

### Step 1

Start: (1, 4), End: (3, 4), Sacrifice: (0, 1)

```
K # L O K
L O K L #
O J L O #
L J O K #
L # K K O
```

### Step 2

Start: (2, 2), End: (4, 2), Sacrifice: (3, 3)

```
K # L O K
L O K L #
O J # O #
L J # # #
L # # K O
```

### Step 3

Start: (0, 2), End: (0, 4), Sacrifice: (3, 1)

```
K # # # #
L O K L #
O J # O #
L # # # #
L # # K O
```

### Step 4

Start: (1, 0), End: (1, 2), Sacrifice: (4, 4)

```
K # # # #
# # # L #
O J # O #
L # # # #
L # # K #
```

### Step 5

Start: (0, 0), End: (3, 0), Sacrifice: (4, 0)

```
# # # # #
# # # L #
# J # O #
# # # # #
# # # K #
```

### Step 6

Start: (1, 3), End: (4, 3), Sacrifice: (2, 1)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

