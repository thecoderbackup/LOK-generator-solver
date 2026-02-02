# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
K O L L L J
O L K O K L
O O K K O L
L K O O O O
L O L L K K
O L L K O K
```

## Solution

```
K O L L L J
O L K O K L
O O K K O L
L K O O O O
L O L L K K
O L L K O K
```

### Step 1

Start: (0, 0), End: (0, 2), Sacrifice: (4, 3)

```
# # # L L J
O L K O K L
O O K K O L
L K O O O O
L O L # K K
O L L K O K
```

### Step 2

Start: (2, 3), End: (2, 5), Sacrifice: (1, 4)

```
# # # L L J
O L K O # L
O O K # # #
L K O O O O
L O L # K K
O L L K O K
```

### Step 3

Start: (1, 1), End: (3, 1), Sacrifice: (2, 0)

```
# # # L L J
O # K O # L
# # K # # #
L # O O O O
L O L # K K
O L L K O K
```

### Step 4

Start: (0, 4), End: (4, 4), Sacrifice: (3, 0)

```
# # # L # J
O # K O # L
# # K # # #
# # O O # O
L O L # # K
O L L K O K
```

### Step 5

Start: (1, 2), End: (1, 5), Sacrifice: (3, 5)

```
# # # L # J
O # # # # #
# # K # # #
# # O O # #
L O L # # K
O L L K O K
```

### Step 6

Start: (2, 2), End: (4, 2), Sacrifice: (5, 1)

```
# # # L # J
O # # # # #
# # # # # #
# # # O # #
L O # # # K
O # L K O K
```

### Step 7

Start: (0, 3), End: (5, 3), Sacrifice: (1, 0)

```
# # # # # J
# # # # # #
# # # # # #
# # # # # #
L O # # # K
O # L # O K
```

### Step 8

Start: (5, 2), End: (5, 5), Sacrifice: (0, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
L O # # # K
O # # # # #
```

### Step 9

Start: (4, 0), End: (4, 5), Sacrifice: (5, 0)

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
J K L O L K
K O L L K O
L L O K O L
K L L O O K
O O K O K L
L K L L L L
```

## Solution

```
J K L O L K
K O L L K O
L L O K O L
K L L O O K
O O K O K L
L K L L L L
```

### Step 1

Start: (3, 1), End: (5, 1), Sacrifice: (4, 4)

```
J K L O L K
K O L L K O
L L O K O L
K # L O O K
O # K O # L
L # L L L L
```

### Step 2

Start: (4, 2), End: (4, 5), Sacrifice: (3, 4)

```
J K L O L K
K O L L K O
L L O K O L
K # L O # K
O # # # # #
L # L L L L
```

### Step 3

Start: (1, 4), End: (5, 4), Sacrifice: (0, 2)

```
J K # O L K
K O L L # O
L L O K # L
K # L O # K
O # # # # #
L # L L # L
```

### Step 4

Start: (0, 1), End: (0, 4), Sacrifice: (5, 3)

```
J # # # # K
K O L L # O
L L O K # L
K # L O # K
O # # # # #
L # L # # L
```

### Step 5

Start: (1, 0), End: (1, 2), Sacrifice: (1, 3)

```
J # # # # K
# # # # # O
L L O K # L
K # L O # K
O # # # # #
L # L # # L
```

### Step 6

Start: (3, 0), End: (5, 0), Sacrifice: (2, 0)

```
J # # # # K
# # # # # O
# L O K # L
# # L O # K
# # # # # #
# # L # # L
```

### Step 7

Start: (0, 5), End: (2, 5), Sacrifice: (5, 2)

```
J # # # # #
# # # # # #
# L O K # #
# # L O # K
# # # # # #
# # # # # L
```

### Step 8

Start: (3, 2), End: (3, 5), Sacrifice: (0, 0)

```
# # # # # #
# # # # # #
# L O K # #
# # # # # #
# # # # # #
# # # # # L
```

### Step 9

Start: (2, 1), End: (2, 3), Sacrifice: (5, 5)

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
L L O K L
L O K # L
L K O L L
O L O K O
K J O O K
```

## Solution

```
L L O K L
L O K # L
L K O L L
O L O K O
K J O O K
```

### Step 1

Start: (3, 1), End: (3, 3), Sacrifice: (0, 0)

