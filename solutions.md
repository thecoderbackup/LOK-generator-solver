# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
L K L O L
O K K K K
K O L O K
K K O L O
K # L K L
```

## Solution

```
L K L O L
O K K K K
K O L O K
K K O L O
K # L K L
```

### Step 1

Start: (2, 4), End: (4, 4), Sacrifice: (4, 0)

```
L K L O L
O K K K K
K O L O #
K K O L #
# # L K #
```

### Step 2

Start: (2, 0), End: (2, 2), Sacrifice: (4, 3)

```
L K L O L
O K K K K
# # # O #
K K O L #
# # L # #
```

### Step 3

Start: (1, 3), End: (3, 3), Sacrifice: (1, 4)

```
L K L O L
O K K # #
# # # # #
K K O # #
# # L # #
```

### Step 4

Start: (0, 0), End: (3, 0), Sacrifice: (0, 2)

```
# K # O L
# K K # #
# # # # #
# K O # #
# # L # #
```

### Step 5

Start: (1, 2), End: (4, 2), Sacrifice: (3, 1)

```
# K # O L
# K # # #
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

# Puzzle 2

## Generated Puzzle

```
K K O L L
# O L O K
L O K O K
O L J K O
K O L O L
```

## Solution

```
K K O L L
# O L O K
L O K O K
O L J K O
K O L O L
```

### Step 1

Start: (1, 2), End: (1, 4), Sacrifice: (3, 2)

```
K K O L L
# O # # #
L O K O K
O L # K O
K O L O L
```

### Step 2

Start: (2, 0), End: (2, 2), Sacrifice: (2, 4)

```
K K O L L
# O # # #
# # # O #
O L # K O
K O L O L
```

### Step 3

Start: (4, 0), End: (4, 2), Sacrifice: (4, 4)

```
K K O L L
# O # # #
# # # O #
O L # K O
# # # O #
```

### Step 4

Start: (0, 1), End: (3, 1), Sacrifice: (4, 3)

```
K # O L L
# # # # #
# # # O #
O # # K O
# # # # #
```

### Step 5

Start: (0, 3), End: (3, 3), Sacrifice: (3, 0)

```
K # O # L
# # # # #
# # # # #
# # # # O
# # # # #
```

### Step 6

Start: (0, 0), End: (0, 4), Sacrifice: (3, 4)

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
J L K O L O
K O K O O L
O K K O L O
L O K K L K
L L O O O K
J L K L K K
```

## Solution

```
J L K O L O
K O K O O L
O K K O L O
L O K K L K
L L O O O K
J L K L K K
```

### Step 1

Start: (0, 2), End: (0, 4), Sacrifice: (5, 2)

```
J L # # # O
K O K O O L
O K K O L O
L O K K L K
L L O O O K
J L # L K K
```

### Step 2

Start: (3, 0), End: (3, 2), Sacrifice: (5, 1)

```
J L # # # O
K O K O O L
O K K O L O
# # # K L K
L L O O O K
J # # L K K
```

### Step 3

Start: (3, 4), End: (5, 4), Sacrifice: (1, 2)

```
J L # # # O
K O # O O L
O K K O L O
# # # K # K
L L O O # K
J # # L # K
```

### Step 4

Start: (3, 3), End: (5, 3), Sacrifice: (1, 3)

```
J L # # # O
K O # # O L
O K K O L O
# # # # # K
L L O # # K
J # # # # K
```

### Step 5

Start: (2, 2), End: (2, 4), Sacrifice: (0, 5)

```
J L # # # #
K O # # O L
O K # # # O
# # # # # K
L L O # # K
J # # # # K
```

### Step 6

Start: (1, 0), End: (4, 0), Sacrifice: (5, 5)

```
J L # # # #
# O # # O L
# K # # # O
# # # # # K
# L O # # K
J # # # # #
```

### Step 7

Start: (1, 5), End: (3, 5), Sacrifice: (1, 4)

```
J L # # # #
# O # # # #
# K # # # #
# # # # # #
# L O # # K
J # # # # #
```

### Step 8

Start: (4, 1), End: (4, 5), Sacrifice: (0, 0)

```
# L # # # #
# O # # # #
# K # # # #
# # # # # #
# # # # # #
J # # # # #
```

### Step 9

Start: (0, 1), End: (2, 1), Sacrifice: (5, 0)

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
J L K K O L
K K O L O K
O L O L L O
L K K K O L
O O O O O L
L L L K K O
```

