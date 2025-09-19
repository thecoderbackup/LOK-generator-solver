# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
K L L O K
L O K O L
K K L # O
O K L O L
L J K O L
```

## Solution

```
K L L O K
L O K O L
K K L # O
O K L O L
L J K O L
```

### Step 1

Start: (1, 2), End: (1, 4), Sacrifice: (2, 4)

```
K L L O K
L O # # #
K K L # #
O K L O L
L J K O L
```

### Step 2

Start: (4, 2), End: (4, 4), Sacrifice: (1, 0)

```
K L L O K
# O # # #
K K L # #
O K L O L
L J # # #
```

### Step 3

Start: (0, 1), End: (2, 1), Sacrifice: (2, 0)

```
K # L O K
# # # # #
# # L # #
O K L O L
L J # # #
```

### Step 4

Start: (0, 2), End: (0, 4), Sacrifice: (3, 2)

```
K # # # #
# # # # #
# # L # #
O K # O L
L J # # #
```

### Step 5

Start: (3, 1), End: (3, 4), Sacrifice: (2, 2)

```
K # # # #
# # # # #
# # # # #
O # # # #
L J # # #
```

### Step 6

Start: (0, 0), End: (4, 0), Sacrifice: (4, 1)

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
K K L L O L K
O O J O L L O
L K L K O O K
O O L L L J L
K L O O O # O
L L K K K O K
K O L K K L J
```

## Solution

```
K K L L O L K
O O J O L L O
L K L K O O K
O O L L L J L
K L O O O # O
L L K K K O K
K O L K K L J
```

### Step 1

Start: (0, 3), End: (2, 3), Sacrifice: (6, 3)

```
K K L # O L K
O O J # L L O
L K L # O O K
O O L L L J L
K L O O O # O
L L K K K O K
K O L # K L J
```

### Step 2

Start: (3, 4), End: (5, 4), Sacrifice: (1, 5)

```
K K L # O L K
O O J # L # O
L K L # O O K
O O L L # J L
K L O O # # O
L L K K # O K
K O L # K L J
```

### Step 3

Start: (2, 1), End: (4, 1), Sacrifice: (6, 2)

```
K K L # O L K
O O J # L # O
L # L # O O K
O # L L # J L
K # O O # # O
L L K K # O K
K O # # K L J
```

### Step 4

Start: (2, 0), End: (4, 0), Sacrifice: (0, 5)

```
K K L # O # K
O O J # L # O
# # L # O O K
# # L L # J L
# # O O # # O
L L K K # O K
K O # # K L J
```

### Step 5

Start: (0, 1), End: (5, 1), Sacrifice: (1, 2)

```
K # L # O # K
O # # # L # O
# # L # O O K
# # L L # J L
# # O O # # O
L # K K # O K
K O # # K L J
```

### Step 6

Start: (1, 4), End: (6, 4), Sacrifice: (3, 2)

```
K # L # O # K
O # # # # # O
# # L # # O K
# # # L # J L
# # O O # # O
L # K K # O K
K O # # # L J
```

### Step 7

Start: (3, 3), End: (5, 3), Sacrifice: (6, 6)

```
K # L # O # K
O # # # # # O
# # L # # O K
# # # # # J L
# # O # # # O
L # K # # O K
K O # # # L #
```

### Step 8

Start: (0, 0), End: (5, 0), Sacrifice: (2, 6)

```
# # L # O # K
# # # # # # O
# # L # # O #
# # # # # J L
# # O # # # O
# # K # # O K
K O # # # L #
```

### Step 9

Start: (3, 6), End: (5, 6), Sacrifice: (2, 5)

```
# # L # O # K
# # # # # # O
# # L # # # #
# # # # # J #
# # O # # # #
# # K # # O #
K O # # # L #
```

### Step 10

Start: (6, 0), End: (6, 5), Sacrifice: (1, 6)

```
# # L # O # K
# # # # # # #
# # L # # # #
# # # # # J #
# # O # # # #
# # K # # O #
# # # # # # #
```

### Step 11

Start: (2, 2), End: (5, 2), Sacrifice: (5, 5)

```
# # L # O # K
# # # # # # #
# # # # # # #
# # # # # J #
# # # # # # #
# # # # # # #
# # # # # # #
```

### Step 12

