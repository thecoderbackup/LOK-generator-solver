# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
L L K J K O K
O K O L J J #
K L L O O K K
L O K L L O K
L K L J K K O
K O O O J O L
L L K K K L L
```

## Solution

```
L L K J K O K
O K O L J J #
K L L O O K K
L O K L L O K
L K L J K K O
K O O O J O L
L L K K K L L
```

### Step 1

Start: (0, 2), End: (2, 2), Sacrifice: (0, 3)

```
L L # # K O K
O K # L J J #
K L # O O K K
L O K L L O K
L K L J K K O
K O O O J O L
L L K K K L L
```

### Step 2

Start: (4, 1), End: (6, 1), Sacrifice: (1, 4)

```
L L # # K O K
O K # L # J #
K L # O O K K
L O K L L O K
L # L J K K O
K # O O J O L
L # K K K L L
```

### Step 3

Start: (0, 4), End: (3, 4), Sacrifice: (6, 6)

```
L L # # # O K
O K # L # J #
K L # O # K K
L O K L # O K
L # L J K K O
K # O O J O L
L # K K K L #
```

### Step 4

Start: (0, 0), End: (2, 0), Sacrifice: (1, 5)

```
# L # # # O K
# K # L # # #
# L # O # K K
L O K L # O K
L # L J K K O
K # O O J O L
L # K K K L #
```

### Step 5

Start: (2, 1), End: (2, 5), Sacrifice: (4, 3)

```
# L # # # O K
# K # L # # #
# # # # # # K
L O K L # O K
L # L # K K O
K # O O J O L
L # K K K L #
```

### Step 6

Start: (3, 3), End: (3, 6), Sacrifice: (6, 0)

```
# L # # # O K
# K # L # # #
# # # # # # K
L O K # # # #
L # L # K K O
K # O O J O L
# # K K K L #
```

### Step 7

Start: (1, 3), End: (6, 3), Sacrifice: (4, 0)

```
# L # # # O K
# K # # # # #
# # # # # # K
L O K # # # #
# # L # K K O
K # O # J O L
# # K # K L #
```

### Step 8

Start: (0, 1), End: (0, 6), Sacrifice: (5, 4)

```
# # # # # # #
# K # # # # #
# # # # # # K
L O K # # # #
# # L # K K O
K # O # # O L
# # K # K L #
```

### Step 9

Start: (4, 2), End: (6, 2), Sacrifice: (1, 1)

```
# # # # # # #
# # # # # # #
# # # # # # K
L O K # # # #
# # # # K K O
K # # # # O L
# # # # K L #
```

### Step 10

Start: (3, 0), End: (3, 2), Sacrifice: (5, 0)

```
# # # # # # #
# # # # # # #
# # # # # # K
# # # # # # #
# # # # K K O
# # # # # O L
# # # # K L #
```

### Step 11

Start: (2, 6), End: (5, 6), Sacrifice: (4, 4)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # K #
# # # # # O #
# # # # K L #
```

### Step 12

Start: (4, 5), End: (6, 5), Sacrifice: (6, 4)

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

# Puzzle 2

## Generated Puzzle

```
O K K O L
L O K O L
O K K O J
K O K O L
# L K O L
```

## Solution

```
O K K O L
L O K O L
O K K O J
K O K O L
# L K O L
```

### Step 1

Start: (1, 0), End: (3, 0), Sacrifice: (2, 3)

```
O K K O L
# O K O L
# K K # J
# O K O L
# L K O L
```

### Step 2

Start: (2, 1), End: (4, 1), Sacrifice: (2, 2)

```
O K K O L
# O K O L
# # # # J
# # K O L
# # K O L
```

### Step 3

Start: (4, 2), End: (4, 4), Sacrifice: (1, 1)

```
O K K O L
# # K O L
# # # # J
# # K O L
# # # # #
```

### Step 4

Start: (3, 2), End: (3, 4), Sacrifice: (0, 2)

```
O K # O L
# # K O L
# # # # J
# # # # #
# # # # #
```

### Step 5

Start: (0, 1), End: (0, 4), Sacrifice: (0, 0)

```
# # # # #
# # K O L
# # # # J
# # # # #
# # # # #
```

### Step 6

Start: (1, 2), End: (1, 4), Sacrifice: (2, 4)

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
K L O L O K
L K O O K L
O K J K O J
K O L L O K
K O O J L L
L L L O K J
```

## Solution

```
K L O L O K
L K O O K L
O K J K O J
K O L L O K
K O O J L L
L L L O K J
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (0, 2)

