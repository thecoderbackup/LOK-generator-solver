# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
J L J O L K
L O L K O K
O O O L K O
L O O K K L
K K O L O L
O O K L O K
```

## Solution

```
J L J O L K
L O L K O K
O O O L K O
L O O K K L
K K O L O L
O O K L O K
```

### Step 1

Start: (4, 1), End: (4, 3), Sacrifice: (2, 2)

```
J L J O L K
L O L K O K
O O # L K O
L O O K K L
K # # # O L
O O K L O K
```

### Step 2

Start: (1, 2), End: (5, 2), Sacrifice: (2, 1)

```
J L J O L K
L O # K O K
O # # L K O
L O # K K L
K # # # O L
O O # L O K
```

### Step 3

Start: (5, 3), End: (5, 5), Sacrifice: (0, 0)

```
# L J O L K
L O # K O K
O # # L K O
L O # K K L
K # # # O L
O O # # # #
```

### Step 4

Start: (0, 4), End: (2, 4), Sacrifice: (0, 2)

```
# L # O # K
L O # K # K
O # # L # O
L O # K K L
K # # # O L
O O # # # #
```

### Step 5

Start: (1, 0), End: (1, 3), Sacrifice: (3, 3)

```
# L # O # K
# # # # # K
O # # L # O
L O # # K L
K # # # O L
O O # # # #
```

### Step 6

Start: (4, 0), End: (4, 5), Sacrifice: (5, 1)

```
# L # O # K
# # # # # K
O # # L # O
L O # # K L
# # # # # #
O # # # # #
```

### Step 7

Start: (0, 1), End: (0, 5), Sacrifice: (2, 3)

```
# # # # # #
# # # # # K
O # # # # O
L O # # K L
# # # # # #
O # # # # #
```

### Step 8

Start: (1, 5), End: (3, 5), Sacrifice: (5, 0)

```
# # # # # #
# # # # # #
O # # # # #
L O # # K #
# # # # # #
# # # # # #
```

### Step 9

Start: (3, 0), End: (3, 4), Sacrifice: (2, 0)

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
L O K K O L K
K L J L K O K
O O L O O K K
L L J K L O K
K J L O K K O
K O L # L O K
L K O L O L K
```

## Solution

```
L O K K O L K
K L J L K O K
O O L O O K K
L L J K L O K
K J L O K K O
K O L # L O K
L K O L O L K
```

### Step 1

Start: (1, 0), End: (3, 0), Sacrifice: (4, 0)

```
L O K K O L K
# L J L K O K
# O L O O K K
# L J K L O K
# J L O K K O
K O L # L O K
L K O L O L K
```

### Step 2

Start: (1, 3), End: (3, 3), Sacrifice: (3, 2)

```
L O K K O L K
# L J # K O K
# O L # O K K
# L # # L O K
# J L O K K O
K O L # L O K
L K O L O L K
```

### Step 3

Start: (4, 5), End: (6, 5), Sacrifice: (2, 6)

```
L O K K O L K
# L J # K O K
# O L # O K #
# L # # L O K
# J L O K # O
K O L # L # K
L K O L O # K
```

### Step 4

Start: (5, 0), End: (5, 2), Sacrifice: (3, 4)

```
L O K K O L K
# L J # K O K
# O L # O K #
# L # # # O K
# J L O K # O
# # # # L # K
L K O L O # K
```

### Step 5

Start: (4, 2), End: (4, 4), Sacrifice: (0, 6)

```
L O K K O L #
# L J # K O K
# O L # O K #
# L # # # O K
# J # # # # O
# # # # L # K
L K O L O # K
```

### Step 6

Start: (0, 0), End: (0, 2), Sacrifice: (5, 6)

```
# # # K O L #
# L J # K O K
# O L # O K #
# L # # # O K
# J # # # # O
# # # # L # #
L K O L O # K
```

### Step 7

Start: (3, 1), End: (3, 6), Sacrifice: (4, 6)

```
# # # K O L #
# L J # K O K
# O L # O K #
# # # # # # #
# J # # # # #
# # # # L # #
L K O L O # K
```

### Step 8

Start: (6, 1), End: (6, 3), Sacrifice: (2, 5)

```
# # # K O L #
# L J # K O K
# O L # O # #
# # # # # # #
# J # # # # #
# # # # L # #
L # # # O # K
```

### Step 9

Start: (1, 4), End: (5, 4), Sacrifice: (2, 1)

```
# # # K O L #
# L J # # O K
# # L # # # #
# # # # # # #
# J # # # # #
# # # # # # #
L # # # O # K
```

