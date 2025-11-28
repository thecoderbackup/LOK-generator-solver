# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
K O K L O
K L O K K
L K O L #
O J K O L
L L O K L
```

## Solution

```
K O K L O
K L O K K
L K O L #
O J K O L
L L O K L
```

### Step 1

Start: (4, 1), End: (4, 3), Sacrifice: (4, 4)

```
K O K L O
K L O K K
L K O L #
O J K O L
L # # # #
```

### Step 2

Start: (1, 1), End: (1, 3), Sacrifice: (0, 2)

```
K O # L O
K # # # K
L K O L #
O J K O L
L # # # #
```

### Step 3

Start: (3, 2), End: (3, 4), Sacrifice: (2, 0)

```
K O # L O
K # # # K
# K O L #
O J # # #
L # # # #
```

### Step 4

Start: (1, 0), End: (4, 0), Sacrifice: (0, 4)

```
K O # L #
# # # # K
# K O L #
# J # # #
# # # # #
```

### Step 5

Start: (2, 1), End: (2, 3), Sacrifice: (3, 1)

```
K O # L #
# # # # K
# # # # #
# # # # #
# # # # #
```

### Step 6

Start: (0, 0), End: (0, 3), Sacrifice: (1, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 2

## Generated Puzzle

```
K # L O K
L O O K K
L O K L O
K L K O L
L O K K L
```

## Solution

```
K # L O K
L O O K K
L O K L O
K L K O L
L O K K L
```

### Step 1

Start: (0, 2), End: (0, 4), Sacrifice: (1, 2)

```
K # # # #
L O # K K
L O K L O
K L K O L
L O K K L
```

### Step 2

Start: (2, 0), End: (2, 2), Sacrifice: (3, 0)

```
K # # # #
L O # K K
# # # L O
# L K O L
L O K K L
```

### Step 3

Start: (4, 0), End: (4, 2), Sacrifice: (3, 1)

```
K # # # #
L O # K K
# # # L O
# # K O L
# # # K L
```

### Step 4

Start: (1, 0), End: (1, 3), Sacrifice: (2, 3)

```
K # # # #
# # # # K
# # # # O
# # K O L
# # # K L
```

### Step 5

Start: (3, 2), End: (3, 4), Sacrifice: (0, 0)

```
# # # # #
# # # # K
# # # # O
# # # # #
# # # K L
```

### Step 6

Start: (1, 4), End: (4, 4), Sacrifice: (4, 3)

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
L L K O K K
K K O J L O
O O L J O J
K L O K K L
L L K O L O
K O L L K L
```

## Solution

```
L L K O K K
K K O J L O
O O L J O J
K L O K K L
L L K O L O
K O L L K L
```

### Step 1

Start: (0, 2), End: (2, 2), Sacrifice: (5, 4)

```
L L # O K K
K K # J L O
O O # J O J
K L O K K L
L L K O L O
K O L L # L
```

### Step 2

Start: (0, 1), End: (0, 4), Sacrifice: (3, 0)

```
L # # # # K
K K # J L O
O O # J O J
# L O K K L
L L K O L O
K O L L # L
```

### Step 3

Start: (1, 0), End: (4, 0), Sacrifice: (0, 0)

```
# # # # # K
# K # J L O
# O # J O J
# L O K K L
# L K O L O
K O L L # L
```

### Step 4

Start: (5, 0), End: (5, 2), Sacrifice: (1, 3)

```
# # # # # K
# K # # L O
# O # J O J
# L O K K L
# L K O L O
# # # L # L
```

### Step 5

Start: (3, 1), End: (3, 3), Sacrifice: (2, 5)

```
# # # # # K
# K # # L O
# O # J O #
# # # # K L
# L K O L O
# # # L # L
```

### Step 6

Start: (4, 2), End: (4, 4), Sacrifice: (5, 3)

```
# # # # # K
# K # # L O
# O # J O #
# # # # K L
# L # # # O
# # # # # L
```

### Step 7

Start: (1, 4), End: (3, 4), Sacrifice: (5, 5)

```
# # # # # K
# K # # # O
# O # J # #
# # # # # L
# L # # # O
# # # # # #
```

### Step 8

Start: (1, 1), End: (4, 1), Sacrifice: (2, 3)

```
# # # # # K
# # # # # O
# # # # # #
# # # # # L
# # # # # O
# # # # # #
```

### Step 9

