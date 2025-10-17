# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
L O L O K K
L K O L K L
O K O O K K
K O L K K K
L L O J O K
K L L O L K
```

## Solution

```
L O L O K K
L K O L K L
O K O O K K
K O L K K K
L L O J O K
K L L O L K
```

### Step 1

Start: (0, 2), End: (0, 4), Sacrifice: (3, 2)

```
L O # # # K
L K O L K L
O K O O K K
K O # K K K
L L O J O K
K L L O L K
```

### Step 2

Start: (3, 4), End: (5, 4), Sacrifice: (2, 4)

```
L O # # # K
L K O L K L
O K O O # K
K O # K # K
L L O J # K
K L L O # K
```

### Step 3

Start: (5, 2), End: (5, 5), Sacrifice: (1, 4)

```
L O # # # K
L K O L # L
O K O O # K
K O # K # K
L L O J # K
K L # # # #
```

### Step 4

Start: (1, 3), End: (3, 3), Sacrifice: (5, 1)

```
L O # # # K
L K O # # L
O K O # # K
K O # # # K
L L O J # K
K # # # # #
```

### Step 5

Start: (2, 1), End: (4, 1), Sacrifice: (3, 5)

```
L O # # # K
L K O # # L
O # O # # K
K # # # # #
L # O J # K
K # # # # #
```

### Step 6

Start: (1, 0), End: (3, 0), Sacrifice: (4, 3)

```
L O # # # K
# K O # # L
# # O # # K
# # # # # #
L # O # # K
K # # # # #
```

### Step 7

Start: (1, 1), End: (1, 5), Sacrifice: (2, 5)

```
L O # # # K
# # # # # #
# # O # # #
# # # # # #
L # O # # K
K # # # # #
```

### Step 8

Start: (4, 0), End: (4, 5), Sacrifice: (2, 2)

```
L O # # # K
# # # # # #
# # # # # #
# # # # # #
# # # # # #
K # # # # #
```

### Step 9

Start: (0, 0), End: (0, 5), Sacrifice: (5, 0)

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
L O O K K
K L O O K
J L O L K
# L L O K
L K L O K
```

## Solution

```
L O O K K
K L O O K
J L O L K
# L L O K
L K L O K
```

### Step 1

Start: (0, 3), End: (2, 3), Sacrifice: (0, 1)

```
L # O # K
K L O # K
J L O # K
# L L O K
L K L O K
```

### Step 2

Start: (3, 2), End: (3, 4), Sacrifice: (4, 1)

```
L # O # K
K L O # K
J L O # K
# L # # #
L # L O K
```

### Step 3

Start: (1, 1), End: (1, 4), Sacrifice: (2, 0)

```
L # O # K
K # # # #
# L O # K
# L # # #
L # L O K
```

### Step 4

Start: (0, 0), End: (0, 4), Sacrifice: (4, 0)

```
# # # # #
K # # # #
# L O # K
# L # # #
# # L O K
```

### Step 5

Start: (2, 1), End: (2, 4), Sacrifice: (3, 1)

```
# # # # #
K # # # #
# # # # #
# # # # #
# # L O K
```

### Step 6