```
# L O K L
L O K # L
L K O L L
O # # # O
K J O O K
```

### Step 2

Start: (2, 4), End: (4, 4), Sacrifice: (4, 3)

```
# L O K L
L O K # L
L K O L #
O # # # #
K J O # #
```

### Step 3

Start: (2, 0), End: (4, 0), Sacrifice: (1, 4)

```
# L O K L
L O K # #
# K O L #
# # # # #
# J O # #
```

### Step 4

Start: (1, 0), End: (1, 2), Sacrifice: (4, 2)

```
# L O K L
# # # # #
# K O L #
# # # # #
# J # # #
```

### Step 5

Start: (2, 1), End: (2, 3), Sacrifice: (0, 4)

```
# L O K #
# # # # #
# # # # #
# # # # #
# J # # #
```

### Step 6

Start: (0, 1), End: (0, 3), Sacrifice: (4, 1)

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
K K O L L
K O K K O
L L O O L
O O L K K
K # K L K
```

## Solution

```
K K O L L
K O K K O
L L O O L
O O L K K
K # K L K
```

### Step 1

Start: (1, 2), End: (3, 2), Sacrifice: (4, 2)

```
K K O L L
K O # K O
L L # O L
O O # K K
K # # L K
```

### Step 2

Start: (0, 1), End: (2, 1), Sacrifice: (3, 3)

```
K # O L L
K # # K O
L # # O L
O O # # K
K # # L K
```

### Step 3

Start: (2, 0), End: (4, 0), Sacrifice: (3, 4)

```
K # O L L
K # # K O
# # # O L
# O # # #
# # # L K
```

### Step 4

Start: (0, 0), End: (0, 3), Sacrifice: (2, 4)

```
# # # # L
K # # K O
# # # O #
# O # # #
# # # L K
```

### Step 5

Start: (1, 3), End: (4, 3), Sacrifice: (3, 1)

```
# # # # L
K # # # O
# # # # #
# # # # #
# # # # K
```

### Step 6

Start: (0, 4), End: (4, 4), Sacrifice: (1, 0)

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
K L O L K K L
K J K O O O O
J K O O L O J
O O L K # L K
K O L K O L K
L O K O L K K
L L O K K O L
```

## Solution

```
K L O L K K L
K J K O O O O
J K O O L O J
O O L K # L K
K O L K O L K
L O K O L K K
L L O K K O L
```

### Step 1

Start: (1, 2), End: (3, 2), Sacrifice: (1, 4)

```
K L O L K K L
K J # O # O O
J K # O L O J
O O # K # L K
K O L K O L K
L O K O L K K
L L O K K O L
```

### Step 2

Start: (2, 1), End: (2, 4), Sacrifice: (2, 0)

```
K L O L K K L
K J # O # O O
# # # # # O J
O O # K # L K
K O L K O L K
L O K O L K K
L L O K K O L
```

### Step 3

Start: (0, 3), End: (3, 3), Sacrifice: (5, 6)

```
K L O # K K L
K J # # # O O
# # # # # O J
O O # # # L K
K O L K O L K
L O K O L K #
L L O K K O L
```

### Step 4

Start: (4, 3), End: (4, 5), Sacrifice: (5, 1)

```
K L O # K K L
K J # # # O O
# # # # # O J
O O # # # L K
K O L # # # K
L # K O L K #
L L O K K O L
```

### Step 5

Start: (6, 1), End: (6, 3), Sacrifice: (1, 0)

```
K L O # K K L
# J # # # O O
# # # # # O J
O O # # # L K
K O L # # # K
L # K O L K #
L # # # K O L
```

### Step 6

Start: (5, 2), End: (5, 4), Sacrifice: (2, 6)

```
K L O # K K L
# J # # # O O
# # # # # O #
O O # # # L K
K O L # # # K
L # # # # K #
L # # # K O L
```

### Step 7

Start: (4, 0), End: (4, 2), Sacrifice: (5, 5)

```
K L O # K K L
# J # # # O O
# # # # # O #
O O # # # L K
# # # # # # K
L # # # # # #
L # # # K O L
```

### Step 8

Start: (0, 1), End: (0, 4), Sacrifice: (1, 5)

```
K # # # # K L
# J # # # # O
# # # # # O #
O O # # # L K
# # # # # # K
L # # # # # #
L # # # K O L
```

### Step 9