## Solution

```
J L K K O L
K K O L O K
O L O L L O
L K K K O L
O O O O O L
L L L K K O
```

### Step 1

Start: (0, 3), End: (0, 5), Sacrifice: (3, 3)

```
J L K # # #
K K O L O K
O L O L L O
L K K # O L
O O O O O L
L L L K K O
```

### Step 2

Start: (3, 2), End: (3, 5), Sacrifice: (0, 0)

```
# L K # # #
K K O L O K
O L O L L O
L K # # # #
O O O O O L
L L L K K O
```

### Step 3

Start: (1, 1), End: (1, 3), Sacrifice: (2, 1)

```
# L K # # #
K # # # O K
O # O L L O
L K # # # #
O O O O O L
L L L K K O
```

### Step 4

Start: (2, 4), End: (5, 4), Sacrifice: (1, 4)

```
# L K # # #
K # # # # K
O # O L # O
L K # # # #
O O O O # L
L L L K # O
```

### Step 5

Start: (2, 3), End: (5, 3), Sacrifice: (4, 0)

```
# L K # # #
K # # # # K
O # O # # O
L K # # # #
# O O # # L
L L L # # O
```

### Step 6

Start: (1, 0), End: (3, 0), Sacrifice: (0, 1)

```
# # K # # #
# # # # # K
# # O # # O
# K # # # #
# O O # # L
L L L # # O
```

### Step 7

Start: (3, 1), End: (5, 1), Sacrifice: (4, 2)

```
# # K # # #
# # # # # K
# # O # # O
# # # # # #
# # # # # L
L # L # # O
```

### Step 8

Start: (1, 5), End: (4, 5), Sacrifice: (5, 5)

```
# # K # # #
# # # # # #
# # O # # #
# # # # # #
# # # # # #
L # L # # #
```

### Step 9

Start: (0, 2), End: (5, 2), Sacrifice: (5, 0)

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
J K L K O L
L O O J K K
J L K K O K
L O K O L O
O K L O K O
K L O L K L
```

## Solution

```
J K L K O L
L O O J K K
J L K K O K
L O K O L O
O K L O K O
K L O L K L
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (4, 3)

```
J K L K O L
L O O J K K
J L K K O K
# # # O L O
O K L # K O
K L O L K L
```

### Step 2

Start: (2, 3), End: (5, 3), Sacrifice: (4, 2)

```
J K L K O L
L O O J K K
J L K # O K
# # # # L O
O K # # K O
K L O # K L
```

### Step 3

Start: (0, 1), End: (2, 1), Sacrifice: (4, 1)

```
J # L K O L
L # O J K K
J # K # O K
# # # # L O
O # # # K O
K L O # K L
```

### Step 4

Start: (5, 1), End: (5, 4), Sacrifice: (0, 0)

```
# # L K O L
L # O J K K
J # K # O K
# # # # L O
O # # # K O
K # # # # L
```

### Step 5

Start: (1, 4), End: (3, 4), Sacrifice: (3, 5)

```
# # L K O L
L # O J # K
J # K # # K
# # # # # #
O # # # K O
K # # # # L
```

### Step 6

Start: (2, 5), End: (5, 5), Sacrifice: (1, 5)

```
# # L K O L
L # O J # #
J # K # # #
# # # # # #
O # # # K #
K # # # # #
```