Start: (4, 2), End: (4, 4), Sacrifice: (1, 0)

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
L O K K L L
K K O L O O
K L K O K K
O O O J J O
O L O K O L
L L L O K K
```

## Solution

```
L O K K L L
K K O L O O
K L K O K K
O O O J J O
O L O K O L
L L L O K K
```

### Step 1

Start: (2, 5), End: (4, 5), Sacrifice: (4, 0)

```
L O K K L L
K K O L O O
K L K O K #
O O O J J #
# L O K O #
L L L O K K
```

### Step 2

Start: (4, 1), End: (4, 3), Sacrifice: (2, 1)

```
L O K K L L
K K O L O O
K # K O K #
O O O J J #
# # # # O #
L L L O K K
```

### Step 3

Start: (5, 2), End: (5, 4), Sacrifice: (0, 3)

```
L O K # L L
K K O L O O
K # K O K #
O O O J J #
# # # # O #
L L # # # K
```

### Step 4

Start: (2, 0), End: (5, 0), Sacrifice: (3, 4)

```
L O K # L L
K K O L O O
# # K O K #
# O O J # #
# # # # O #
# L # # # K
```

### Step 5

Start: (0, 0), End: (0, 2), Sacrifice: (4, 4)

```
# # # # L L
K K O L O O
# # K O K #
# O O J # #
# # # # # #
# L # # # K
```

### Step 6

Start: (0, 5), End: (5, 5), Sacrifice: (2, 3)

```
# # # # L #
K K O L O #
# # K # K #
# O O J # #
# # # # # #
# L # # # #
```

### Step 7

Start: (1, 1), End: (5, 1), Sacrifice: (2, 2)

```
# # # # L #
K # O L O #
# # # # K #
# # O J # #
# # # # # #
# # # # # #
```

### Step 8

Start: (0, 4), End: (2, 4), Sacrifice: (3, 3)

```
# # # # # #
K # O L # #
# # # # # #
# # O # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (1, 0), End: (1, 3), Sacrifice: (3, 2)

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
L # L K K J K
K L O O O O L
L O K K L K L
L O K L O K L
L O K K O L K
K O O O O L O
L O L L K O L
```

## Solution

```
L # L K K J K
K L O O O O L
L O K K L K L
L O K L O K L
L O K K O L K
K O O O O L O
L O L L K O L
```

### Step 1

Start: (4, 2), End: (6, 2), Sacrifice: (0, 0)

```
# # L K K J K
K L O O O O L
L O K K L K L
L O K L O K L
L O # K O L K
K O # O O L O
L O # L K O L
```

### Step 2

Start: (3, 3), End: (3, 5), Sacrifice: (1, 1)

```
# # L K K J K
K # O O O O L
L O K K L K L
L O K # # # L
L O # K O L K
K O # O O L O
L O # L K O L
```

### Step 3

Start: (4, 3), End: (4, 5), Sacrifice: (0, 6)

```
# # L K K J #
K # O O O O L
L O K K L K L
L O K # # # L
L O # # # # K
K O # O O L O
L O # L K O L
```

### Step 4

Start: (2, 3), End: (6, 3), Sacrifice: (5, 1)

```
# # L K K J #
K # O O O O L
L O K # L K L
L O K # # # L
L O # # # # K
K # # # O L O
L O # # K O L
```

### Step 5

Start: (5, 0), End: (5, 5), Sacrifice: (3, 6)

```
# # L K K J #
K # O O O O L
L O K # L K L
L O K # # # #
L O # # # # K
# # # # # # O
L O # # K O L
```

### Step 6

Start: (0, 4), End: (2, 4), Sacrifice: (2, 6)

```
# # L K # J #
K # O O # O L
L O K # # K #
L O K # # # #
L O # # # # K
# # # # # # O
L O # # K O L
```

### Step 7

Start: (6, 0), End: (6, 4), Sacrifice: (4, 1)

```
# # L K # J #
K # O O # O L
L O K # # K #
L O K # # # #
L # # # # # K
# # # # # # O
# # # # # O L
```

### Step 8

Start: (0, 2), End: (2, 2), Sacrifice: (6, 5)

```
# # # K # J #
K # # O # O L
L O # # # K #
L O K # # # #
L # # # # # K
# # # # # # O
# # # # # # L
```

### Step 9

Start: (2, 0), End: (2, 5), Sacrifice: (0, 3)

```
# # # # # J #
K # # O # O L
# # # # # # #
L O K # # # #
L # # # # # K
# # # # # # O
# # # # # # L
```

### Step 10

Start: (4, 6), End: (6, 6), Sacrifice: (1, 5)

```
# # # # # J #
K # # O # # L
# # # # # # #
L O K # # # #
L # # # # # #
# # # # # # #
# # # # # # #
```

### Step 11

Start: (3, 0), End: (3, 2), Sacrifice: (4, 0)

```
# # # # # J #
K # # O # # L
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

### Step 12