### Step 10

Start: (6, 0), End: (6, 6), Sacrifice: (1, 2)

```
# # # K O L #
# L # # # O K
# # L # # # #
# # # # # # #
# J # # # # #
# # # # # # #
# # # # # # #
```

### Step 11

Start: (0, 3), End: (0, 5), Sacrifice: (2, 2)

```
# # # # # # #
# L # # # O K
# # # # # # #
# # # # # # #
# J # # # # #
# # # # # # #
# # # # # # #
```

### Step 12

Start: (1, 1), End: (1, 6), Sacrifice: (4, 1)

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

# Puzzle 3

## Generated Puzzle

```
K L K O K
K L K O L
# L O K K
K O L O O
L O K L K
```

## Solution

```
K L K O K
K L K O L
# L O K K
K O L O O
L O K L K
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (0, 2)

```
K L # O K
K L K O L
# L O K K
# # # O O
L O K L K
```

### Step 2

Start: (2, 3), End: (4, 3), Sacrifice: (0, 0)

```
# L # O K
K L K O L
# L O # K
# # # # O
L O K # K
```

### Step 3

Start: (4, 0), End: (4, 2), Sacrifice: (1, 3)

```
# L # O K
K L K # L
# L O # K
# # # # O
# # # # K
```

### Step 4

Start: (2, 1), End: (2, 4), Sacrifice: (1, 2)

```
# L # O K
K L # # L
# # # # #
# # # # O
# # # # K
```

### Step 5

Start: (1, 4), End: (4, 4), Sacrifice: (1, 0)

```
# L # O K
# L # # #
# # # # #
# # # # #
# # # # #
```

### Step 6

Start: (0, 1), End: (0, 4), Sacrifice: (1, 1)

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
O K K O K
K O K L O
O L # O L
K O L K L
L L O K J
```

## Solution

```
O K K O K
K O K L O
O L # O L
K O L K L
L L O K J
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (4, 4)

```
O K K O K
K O K L O
O L # O L
# # # K L
L L O K #
```

### Step 2

Start: (0, 1), End: (2, 1), Sacrifice: (0, 3)

```
O # K # K
K # K L O
O # # O L
# # # K L
L L O K #
```

### Step 3

Start: (0, 4), End: (2, 4), Sacrifice: (0, 0)

```
# # K # #
K # K L #
O # # O #
# # # K L
L L O K #
```

### Step 4

Start: (1, 0), End: (4, 0), Sacrifice: (0, 2)

```
# # # # #
# # K L #
# # # O #
# # # K L
# L O K #
```

### Step 5

Start: (4, 1), End: (4, 3), Sacrifice: (3, 4)

```
# # # # #
# # K L #
# # # O #
# # # K #
# # # # #
```

### Step 6

Start: (1, 3), End: (3, 3), Sacrifice: (1, 2)

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
K K O K L
K O L O L
O K O L #
K O L O L
L L K O L
```

## Solution

```
K K O K L
K O L O L
O K O L #
K O L O L
L L K O L
```

### Step 1

Start: (0, 3), End: (2, 3), Sacrifice: (1, 1)

```
K K O # L
K # L # L
O K O # #
K O L O L
L L K O L
```

### Step 2

Start: (2, 1), End: (4, 1), Sacrifice: (3, 2)

```
K K O # L
K # L # L
O # O # #
K # # O L
L # K O L
```

### Step 3

Start: (3, 0), End: (3, 4), Sacrifice: (0, 0)

```
# K O # L
K # L # L
O # O # #
# # # # #
L # K O L
```

### Step 4

Start: (0, 1), End: (0, 4), Sacrifice: (4, 4)

```
# # # # #
K # L # L
O # O # #
# # # # #
L # K O #
```

### Step 5

Start: (1, 2), End: (4, 2), Sacrifice: (1, 4)

```
# # # # #
K # # # #
O # # # #
# # # # #
L # # O #
```

### Step 6

Start: (1, 0), End: (4, 0), Sacrifice: (4, 3)

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
K O L O K L
K K O K K L
L O O K L O
K O L L O K
L L L O K K
J L K K O L
```

## Solution

```
K O L O K L
K K O K K L
L O O K L O
K O L L O K
L L L O K K
J L K K O L
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (4, 0)

```
K O L O K L
K K O K K L
L O O K L O
# # # L O K
# L L O K K
J L K K O L
```

### Step 2

Start: (4, 2), End: (4, 4), Sacrifice: (1, 3)