Start: (0, 2), End: (0, 6), Sacrifice: (3, 5)

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
K O K J J
K L O O L
K O J O L
K K L O L
O L O K #
```

## Solution

```
K O K J J
K L O O L
K O J O L
K K L O L
O L O K #
```

### Step 1

Start: (1, 1), End: (3, 1), Sacrifice: (2, 2)

```
K O K J J
K # O O L
K # # O L
K # L O L
O L O K #
```

### Step 2

Start: (4, 1), End: (4, 3), Sacrifice: (0, 3)

```
K O K # J
K # O O L
K # # O L
K # L O L
O # # # #
```

### Step 3

Start: (0, 2), End: (3, 2), Sacrifice: (0, 0)

```
# O # # J
K # # O L
K # # O L
K # # O L
O # # # #
```

### Step 4

Start: (3, 0), End: (3, 4), Sacrifice: (4, 0)

```
# O # # J
K # # O L
K # # O L
# # # # #
# # # # #
```

### Step 5

Start: (1, 0), End: (1, 4), Sacrifice: (0, 1)

```
# # # # J
# # # # #
K # # O L
# # # # #
# # # # #
```

### Step 6

Start: (2, 0), End: (2, 4), Sacrifice: (0, 4)

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
K # L O K
L K O L J
O K L O K
K O K O L
J L L K L
```

## Solution

```
K # L O K
L K O L J
O K L O K
K O K O L
J L L K L
```

### Step 1

Start: (1, 0), End: (3, 0), Sacrifice: (4, 4)

```
K # L O K
# K O L J
# K L O K
# O K O L
J L L K #
```

### Step 2

Start: (1, 1), End: (1, 3), Sacrifice: (4, 2)

```
K # L O K
# # # # J
# K L O K
# O K O L
J L # K #
```

### Step 3

Start: (3, 2), End: (3, 4), Sacrifice: (4, 0)

```
K # L O K
# # # # J
# K L O K
# O # # #
# L # K #
```

### Step 4

Start: (0, 2), End: (0, 4), Sacrifice: (0, 0)

```
# # # # #
# # # # J
# K L O K
# O # # #
# L # K #
```

### Step 5

Start: (2, 1), End: (4, 1), Sacrifice: (4, 3)

```
# # # # #
# # # # J
# # L O K
# # # # #
# # # # #
```

### Step 6

Start: (2, 2), End: (2, 4), Sacrifice: (1, 4)

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
K K L O K O L
L L O L K L J
O L L K L L O
L K L O K O K
K O L O O J K
O L O L K K O
L K K # K K L
```

## Solution

```
K K L O K O L
L L O L K L J
O L L K L L O
L K L O K O K
K O L O O J K
O L O L K K O
L K K # K K L
```

### Step 1

Start: (4, 0), End: (6, 0), Sacrifice: (4, 5)

```
K K L O K O L
L L O L K L J
O L L K L L O
L K L O K O K
# O L O O # K
# L O L K K O
# K K # K K L
```

### Step 2

Start: (4, 2), End: (6, 2), Sacrifice: (2, 2)

```
K K L O K O L
L L O L K L J
O L # K L L O
L K L O K O K
# O # O O # K
# L # L K K O
# K # # K K L
```

### Step 3

Start: (3, 2), End: (3, 4), Sacrifice: (4, 6)

```
K K L O K O L
L L O L K L J
O L # K L L O
L K # # # O K
# O # O O # #
# L # L K K O
# K # # K K L
```

### Step 4

Start: (3, 6), End: (6, 6), Sacrifice: (1, 0)

```
K K L O K O L
# L O L K L J
O L # K L L O
L K # # # O #
# O # O O # #
# L # L K K #
# K # # K K #
```

### Step 5

Start: (3, 1), End: (5, 1), Sacrifice: (5, 5)

```
K K L O K O L
# L O L K L J
O L # K L L O
L # # # # O #
# # # O O # #
# # # L K # #
# K # # K K #
```

### Step 6

Start: (2, 5), End: (6, 5), Sacrifice: (6, 4)

```
K K L O K O L
# L O L K L J
O L # K L # O
L # # # # # #
# # # O O # #
# # # L K # #
# K # # # # #
```

### Step 7

Start: (0, 0), End: (3, 0), Sacrifice: (2, 1)

```
# K L O K O L
# L O L K L J
# # # K L # O
# # # # # # #
# # # O O # #
# # # L K # #
# K # # # # #
```

### Step 8

Start: (2, 3), End: (5, 3), Sacrifice: (1, 6)

```
# K L O K O L
# L O L K L #
# # # # L # O
# # # # # # #
# # # # O # #
# # # # K # #
# K # # # # #
```

### Step 9

Start: (0, 2), End: (0, 4), Sacrifice: (1, 3)

```
# K # # # O L
# L O # K L #
# # # # L # O
# # # # # # #
# # # # O # #
# # # # K # #
# K # # # # #
```

### Step 10

Start: (1, 1), End: (1, 4), Sacrifice: (2, 6)

```
# K # # # O L
# # # # # L #
# # # # L # #
# # # # # # #
# # # # O # #
# # # # K # #
# K # # # # #
```

### Step 11

Start: (0, 1), End: (0, 6), Sacrifice: (1, 5)

```
# # # # # # #
# # # # # # #
# # # # L # #
# # # # # # #
# # # # O # #
# # # # K # #
# K # # # # #
```

### Step 12

Start: (2, 4), End: (5, 4), Sacrifice: (6, 1)

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

# Puzzle 6

## Generated Puzzle

```
# L O L K
L O K L O
O K O O O
K O L K L
K L K O L
```

## Solution

```
# L O L K
L O K L O
O K O O O
K O L K L
K L K O L
```

### Step 1

Start: (4, 2), End: (4, 4), Sacrifice: (1, 3)

```
# L O L K
L O K # O
O K O O O
K O L K L
K L # # #
```

### Step 2

Start: (2, 1), End: (4, 1), Sacrifice: (4, 0)

```
# L O L K
L O K # O
O # O O O
K # L K L
# # # # #
```

### Step 3

Start: (0, 3), End: (3, 3), Sacrifice: (2, 4)

```
# L O # K
L O K # O
O # O # #
K # L # L
# # # # #
```

### Step 4

Start: (1, 2), End: (3, 2), Sacrifice: (3, 4)

```
# L O # K
L O # # O
O # # # #
K # # # #
# # # # #
```

### Step 5

Start: (0, 1), End: (0, 4), Sacrifice: (1, 4)

```
# # # # #
L O # # #
O # # # #
K # # # #
# # # # #
```

### Step 6

Start: (1, 0), End: (3, 0), Sacrifice: (1, 1)

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
K L O K J
O L K O L
L O L J L
# K L O K
K O L J J
```