```
K L # L O K
L K O O K L
O K J K O J
# # # L O K
K O O J L L
L L L O K J
```

### Step 2

Start: (3, 3), End: (3, 5), Sacrifice: (4, 2)

```
K L # L O K
L K O O K L
O K J K O J
# # # # # #
K O # J L L
L L L O K J
```

### Step 3

Start: (1, 0), End: (4, 0), Sacrifice: (4, 5)

```
K L # L O K
# K O O K L
# K J K O J
# # # # # #
# O # J L #
L L L O K J
```

### Step 4

Start: (0, 3), End: (2, 3), Sacrifice: (5, 5)

```
K L # # O K
# K O # K L
# K J # O J
# # # # # #
# O # J L #
L L L O K #
```

### Step 5

Start: (2, 1), End: (5, 1), Sacrifice: (2, 5)

```
K L # # O K
# K O # K L
# # J # O #
# # # # # #
# # # J L #
L # L O K #
```

### Step 6

Start: (5, 2), End: (5, 4), Sacrifice: (0, 0)

```
# L # # O K
# K O # K L
# # J # O #
# # # # # #
# # # J L #
L # # # # #
```

### Step 7

Start: (1, 4), End: (4, 4), Sacrifice: (2, 2)

```
# L # # O K
# K O # # L
# # # # # #
# # # # # #
# # # J # #
L # # # # #
```

### Step 8

Start: (1, 1), End: (1, 5), Sacrifice: (4, 3)

```
# L # # O K
# # # # # #
# # # # # #
# # # # # #
# # # # # #
L # # # # #
```

### Step 9

Start: (0, 1), End: (0, 5), Sacrifice: (5, 0)

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
J K L O L
K L O K L
L O K K O
O K L O K
K # L K K
```

## Solution

```
J K L O L
K L O K L
L O K K O
O K L O K
K # L K K
```

### Step 1

Start: (3, 2), End: (3, 4), Sacrifice: (1, 3)

```
J K L O L
K L O # L
L O K K O
O K # # #
K # L K K
```

### Step 2

Start: (0, 2), End: (2, 2), Sacrifice: (1, 0)

```
J K # O L
# L # # L
L O # K O
O K # # #
K # L K K
```

### Step 3

Start: (2, 0), End: (4, 0), Sacrifice: (2, 3)

```
J K # O L
# L # # L
# O # # O
# K # # #
# # L K K
```

### Step 4

Start: (1, 4), End: (4, 4), Sacrifice: (0, 0)

```
# K # O L
# L # # #
# O # # #
# K # # #
# # L K #
```

### Step 5

Start: (0, 1), End: (0, 4), Sacrifice: (4, 2)

```
# # # # #
# L # # #
# O # # #
# K # # #
# # # K #
```

### Step 6

Start: (1, 1), End: (3, 1), Sacrifice: (4, 3)

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
O L L O K J K
K J L L O K O
O O O L O K K
L K K L O K O
L O L L K O K
O J O O L L O
# K K K O L L
```

## Solution

```
O L L O K J K
K J L L O K O
O O O L O K K
L K K L O K O
L O L L K O K
O J O O L L O
# K K K O L L
```

### Step 1

Start: (4, 3), End: (6, 3), Sacrifice: (1, 1)

```
O L L O K J K
K # L L O K O
O O O L O K K
L K K L O K O
L O L # K O K
O J O # L L O
# K K # O L L
```

### Step 2

Start: (2, 3), End: (2, 5), Sacrifice: (5, 6)

```
O L L O K J K
K # L L O K O
O O O # # # K
L K K L O K O
L O L # K O K
O J O # L L #
# K K # O L L
```

### Step 3

Start: (1, 0), End: (3, 0), Sacrifice: (2, 6)

```
O L L O K J K
# # L L O K O
# O O # # # #
# K K L O K O
L O L # K O K
O J O # L L #
# K K # O L L
```

### Step 4

Start: (4, 2), End: (6, 2), Sacrifice: (1, 6)

```
O L L O K J K
# # L L O K #
# O O # # # #
# K K L O K O
L O # # K O K
O J # # L L #
# K # # O L L
```

### Step 5

Start: (0, 2), End: (0, 4), Sacrifice: (5, 5)

```
O L # # # J K
# # L L O K #
# O O # # # #
# K K L O K O
L O # # K O K
O J # # L # #
# K # # O L L
```

### Step 6