### Step 7

Start: (0, 2), End: (2, 2), Sacrifice: (4, 4)

```
# # # K O L
L # # J # #
J # # # # #
# # # # # #
O # # # # #
K # # # # #
```

### Step 8

Start: (0, 3), End: (0, 5), Sacrifice: (2, 0)

```
# # # # # #
L # # J # #
# # # # # #
# # # # # #
O # # # # #
K # # # # #
```

### Step 9

Start: (1, 0), End: (5, 0), Sacrifice: (1, 3)

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
K L O L J L K
K O O L K O J
K K L O L K O
O O O K J K J
L O K K K O L
O O L O O L K
L # J L L O K
```

## Solution

```
K L O L J L K
K O O L K O J
K K L O L K O
O O O K J K J
L O K K K O L
O O L O O L K
L # J L L O K
```

### Step 1

Start: (4, 4), End: (6, 4), Sacrifice: (3, 1)

```
K L O L J L K
K O O L K O J
K K L O L K O
O # O K J K J
L O K K # O L
O O L O # L K
L # J L # O K
```

### Step 2

Start: (2, 2), End: (4, 2), Sacrifice: (1, 4)

```
K L O L J L K
K O O L # O J
K K # O L K O
O # # K J K J
L O # K # O L
O O L O # L K
L # J L # O K
```

### Step 3

Start: (6, 3), End: (6, 6), Sacrifice: (5, 1)

```
K L O L J L K
K O O L # O J
K K # O L K O
O # # K J K J
L O # K # O L
O # L O # L K
L # J # # # #
```

### Step 4

Start: (0, 1), End: (2, 1), Sacrifice: (2, 4)

```
K # O L J L K
K # O L # O J
K # # O # K O
O # # K J K J
L O # K # O L
O # L O # L K
L # J # # # #
```

### Step 5

Start: (0, 5), End: (2, 5), Sacrifice: (3, 0)

```
K # O L J # K
K # O L # # J
K # # O # # O
# # # K J K J
L O # K # O L
O # L O # L K
L # J # # # #
```

### Step 6

Start: (1, 0), End: (1, 3), Sacrifice: (2, 3)

```
K # O L J # K
# # # # # # J
K # # # # # O
# # # K J K J
L O # K # O L
O # L O # L K
L # J # # # #
```

### Step 7

Start: (4, 0), End: (4, 3), Sacrifice: (1, 6)

```
K # O L J # K
# # # # # # #
K # # # # # O
# # # K J K J
# # # # # O L
O # L O # L K
L # J # # # #
```

### Step 8

Start: (0, 0), End: (0, 3), Sacrifice: (3, 6)

```
# # # # J # K
# # # # # # #
K # # # # # O
# # # K J K #
# # # # # O L
O # L O # L K
L # J # # # #
```

### Step 9

Start: (0, 6), End: (4, 6), Sacrifice: (0, 4)

```
# # # # # # #
# # # # # # #
K # # # # # #
# # # K J K #
# # # # # O #
O # L O # L K
L # J # # # #
```

### Step 10

Start: (3, 5), End: (5, 5), Sacrifice: (3, 4)

```
# # # # # # #
# # # # # # #
K # # # # # #
# # # K # # #
# # # # # # #
O # L O # # K
L # J # # # #
```

### Step 11

Start: (2, 0), End: (6, 0), Sacrifice: (6, 2)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # K # # #
# # # # # # #
# # L O # # K
# # # # # # #
```

### Step 12