## Solution

```
K L O K J
O L K O L
L O L J L
# K L O K
K O L J J
```

### Step 1

Start: (0, 0), End: (2, 0), Sacrifice: (2, 3)

```
# L O K J
# L K O L
# O L # L
# K L O K
K O L J J
```

### Step 2

Start: (0, 1), End: (0, 3), Sacrifice: (2, 2)

```
# # # # J
# L K O L
# O # # L
# K L O K
K O L J J
```

### Step 3

Start: (1, 1), End: (3, 1), Sacrifice: (0, 4)

```
# # # # #
# # K O L
# # # # L
# # L O K
K O L J J
```

### Step 4

Start: (3, 2), End: (3, 4), Sacrifice: (4, 3)

```
# # # # #
# # K O L
# # # # L
# # # # #
K O L # J
```

### Step 5

Start: (1, 2), End: (1, 4), Sacrifice: (2, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
K O L # J
```

### Step 6

Start: (4, 0), End: (4, 2), Sacrifice: (4, 4)

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
J O L J L
# K O L J
L O K O L
O L O K O
K K O L K
```

## Solution

```
J O L J L
# K O L J
L O K O L
O L O K O
K K O L K
```

### Step 1

Start: (3, 1), End: (3, 3), Sacrifice: (0, 2)

```
J O # J L
# K O L J
L O K O L
O # # # O
K K O L K
```

### Step 2

Start: (1, 1), End: (1, 3), Sacrifice: (1, 4)

```
J O # J L
# # # # #
L O K O L
O # # # O
K K O L K
```

### Step 3

Start: (2, 0), End: (4, 0), Sacrifice: (0, 1)

```
J # # J L
# # # # #
# O K O L
# # # # O
# K O L K
```

### Step 4

Start: (2, 2), End: (2, 4), Sacrifice: (0, 3)

```
J # # # L
# # # # #
# O # # #
# # # # O
# K O L K
```

### Step 5

Start: (4, 1), End: (4, 3), Sacrifice: (2, 1)

```
J # # # L
# # # # #
# # # # #
# # # # O
# # # # K
```

### Step 6

Start: (0, 4), End: (4, 4), Sacrifice: (0, 0)

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
L O K L O K K
# L L O K K L
O L K O O L L
K K O L K L O
L O K K O O K
O K O O L K O
K K L K O L J
```

## Solution

```
L O K L O K K
# L L O K K L
O L K O O L L
K K O L K L O
L O K K O O K
O K O O L K O
K K L K O L J
```

### Step 1

Start: (6, 3), End: (6, 5), Sacrifice: (5, 6)

```
L O K L O K K
# L L O K K L
O L K O O L L
K K O L K L O
L O K K O O K
O K O O L K #
K K L # # # J
```

### Step 2

Start: (3, 5), End: (5, 5), Sacrifice: (3, 0)

```
L O K L O K K
# L L O K K L
O L K O O L L
# K O L K # O
L O K K O # K
O K O O L # #
K K L # # # J
```

### Step 3

Start: (2, 6), End: (4, 6), Sacrifice: (0, 2)

```
L O # L O K K
# L L O K K L
O L K O O L #
# K O L K # #
L O K K O # #
O K O O L # #
K K L # # # J
```

### Step 4

Start: (4, 2), End: (6, 2), Sacrifice: (4, 3)

```
L O # L O K K
# L L O K K L
O L K O O L #
# K O L K # #
L O # # O # #
O K # O L # #
K K # # # # J
```

### Step 5

Start: (3, 4), End: (5, 4), Sacrifice: (1, 4)

```
L O # L O K K
# L L O # K L
O L K O O L #
# K O L # # #
L O # # # # #
O K # O # # #
K K # # # # J
```

### Step 6

Start: (0, 3), End: (0, 5), Sacrifice: (6, 6)

```
L O # # # # K
# L L O # K L
O L K O O L #
# K O L # # #
L O # # # # #
O K # O # # #
K K # # # # #
```

### Step 7

Start: (4, 0), End: (6, 0), Sacrifice: (1, 6)

```
L O # # # # K
# L L O # K #
O L K O O L #
# K O L # # #
# O # # # # #
# K # O # # #
# K # # # # #
```

### Step 8

Start: (3, 1), End: (3, 3), Sacrifice: (2, 1)

```
L O # # # # K
# L L O # K #
O # K O O L #
# # # # # # #
# O # # # # #
# K # O # # #
# K # # # # #
```

### Step 9

Start: (1, 1), End: (5, 1), Sacrifice: (2, 0)

```
L O # # # # K
# # L O # K #
# # K O O L #
# # # # # # #
# # # # # # #
# # # O # # #
# K # # # # #
```

### Step 10

Start: (1, 2), End: (1, 5), Sacrifice: (2, 3)

```
L O # # # # K
# # # # # # #
# # K # O L #
# # # # # # #
# # # # # # #
# # # O # # #
# K # # # # #
```

### Step 11

Start: (0, 0), End: (0, 6), Sacrifice: (6, 1)

```
# # # # # # #
# # # # # # #
# # K # O L #
# # # # # # #
# # # # # # #
# # # O # # #
# # # # # # #
```

### Step 12

Start: (2, 2), End: (2, 5), Sacrifice: (5, 3)

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
K L O K K L
O K J O L O
L O K K O L
K L K O O L
O O K L K O
L L K O L K
```

## Solution

```
K L O K K L
O K J O L O
L O K K O L
K L K O O L
O O K L K O
L L K O L K
```

### Step 1

Start: (5, 2), End: (5, 4), Sacrifice: (2, 1)

```
K L O K K L
O K J O L O
L # K K O L
K L K O O L
O O K L K O
L L # # # K
```

### Step 2

Start: (0, 1), End: (0, 3), Sacrifice: (1, 3)

```
K # # # K L
O K J # L O
L # K K O L
K L K O O L
O O K L K O
L L # # # K
```

### Step 3

Start: (2, 3), End: (4, 3), Sacrifice: (3, 1)

```
K # # # K L
O K J # L O
L # K # O L
K # K # O L
O O K # K O
L L # # # K
```

### Step 4

Start: (3, 0), End: (5, 0), Sacrifice: (0, 5)

```
K # # # K #
O K J # L O
L # K # O L
# # K # O L
# O K # K O
# L # # # K
```

### Step 5

Start: (2, 2), End: (2, 5), Sacrifice: (1, 5)

```
K # # # K #
O K J # L #
L # # # # #
# # K # O L
# O K # K O
# L # # # K
```

### Step 6

Start: (1, 1), End: (5, 1), Sacrifice: (0, 4)

```
K # # # # #
O # J # L #
L # # # # #
# # K # O L
# # K # K O
# # # # # K
```

### Step 7

Start: (1, 4), End: (4, 4), Sacrifice: (4, 2)

```
K # # # # #
O # J # # #
L # # # # #
# # K # # L
# # # # # O
# # # # # K
```

### Step 8

Start: (0, 0), End: (2, 0), Sacrifice: (3, 2)

```
# # # # # #
# # J # # #
# # # # # #
# # # # # L
# # # # # O
# # # # # K
```

### Step 9

Start: (3, 5), End: (5, 5), Sacrifice: (1, 2)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