Start: (0, 6), End: (3, 6), Sacrifice: (1, 1)

```
K # # # # K #
# # # # # # #
# # # # # O #
O O # # # L #
# # # # # # K
L # # # # # #
L # # # K O L
```

### Step 10

Start: (6, 4), End: (6, 6), Sacrifice: (6, 0)

```
K # # # # K #
# # # # # # #
# # # # # O #
O O # # # L #
# # # # # # K
L # # # # # #
# # # # # # #
```

### Step 11

Start: (0, 5), End: (3, 5), Sacrifice: (3, 1)

```
K # # # # # #
# # # # # # #
# # # # # # #
O # # # # # #
# # # # # # K
L # # # # # #
# # # # # # #
```

### Step 12

Start: (0, 0), End: (5, 0), Sacrifice: (4, 6)

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
O K K K # K K
L O O O K L L
L J L L O K O
O K O L J O L
L L O O K L L
K L L O K L O
K L L O L K K
```

## Solution

```
O K K K # K K
L O O O K L L
L J L L O K O
O K O L J O L
L L O O K L L
K L L O K L O
K L L O L K K
```

### Step 1

Start: (4, 6), End: (6, 6), Sacrifice: (0, 0)

```
# K K K # K K
L O O O K L L
L J L L O K O
O K O L J O L
L L O O K L #
K L L O K L #
K L L O L K #
```

### Step 2

Start: (0, 3), End: (2, 3), Sacrifice: (4, 1)

```
# K K # # K K
L O O # K L L
L J L # O K O
O K O L J O L
L # O O K L #
K L L O K L #
K L L O L K #
```

### Step 3

Start: (2, 2), End: (2, 5), Sacrifice: (4, 2)

```
# K K # # K K
L O O # K L L
L J # # # # O
O K O L J O L
L # # O K L #
K L L O K L #
K L L O L K #
```

### Step 4

Start: (4, 0), End: (4, 4), Sacrifice: (2, 1)

```
# K K # # K K
L O O # K L L
L # # # # # O
O K O L J O L
# # # # # L #
K L L O K L #
K L L O L K #
```

### Step 5

Start: (3, 1), End: (3, 3), Sacrifice: (5, 0)

```
# K K # # K K
L O O # K L L
L # # # # # O
O # # # J O L
# # # # # L #
# L L O K L #
K L L O L K #
```

### Step 6

Start: (0, 2), End: (5, 2), Sacrifice: (6, 2)

```
# K # # # K K
L O # # K L L
L # # # # # O
O # # # J O L
# # # # # L #
# L # O K L #
K L # O L K #
```

### Step 7

Start: (5, 1), End: (5, 4), Sacrifice: (1, 6)

```
# K # # # K K
L O # # K L #
L # # # # # O
O # # # J O L
# # # # # L #
# # # # # L #
K L # O L K #
```

### Step 8

Start: (1, 0), End: (1, 4), Sacrifice: (4, 5)

```
# K # # # K K
# # # # # L #
L # # # # # O
O # # # J O L
# # # # # # #
# # # # # L #
K L # O L K #
```

### Step 9

Start: (2, 0), End: (6, 0), Sacrifice: (1, 5)

```
# K # # # K K
# # # # # # #
# # # # # # O
# # # # J O L
# # # # # # #
# # # # # L #
# L # O L K #
```

### Step 10

Start: (0, 5), End: (5, 5), Sacrifice: (3, 4)

```
# K # # # # K
# # # # # # #
# # # # # # O
# # # # # # L
# # # # # # #
# # # # # # #
# L # O L K #
```

### Step 11

Start: (0, 6), End: (3, 6), Sacrifice: (6, 4)

```
# K # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# L # O # K #
```

### Step 12

Start: (6, 1), End: (6, 5), Sacrifice: (0, 1)

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
L O J L L
L O K O O
K O L J J
L O K K K
O # K O L
```

## Solution

```
L O J L L
L O K O O
K O L J J
L O K K K
O # K O L
```

### Step 1

Start: (2, 0), End: (2, 2), Sacrifice: (0, 0)

```
# O J L L
L O K O O
# # # J J
L O K K K
O # K O L
```

### Step 2

Start: (1, 0), End: (1, 2), Sacrifice: (4, 0)

```
# O J L L
# # # O O
# # # J J
L O K K K
# # K O L
```