Start: (1, 0), End: (1, 6), Sacrifice: (0, 5)

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
K O L L K O
K O J J O L
L O K O K K
L O O K K J
K O L L O L
J L O K L K
```

## Solution

```
K O L L K O
K O J J O L
L O K O K K
L O O K K J
K O L L O L
J L O K L K
```

### Step 1

Start: (2, 2), End: (4, 2), Sacrifice: (1, 2)

```
K O L L K O
K O # J O L
L O # O K K
L O # K K J
K O # L O L
J L O K L K
```

### Step 2

Start: (0, 0), End: (0, 2), Sacrifice: (1, 3)

```
# # # L K O
K O # # O L
L O # O K K
L O # K K J
K O # L O L
J L O K L K
```

### Step 3

Start: (4, 0), End: (4, 3), Sacrifice: (1, 4)

```
# # # L K O
K O # # # L
L O # O K K
L O # K K J
# # # # O L
J L O K L K
```

### Step 4

Start: (5, 1), End: (5, 3), Sacrifice: (5, 0)

```
# # # L K O
K O # # # L
L O # O K K
L O # K K J
# # # # O L
# # # # L K
```

### Step 5

Start: (1, 0), End: (1, 5), Sacrifice: (3, 5)

```
# # # L K O
# # # # # #
L O # O K K
L O # K K #
# # # # O L
# # # # L K
```

### Step 6

Start: (0, 3), End: (3, 3), Sacrifice: (2, 4)

```
# # # # K O
# # # # # #
L O # # # K
L O # # K #
# # # # O L
# # # # L K
```

### Step 7

Start: (2, 0), End: (2, 5), Sacrifice: (5, 5)

```
# # # # K O
# # # # # #
# # # # # #
L O # # K #
# # # # O L
# # # # L #
```

### Step 8

Start: (3, 0), End: (3, 4), Sacrifice: (0, 5)

```
# # # # K #
# # # # # #
# # # # # #
# # # # # #
# # # # O L
# # # # L #
```

### Step 9

Start: (0, 4), End: (5, 4), Sacrifice: (4, 5)

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
L K L L L K
K O K L O O
K L O O J L
L O L K L K
K O O K O L
L O K K K K
```

## Solution

```
L K L L L K
K O K L O O
K L O O J L
L O L K L K
K O O K O L
L O K K K K
```

### Step 1

Start: (1, 3), End: (3, 3), Sacrifice: (1, 4)

```
L K L L L K
K O K # # O
K L O # J L
L O L # L K
K O O K O L
L O K K K K
```

### Step 2

Start: (1, 2), End: (3, 2), Sacrifice: (2, 4)

```
L K L L L K
K O # # # O
K L # # # L
L O # # L K
K O O K O L
L O K K K K
```

### Step 3

Start: (0, 2), End: (5, 2), Sacrifice: (0, 0)

```
# K # L L K
K O # # # O
K L # # # L
L O # # L K
K O # K O L
L O # K K K
```

### Step 4

Start: (3, 4), End: (5, 4), Sacrifice: (4, 3)

```
# K # L L K
K O # # # O
K L # # # L
L O # # # K
K O # # # L
L O # K # K
```

### Step 5

Start: (0, 1), End: (2, 1), Sacrifice: (5, 5)

```
# # # L L K
K # # # # O
K # # # # L
L O # # # K
K O # # # L
L O # K # #
```

### Step 6

Start: (5, 0), End: (5, 3), Sacrifice: (2, 0)

```
# # # L L K
K # # # # O
# # # # # L
L O # # # K
K O # # # L
# # # # # #
```

### Step 7

Start: (4, 0), End: (4, 5), Sacrifice: (0, 3)

```
# # # # L K
K # # # # O
# # # # # L
L O # # # K
# # # # # #
# # # # # #
```

### Step 8

Start: (0, 5), End: (2, 5), Sacrifice: (1, 0)

```
# # # # L #
# # # # # #
# # # # # #
L O # # # K
# # # # # #
# # # # # #
```

### Step 9