Start: (6, 1), End: (6, 5), Sacrifice: (0, 0)

```
# L # # # J K
# # L L O K #
# O O # # # #
# K K L O K O
L O # # K O K
O J # # L # #
# # # # # # L
```

### Step 7

Start: (4, 0), End: (4, 4), Sacrifice: (4, 6)

```
# L # # # J K
# # L L O K #
# O O # # # #
# K K L O K O
# # # # # O #
O J # # L # #
# # # # # # L
```

### Step 8

Start: (1, 2), End: (3, 2), Sacrifice: (4, 5)

```
# L # # # J K
# # # L O K #
# O # # # # #
# K # L O K O
# # # # # # #
O J # # L # #
# # # # # # L
```

### Step 9

Start: (0, 6), End: (6, 6), Sacrifice: (5, 4)

```
# L # # # J #
# # # L O K #
# O # # # # #
# K # L O K #
# # # # # # #
O J # # # # #
# # # # # # #
```

### Step 10

Start: (0, 1), End: (3, 1), Sacrifice: (5, 1)

```
# # # # # J #
# # # L O K #
# # # # # # #
# # # L O K #
# # # # # # #
O # # # # # #
# # # # # # #
```

### Step 11

Start: (1, 3), End: (1, 5), Sacrifice: (5, 0)

```
# # # # # J #
# # # # # # #
# # # # # # #
# # # L O K #
# # # # # # #
# # # # # # #
# # # # # # #
```

### Step 12

Start: (3, 3), End: (3, 5), Sacrifice: (0, 5)

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
L O K K O L
L L O L K J
L O K K K L
O O J O O O
J K K K L K
K L O K K J
```

## Solution

```
L O K K O L
L L O L K J
L O K K K L
O O J O O O
J K K K L K
K L O K K J
```

### Step 1

Start: (0, 0), End: (0, 2), Sacrifice: (2, 3)

```
# # # K O L
L L O L K J
L O K # K L
O O J O O O
J K K K L K
K L O K K J
```

### Step 2

Start: (1, 3), End: (4, 3), Sacrifice: (4, 0)

```
# # # K O L
L L O # K J
L O K # K L
O O J # O O
# K K # L K
K L O K K J
```

### Step 3

Start: (2, 0), End: (5, 0), Sacrifice: (2, 2)

```
# # # K O L
L L O # K J
# O # # K L
# O J # O O
# K K # L K
# L O K K J
```

### Step 4

Start: (0, 3), End: (0, 5), Sacrifice: (4, 2)

```
# # # # # #
L L O # K J
# O # # K L
# O J # O O
# K # # L K
# L O K K J
```

### Step 5

Start: (2, 4), End: (4, 4), Sacrifice: (1, 5)

```
# # # # # #
L L O # K #
# O # # # L
# O J # # O
# K # # # K
# L O K K J
```

### Step 6

Start: (2, 5), End: (4, 5), Sacrifice: (5, 4)

```
# # # # # #
L L O # K #
# O # # # #
# O J # # #
# K # # # #
# L O K # J
```

### Step 7

Start: (5, 1), End: (5, 3), Sacrifice: (3, 1)

```
# # # # # #
L L O # K #
# O # # # #
# # J # # #
# K # # # #
# # # # # J
```

### Step 8

Start: (1, 1), End: (4, 1), Sacrifice: (5, 5)

```
# # # # # #
L # O # K #
# # # # # #
# # J # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (1, 0), End: (1, 4), Sacrifice: (3, 2)

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
K K L K O K
L L K O L K
O O O L O O
J K L L K K
K O L O K L
J L J L O K
```

## Solution

```
K K L K O K
L L K O L K
O O O L O O
J K L L K K
K O L O K L
J L J L O K
```

### Step 1

Start: (1, 1), End: (3, 1), Sacrifice: (3, 0)

```
K K L K O K
L # K O L K
O # O L O O
# # L L K K
K O L O K L
J L J L O K
```

### Step 2

Start: (4, 2), End: (4, 4), Sacrifice: (3, 5)

```
K K L K O K
L # K O L K
O # O L O O
# # L L K #
K O # # # L
J L J L O K
```

### Step 3

Start: (1, 5), End: (4, 5), Sacrifice: (0, 1)

```
K # L K O K
L # K O L #
O # O L O #
# # L L K #
K O # # # #
J L J L O K
```

### Step 4

Start: (0, 3), End: (2, 3), Sacrifice: (4, 1)

```
K # L # O K
L # K # L #
O # O # O #
# # L L K #
K # # # # #
J L J L O K
```

### Step 5

Start: (1, 0), End: (4, 0), Sacrifice: (5, 1)

```
K # L # O K
# # K # L #
# # O # O #
# # L L K #
# # # # # #
J # J L O K
```

### Step 6

Start: (5, 3), End: (5, 5), Sacrifice: (5, 2)

```
K # L # O K
# # K # L #
# # O # O #
# # L L K #
# # # # # #
J # # # # #
```

### Step 7

Start: (1, 4), End: (3, 4), Sacrifice: (5, 0)

```
K # L # O K
# # K # # #
# # O # # #
# # L L # #
# # # # # #
# # # # # #
```

### Step 8

Start: (1, 2), End: (3, 2), Sacrifice: (0, 0)

```
# # L # O K
# # # # # #
# # # # # #
# # # L # #
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 2), End: (0, 5), Sacrifice: (3, 3)

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
L O K L O
O L L L K
O L O K O
K O O # L
K K K O L
```

## Solution

```
L O K L O
O L L L K
O L O K O
K O O # L
K K K O L
```

### Step 1

Start: (2, 1), End: (2, 3), Sacrifice: (3, 0)

```
L O K L O
O L L L K
O # # # O
# O O # L
K K K O L
```

### Step 2

Start: (1, 2), End: (4, 2), Sacrifice: (1, 3)

```
L O K L O
O L # # K
O # # # O
# O # # L
K K # O L
```

### Step 3

Start: (1, 1), End: (4, 1), Sacrifice: (2, 0)

```
L O K L O
O # # # K
# # # # O
# # # # L
K # # O L
```

### Step 4

Start: (4, 0), End: (4, 4), Sacrifice: (0, 4)

```
L O K L #
O # # # K
# # # # O
# # # # L
# # # # #
```

### Step 5

Start: (0, 0), End: (0, 2), Sacrifice: (1, 0)

```
# # # L #
# # # # K
# # # # O
# # # # L
# # # # #
```

### Step 6

Start: (1, 4), End: (3, 4), Sacrifice: (0, 3)

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
L K K O L
O L O K J
K K O L L
L O O K O
J # L K K
```