### Step 3

Start: (4, 2), End: (4, 4), Sacrifice: (2, 4)

```
# O J L L
# # # O O
# # # J #
L O K K K
# # # # #
```

### Step 4

Start: (3, 0), End: (3, 2), Sacrifice: (0, 2)

```
# O # L L
# # # O O
# # # J #
# # # K K
# # # # #
```

### Step 5

Start: (0, 4), End: (3, 4), Sacrifice: (2, 3)

```
# O # L #
# # # O #
# # # # #
# # # K #
# # # # #
```

### Step 6

Start: (0, 3), End: (3, 3), Sacrifice: (0, 1)

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
O K L O K O L
L L O K J L L
O K O K L L J
K J O J L L K
O K L L O O O
L O O O K K L
L L K K O K #
```

## Solution

```
O K L O K O L
L L O K J L L
O K O K L L J
K J O J L L K
O K L L O O O
L O O O K K L
L L K K O K #
```

### Step 1

Start: (4, 2), End: (6, 2), Sacrifice: (3, 1)

```
O K L O K O L
L L O K J L L
O K O K L L J
K # O J L L K
O K # L O O O
L O # O K K L
L L # K O K #
```

### Step 2

Start: (4, 3), End: (6, 3), Sacrifice: (2, 3)

```
O K L O K O L
L L O K J L L
O K O # L L J
K # O J L L K
O K # # O O O
L O # # K K L
L L # # O K #
```

### Step 3

Start: (0, 2), End: (0, 4), Sacrifice: (2, 6)

```
O K # # # O L
L L O K J L L
O K O # L L #
K # O J L L K
O K # # O O O
L O # # K K L
L L # # O K #
```

### Step 4

Start: (3, 0), End: (5, 0), Sacrifice: (1, 6)

```
O K # # # O L
L L O K J L #
O K O # L L #
# # O J L L K
# K # # O O O
# O # # K K L
L L # # O K #
```

### Step 5

Start: (4, 1), End: (6, 1), Sacrifice: (2, 0)

```
O K # # # O L
L L O K J L #
# K O # L L #
# # O J L L K
# # # # O O O
# # # # K K L
L # # # O K #
```

### Step 6

Start: (3, 5), End: (5, 5), Sacrifice: (2, 4)

```
O K # # # O L
L L O K J L #
# K O # # L #
# # O J L # K
# # # # O # O
# # # # K # L
L # # # O K #
```

### Step 7

Start: (6, 0), End: (6, 5), Sacrifice: (1, 4)

```
O K # # # O L
L L O K # L #
# K O # # L #
# # O J L # K
# # # # O # O
# # # # K # L
# # # # # # #
```

### Step 8

Start: (1, 1), End: (1, 3), Sacrifice: (3, 2)

```
O K # # # O L
L # # # # L #
# K O # # L #
# # # J L # K
# # # # O # O
# # # # K # L
# # # # # # #
```

### Step 9

Start: (3, 6), End: (5, 6), Sacrifice: (1, 0)

```
O K # # # O L
# # # # # L #
# K O # # L #
# # # J L # #
# # # # O # #
# # # # K # #
# # # # # # #
```

### Step 10

Start: (2, 1), End: (2, 5), Sacrifice: (0, 0)

```
# K # # # O L
# # # # # L #
# # # # # # #
# # # J L # #
# # # # O # #
# # # # K # #
# # # # # # #
```

### Step 11

Start: (3, 4), End: (5, 4), Sacrifice: (3, 3)

```
# K # # # O L
# # # # # L #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

### Step 12

