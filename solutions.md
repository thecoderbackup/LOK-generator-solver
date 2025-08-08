# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
K O L K K
K J O O L
O L K L O
L O O K K
L K L J #
```

## Solution

```
K O L K K
K J O O L
O L K L O
L O O K K
L K L J #
```

### Step 1

Start: (1, 4), End: (3, 4), Sacrifice: (0, 4)

```
K O L K #
K J O O #
O L K L #
L O O K #
L K L J #
```

### Step 2

Start: (0, 2), End: (2, 2), Sacrifice: (4, 3)

```
K O # K #
K J # O #
O L # L #
L O O K #
L K L # #
```

### Step 3

Start: (2, 1), End: (4, 1), Sacrifice: (1, 0)

```
K O # K #
# J # O #
O # # L #
L # O K #
L # L # #
```

### Step 4

Start: (3, 0), End: (3, 3), Sacrifice: (0, 1)

```
K # # K #
# J # O #
O # # L #
# # # # #
L # L # #
```

### Step 5

Start: (0, 0), End: (4, 0), Sacrifice: (4, 2)

```
# # # K #
# J # O #
# # # L #
# # # # #
# # # # #
```

### Step 6

Start: (0, 3), End: (2, 3), Sacrifice: (1, 1)

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
L L L K O L K
O O K J K O O
K K L L O L L
L O O O L O #
O O K K K O L
K O K K O L J
K O L L O K L
```

## Solution

```
L L L K O L K
O O K J K O O
K K L L O L L
L O O O L O #
O O K K K O L
K O K K O L J
K O L L O K L
```

### Step 1

Start: (0, 0), End: (2, 0), Sacrifice: (1, 5)

```
# L L K O L K
# O K J K # O
# K L L O L L
L O O O L O #
O O K K K O L
K O K K O L J
K O L L O K L
```

### Step 2

Start: (0, 6), End: (2, 6), Sacrifice: (5, 6)

```
# L L K O L #
# O K J K # #
# K L L O L #
L O O O L O #
O O K K K O L
K O K K O L #
K O L L O K L
```

### Step 3

Start: (4, 4), End: (4, 6), Sacrifice: (3, 1)

```
# L L K O L #
# O K J K # #
# K L L O L #
L # O O L O #
O O K K # # #
K O K K O L #
K O L L O K L
```

### Step 4

Start: (1, 4), End: (3, 4), Sacrifice: (2, 5)

```
# L L K O L #
# O K J # # #
# K L L # # #
L # O O # O #
O O K K # # #
K O K K O L #
K O L L O K L
```

### Step 5

Start: (0, 3), End: (0, 5), Sacrifice: (1, 2)

```
# L L # # # #
# O # J # # #
# K L L # # #
L # O O # O #
O O K K # # #
K O K K O L #
K O L L O K L
```

### Step 6

Start: (0, 1), End: (2, 1), Sacrifice: (4, 1)

```
# # L # # # #
# # # J # # #
# # L L # # #
L # O O # O #
O # K K # # #
K O K K O L #
K O L L O K L
```

### Step 7

Start: (3, 0), End: (5, 0), Sacrifice: (5, 1)

```
# # L # # # #
# # # J # # #
# # L L # # #
# # O O # O #
# # K K # # #
# # K K O L #
K O L L O K L
```

### Step 8

Start: (6, 3), End: (6, 5), Sacrifice: (6, 2)

```
# # L # # # #
# # # J # # #
# # L L # # #
# # O O # O #
# # K K # # #
# # K K O L #
K O # # # # L
```

### Step 9

Start: (2, 3), End: (4, 3), Sacrifice: (0, 2)

```
# # # # # # #
# # # J # # #
# # L # # # #
# # O # # O #
# # K # # # #
# # K K O L #
K O # # # # L
```

### Step 10

Start: (2, 2), End: (4, 2), Sacrifice: (5, 2)

```
# # # # # # #
# # # J # # #
# # # # # # #
# # # # # O #
# # # # # # #
# # # K O L #
K O # # # # L
```

### Step 11

Start: (6, 0), End: (6, 6), Sacrifice: (3, 5)

```
# # # # # # #
# # # J # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # K O L #
# # # # # # #
```

### Step 12

