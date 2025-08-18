# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
K O L K L
K K O L O
L O K O K
K O L L K
J # J L O
```

## Solution

```
K O L K L
K K O L O
L O K O K
K O L L K
J # J L O
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (4, 4)

```
K O L K L
K K O L O
L O K O K
# # # L K
J # J L #
```

### Step 2

Start: (1, 1), End: (1, 3), Sacrifice: (2, 4)

```
K O L K L
K # # # O
L O K O #
# # # L K
J # J L #
```

### Step 3

Start: (2, 0), End: (2, 2), Sacrifice: (1, 0)

```
K O L K L
# # # # O
# # # O #
# # # L K
J # J L #
```

### Step 4

Start: (0, 4), End: (3, 4), Sacrifice: (4, 3)

```
K O L K #
# # # # #
# # # O #
# # # L #
J # J # #
```

### Step 5

Start: (0, 0), End: (0, 2), Sacrifice: (4, 2)

```
# # # K #
# # # # #
# # # O #
# # # L #
J # # # #
```

### Step 6

Start: (0, 3), End: (3, 3), Sacrifice: (4, 0)

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
K J L K O K K
K O L J # J L
L O J K K K O
O L O O L O K
J J O L O L O
L K O K O L L
L K L O K K L
```

## Solution

```
K J L K O K K
K O L J # J L
L O J K K K O
O L O O L O K
J J O L O L O
L K O K O L L
L K L O K K L
```

### Step 1

Start: (5, 3), End: (5, 5), Sacrifice: (4, 0)

```
K J L K O K K
K O L J # J L
L O J K K K O
O L O O L O K
# J O L O L O
L K O # # # L
L K L O K K L
```

### Step 2

Start: (2, 3), End: (4, 3), Sacrifice: (0, 1)

```
K # L K O K K
K O L J # J L
L O J # K K O
O L O # L O K
# J O # O L O
L K O # # # L
L K L O K K L
```

### Step 3

Start: (3, 4), End: (6, 4), Sacrifice: (1, 5)

```
K # L K O K K
K O L J # # L
L O J # K K O
O L O # # O K
# J O # # L O
L K O # # # L
L K L O # K L
```

### Step 4

Start: (1, 0), End: (1, 2), Sacrifice: (6, 1)

```
K # L K O K K
# # # J # # L
L O J # K K O
O L O # # O K
# J O # # L O
L K O # # # L
L # L O # K L
```

### Step 5

Start: (2, 5), End: (4, 5), Sacrifice: (4, 6)

```
K # L K O K K
# # # J # # L
L O J # K # O
O L O # # # K
# J O # # # #
L K O # # # L
L # L O # K L
```

### Step 6

Start: (3, 1), End: (3, 6), Sacrifice: (2, 2)

```
K # L K O K K
# # # J # # L
L O # # K # O
O # # # # # #
# J O # # # #
L K O # # # L
L # L O # K L
```

### Step 7

Start: (2, 0), End: (2, 4), Sacrifice: (4, 2)

```
K # L K O K K
# # # J # # L
# # # # # # O
O # # # # # #
# J # # # # #
L K O # # # L
L # L O # K L
```

### Step 8

Start: (6, 2), End: (6, 5), Sacrifice: (0, 3)

```
K # L # O K K
# # # J # # L
# # # # # # O
O # # # # # #
# J # # # # #
L K O # # # L
L # # # # # L
```

### Step 9

Start: (0, 2), End: (0, 5), Sacrifice: (1, 6)

```
K # # # # # K
# # # J # # #
# # # # # # O
O # # # # # #
# J # # # # #
L K O # # # L
L # # # # # L
```

### Step 10

Start: (5, 1), End: (5, 6), Sacrifice: (6, 0)

```
K # # # # # K
# # # J # # #
# # # # # # O
O # # # # # #
# J # # # # #
L # # # # # #
# # # # # # L
```

### Step 11

Start: (0, 6), End: (6, 6), Sacrifice: (4, 1)

```
K # # # # # #
# # # J # # #
# # # # # # #
O # # # # # #
# # # # # # #
L # # # # # #
# # # # # # #
```

### Step 12

Start: (0, 0), End: (5, 0), Sacrifice: (1, 3)

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
L O O K L
O K O L L
L # K O K
O K O L O
K L O K K
```

