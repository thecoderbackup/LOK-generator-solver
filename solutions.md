# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
L O K J #
O L L J J
K O K O L
O K K O L
L K O L K
```

## Solution

```
L O K J #
O L L J J
K O K O L
O K K O L
L K O L K
```

### Step 1

Start: (2, 2), End: (2, 4), Sacrifice: (4, 4)

```
L O K J #
O L L J J
K O # # #
O K K O L
L K O L #
```

### Step 2

Start: (0, 0), End: (0, 2), Sacrifice: (1, 0)

```
# # # J #
# L L J J
K O # # #
O K K O L
L K O L #
```

### Step 3

Start: (2, 0), End: (4, 0), Sacrifice: (1, 3)

```
# # # J #
# L L # J
# O # # #
# K K O L
# K O L #
```

### Step 4

Start: (1, 1), End: (3, 1), Sacrifice: (1, 2)

```
# # # J #
# # # # J
# # # # #
# # K O L
# K O L #
```

### Step 5

Start: (4, 1), End: (4, 3), Sacrifice: (1, 4)

```
# # # J #
# # # # #
# # # # #
# # K O L
# # # # #
```

### Step 6

Start: (3, 2), End: (3, 4), Sacrifice: (0, 3)

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
K K O L L O
L J O K O K
K L O L K L
K L J L K O
O O K O O L
L K K K L K
```

## Solution

```
K K O L L O
L J O K O K
K L O L K L
K L J L K O
O O K O O L
L K K K L K
```

### Step 1

Start: (3, 3), End: (5, 3), Sacrifice: (2, 1)

```
K K O L L O
L J O K O K
K # O L K L
K L J # K O
O O K # O L
L K K # L K
```

### Step 2

Start: (3, 0), End: (5, 0), Sacrifice: (5, 5)

```
K K O L L O
L J O K O K
K # O L K L
# L J # K O
# O K # O L
# K K # L #
```

### Step 3

Start: (2, 0), End: (2, 3), Sacrifice: (3, 2)

```
K K O L L O
L J O K O K
# # # # K L
# L # # K O
# O K # O L
# K K # L #
```

### Step 4

Start: (3, 4), End: (5, 4), Sacrifice: (4, 2)

```
K K O L L O
L J O K O K
# # # # K L
# L # # # O
# O # # # L
# K K # # #
```

### Step 5

Start: (0, 1), End: (0, 3), Sacrifice: (1, 1)

```
K # # # L O
L # O K O K
# # # # K L
# L # # # O
# O # # # L
# K K # # #
```

### Step 6

Start: (0, 4), End: (2, 4), Sacrifice: (5, 2)

```
K # # # # O
L # O K # K
# # # # # L
# L # # # O
# O # # # L
# K # # # #
```

### Step 7

Start: (1, 0), End: (1, 3), Sacrifice: (0, 5)

```
K # # # # #
# # # # # K
# # # # # L
# L # # # O
# O # # # L
# K # # # #
```

### Step 8

Start: (3, 1), End: (5, 1), Sacrifice: (2, 5)

```
K # # # # #
# # # # # K
# # # # # #
# # # # # O
# # # # # L
# # # # # #
```

### Step 9

Start: (1, 5), End: (4, 5), Sacrifice: (0, 0)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 3

## Generated Puzzle

```
L O L K K O L
L K O K O K L
K O L J L K K
L O K J L O O
K L O L O L L
L O K O K # L
L O K O K O L
```

## Solution

```
L O L K K O L
L K O K O K L
K O L J L K K
L O K J L O O
K L O L O L L
L O K O K # L
L O K O K O L
```

### Step 1

Start: (2, 0), End: (2, 2), Sacrifice: (6, 0)

```
L O L K K O L
L K O K O K L
# # # J L K K
L O K J L O O
K L O L O L L
L O K O K # L
# O K O K O L
```

### Step 2

Start: (0, 2), End: (3, 2), Sacrifice: (2, 5)

```
L O # K K O L
L K # K O K L
# # # J L # K
L O # J L O O
K L O L O L L
L O K O K # L
# O K O K O L
```

### Step 3

Start: (6, 4), End: (6, 6), Sacrifice: (6, 2)

```
L O # K K O L
L K # K O K L
# # # J L # K
L O # J L O O
K L O L O L L
L O K O K # L
# O # O # # #
```

### Step 4

Start: (1, 1), End: (4, 1), Sacrifice: (6, 3)

```
L O # K K O L
L # # K O K L
# # # J L # K
L # # J L O O
K # O L O L L
L O K O K # L
# O # # # # #
```

### Step 5

Start: (4, 0), End: (4, 3), Sacrifice: (4, 6)

```
L O # K K O L
L # # K O K L
# # # J L # K
L # # J L O O
# # # # O L #
L O K O K # L
# O # # # # #
```