Start: (5, 3), End: (5, 5), Sacrifice: (1, 3)

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
L K L J L
O O O # O
L L K K K
O L O K K
K K J O L
```

## Solution

```
L K L J L
O O O # O
L L K K K
O L O K K
K K J O L
```

### Step 1

Start: (0, 1), End: (2, 1), Sacrifice: (2, 0)

```
L # L J L
O # O # O
# # K K K
O L O K K
K K J O L
```

### Step 2

Start: (0, 4), End: (2, 4), Sacrifice: (0, 3)

```
L # L # #
O # O # #
# # K K #
O L O K K
K K J O L
```

### Step 3

Start: (0, 2), End: (2, 2), Sacrifice: (1, 0)

```
L # # # #
# # # # #
# # # K #
O L O K K
K K J O L
```

### Step 4

Start: (0, 0), End: (4, 0), Sacrifice: (4, 2)

```
# # # # #
# # # # #
# # # K #
# L O K K
# K # O L
```

### Step 5

Start: (4, 1), End: (4, 4), Sacrifice: (3, 4)

```
# # # # #
# # # # #
# # # K #
# L O K #
# # # # #
```

### Step 6

Start: (3, 1), End: (3, 3), Sacrifice: (2, 3)

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
L O K J K
K O L L J
K O L L K
# L O J O
K O K L L
```

## Solution

```
L O K J K
K O L L J
K O L L K
# L O J O
K O K L L
```

### Step 1

Start: (1, 0), End: (1, 2), Sacrifice: (3, 3)

```
L O K J K
# # # L J
K O L L K
# L O # O
K O K L L
```

### Step 2

Start: (2, 2), End: (4, 2), Sacrifice: (1, 3)

```
L O K J K
# # # # J
K O # L K
# L # # O
K O # L L
```

### Step 3

Start: (2, 0), End: (2, 3), Sacrifice: (1, 4)

```
L O K J K
# # # # #
# # # # K
# L # # O
K O # L L
```

### Step 4

Start: (4, 0), End: (4, 3), Sacrifice: (3, 1)

```
L O K J K
# # # # #
# # # # K
# # # # O
# # # # L
```

### Step 5

Start: (0, 0), End: (0, 2), Sacrifice: (2, 4)

```
# # # J K
# # # # #
# # # # #
# # # # O
# # # # L
```

### Step 6

Start: (0, 4), End: (4, 4), Sacrifice: (0, 3)

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
O K K O L K
K L K L O K
O K O O K L
L L L K O O
L O O K J K
K K O L O L
```

## Solution

```
O K K O L K
K L K L O K
O K O O K L
L L L K O O
L O O K J K
K K O L O L
```

### Step 1

Start: (1, 3), End: (3, 3), Sacrifice: (5, 4)

```
O K K O L K
K L K # O K
O K O # K L
L L L # O O
L O O K J K
K K O L # L
```

### Step 2

Start: (2, 5), End: (4, 5), Sacrifice: (2, 4)

```
O K K O L K
K L K # O K
O K O # # #
L L L # O #
L O O K J #
K K O L # L
```

### Step 3

Start: (3, 1), End: (5, 1), Sacrifice: (4, 4)

```
O K K O L K
K L K # O K
O K O # # #
L # L # O #
L # O K # #
K # O L # L
```

### Step 4

Start: (1, 2), End: (3, 2), Sacrifice: (5, 5)

```
O K K O L K
K L # # O K
O K # # # #
L # # # O #
L # O K # #
K # O L # #
```

### Step 5

Start: (1, 0), End: (3, 0), Sacrifice: (0, 5)

```
O K K O L #
# L # # O K
# K # # # #
# # # # O #
L # O K # #
K # O L # #
```

### Step 6

Start: (5, 0), End: (5, 3), Sacrifice: (0, 1)

```
O # K O L #
# L # # O K
# K # # # #
# # # # O #
L # O K # #
# # # # # #
```

### Step 7

Start: (4, 0), End: (4, 3), Sacrifice: (0, 0)

```
# # K O L #
# L # # O K
# K # # # #
# # # # O #
# # # # # #
# # # # # #
```

### Step 8

Start: (0, 2), End: (0, 4), Sacrifice: (2, 1)

```
# # # # # #
# L # # O K
# # # # # #
# # # # O #
# # # # # #
# # # # # #
```

### Step 9

Start: (1, 1), End: (1, 5), Sacrifice: (3, 4)

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
J L K O L
J O L K #
K L O O J
O O K L O
L K K O L
```

## Solution

```
J L K O L
J O L K #
K L O O J
O O K L O
L K K O L
```

### Step 1

Start: (0, 2), End: (0, 4), Sacrifice: (1, 1)

```
J L # # #
J # L K #
K L O O J
O O K L O
L K K O L
```

### Step 2

Start: (2, 1), End: (4, 1), Sacrifice: (2, 4)

```
J L # # #
J # L K #
K # O O #
O # K L O
L # K O L
```