## Solution

```
L O O K L
O K O L L
L # K O K
O K O L O
K L O K K
```

### Step 1

Start: (3, 1), End: (3, 3), Sacrifice: (2, 2)

```
L O O K L
O K O L L
L # # O K
O # # # O
K L O K K
```

### Step 2

Start: (4, 1), End: (4, 3), Sacrifice: (1, 3)

```
L O O K L
O K O # L
L # # O K
O # # # O
K # # # K
```

### Step 3

Start: (1, 1), End: (1, 4), Sacrifice: (2, 4)

```
L O O K L
O # # # #
L # # O #
O # # # O
K # # # K
```

### Step 4

Start: (0, 4), End: (4, 4), Sacrifice: (0, 2)

```
L O # K #
O # # # #
L # # O #
O # # # #
K # # # #
```

### Step 5

Start: (2, 0), End: (4, 0), Sacrifice: (2, 3)

```
L O # K #
O # # # #
# # # # #
# # # # #
# # # # #
```

### Step 6

Start: (0, 0), End: (0, 3), Sacrifice: (1, 0)

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
K O L L J L L
L L O K K O K
L K L O O K O
O O O K L K L
K L K K L O K
O # K J O O L
L L O K O K K
```

## Solution

```
K O L L J L L
L L O K K O K
L K L O O K O
O O O K L K L
K L K K L O K
O # K J O O L
L L O K O K K
```

### Step 1

Start: (2, 1), End: (4, 1), Sacrifice: (5, 5)

```
K O L L J L L
L L O K K O K
L # L O O K O
O # O K L K L
K # K K L O K
O # K J O # L
L L O K O K K
```

### Step 2

Start: (4, 4), End: (4, 6), Sacrifice: (3, 3)

```
K O L L J L L
L L O K K O K
L # L O O K O
O # O # L K L
K # K K # # #
O # K J O # L
L L O K O K K
```

### Step 3

Start: (6, 1), End: (6, 3), Sacrifice: (5, 3)

```
K O L L J L L
L L O K K O K
L # L O O K O
O # O # L K L
K # K K # # #
O # K # O # L
L # # # O K K
```

### Step 4

Start: (5, 2), End: (5, 6), Sacrifice: (2, 0)

```
K O L L J L L
L L O K K O K
# # L O O K O
O # O # L K L
K # K K # # #
O # # # # # #
L # # # O K K
```

### Step 5

Start: (6, 0), End: (6, 5), Sacrifice: (0, 4)

```
K O L L # L L
L L O K K O K
# # L O O K O
O # O # L K L
K # K K # # #
O # # # # # #
# # # # # # K
```

### Step 6

Start: (0, 0), End: (0, 2), Sacrifice: (3, 5)

```
# # # L # L L
L L O K K O K
# # L O O K O
O # O # L # L
K # K K # # #
O # # # # # #
# # # # # # K
```

### Step 7

Start: (0, 5), End: (2, 5), Sacrifice: (6, 6)

```
# # # L # # L
L L O K K # K
# # L O O # O
O # O # L # L
K # K K # # #
O # # # # # #
# # # # # # #
```

### Step 8

Start: (1, 6), End: (3, 6), Sacrifice: (1, 3)

```
# # # L # # L
L L O # K # #
# # L O O # #
O # O # L # #
K # K K # # #
O # # # # # #
# # # # # # #
```

### Step 9

Start: (0, 3), End: (4, 3), Sacrifice: (5, 0)

```
# # # # # # L
L L O # K # #
# # L # O # #
O # O # L # #
K # K # # # #
# # # # # # #
# # # # # # #
```

### Step 10

Start: (2, 2), End: (4, 2), Sacrifice: (3, 4)

```
# # # # # # L
L L O # K # #
# # # # O # #
O # # # # # #
K # # # # # #
# # # # # # #
# # # # # # #
```

### Step 11

Start: (1, 1), End: (1, 4), Sacrifice: (0, 6)

```
# # # # # # #
L # # # # # #
# # # # O # #
O # # # # # #
K # # # # # #
# # # # # # #
# # # # # # #
```

### Step 12

Start: (1, 0), End: (4, 0), Sacrifice: (2, 4)

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

# Puzzle 5

## Generated Puzzle

```
L O K K K K
O L O O K J
L O L K J K
K L O O O K
O K J L O L
L O K K O L
```

## Solution

```
L O K K K K
O L O O K J
L O L K J K
K L O O O K
O K J L O L
L O K K O L
```

### Step 1

Start: (5, 3), End: (5, 5), Sacrifice: (0, 5)

```
L O K K K #
O L O O K J
L O L K J K
K L O O O K
O K J L O L
L O K # # #
```

### Step 2

Start: (2, 3), End: (4, 3), Sacrifice: (3, 2)

```
L O K K K #
O L O O K J
L O L # J K
K L # # O K
O K J # O L
L O K # # #
```

### Step 3

Start: (0, 2), End: (2, 2), Sacrifice: (4, 2)

```
L O # K K #
O L # O K J
L O # # J K
K L # # O K
O K # # O L
L O K # # #
```

### Step 4

Start: (3, 1), End: (3, 5), Sacrifice: (2, 4)

```
L O # K K #
O L # O K J
L O # # # K
K # # # # #
O K # # O L
L O K # # #
```

### Step 5

Start: (1, 1), End: (1, 4), Sacrifice: (0, 3)

```
L O # # K #
O # # # # J
L O # # # K
K # # # # #
O K # # O L
L O K # # #
```

### Step 6

Start: (4, 1), End: (4, 5), Sacrifice: (0, 1)

```
L # # # K #
O # # # # J
L O # # # K
K # # # # #
O # # # # #
L O K # # #
```

### Step 7

Start: (5, 0), End: (5, 2), Sacrifice: (1, 5)

```
L # # # K #
O # # # # #
L O # # # K
K # # # # #
O # # # # #
# # # # # #
```

### Step 8

Start: (2, 0), End: (2, 5), Sacrifice: (4, 0)

```
L # # # K #
O # # # # #
# # # # # #
K # # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 0), End: (3, 0), Sacrifice: (0, 4)

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
O L K O L
# K O J L
L O L K L
K K O L O
O L O K K
```

## Solution

```
O L K O L
# K O J L
L O L K L
K K O L O
O L O K K
```

### Step 1

Start: (2, 4), End: (4, 4), Sacrifice: (4, 0)

```
O L K O L
# K O J L
L O L K #
K K O L #
# L O K #
```

### Step 2

Start: (3, 1), End: (3, 3), Sacrifice: (1, 3)

```
O L K O L
# K O # L
L O L K #
K # # # #
# L O K #
```

### Step 3

Start: (0, 2), End: (0, 4), Sacrifice: (0, 0)

```
# L # # #
# K O # L
L O L K #
K # # # #
# L O K #
```

### Step 4

Start: (4, 1), End: (4, 3), Sacrifice: (2, 2)

```
# L # # #
# K O # L
L O # K #
K # # # #
# # # # #
```

### Step 5

Start: (2, 0), End: (2, 3), Sacrifice: (0, 1)

```
# # # # #
# K O # L
# # # # #
K # # # #
# # # # #
```

### Step 6

Start: (1, 1), End: (1, 4), Sacrifice: (3, 0)

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
K J # K K O L
K K O L L O K
O O K L L K L
K L O O L O K
O K L K O K O
L J L O K K J
K O L L K L K
```