### Step 6

Start: (1, 5), End: (4, 5), Sacrifice: (3, 3)

```
L O # K K O L
L # # K O # L
# # # J L # K
L # # # L # O
# # # # O # #
L O K O K # L
# O # # # # #
```

### Step 7

Start: (1, 3), End: (1, 6), Sacrifice: (5, 3)

```
L O # K K O L
L # # # # # #
# # # J L # K
L # # # L # O
# # # # O # #
L O K # K # L
# O # # # # #
```

### Step 8

Start: (0, 4), End: (0, 6), Sacrifice: (2, 3)

```
L O # K # # #
L # # # # # #
# # # # L # K
L # # # L # O
# # # # O # #
L O K # K # L
# O # # # # #
```

### Step 9

Start: (5, 0), End: (5, 2), Sacrifice: (1, 0)

```
L O # K # # #
# # # # # # #
# # # # L # K
L # # # L # O
# # # # O # #
# # # # K # L
# O # # # # #
```

### Step 10

Start: (0, 0), End: (0, 3), Sacrifice: (3, 4)

```
# # # # # # #
# # # # # # #
# # # # L # K
L # # # # # O
# # # # O # #
# # # # K # L
# O # # # # #
```

### Step 11

Start: (2, 6), End: (5, 6), Sacrifice: (6, 1)

```
# # # # # # #
# # # # # # #
# # # # L # #
L # # # # # #
# # # # O # #
# # # # K # #
# # # # # # #
```

### Step 12

Start: (2, 4), End: (5, 4), Sacrifice: (3, 0)

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

# Puzzle 4

## Generated Puzzle

```
O K # K L O K
J K O L L L L
L L L O O O J
J O L L K O O
K K L O K K O
O K O O K O L
L J K L O K K
```

## Solution

```
O K # K L O K
J K O L L L L
L L L O O O J
J O L L K O O
K K L O K K O
O K O O K O L
L J K L O K K
```

### Step 1

Start: (5, 4), End: (5, 6), Sacrifice: (6, 1)

```
O K # K L O K
J K O L L L L
L L L O O O J
J O L L K O O
K K L O K K O
O K O O # # #
L # K L O K K
```

### Step 2

Start: (1, 1), End: (1, 3), Sacrifice: (2, 0)

```
O K # K L O K
J # # # L L L
# L L O O O J
J O L L K O O
K K L O K K O
O K O O # # #
L # K L O K K
```

### Step 3

Start: (4, 0), End: (6, 0), Sacrifice: (4, 1)

```
O K # K L O K
J # # # L L L
# L L O O O J
J O L L K O O
# # L O K K O
# K O O # # #
# # K L O K K
```

### Step 4

Start: (4, 2), End: (4, 4), Sacrifice: (2, 6)

```
O K # K L O K
J # # # L L L
# L L O O O #
J O L L K O O
# # # # # K O
# K O O # # #
# # K L O K K
```

### Step 5

Start: (1, 4), End: (3, 4), Sacrifice: (0, 1)

```
O # # K L O K
J # # # # L L
# L L O # O #
J O L L # O O
# # # # # K O
# K O O # # #
# # K L O K K
```

### Step 6

Start: (0, 3), End: (3, 3), Sacrifice: (0, 0)

```
# # # # L O K
J # # # # L L
# L L # # O #
J O L # # O O
# # # # # K O
# K O O # # #
# # K L O K K
```

### Step 7

Start: (6, 3), End: (6, 5), Sacrifice: (3, 5)

```
# # # # L O K
J # # # # L L
# L L # # O #
J O L # # # O
# # # # # K O
# K O O # # #
# # K # # # K
```

### Step 8

Start: (0, 4), End: (0, 6), Sacrifice: (1, 0)

```
# # # # # # #
# # # # # L L
# L L # # O #
J O L # # # O
# # # # # K O
# K O O # # #
# # K # # # K
```

### Step 9

Start: (1, 5), End: (4, 5), Sacrifice: (4, 6)

```
# # # # # # #
# # # # # # L
# L L # # # #
J O L # # # O
# # # # # # #
# K O O # # #
# # K # # # K
```

### Step 10

Start: (3, 2), End: (6, 2), Sacrifice: (2, 2)

```
# # # # # # #
# # # # # # L
# L # # # # #
J O # # # # O
# # # # # # #
# K # O # # #
# # # # # # K
```

### Step 11

Start: (2, 1), End: (5, 1), Sacrifice: (3, 0)

```
# # # # # # #
# # # # # # L
# # # # # # #
# # # # # # O
# # # # # # #
# # # O # # #
# # # # # # K
```

### Step 12