Start: (3, 0), End: (3, 5), Sacrifice: (0, 4)

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
J J O K #
K K K O L
O O K O L
L L K O L
K O L L L
```

## Solution

```
J J O K #
K K K O L
O O K O L
L L K O L
K O L L L
```

### Step 1

Start: (1, 1), End: (3, 1), Sacrifice: (0, 1)

```
J # O K #
K # K O L
O # K O L
L # K O L
K O L L L
```

### Step 2

Start: (1, 2), End: (1, 4), Sacrifice: (0, 3)

```
J # O # #
K # # # #
O # K O L
L # K O L
K O L L L
```

### Step 3

Start: (1, 0), End: (3, 0), Sacrifice: (0, 0)

```
# # O # #
# # # # #
# # K O L
# # K O L
K O L L L
```

### Step 4

Start: (3, 2), End: (3, 4), Sacrifice: (4, 2)

```
# # O # #
# # # # #
# # K O L
# # # # #
K O # L L
```

### Step 5

Start: (4, 0), End: (4, 3), Sacrifice: (4, 4)

```
# # O # #
# # # # #
# # K O L
# # # # #
# # # # #
```

### Step 6

Start: (2, 2), End: (2, 4), Sacrifice: (0, 2)

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
K L O O K L
L O K O J L
O K L K O L
L L K O L L
L O L O O K
K K L O K K
```

## Solution

```
K L O O K L
L O K O J L
O K L K O L
L L K O L L
L O L O O K
K K L O K K
```

### Step 1

Start: (2, 3), End: (2, 5), Sacrifice: (1, 0)

```
K L O O K L
# O K O J L
O K L # # #
L L K O L L
L O L O O K
K K L O K K
```

### Step 2

Start: (0, 0), End: (3, 0), Sacrifice: (1, 1)

```
# L O O K L
# # K O J L
# K L # # #
# L K O L L
L O L O O K
K K L O K K
```

### Step 3

Start: (3, 4), End: (5, 4), Sacrifice: (0, 2)

```
# L # O K L
# # K O J L
# K L # # #
# L K O # L
L O L O # K
K K L O # K
```

### Step 4

Start: (5, 2), End: (5, 5), Sacrifice: (5, 0)

```
# L # O K L
# # K O J L
# K L # # #
# L K O # L
L O L O # K
# K # # # #
```

### Step 5

Start: (3, 2), End: (3, 5), Sacrifice: (4, 0)

```
# L # O K L
# # K O J L
# K L # # #
# L # # # #
# O L O # K
# K # # # #
```

### Step 6

Start: (4, 2), End: (4, 5), Sacrifice: (1, 4)

```
# L # O K L
# # K O # L
# K L # # #
# L # # # #
# O # # # #
# K # # # #
```

### Step 7

Start: (0, 1), End: (0, 4), Sacrifice: (2, 2)

```
# # # # # L
# # K O # L
# K # # # #
# L # # # #
# O # # # #
# K # # # #
```

### Step 8

Start: (3, 1), End: (5, 1), Sacrifice: (2, 1)

```
# # # # # L
# # K O # L
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (1, 2), End: (1, 5), Sacrifice: (0, 5)

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
K L L O K K
L O L L O K
L K O L O L
O L O O K O
K K K K J O
J L K O K L
```

## Solution

```
K L L O K K
L O L L O K
L K O L O L
O L O O K O
K K K K J O
J L K O K L
```

### Step 1

Start: (2, 1), End: (2, 3), Sacrifice: (4, 3)

```
K L L O K K
L O L L O K
L # # # O L
O L O O K O
K K K # J O
J L K O K L
```

### Step 2

Start: (1, 3), End: (1, 5), Sacrifice: (2, 0)

```
K L L O K K
L O L # # #
# # # # O L
O L O O K O
K K K # J O
J L K O K L
```

### Step 3

Start: (1, 0), End: (4, 0), Sacrifice: (0, 0)

```
# L L O K K
# O L # # #
# # # # O L
# L O O K O
# K K # J O
J L K O K L
```

### Step 4

Start: (1, 2), End: (4, 2), Sacrifice: (5, 2)

```
# L L O K K
# O # # # #
# # # # O L
# L # O K O
# K # # J O
J L # O K L
```