## Solution

```
K J # K K O L
K K O L L O K
O O K L L K L
K L O O L O K
O K L K O K O
L J L O K K J
K O L L K L K
```

### Step 1

Start: (1, 4), End: (1, 6), Sacrifice: (5, 6)

```
K J # K K O L
K K O L # # #
O O K L L K L
K L O O L O K
O K L K O K O
L J L O K K #
K O L L K L K
```

### Step 2

Start: (2, 3), End: (4, 3), Sacrifice: (5, 4)

```
K J # K K O L
K K O L # # #
O O K # L K L
K L O # L O K
O K L # O K O
L J L O # K #
K O L L K L K
```

### Step 3

Start: (0, 4), End: (0, 6), Sacrifice: (0, 1)

```
K # # K # # #
K K O L # # #
O O K # L K L
K L O # L O K
O K L # O K O
L J L O # K #
K O L L K L K
```

### Step 4

Start: (3, 4), End: (3, 6), Sacrifice: (6, 3)

```
K # # K # # #
K K O L # # #
O O K # L K L
K L O # # # #
O K L # O K O
L J L O # K #
K O L # K L K
```

### Step 5

Start: (1, 1), End: (3, 1), Sacrifice: (6, 5)

```
K # # K # # #
K # O L # # #
O # K # L K L
K # O # # # #
O K L # O K O
L J L O # K #
K O L # K # K
```