## Solution

```
L K K O L
O L O K J
K K O L L
L O O K O
J # L K K
```

### Step 1

Start: (2, 1), End: (2, 3), Sacrifice: (4, 2)

```
L K K O L
O L O K J
K # # # L
L O O K O
J # # K K
```

### Step 2

Start: (2, 4), End: (4, 4), Sacrifice: (0, 2)

```
L K # O L
O L O K J
K # # # #
L O O K #
J # # K #
```

### Step 3

Start: (0, 0), End: (2, 0), Sacrifice: (3, 1)

```
# K # O L
# L O K J
# # # # #
L # O K #
J # # K #
```

### Step 4

Start: (1, 1), End: (1, 3), Sacrifice: (4, 0)

```
# K # O L
# # # # J
# # # # #
L # O K #
# # # K #
```

### Step 5

Start: (3, 0), End: (3, 3), Sacrifice: (4, 3)

```
# K # O L
# # # # J
# # # # #
# # # # #
# # # # #
```

### Step 6

Start: (0, 1), End: (0, 4), Sacrifice: (1, 4)

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
# O L O K
K O L J J
L L O K K
O L O J K
K L O K J
```

## Solution

```
# O L O K
K O L J J
L L O K K
O L O J K
K L O K J
```

### Step 1

Start: (1, 0), End: (1, 2), Sacrifice: (3, 3)

```
# O L O K
# # # J J
L L O K K
O L O # K
K L O K J
```

### Step 2

Start: (0, 2), End: (0, 4), Sacrifice: (0, 1)

```
# # # # #
# # # J J
L L O K K
O L O # K
K L O K J
```

### Step 3

Start: (3, 1), End: (3, 4), Sacrifice: (1, 4)

```
# # # # #
# # # J #
L L O K K
O # # # #
K L O K J
```

### Step 4

Start: (2, 0), End: (4, 0), Sacrifice: (1, 3)

```
# # # # #
# # # # #
# L O K K
# # # # #
# L O K J
```

### Step 5

Start: (2, 1), End: (2, 3), Sacrifice: (4, 4)

```
# # # # #
# # # # #
# # # # K
# # # # #
# L O K #
```

### Step 6

Start: (4, 1), End: (4, 3), Sacrifice: (2, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