Start: (5, 2), End: (5, 6), Sacrifice: (3, 3)

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
J O L O K
# L O K L
J L L L O
L O K O K
K L O K L
```

## Solution

```
J O L O K
# L O K L
J L L L O
L O K O K
K L O K L
```

### Step 1

Start: (0, 2), End: (0, 4), Sacrifice: (4, 1)

```
J O # # #
# L O K L
J L L L O
L O K O K
K # O K L
```

### Step 2

Start: (1, 4), End: (3, 4), Sacrifice: (0, 1)

```
J # # # #
# L O K #
J L L L #
L O K O #
K # O K L
```

### Step 3

Start: (3, 0), End: (3, 2), Sacrifice: (2, 2)

```
J # # # #
# L O K #
J L # L #
# # # O #
K # O K L
```

### Step 4

Start: (1, 1), End: (1, 3), Sacrifice: (2, 1)

```
J # # # #
# # # # #
J # # L #
# # # O #
K # O K L
```

### Step 5

Start: (2, 3), End: (4, 3), Sacrifice: (0, 0)

```
# # # # #
# # # # #
J # # # #
# # # # #
K # O # L
```

### Step 6

Start: (4, 0), End: (4, 4), Sacrifice: (2, 0)

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
K K K L O J
L O K L O K
O O O K K L
O L O K O K
K K O L L O
L L L O K L
```

## Solution

```
K K K L O J
L O K L O K
O O O K K L
O L O K O K
K K O L L O
L L L O K L
```

### Step 1

Start: (5, 2), End: (5, 4), Sacrifice: (4, 1)

```
K K K L O J
L O K L O K
O O O K K L
O L O K O K
K # O L L O
L L # # # L
```

### Step 2

Start: (3, 5), End: (5, 5), Sacrifice: (2, 5)

```
K K K L O J
L O K L O K
O O O K K #
O L O K O #
K # O L L #
L L # # # #
```

### Step 3

Start: (1, 0), End: (1, 2), Sacrifice: (2, 2)

```
K K K L O J
# # # L O K
O O # K K #
O L O K O #
K # O L L #
L L # # # #
```

### Step 4

Start: (4, 0), End: (4, 3), Sacrifice: (2, 3)

```
K K K L O J
# # # L O K
O O # # K #
O L O K O #
# # # # L #
L L # # # #
```

### Step 5

Start: (3, 1), End: (3, 3), Sacrifice: (3, 0)

```
K K K L O J
# # # L O K
O O # # K #
# # # # O #
# # # # L #
L L # # # #
```

### Step 6

Start: (0, 1), End: (5, 1), Sacrifice: (0, 4)

```
K # K L # J
# # # L O K
O # # # K #
# # # # O #
# # # # L #
L # # # # #
```

### Step 7

Start: (2, 4), End: (4, 4), Sacrifice: (0, 5)

```
K # K L # #
# # # L O K
O # # # # #
# # # # # #
# # # # # #
L # # # # #
```

### Step 8

Start: (1, 3), End: (1, 5), Sacrifice: (0, 3)

```
K # K # # #
# # # # # #
O # # # # #
# # # # # #
# # # # # #
L # # # # #
```

### Step 9