### Step 6

Start: (2, 6), End: (6, 6), Sacrifice: (2, 5)

```
K # # K # # #
K # O L # # #
O # K # L # #
K # O # # # #
O K L # O K #
L J L O # K #
K O L # K # #
```

### Step 7

Start: (2, 2), End: (4, 2), Sacrifice: (5, 1)

```
K # # K # # #
K # O L # # #
O # # # L # #
K # # # # # #
O K # # O K #
L # L O # K #
K O L # K # #
```

### Step 8

Start: (6, 0), End: (6, 2), Sacrifice: (4, 1)

```
K # # K # # #
K # O L # # #
O # # # L # #
K # # # # # #
O # # # O K #
L # L O # K #
# # # # K # #
```

### Step 9

Start: (3, 0), End: (5, 0), Sacrifice: (2, 0)

```
K # # K # # #
K # O L # # #
# # # # L # #
# # # # # # #
# # # # O K #
# # L O # K #
# # # # K # #
```

### Step 10

Start: (1, 0), End: (1, 3), Sacrifice: (0, 3)

```
K # # # # # #
# # # # # # #
# # # # L # #
# # # # # # #
# # # # O K #
# # L O # K #
# # # # K # #
```

### Step 11

Start: (2, 4), End: (6, 4), Sacrifice: (4, 5)

```
K # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # L O # K #
# # # # # # #
```

### Step 12

Start: (5, 2), End: (5, 5), Sacrifice: (0, 0)

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
J L L L J K
L L O K O O
O O J K L L
L K O L O K
O O K O K O
K K J K K L
```

## Solution

```
J L L L J K
L L O K O O
O O J K L L
L K O L O K
O O K O K O
K K J K K L
```

### Step 1

Start: (0, 5), End: (2, 5), Sacrifice: (2, 3)

```
J L L L J #
L L O K O #
O O J # L #
L K O L O K
O O K O K O
K K J K K L
```

### Step 2

Start: (1, 1), End: (3, 1), Sacrifice: (4, 4)

```
J L L L J #
L # O K O #
O # J # L #
L # O L O K
O O K O # O
K K J K K L
```

### Step 3

Start: (1, 0), End: (1, 3), Sacrifice: (0, 4)

```
J L L L # #
# # # # O #
O # J # L #
L # O L O K
O O K O # O
K K J K K L
```

### Step 4

Start: (3, 0), End: (5, 0), Sacrifice: (2, 2)

```
J L L L # #
# # # # O #
O # # # L #
# # O L O K
# O K O # O
# K J K K L
```

### Step 5

Start: (3, 3), End: (5, 3), Sacrifice: (2, 0)

```
J L L L # #
# # # # O #
# # # # L #
# # O # O K
# O K # # O
# K J # K L
```

### Step 6

Start: (0, 2), End: (4, 2), Sacrifice: (1, 4)

```
J L # L # #
# # # # # #
# # # # L #
# # # # O K
# O # # # O
# K J # K L
```

### Step 7

Start: (2, 4), End: (5, 4), Sacrifice: (0, 3)

```
J L # # # #
# # # # # #
# # # # # #
# # # # # K
# O # # # O
# K J # # L
```

### Step 8

Start: (3, 5), End: (5, 5), Sacrifice: (5, 2)

```
J L # # # #
# # # # # #
# # # # # #
# # # # # #
# O # # # #
# K # # # #
```

### Step 9

Start: (0, 1), End: (5, 1), Sacrifice: (0, 0)

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
O L O L K K
K O L L O K
K L O K O L
K L K O L L
O L K O L L
L L O L J K
```