```
K O L O K L
K K O # K L
L O O K L O
# # # L O K
# L # # # K
J L K K O L
```

### Step 3

Start: (1, 1), End: (4, 1), Sacrifice: (5, 0)

```
K O L O K L
K # O # K L
L # O K L O
# # # L O K
# # # # # K
# L K K O L
```

### Step 4

Start: (0, 2), End: (0, 4), Sacrifice: (5, 3)

```
K O # # # L
K # O # K L
L # O K L O
# # # L O K
# # # # # K
# L K # O L
```

### Step 5

Start: (3, 3), End: (3, 5), Sacrifice: (2, 5)

```
K O # # # L
K # O # K L
L # O K L #
# # # # # #
# # # # # K
# L K # O L
```

### Step 6

Start: (2, 0), End: (2, 3), Sacrifice: (4, 5)

```
K O # # # L
K # O # K L
# # # # L #
# # # # # #
# # # # # #
# L K # O L
```

### Step 7

Start: (5, 2), End: (5, 5), Sacrifice: (1, 4)

```
K O # # # L
K # O # # L
# # # # L #
# # # # # #
# # # # # #
# L # # # #
```

### Step 8

Start: (1, 0), End: (1, 5), Sacrifice: (2, 4)

```
K O # # # L
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# L # # # #
```

### Step 9

Start: (0, 0), End: (0, 5), Sacrifice: (5, 1)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 7

## Generated Puzzle

```
L K K K O L
O K L K J K
K O O O L O
K L K L O L
O K O L K K
J O L L O K
```

## Solution

```
L K K K O L
O K L K J K
K O O O L O
K L K L O L
O K O L K K
J O L L O K
```

### Step 1

Start: (1, 5), End: (3, 5), Sacrifice: (1, 4)

```
L K K K O L
O K L K # #
K O O O L #
K L K L O #
O K O L K K
J O L L O K
```

### Step 2

Start: (2, 4), End: (4, 4), Sacrifice: (5, 3)

```
L K K K O L
O K L K # #
K O O O # #
K L K L # #
O K O L # K
J O L # O K
```

### Step 3

Start: (1, 1), End: (3, 1), Sacrifice: (5, 0)

```
L K K K O L
O # L K # #
K # O O # #
K # K L # #
O K O L # K
# O L # O K
```

### Step 4

Start: (1, 3), End: (3, 3), Sacrifice: (5, 1)

```
L K K K O L
O # L # # #
K # O # # #
K # K # # #
O K O L # K
# # L # O K
```

### Step 5

Start: (5, 2), End: (5, 5), Sacrifice: (4, 0)

```
L K K K O L
O # L # # #
K # O # # #
K # K # # #
# K O L # K
# # # # # #
```

### Step 6

Start: (1, 2), End: (3, 2), Sacrifice: (0, 1)

```
L # K K O L
O # # # # #
K # # # # #
K # # # # #
# K O L # K
# # # # # #
```

### Step 7

Start: (0, 3), End: (0, 5), Sacrifice: (4, 5)

```
L # K # # #
O # # # # #
K # # # # #
K # # # # #
# K O L # #
# # # # # #
```

### Step 8

Start: (0, 0), End: (2, 0), Sacrifice: (0, 2)

```
# # # # # #
# # # # # #
# # # # # #
K # # # # #
# K O L # #
# # # # # #
```

### Step 9