### Step 3

Start: (1, 2), End: (3, 2), Sacrifice: (0, 1)

```
J # # # #
J # # K #
K # # O #
O # # L O
L # K O L
```

### Step 4

Start: (1, 3), End: (3, 3), Sacrifice: (1, 0)

```
J # # # #
# # # # #
K # # # #
O # # # O
L # K O L
```

### Step 5

Start: (4, 2), End: (4, 4), Sacrifice: (0, 0)

```
# # # # #
# # # # #
K # # # #
O # # # O
L # # # #
```

### Step 6

Start: (2, 0), End: (4, 0), Sacrifice: (3, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 7

## Generated Puzzle

```
O L J O L
K O K O L
O K # K L
L J O O O
L O K L K
```

## Solution

```
O L J O L
K O K O L
O K # K L
L J O O O
L O K L K
```

### Step 1

Start: (1, 0), End: (3, 0), Sacrifice: (3, 2)

```
O L J O L
# O K O L
# K # K L
# J # O O
L O K L K
```

### Step 2

Start: (2, 4), End: (4, 4), Sacrifice: (0, 2)

```
O L # O L
# O K O L
# K # K #
# J # O #
L O K L #
```

### Step 3

Start: (0, 1), End: (2, 1), Sacrifice: (0, 0)

```
# # # O L
# # K O L
# # # K #
# J # O #
L O K L #
```

### Step 4

Start: (2, 3), End: (4, 3), Sacrifice: (3, 1)

```
# # # O L
# # K O L
# # # # #
# # # # #
L O K # #
```

### Step 5

Start: (1, 2), End: (1, 4), Sacrifice: (0, 4)

```
# # # O #
# # # # #
# # # # #
# # # # #
L O K # #
```

### Step 6

Start: (4, 0), End: (4, 2), Sacrifice: (0, 3)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 8

## Generated Puzzle

```
K K O L O L #
L O K L L O K
O L O K L L L
J L L O O L O
K J K O O O K
J O O K K K K
K O L L O K L
```

## Solution

```
K K O L O L #
L O K L L O K
O L O K L L L
J L L O O L O
K J K O O O K
J O O K K K K
K O L L O K L
```

### Step 1

Start: (2, 1), End: (2, 3), Sacrifice: (4, 4)

```
K K O L O L #
L O K L L O K
O # # # L L L
J L L O O L O
K J K O # O K
J O O K K K K
K O L L O K L
```

### Step 2

Start: (0, 1), End: (0, 3), Sacrifice: (4, 3)

```
K # # # O L #
L O K L L O K
O # # # L L L
J L L O O L O
K J K # # O K
J O O K K K K
K O L L O K L
```

### Step 3

Start: (3, 5), End: (5, 5), Sacrifice: (3, 1)

```
K # # # O L #
L O K L L O K
O # # # L L L
J # L O O # O
K J K # # # K
J O O K K # K
K O L L O K L
```

### Step 4

Start: (1, 0), End: (1, 2), Sacrifice: (5, 1)

```
K # # # O L #
# # # L L O K
O # # # L L L
J # L O O # O
K J K # # # K
J # O K K # K
K O L L O K L
```

### Step 5

Start: (6, 3), End: (6, 5), Sacrifice: (3, 0)

```
K # # # O L #
# # # L L O K
O # # # L L L
# # L O O # O
K J K # # # K
J # O K K # K
K O L # # # L
```

### Step 6

Start: (2, 4), End: (5, 4), Sacrifice: (5, 0)

```
K # # # O L #
# # # L L O K
O # # # # L L
# # L O # # O
K J K # # # K
# # O K # # K
K O L # # # L
```

### Step 7

Start: (1, 3), End: (5, 3), Sacrifice: (2, 0)

```
K # # # O L #
# # # # L O K
# # # # # L L
# # L # # # O
K J K # # # K
# # O # # # K
K O L # # # L
```

### Step 8

Start: (2, 6), End: (4, 6), Sacrifice: (5, 6)

```
K # # # O L #
# # # # L O K
# # # # # L #
# # L # # # #
K J K # # # #
# # O # # # #
K O L # # # L
```

### Step 9

Start: (4, 2), End: (6, 2), Sacrifice: (2, 5)

```
K # # # O L #
# # # # L O K
# # # # # # #
# # L # # # #
K J # # # # #
# # # # # # #
K O # # # # L
```

### Step 10

Start: (6, 0), End: (6, 6), Sacrifice: (4, 0)

```
K # # # O L #
# # # # L O K
# # # # # # #
# # L # # # #
# J # # # # #
# # # # # # #
# # # # # # #
```

### Step 11

Start: (0, 0), End: (0, 5), Sacrifice: (4, 1)

```
# # # # # # #
# # # # L O K
# # # # # # #
# # L # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

### Step 12

Start: (1, 4), End: (1, 6), Sacrifice: (3, 2)

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

# Puzzle 9

## Generated Puzzle

```
J O O L O K L
K L K O K L O
O K L O K L K
L K # K O L L
O O L K O L O
K L O L K O L
L K K K O O L
```

## Solution

```
J O O L O K L
K L K O K L O
O K L O K L K
L K # K O L L
O O L K O L O
K L O L K O L
L K K K O O L
```

### Step 1

Start: (0, 3), End: (0, 5), Sacrifice: (1, 5)

```
J O O # # # L
K L K O K # O
O K L O K L K
L K # K O L L
O O L K O L O
K L O L K O L
L K K K O O L
```

### Step 2

Start: (3, 0), End: (5, 0), Sacrifice: (6, 3)

```
J O O # # # L
K L K O K # O
O K L O K L K
# K # K O L L
# O L K O L O
# L O L K O L
L K K # O O L
```

### Step 3

Start: (4, 2), End: (6, 2), Sacrifice: (2, 5)

```
J O O # # # L
K L K O K # O
O K L O K # K
# K # K O L L
# O # K O L O
# L # L K O L
L K # # O O L
```

### Step 4

Start: (0, 6), End: (2, 6), Sacrifice: (3, 6)

```
J O O # # # #
K L K O K # #
O K L O K # #
# K # K O L #
# O # K O L O
# L # L K O L
L K # # O O L
```

### Step 5

Start: (3, 3), End: (3, 5), Sacrifice: (4, 6)

```
J O O # # # #
K L K O K # #
O K L O K # #
# K # # # # #
# O # K O L #
# L # L K O L
L K # # O O L
```

### Step 6

Start: (3, 1), End: (5, 1), Sacrifice: (6, 4)

```
J O O # # # #
K L K O K # #
O K L O K # #
# # # # # # #
# # # K O L #
# # # L K O L
L K # # # O L
```

### Step 7

Start: (5, 4), End: (5, 6), Sacrifice: (5, 3)

```
J O O # # # #
K L K O K # #
O K L O K # #
# # # # # # #
# # # K O L #
# # # # # # #
L K # # # O L
```

### Step 8

Start: (2, 2), End: (2, 4), Sacrifice: (1, 2)

```
J O O # # # #
K L # O K # #
O K # # # # #
# # # # # # #
# # # K O L #
# # # # # # #
L K # # # O L
```

### Step 9

Start: (1, 1), End: (1, 4), Sacrifice: (0, 0)

```
# O O # # # #
K # # # # # #
O K # # # # #
# # # # # # #
# # # K O L #
# # # # # # #
L K # # # O L
```

### Step 10

Start: (6, 1), End: (6, 6), Sacrifice: (2, 1)

```
# O O # # # #
K # # # # # #
O # # # # # #
# # # # # # #
# # # K O L #
# # # # # # #
L # # # # # #
```

### Step 11

Start: (4, 3), End: (4, 5), Sacrifice: (0, 2)

```
# O # # # # #
K # # # # # #
O # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
L # # # # # #
```

### Step 12

Start: (1, 0), End: (6, 0), Sacrifice: (0, 1)

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

# Puzzle 10

## Generated Puzzle

```
L O K # L
O K O K L
L K K O L
K O O O L
K L L O L
```

## Solution

```
L O K # L
O K O K L
L K K O L
K O O O L
K L L O L
```

### Step 1

Start: (2, 2), End: (2, 4), Sacrifice: (1, 3)

```
L O K # L
O K O # L
L K # # #
K O O O L
K L L O L
```

### Step 2

Start: (2, 1), End: (4, 1), Sacrifice: (0, 4)

```
L O K # #
O K O # L
L # # # #
K # O O L
K # L O L
```

### Step 3

Start: (1, 1), End: (1, 4), Sacrifice: (2, 0)

```
L O K # #
O # # # #
# # # # #
K # O O L
K # L O L
```

### Step 4

Start: (0, 2), End: (4, 2), Sacrifice: (0, 1)

```
L # # # #
O # # # #
# # # # #
K # # O L
K # # O L
```

### Step 5

Start: (3, 0), End: (3, 4), Sacrifice: (4, 3)

```
L # # # #
O # # # #
# # # # #
# # # # #
K # # # L
```

### Step 6

Start: (0, 0), End: (4, 0), Sacrifice: (4, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