Start: (0, 1), End: (0, 6), Sacrifice: (1, 5)

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
O L L K O L K
L J O J K O O
O K L K L O K
K O O O # K L
L L K O K O K
O K O L J L K
K L K K O O L
```

## Solution

```
O L L K O L K
L J O J K O O
O K L K L O K
K O O O # K L
L L K O K O K
O K O L J L K
K L K K O O L
```

### Step 1

Start: (0, 3), End: (0, 5), Sacrifice: (4, 6)

```
O L L # # # K
L J O J K O O
O K L K L O K
K O O O # K L
L L K O K O #
O K O L J L K
K L K K O O L
```

### Step 2

Start: (4, 0), End: (6, 0), Sacrifice: (1, 4)

```
O L L # # # K
L J O J # O O
O K L K L O K
K O O O # K L
# L K O K O #
# K O L J L K
# L K K O O L
```

### Step 3

Start: (2, 4), End: (2, 6), Sacrifice: (2, 1)

```
O L L # # # K
L J O J # O O
O # L K # # #
K O O O # K L
# L K O K O #
# K O L J L K
# L K K O O L
```

### Step 4

Start: (2, 2), End: (4, 2), Sacrifice: (1, 2)

```
O L L # # # K
L J # J # O O
O # # K # # #
K O # O # K L
# L # O K O #
# K O L J L K
# L K K O O L
```

### Step 5

Start: (1, 0), End: (3, 0), Sacrifice: (6, 4)

```
O L L # # # K
# J # J # O O
# # # K # # #
# O # O # K L
# L # O K O #
# K O L J L K
# L K K # O L
```

### Step 6

Start: (6, 3), End: (6, 6), Sacrifice: (1, 1)

```
O L L # # # K
# # # J # O O
# # # K # # #
# O # O # K L
# L # O K O #
# K O L J L K
# L K # # # #
```

### Step 7

Start: (4, 1), End: (4, 4), Sacrifice: (5, 6)

```
O L L # # # K
# # # J # O O
# # # K # # #
# O # O # K L
# # # # # O #
# K O L J L #
# L K # # # #
```

### Step 8

Start: (0, 6), End: (3, 6), Sacrifice: (6, 1)

```
O L L # # # #
# # # J # O #
# # # K # # #
# O # O # K #
# # # # # O #
# K O L J L #
# # K # # # #
```

### Step 9

Start: (0, 1), End: (5, 1), Sacrifice: (1, 5)

```
O # L # # # #
# # # J # # #
# # # K # # #
# # # O # K #
# # # # # O #
# # O L J L #
# # K # # # #
```

### Step 10

Start: (2, 3), End: (5, 3), Sacrifice: (5, 4)

```
O # L # # # #
# # # J # # #
# # # # # # #
# # # # # K #
# # # # # O #
# # O # # L #
# # K # # # #
```

### Step 11

Start: (0, 2), End: (6, 2), Sacrifice: (1, 3)

```
O # # # # # #
# # # # # # #
# # # # # # #
# # # # # K #
# # # # # O #
# # # # # L #
# # # # # # #
```

### Step 12

Start: (3, 5), End: (5, 5), Sacrifice: (0, 0)

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
L L L O K K
O O O K L O
K J K L O K
O L O K O K
L O K K K L
K L J L O K
```

## Solution

```
L L L O K K
O O O K L O
K J K L O K
O L O K O K
L O K K K L
K L J L O K
```

### Step 1

Start: (4, 0), End: (4, 2), Sacrifice: (1, 1)

```
L L L O K K
O # O K L O
K J K L O K
O L O K O K
# # # K K L
K L J L O K
```

### Step 2

Start: (2, 3), End: (2, 5), Sacrifice: (3, 3)

```
L L L O K K
O # O K L O
K J K # # #
O L O # O K
# # # K K L
K L J L O K
```

### Step 3

Start: (1, 4), End: (4, 4), Sacrifice: (5, 1)

```
L L L O K K
O # O K # O
K J K # # #
O L O # # K
# # # K # L
K # J L O K
```

### Step 4

Start: (3, 1), End: (3, 5), Sacrifice: (5, 2)

```
L L L O K K
O # O K # O
K J K # # #
O # # # # #
# # # K # L
K # # L O K
```

### Step 5

Start: (5, 3), End: (5, 5), Sacrifice: (4, 3)

```
L L L O K K
O # O K # O
K J K # # #
O # # # # #
# # # # # L
K # # # # #
```

### Step 6

Start: (0, 2), End: (2, 2), Sacrifice: (1, 3)

```
L L # O K K
O # # # # O
K J # # # #
O # # # # #
# # # # # L
K # # # # #
```

### Step 7

Start: (0, 0), End: (2, 0), Sacrifice: (3, 0)

```
# L # O K K
# # # # # O
# J # # # #
# # # # # #
# # # # # L
K # # # # #
```

### Step 8

Start: (0, 1), End: (0, 4), Sacrifice: (2, 1)

```
# # # # # K
# # # # # O
# # # # # #
# # # # # #
# # # # # L
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