### Step 5

Start: (5, 1), End: (5, 4), Sacrifice: (2, 5)

```
# L L O K K
# O # # # #
# # # # O #
# L # O K O
# K # # J O
J # # # # L
```

### Step 6

Start: (3, 1), End: (3, 4), Sacrifice: (5, 0)

```
# L L O K K
# O # # # #
# # # # O #
# # # # # O
# K # # J O
# # # # # L
```

### Step 7

Start: (0, 2), End: (0, 4), Sacrifice: (3, 5)

```
# L # # # K
# O # # # #
# # # # O #
# # # # # #
# K # # J O
# # # # # L
```

### Step 8

Start: (0, 5), End: (5, 5), Sacrifice: (2, 4)

```
# L # # # #
# O # # # #
# # # # # #
# # # # # #
# K # # J #
# # # # # #
```

### Step 9

Start: (0, 1), End: (4, 1), Sacrifice: (4, 4)

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
K K O L K O L
J K O K K O L
K O L O K O L
O K O L K L L
O L J L O O K
L O K L L K O
# L L J O K L
```

## Solution

```
K K O L K O L
J K O K K O L
K O L O K O L
O K O L K L L
O L J L O O K
L O K L L K O
# L L J O K L
```

### Step 1

Start: (1, 4), End: (1, 6), Sacrifice: (1, 2)

```
K K O L K O L
J K # K # # #
K O L O K O L
O K O L K L L
O L J L O O K
L O K L L K O
# L L J O K L
```

### Step 2

Start: (4, 6), End: (6, 6), Sacrifice: (1, 1)

```
K K O L K O L
J # # K # # #
K O L O K O L
O K O L K L L
O L J L O O #
L O K L L K #
# L L J O K #
```

### Step 3

Start: (3, 1), End: (3, 3), Sacrifice: (2, 0)

```
K K O L K O L
J # # K # # #
# O L O K O L
O # # # K L L
O L J L O O #
L O K L L K #
# L L J O K #
```

### Step 4

Start: (0, 4), End: (0, 6), Sacrifice: (2, 2)

```
K K O L # # #
J # # K # # #
# O # O K O L
O # # # K L L
O L J L O O #
L O K L L K #
# L L J O K #
```

### Step 5

Start: (3, 4), End: (5, 4), Sacrifice: (5, 3)

```
K K O L # # #
J # # K # # #
# O # O K O L
O # # # # L L
O L J L # O #
L O K # # K #
# L L J O K #
```

### Step 6

Start: (0, 1), End: (4, 1), Sacrifice: (3, 0)

```
K # O L # # #
J # # K # # #
# # # O K O L
# # # # # L L
O # J L # O #
L O K # # K #
# L L J O K #
```

### Step 7

Start: (5, 0), End: (5, 2), Sacrifice: (3, 6)

```
K # O L # # #
J # # K # # #
# # # O K O L
# # # # # L #
O # J L # O #
# # # # # K #
# L L J O K #
```

### Step 8

Start: (1, 3), End: (4, 3), Sacrifice: (6, 3)

```
K # O L # # #
J # # # # # #
# # # # K O L
# # # # # L #
O # J # # O #
# # # # # K #
# L L # O K #
```

### Step 9

Start: (0, 0), End: (0, 3), Sacrifice: (1, 0)

```
# # # # # # #
# # # # # # #
# # # # K O L
# # # # # L #
O # J # # O #
# # # # # K #
# L L # O K #
```

### Step 10

Start: (6, 2), End: (6, 5), Sacrifice: (4, 0)

```
# # # # # # #
# # # # # # #
# # # # K O L
# # # # # L #
# # J # # O #
# # # # # K #
# L # # # # #
```

### Step 11

Start: (3, 5), End: (5, 5), Sacrifice: (4, 2)

```
# # # # # # #
# # # # # # #
# # # # K O L
# # # # # # #
# # # # # # #
# # # # # # #
# L # # # # #
```

### Step 12

Start: (2, 4), End: (2, 6), Sacrifice: (6, 1)

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