Start: (0, 5), End: (3, 5), Sacrifice: (4, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 4

## Generated Puzzle

```
L O L L O K
K O L O K L
O K O K O L
K J K L J L
K O O L J O
K L K L K K
```

## Solution

```
L O L L O K
K O L O K L
O K O K O L
K J K L J L
K O O L J O
K L K L K K
```

### Step 1

Start: (2, 3), End: (2, 5), Sacrifice: (3, 1)

```
L O L L O K
K O L O K L
O K O # # #
K # K L J L
K O O L J O
K L K L K K
```

### Step 2

Start: (3, 5), End: (5, 5), Sacrifice: (3, 4)

```
L O L L O K
K O L O K L
O K O # # #
K # K L # #
K O O L J #
K L K L K #
```

### Step 3

Start: (1, 2), End: (1, 4), Sacrifice: (3, 3)

```
L O L L O K
K O # # # L
O K O # # #
K # K # # #
K O O L J #
K L K L K #
```

### Step 4

Start: (1, 0), End: (1, 5), Sacrifice: (5, 0)

```
L O L L O K
# # # # # #
O K O # # #
K # K # # #
K O O L J #
# L K L K #
```

### Step 5

Start: (0, 3), End: (0, 5), Sacrifice: (0, 1)

```
L # L # # #
# # # # # #
O K O # # #
K # K # # #
K O O L J #
# L K L K #
```

### Step 6

Start: (2, 1), End: (5, 1), Sacrifice: (5, 4)

```
L # L # # #
# # # # # #
O # O # # #
K # K # # #
K # O L J #
# # K L # #
```

### Step 7

Start: (4, 0), End: (4, 3), Sacrifice: (3, 2)

```
L # L # # #
# # # # # #
O # O # # #
K # # # # #
# # # # J #
# # K L # #
```

### Step 8

Start: (0, 0), End: (3, 0), Sacrifice: (4, 4)

```
# # L # # #
# # # # # #
# # O # # #
# # # # # #
# # # # # #
# # K L # #
```

### Step 9

Start: (0, 2), End: (5, 2), Sacrifice: (5, 3)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 5

## Generated Puzzle

```
J J L K #
L L O O K
J K O L K
L J K O O
L O K L L
```

## Solution

```
J J L K #
L L O O K
J K O L K
L J K O O
L O K L L
```

### Step 1

Start: (4, 0), End: (4, 2), Sacrifice: (0, 0)

```
# J L K #
L L O O K
J K O L K
L J K O O
# # # L L
```

### Step 2

Start: (2, 1), End: (2, 3), Sacrifice: (2, 0)

```
# J L K #
L L O O K
# # # # K
L J K O O
# # # L L
```

### Step 3

Start: (0, 2), End: (3, 2), Sacrifice: (0, 1)

```
# # # K #
L L # O K
# # # # K
L J # O O
# # # L L
```

### Step 4

Start: (1, 1), End: (1, 4), Sacrifice: (1, 0)

```
# # # K #
# # # # #
# # # # K
L J # O O
# # # L L
```

### Step 5

Start: (0, 3), End: (4, 3), Sacrifice: (3, 0)

```
# # # # #
# # # # #
# # # # K
# J # # O
# # # # L
```

### Step 6

Start: (2, 4), End: (4, 4), Sacrifice: (3, 1)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 6

## Generated Puzzle

```
K L O L O K K
O L O L O K K
L L K O J J K
K O O K L L L
O K # O O O O
L O K L K K K
L K O K J K J
```

## Solution

```
K L O L O K K
O L O L O K K
L L K O J J K
K O O K L L L
O K # O O O O
L O K L K K K
L K O K J K J
```

### Step 1

Start: (3, 6), End: (5, 6), Sacrifice: (6, 3)

```
K L O L O K K
O L O L O K K
L L K O J J K
K O O K L L #
O K # O O O #
L O K L K K #
L K O # J K J
```

### Step 2

Start: (3, 5), End: (5, 5), Sacrifice: (2, 6)

```
K L O L O K K
O L O L O K K
L L K O J J #
K O O K L # #
O K # O O # #
L O K L K # #
L K O # J K J
```

### Step 3

Start: (0, 0), End: (2, 0), Sacrifice: (4, 4)

```
# L O L O K K
# L O L O K K
# L K O J J #
K O O K L # #
O K # O # # #
L O K L K # #
L K O # J K J
```

### Step 4

Start: (2, 1), End: (4, 1), Sacrifice: (2, 4)

```
# L O L O K K
# L O L O K K
# # K O # J #
K # O K L # #
O # # O # # #
L O K L K # #
L K O # J K J
```

### Step 5

Start: (3, 3), End: (5, 3), Sacrifice: (6, 4)

```
# L O L O K K
# L O L O K K
# # K O # J #
K # O # L # #
O # # # # # #
L O K # K # #
L K O # # K J
```

### Step 6

Start: (1, 3), End: (1, 5), Sacrifice: (4, 0)

```
# L O L O K K
# L O # # # K
# # K O # J #
K # O # L # #
# # # # # # #
L O K # K # #
L K O # # K J
```

### Step 7

Start: (1, 1), End: (1, 6), Sacrifice: (2, 3)

```
# L O L O K K
# # # # # # #
# # K # # J #
K # O # L # #
# # # # # # #
L O K # K # #
L K O # # K J
```

### Step 8

Start: (3, 0), End: (3, 4), Sacrifice: (6, 1)

```
# L O L O K K
# # # # # # #
# # K # # J #
# # # # # # #
# # # # # # #
L O K # K # #
L # O # # K J
```

### Step 9

Start: (6, 0), End: (6, 5), Sacrifice: (2, 5)

```
# L O L O K K
# # # # # # #
# # K # # # #
# # # # # # #
# # # # # # #
L O K # K # #
# # # # # # J
```

### Step 10

Start: (0, 3), End: (0, 5), Sacrifice: (5, 2)

```
# L O # # # K
# # # # # # #
# # K # # # #
# # # # # # #
# # # # # # #
L O # # K # #
# # # # # # J
```

### Step 11

Start: (0, 1), End: (0, 6), Sacrifice: (2, 2)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
L O # # K # #
# # # # # # J
```

### Step 12

Start: (5, 0), End: (5, 4), Sacrifice: (6, 6)

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
L L L O K K O
K J O L L O K
L K O L L L O
L O # L O J L
O K O L K J J
O K K O L L O
K K L O K O L
```

## Solution

```
L L L O K K O
K J O L L O K
L K O L L L O
L O # L O J L
O K O L K J J
O K K O L L O
K K L O K O L
```

### Step 1

Start: (5, 2), End: (5, 4), Sacrifice: (2, 0)

```
L L L O K K O
K J O L L O K
# K O L L L O
L O # L O J L
O K O L K J J
O K # # # L O
K K L O K O L
```

### Step 2

Start: (4, 1), End: (4, 3), Sacrifice: (1, 1)

```
L L L O K K O
K # O L L O K
# K O L L L O
L O # L O J L
O # # # K J J
O K # # # L O
K K L O K O L
```

### Step 3

Start: (2, 1), End: (2, 3), Sacrifice: (3, 3)

```
L L L O K K O
K # O L L O K
# # # # L L O
L O # # O J L
O # # # K J J
O K # # # L O
K K L O K O L
```

### Step 4

Start: (0, 5), End: (2, 5), Sacrifice: (4, 6)

```
L L L O K # O
K # O L L # K
# # # # L # O
L O # # O J L
O # # # K J #
O K # # # L O
K K L O K O L
```

### Step 5

Start: (6, 2), End: (6, 4), Sacrifice: (5, 0)

```
L L L O K # O
K # O L L # K
# # # # L # O
L O # # O J L
O # # # K J #
# K # # # L O
K K # # # O L
```

### Step 6

Start: (1, 0), End: (1, 3), Sacrifice: (0, 6)

```
L L L O K # #
# # # # L # K
# # # # L # O
L O # # O J L
O # # # K J #
# K # # # L O
K K # # # O L
```

### Step 7

Start: (2, 4), End: (4, 4), Sacrifice: (5, 6)

```
L L L O K # #
# # # # L # K
# # # # # # O
L O # # # J L
O # # # # J #
# K # # # L #
K K # # # O L
```

### Step 8

Start: (6, 1), End: (6, 6), Sacrifice: (3, 5)

```
L L L O K # #
# # # # L # K
# # # # # # O
L O # # # # L
O # # # # J #
# K # # # L #
K # # # # # #
```

### Step 9

Start: (1, 6), End: (3, 6), Sacrifice: (3, 0)

```
L L L O K # #
# # # # L # #
# # # # # # #
# O # # # # #
O # # # # J #
# K # # # L #
K # # # # # #
```

### Step 10

Start: (0, 1), End: (5, 1), Sacrifice: (5, 5)

```
L # L O K # #
# # # # L # #
# # # # # # #
# # # # # # #
O # # # # J #
# # # # # # #
K # # # # # #
```

### Step 11

Start: (0, 2), End: (0, 4), Sacrifice: (4, 5)

```
L # # # # # #
# # # # L # #
# # # # # # #
# # # # # # #
O # # # # # #
# # # # # # #
K # # # # # #
```

### Step 12

Start: (0, 0), End: (6, 0), Sacrifice: (1, 4)

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

# Puzzle 8

## Generated Puzzle

```
L K L K O K
L O O L L L
O L K O L L
J K O L O O
J K K K K K
K K O K J L
```

## Solution

```
L K L K O K
L O O L L L
O L K O L L
J K O L O O
J K K K K K
K K O K J L
```

### Step 1

Start: (0, 1), End: (2, 1), Sacrifice: (3, 0)

```
L # L K O K
L # O L L L
O # K O L L
# K O L O O
J K K K K K
K K O K J L
```

### Step 2

Start: (0, 2), End: (2, 2), Sacrifice: (4, 3)

```
L # # K O K
L # # L L L
O # # O L L
# K O L O O
J K K # K K
K K O K J L
```

### Step 3

Start: (2, 4), End: (4, 4), Sacrifice: (4, 0)

```
L # # K O K
L # # L L L
O # # O # L
# K O L # O
# K K # # K
K K O K J L
```

### Step 4

Start: (3, 1), End: (3, 3), Sacrifice: (5, 4)

```
L # # K O K
L # # L L L
O # # O # L
# # # # # O
# K K # # K
K K O K # L
```

### Step 5

Start: (2, 5), End: (4, 5), Sacrifice: (1, 5)

```
L # # K O K
L # # L L #
O # # O # #
# # # # # #
# K K # # #
K K O K # L
```

### Step 6

Start: (1, 0), End: (5, 0), Sacrifice: (0, 3)

```
L # # # O K
# # # L L #
# # # O # #
# # # # # #
# K K # # #
# K O K # L
```

### Step 7

Start: (1, 3), End: (5, 3), Sacrifice: (1, 4)

```
L # # # O K
# # # # # #
# # # # # #
# # # # # #
# K K # # #
# K O # # L
```

### Step 8

Start: (5, 1), End: (5, 5), Sacrifice: (4, 2)

```
L # # # O K
# # # # # #
# # # # # #
# # # # # #
# K # # # #
# # # # # #
```

### Step 9

Start: (0, 0), End: (0, 5), Sacrifice: (4, 1)

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
L L O K K
K O L O J
O L L L #
K L O O K
K O K L K
```

## Solution

```
L L O K K
K O L O J
O L L L #
K L O O K
K O K L K
```

### Step 1

Start: (2, 2), End: (4, 2), Sacrifice: (1, 4)

```
L L O K K
K O L O #
O L # L #
K L # O K
K O # L K
```

### Step 2

Start: (3, 1), End: (3, 4), Sacrifice: (2, 1)

```
L L O K K
K O L O #
O # # L #
K # # # #
K O # L K
```

### Step 3

Start: (0, 3), End: (2, 3), Sacrifice: (0, 0)

```
# L O # K
K O L # #
O # # # #
K # # # #
K O # L K
```

### Step 4

Start: (0, 1), End: (0, 4), Sacrifice: (2, 0)

```
# # # # #
K O L # #
# # # # #
K # # # #
K O # L K
```

### Step 5

Start: (1, 0), End: (1, 2), Sacrifice: (4, 4)

```
# # # # #
# # # # #
# # # # #
K # # # #
K O # L #
```

### Step 6

Start: (4, 0), End: (4, 3), Sacrifice: (3, 0)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 10

## Generated Puzzle

```
K L O L J L
K O L L O K
L O L O O K
L K L K O K
L K O L O K
K O L L K K
```

## Solution

```
K L O L J L
K O L L O K
L O L O O K
L K L K O K
L K O L O K
K O L L K K
```

### Step 1

Start: (1, 3), End: (1, 5), Sacrifice: (5, 4)

```
K L O L J L
K O L # # #
L O L O O K
L K L K O K
L K O L O K
K O L L # K
```

### Step 2

Start: (4, 1), End: (4, 3), Sacrifice: (0, 4)

```
K L O L # L
K O L # # #
L O L O O K
L K L K O K
L # # # O K
K O L L # K
```

### Step 3

Start: (4, 0), End: (4, 5), Sacrifice: (2, 0)

```
K L O L # L
K O L # # #
# O L O O K
L K L K O K
# # # # # #
K O L L # K
```

### Step 4

Start: (1, 0), End: (1, 2), Sacrifice: (5, 1)

```
K L O L # L
# # # # # #
# O L O O K
L K L K O K
# # # # # #
K # L L # K
```

### Step 5

Start: (0, 3), End: (3, 3), Sacrifice: (5, 3)

```
K L O # # L
# # # # # #
# O L # O K
L K L # O K
# # # # # #
K # L # # K
```

### Step 6

Start: (0, 1), End: (3, 1), Sacrifice: (5, 0)

```
K # O # # L
# # # # # #
# # L # O K
L # L # O K
# # # # # #
# # L # # K
```

### Step 7

Start: (2, 2), End: (2, 5), Sacrifice: (3, 0)

```
K # O # # L
# # # # # #
# # # # # #
# # L # O K
# # # # # #
# # L # # K
```

### Step 8

Start: (0, 0), End: (0, 5), Sacrifice: (5, 2)

```
# # # # # #
# # # # # #
# # # # # #
# # L # O K
# # # # # #
# # # # # K
```

### Step 9

Start: (3, 2), End: (3, 5), Sacrifice: (5, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