Start: (1, 6), End: (6, 6), Sacrifice: (5, 3)

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
K J O J L
O # K K O
L O O K K
K O L O L
L O K L K
```

## Solution

```
K J O J L
O # K K O
L O O K K
K O L O L
L O K L K
```

### Step 1

Start: (4, 0), End: (4, 2), Sacrifice: (0, 3)

```
K J O # L
O # K K O
L O O K K
K O L O L
# # # L K
```

### Step 2

Start: (2, 3), End: (4, 3), Sacrifice: (1, 3)

```
K J O # L
O # K # O
L O O # K
K O L # L
# # # # K
```

### Step 3

Start: (0, 4), End: (2, 4), Sacrifice: (0, 1)

```
K # O # #
O # K # #
L O O # #
K O L # L
# # # # K
```

### Step 4

Start: (1, 2), End: (3, 2), Sacrifice: (4, 4)

```
K # O # #
O # # # #
L O # # #
K O # # L
# # # # #
```

### Step 5

Start: (0, 0), End: (2, 0), Sacrifice: (2, 1)

```
# # O # #
# # # # #
# # # # #
K O # # L
# # # # #
```

### Step 6

Start: (3, 0), End: (3, 4), Sacrifice: (0, 2)

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
K L K L K
J K O L #
O L L O K
L O O K K
L K L O K
```

## Solution

```
K L K L K
J K O L #
O L L O K
L O O K K
L K L O K
```

### Step 1

Start: (1, 1), End: (1, 3), Sacrifice: (3, 3)

```
K L K L K
J # # # #
O L L O K
L O O # K
L K L O K
```

### Step 2

Start: (4, 2), End: (4, 4), Sacrifice: (1, 0)

```
K L K L K
# # # # #
O L L O K
L O O # K
L K # # #
```

### Step 3

Start: (2, 1), End: (4, 1), Sacrifice: (0, 2)

```
K L # L K
# # # # #
O # L O K
L # O # K
L # # # #
```

### Step 4

Start: (2, 2), End: (2, 4), Sacrifice: (0, 4)

```
K L # L #
# # # # #
O # # # #
L # O # K
L # # # #
```

### Step 5

Start: (3, 0), End: (3, 4), Sacrifice: (0, 1)

```
K # # L #
# # # # #
O # # # #
# # # # #
L # # # #
```

### Step 6

Start: (0, 0), End: (4, 0), Sacrifice: (0, 3)

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
J L K O L L K
L K O K K K J
O L O O K O #
K O L L O L O
K O L O K K J
J K O K O O L
J K K L O L L
```

## Solution

```
J L K O L L K
L K O K K K J
O L O O K O #
K O L L O L O
K O L O K K J
J K O K O O L
J K K L O L L
```

### Step 1

Start: (1, 3), End: (3, 3), Sacrifice: (6, 3)

```
J L K O L L K
L K O # K K J
O L O # K O #
K O L # O L O
K O L O K K J
J K O K O O L
J K K # O L L
```

### Step 2

Start: (4, 5), End: (6, 5), Sacrifice: (1, 6)

```
J L K O L L K
L K O # K K #
O L O # K O #
K O L # O L O
K O L O K # J
J K O K O # L
J K K # O # L
```

### Step 3

Start: (5, 3), End: (5, 6), Sacrifice: (3, 6)

```
J L K O L L K
L K O # K K #
O L O # K O #
K O L # O L #
K O L O K # J
J K O # # # #
J K K # O # L
```

### Step 4

Start: (4, 2), End: (6, 2), Sacrifice: (1, 1)

```
J L K O L L K
L # O # K K #
O L O # K O #
K O L # O L #
K O # O K # J
J K # # # # #
J K # # O # L
```

### Step 5

Start: (2, 1), End: (2, 4), Sacrifice: (4, 0)

```
J L K O L L K
L # O # K K #
O # # # # O #
K O L # O L #
# O # O K # J
J K # # # # #
J K # # O # L
```

### Step 6

Start: (1, 0), End: (1, 4), Sacrifice: (0, 6)

```
J L K O L L #
# # # # # K #
O # # # # O #
K O L # O L #
# O # O K # J
J K # # # # #
J K # # O # L
```

### Step 7

Start: (1, 5), End: (3, 5), Sacrifice: (4, 3)

```
J L K O L L #
# # # # # # #
O # # # # # #
K O L # O # #
# O # # K # J
J K # # # # #
J K # # O # L
```

### Step 8

Start: (3, 0), End: (3, 2), Sacrifice: (5, 0)

```
J L K O L L #
# # # # # # #
O # # # # # #
# # # # O # #
# O # # K # J
# K # # # # #
J K # # O # L
```

### Step 9

Start: (0, 4), End: (4, 4), Sacrifice: (6, 0)

```
J L K O # L #
# # # # # # #
O # # # # # #
# # # # # # #
# O # # # # J
# K # # # # #
# K # # O # L
```

### Step 10

Start: (6, 1), End: (6, 6), Sacrifice: (2, 0)

```
J L K O # L #
# # # # # # #
# # # # # # #
# # # # # # #
# O # # # # J
# K # # # # #
# # # # # # #
```

### Step 11

Start: (0, 2), End: (0, 5), Sacrifice: (4, 6)

```
J L # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# O # # # # #
# K # # # # #
# # # # # # #
```

### Step 12

Start: (0, 1), End: (5, 1), Sacrifice: (0, 0)

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
L J L O K
O L O K #
O J K O L
K J K O L
J K O L L
```