Start: (4, 1), End: (4, 3), Sacrifice: (3, 0)

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
K O O L K L
O K J O K L
K O K K O L
O L L O K O
L K O K O K
K K L J L O
```

## Solution

```
K O O L K L
O K J O K L
K O K K O L
O L L O K O
L K O K O K
K K L J L O
```

### Step 1

Start: (2, 3), End: (2, 5), Sacrifice: (5, 1)

```
K O O L K L
O K J O K L
K O K # # #
O L L O K O
L K O K O K
K # L J L O
```

### Step 2

Start: (3, 2), End: (3, 4), Sacrifice: (5, 3)

```
K O O L K L
O K J O K L
K O K # # #
O L # # # O
L K O K O K
K # L # L O
```

### Step 3

Start: (2, 2), End: (5, 2), Sacrifice: (0, 1)

```
K # O L K L
O K J O K L
K O # # # #
O L # # # O
L K # K O K
K # # # L O
```

### Step 4

Start: (1, 1), End: (3, 1), Sacrifice: (5, 5)

```
K # O L K L
O # J O K L
K # # # # #
O # # # # O
L K # K O K
K # # # L #
```

### Step 5

Start: (1, 4), End: (5, 4), Sacrifice: (1, 2)

```
K # O L K L
O # # O # L
K # # # # #
O # # # # O
L K # K # K
K # # # # #
```

### Step 6

Start: (1, 5), End: (4, 5), Sacrifice: (1, 0)

```
K # O L K L
# # # O # #
K # # # # #
O # # # # #
L K # K # #
K # # # # #
```

### Step 7

Start: (2, 0), End: (4, 0), Sacrifice: (5, 0)

```
K # O L K L
# # # O # #
# # # # # #
# # # # # #
# K # K # #
# # # # # #
```

### Step 8

Start: (0, 3), End: (4, 3), Sacrifice: (0, 4)

```
K # O # # L
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
O K O L L K
K K O L O O
O L L O K O
L O O L K K
K K O K L L
L J O L O K
```

## Solution

```
O K O L L K
K K O L O O
O L L O K O
L O O L K K
K K O K L L
L J O L O K
```

### Step 1

Start: (0, 1), End: (0, 3), Sacrifice: (3, 5)

```
O # # # L K
K K O L O O
O L L O K O
L O O L K #
K K O K L L
L J O L O K
```

### Step 2

Start: (2, 2), End: (2, 4), Sacrifice: (0, 0)

```
# # # # L K
K K O L O O
O L # # # O
L O O L K #
K K O K L L
L J O L O K
```

### Step 3

Start: (5, 3), End: (5, 5), Sacrifice: (3, 3)

```
# # # # L K
K K O L O O
O L # # # O
L O O # K #
K K O K L L
L J O # # #
```

### Step 4

Start: (1, 0), End: (3, 0), Sacrifice: (5, 1)

```
# # # # L K
# K O L O O
# L # # # O
# O O # K #
K K O K L L
L # O # # #
```

### Step 5

Start: (2, 1), End: (4, 1), Sacrifice: (1, 5)

```
# # # # L K
# K O L O #
# # # # # O
# # O # K #
K # O K L L
L # O # # #
```

### Step 6

Start: (0, 5), End: (4, 5), Sacrifice: (5, 0)

```
# # # # L #
# K O L O #
# # # # # #
# # O # K #
K # O K L #
# # O # # #
```

### Step 7

Start: (1, 1), End: (1, 3), Sacrifice: (4, 3)

```
# # # # L #
# # # # O #
# # # # # #
# # O # K #
K # O # L #
# # O # # #
```

### Step 8

Start: (4, 0), End: (4, 4), Sacrifice: (5, 2)

```
# # # # L #
# # # # O #
# # # # # #
# # O # K #
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 4), End: (3, 4), Sacrifice: (3, 2)

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
K O L O L K
J J J L O K
K O L L K K
L K O L O O
K O L K O L
L K O L K L
```

## Solution

```
K O L O L K
J J J L O K
K O L L K K
L K O L O O
K O L K O L
L K O L K L
```

### Step 1

Start: (3, 1), End: (3, 3), Sacrifice: (2, 2)

```
K O L O L K
J J J L O K
K O # L K K
L # # # O O
K O L K O L
L K O L K L
```

### Step 2

Start: (2, 0), End: (2, 3), Sacrifice: (3, 0)

```
K O L O L K
J J J L O K
# # # # K K
# # # # O O
K O L K O L
L K O L K L
```

### Step 3

Start: (5, 1), End: (5, 3), Sacrifice: (0, 3)

```
K O L # L K
J J J L O K
# # # # K K
# # # # O O
K O L K O L
L # # # K L
```

### Step 4

Start: (1, 3), End: (1, 5), Sacrifice: (1, 2)

```
K O L # L K
J J # # # #
# # # # K K
# # # # O O
K O L K O L
L # # # K L
```

### Step 5

Start: (4, 3), End: (4, 5), Sacrifice: (2, 4)

```
K O L # L K
J J # # # #
# # # # # K
# # # # O O
K O L # # #
L # # # K L
```

### Step 6

Start: (0, 4), End: (5, 4), Sacrifice: (5, 0)

```
K O L # # K
J J # # # #
# # # # # K
# # # # # O
K O L # # #
# # # # # L
```

### Step 7

Start: (2, 5), End: (5, 5), Sacrifice: (1, 1)

```
K O L # # K
J # # # # #
# # # # # #
# # # # # #
K O L # # #
# # # # # #
```

### Step 8

Start: (4, 0), End: (4, 2), Sacrifice: (1, 0)

```
K O L # # K
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 0), End: (0, 2), Sacrifice: (0, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