Start: (0, 0), End: (5, 0), Sacrifice: (0, 2)

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
L K O L K K J
L O L O L O K
O L L L L L O
K K K O O O L
# L O K J O J
L O O K K K J
O K K L O K J
```

## Solution

```
L K O L K K J
L O L O L O K
O L L L L L O
K K K O O O L
# L O K J O J
L O O K K K J
O K K L O K J
```

### Step 1

Start: (2, 3), End: (4, 3), Sacrifice: (4, 4)

```
L K O L K K J
L O L O L O K
O L L # L L O
K K K # O O L
# L O # # O J
L O O K K K J
O K K L O K J
```

### Step 2

Start: (0, 3), End: (5, 3), Sacrifice: (0, 6)

```
L K O # K K #
L O L # L O K
O L L # L L O
K K K # O O L
# L O # # O J
L O O # K K J
O K K L O K J
```

### Step 3

Start: (2, 4), End: (5, 4), Sacrifice: (5, 6)

```
L K O # K K #
L O L # L O K
O L L # # L O
K K K # # O L
# L O # # O J
L O O # # K #
O K K L O K J
```

### Step 4

Start: (0, 1), End: (2, 1), Sacrifice: (4, 6)

```
L # O # K K #
L # L # L O K
O # L # # L O
K K K # # O L
# L O # # O #
L O O # # K #
O K K L O K J
```

### Step 5

Start: (3, 2), End: (3, 6), Sacrifice: (6, 0)

```
L # O # K K #
L # L # L O K
O # L # # L O
K K # # # # #
# L O # # O #
L O O # # K #
# K K L O K J
```

### Step 6

Start: (1, 4), End: (1, 6), Sacrifice: (2, 2)

```
L # O # K K #
L # L # # # #
O # # # # L O
K K # # # # #
# L O # # O #
L O O # # K #
# K K L O K J
```

### Step 7

Start: (2, 5), End: (5, 5), Sacrifice: (5, 2)

```
L # O # K K #
L # L # # # #
O # # # # # O
K K # # # # #
# L O # # # #
L O # # # # #
# K K L O K J
```

### Step 8

Start: (1, 0), End: (3, 0), Sacrifice: (2, 6)

```
L # O # K K #
# # L # # # #
# # # # # # #
# K # # # # #
# L O # # # #
L O # # # # #
# K K L O K J
```

### Step 9

Start: (4, 1), End: (6, 1), Sacrifice: (6, 6)

```
L # O # K K #
# # L # # # #
# # # # # # #
# K # # # # #
# # O # # # #
L # # # # # #
# # K L O K #
```

### Step 10

Start: (6, 3), End: (6, 5), Sacrifice: (0, 4)

```
L # O # # K #
# # L # # # #
# # # # # # #
# K # # # # #
# # O # # # #
L # # # # # #
# # K # # # #
```

### Step 11

Start: (1, 2), End: (6, 2), Sacrifice: (3, 1)

```
L # O # # K #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
L # # # # # #
# # # # # # #
```

### Step 12

Start: (0, 0), End: (0, 5), Sacrifice: (5, 0)

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
L L L K O L
K J O J O L
L O K L O K
O K L O L K
K K J O O L
L J L O K K
```

## Solution

```
L L L K O L
K J O J O L
L O K L O K
O K L O L K
K K J O O L
L J L O K K
```

### Step 1

Start: (3, 4), End: (5, 4), Sacrifice: (4, 1)

```
L L L K O L
K J O J O L
L O K L O K
O K L O # K
K # J O # L
L J L O # K
```

### Step 2

Start: (0, 3), End: (0, 5), Sacrifice: (4, 2)

```
L L L # # #
K J O J O L
L O K L O K
O K L O # K
K # # O # L
L J L O # K
```

### Step 3

Start: (0, 2), End: (2, 2), Sacrifice: (5, 0)

```
L L # # # #
K J # J O L
L O # L O K
O K L O # K
K # # O # L
# J L O # K
```

### Step 4

Start: (2, 3), End: (2, 5), Sacrifice: (2, 0)

```
L L # # # #
K J # J O L
# O # # # #
O K L O # K
K # # O # L
# J L O # K
```

### Step 5

Start: (4, 0), End: (4, 5), Sacrifice: (1, 1)

```
L L # # # #
K # # J O L
# O # # # #
O K L O # K
# # # # # #
# J L O # K
```

### Step 6

Start: (5, 2), End: (5, 5), Sacrifice: (5, 1)

```
L L # # # #
K # # J O L
# O # # # #
O K L O # K
# # # # # #
# # # # # #
```

### Step 7

Start: (3, 2), End: (3, 5), Sacrifice: (1, 3)

```
L L # # # #
K # # # O L
# O # # # #
O K # # # #
# # # # # #
# # # # # #
```

### Step 8

Start: (1, 0), End: (1, 5), Sacrifice: (0, 0)

```
# L # # # #
# # # # # #
# O # # # #
O K # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 1), End: (3, 1), Sacrifice: (3, 0)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