## Solution

```
O L O L K K
K O L L O K
K L O K O L
K L K O L L
O L K O L L
L L O L J K
```

### Step 1

Start: (1, 0), End: (1, 2), Sacrifice: (5, 3)

```
O L O L K K
# # # L O K
K L O K O L
K L K O L L
O L K O L L
L L O # J K
```

### Step 2

Start: (3, 2), End: (3, 4), Sacrifice: (0, 3)

```
O L O # K K
# # # L O K
K L O K O L
K L # # # L
O L K O L L
L L O # J K
```

### Step 3

Start: (4, 2), End: (4, 4), Sacrifice: (0, 5)

```
O L O # K #
# # # L O K
K L O K O L
K L # # # L
O L # # # L
L L O # J K
```

### Step 4

Start: (3, 0), End: (5, 0), Sacrifice: (5, 4)

```
O L O # K #
# # # L O K
K L O K O L
# L # # # L
# L # # # L
# L O # # K
```

### Step 5

Start: (2, 1), End: (2, 3), Sacrifice: (3, 1)

```
O L O # K #
# # # L O K
K # # # O L
# # # # # L
# L # # # L
# L O # # K
```

### Step 6

Start: (1, 3), End: (1, 5), Sacrifice: (4, 5)

```
O L O # K #
# # # # # #
K # # # O L
# # # # # L
# L # # # #
# L O # # K
```

### Step 7

Start: (5, 1), End: (5, 5), Sacrifice: (3, 5)

```
O L O # K #
# # # # # #
K # # # O L
# # # # # #
# L # # # #
# # # # # #
```

### Step 8

Start: (2, 0), End: (2, 5), Sacrifice: (0, 0)

```
# L O # K #
# # # # # #
# # # # # #
# # # # # #
# L # # # #
# # # # # #
```

### Step 9

Start: (0, 1), End: (0, 4), Sacrifice: (4, 1)

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
K O L L O L
L O O L K J
J O K L O K
O L K O O L
K O O K O L
K K K O L L
```

## Solution

```
K O L L O L
L O O L K J
J O K L O K
O L K O O L
K O O K O L
K K K O L L
```

### Step 1

Start: (2, 3), End: (2, 5), Sacrifice: (4, 2)

```
K O L L O L
L O O L K J
J O K # # #
O L K O O L
K O # K O L
K K K O L L
```

### Step 2

Start: (0, 2), End: (2, 2), Sacrifice: (1, 5)

```
K O # L O L
L O # L K #
J O # # # #
O L K O O L
K O # K O L
K K K O L L
```

### Step 3

Start: (3, 1), End: (5, 1), Sacrifice: (1, 1)

```
K O # L O L
L # # L K #
J O # # # #
O # K O O L
K # # K O L
K # K O L L
```

### Step 4

Start: (1, 3), End: (4, 3), Sacrifice: (2, 0)

```
K O # L O L
L # # # K #
# O # # # #
O # K # O L
K # # # O L
K # K O L L
```

### Step 5

Start: (0, 0), End: (0, 3), Sacrifice: (5, 5)

```
# # # # O L
L # # # K #
# O # # # #
O # K # O L
K # # # O L
K # K O L #
```

### Step 6

Start: (5, 2), End: (5, 4), Sacrifice: (0, 4)

```
# # # # # L
L # # # K #
# O # # # #
O # K # O L
K # # # O L
K # # # # #
```

### Step 7

Start: (4, 0), End: (4, 5), Sacrifice: (2, 1)

```
# # # # # L
L # # # K #
# # # # # #
O # K # O L
# # # # # #
K # # # # #
```

### Step 8

Start: (1, 0), End: (5, 0), Sacrifice: (1, 4)

```
# # # # # L
# # # # # #
# # # # # #
# # K # O L
# # # # # #
# # # # # #
```

### Step 9

Start: (3, 2), End: (3, 5), Sacrifice: (0, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