## Solution

```
L J L O K
O L O K #
O J K O L
K J K O L
J K O L L
```

### Step 1

Start: (0, 2), End: (0, 4), Sacrifice: (1, 0)

```
L J # # #
# L O K #
O J K O L
K J K O L
J K O L L
```

### Step 2

Start: (4, 1), End: (4, 3), Sacrifice: (2, 1)

```
L J # # #
# L O K #
O # K O L
K J K O L
J # # # L
```

### Step 3

Start: (3, 2), End: (3, 4), Sacrifice: (4, 0)

```
L J # # #
# L O K #
O # K O L
K J # # #
# # # # L
```

### Step 4

Start: (0, 0), End: (3, 0), Sacrifice: (0, 1)

```
# # # # #
# L O K #
# # K O L
# J # # #
# # # # L
```

### Step 5

Start: (2, 2), End: (2, 4), Sacrifice: (3, 1)

```
# # # # #
# L O K #
# # # # #
# # # # #
# # # # L
```

### Step 6

Start: (1, 1), End: (1, 3), Sacrifice: (4, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

# Puzzle 9

## Generated Puzzle

```
L O K K L
K K K L O
L O O K K
O K L L #
L J K O L
```

## Solution

```
L O K K L
K K K L O
L O O K K
O K L L #
L J K O L
```

### Step 1

Start: (0, 4), End: (2, 4), Sacrifice: (0, 3)

```
L O K # #
K K K L #
L O O K #
O K L L #
L J K O L
```

### Step 2

Start: (1, 2), End: (3, 2), Sacrifice: (4, 1)

```
L O K # #
K K # L #
L O # K #
O K # L #
L # K O L
```

### Step 3

Start: (2, 0), End: (2, 3), Sacrifice: (3, 3)

```
L O K # #
K K # L #
# # # # #
O K # # #
L # K O L
```

### Step 4

Start: (1, 0), End: (4, 0), Sacrifice: (1, 1)

```
L O K # #
# # # L #
# # # # #
# K # # #
# # K O L
```

### Step 5

Start: (0, 0), End: (0, 2), Sacrifice: (3, 1)

```
# # # # #
# # # L #
# # # # #
# # # # #
# # K O L
```

### Step 6

Start: (4, 2), End: (4, 4), Sacrifice: (1, 3)

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
K K L J K K
L O K L L O
L K O L O L
O O O J K L
K L K K O L
L O K O J L
```

## Solution

```
K K L J K K
L O K L L O
L K O L O L
O O O J K L
K L K K O L
L O K O J L
```

### Step 1

Start: (2, 0), End: (4, 0), Sacrifice: (2, 5)

```
K K L J K K
L O K L L O
# K O L O #
# O O J K L
# L K K O L
L O K O J L
```

### Step 2

Start: (5, 0), End: (5, 2), Sacrifice: (0, 3)

```
K K L # K K
L O K L L O
# K O L O #
# O O J K L
# L K K O L
# # # O J L
```

### Step 3

Start: (0, 5), End: (3, 5), Sacrifice: (0, 0)

```
# K L # K #
L O K L L #
# K O L O #
# O O J K #
# L K K O L
# # # O J L
```

### Step 4

Start: (1, 4), End: (3, 4), Sacrifice: (1, 3)

```
# K L # K #
L O K # # #
# K O L # #
# O O J # #
# L K K O L
# # # O J L
```

### Step 5

Start: (2, 1), End: (2, 3), Sacrifice: (3, 3)

```
# K L # K #
L O K # # #
# # # # # #
# O O # # #
# L K K O L
# # # O J L
```

### Step 6

Start: (1, 0), End: (1, 2), Sacrifice: (0, 4)

```
# K L # # #
# # # # # #
# # # # # #
# O O # # #
# L K K O L
# # # O J L
```

### Step 7

Start: (4, 3), End: (4, 5), Sacrifice: (5, 5)

```
# K L # # #
# # # # # #
# # # # # #
# O O # # #
# L K # # #
# # # O J #
```

### Step 8

Start: (0, 2), End: (4, 2), Sacrifice: (5, 3)

```
# K # # # #
# # # # # #
# # # # # #
# O # # # #
# L # # # #
# # # # J #
```

### Step 9

Start: (0, 1), End: (4, 1), Sacrifice: (5, 4)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

