# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
J K K O K L
L O K O O K
J L O O L O
L O L O K L
L O K O L K
L O K O L K
```

## Solution

```
J K K O K L
L O K O O K
J L O O L O
L O L O K L
L O K O L K
L O K O L K
```

### Step 1

Start: (1, 2), End: (3, 2), Sacrifice: (3, 3)

```
J K K O K L
L O # O O K
J L # O L O
L O # # K L
L O K O L K
L O K O L K
```

### Step 2

Start: (0, 1), End: (2, 1), Sacrifice: (0, 4)

```
J # K O # L
L # # O O K
J # # O L O
L O # # K L
L O K O L K
L O K O L K
```

### Step 3

Start: (4, 2), End: (4, 4), Sacrifice: (2, 3)

```
J # K O # L
L # # O O K
J # # # L O
L O # # K L
L O # # # K
L O K O L K
```

### Step 4

Start: (4, 0), End: (4, 5), Sacrifice: (0, 0)

```
# # K O # L
L # # O O K
J # # # L O
L O # # K L
# # # # # #
L O K O L K
```

### Step 5

Start: (0, 2), End: (0, 5), Sacrifice: (2, 0)

```
# # # # # #
L # # O O K
# # # # L O
L O # # K L
# # # # # #
L O K O L K
```

### Step 6

Start: (1, 5), End: (3, 5), Sacrifice: (2, 4)

```
# # # # # #
L # # O O #
# # # # # #
L O # # K #
# # # # # #
L O K O L K
```

### Step 7

Start: (5, 2), End: (5, 4), Sacrifice: (1, 4)

```
# # # # # #
L # # O # #
# # # # # #
L O # # K #
# # # # # #
L O # # # K
```

### Step 8

Start: (3, 0), End: (3, 4), Sacrifice: (1, 3)

```
# # # # # #
L # # # # #
# # # # # #
# # # # # #
# # # # # #
L O # # # K
```

### Step 9

Start: (5, 0), End: (5, 5), Sacrifice: (1, 0)

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
K O L O K
# K K J O
K O K O L
O L L O K
L L O K J
```

## Solution

```
K O L O K
# K K J O
K O K O L
O L L O K
L L O K J
```

### Step 1

Start: (3, 2), End: (3, 4), Sacrifice: (0, 4)

```
K O L O #
# K K J O
K O K O L
O L # # #
L L O K J
```

### Step 2

Start: (1, 1), End: (3, 1), Sacrifice: (1, 3)

```
K O L O #
# # K # O
K # K O L
O # # # #
L L O K J
```

### Step 3

Start: (0, 0), End: (0, 2), Sacrifice: (1, 2)

```
# # # O #
# # # # O
K # K O L
O # # # #
L L O K J
```

### Step 4

Start: (2, 0), End: (4, 0), Sacrifice: (0, 3)

```
# # # # #
# # # # O
# # K O L
# # # # #
# L O K J
```

### Step 5

Start: (2, 2), End: (2, 4), Sacrifice: (4, 4)

```
# # # # #
# # # # O
# # # # #
# # # # #
# L O K #
```

### Step 6

Start: (4, 1), End: (4, 3), Sacrifice: (1, 4)

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
K K O L L L K
K L O K O O K
J L K K K K L
K L L O K K O
O O O O J L K
L K O L J O K
L O L K L L #
```

## Solution

```
K K O L L L K
K L O K O O K
J L K K K K L
K L L O K K O
O O O O J L K
L K O L J O K
L O L K L L #
```

### Step 1

Start: (3, 0), End: (5, 0), Sacrifice: (6, 4)

```
K K O L L L K
K L O K O O K
J L K K K K L
# L L O K K O
# O O O J L K
# K O L J O K
L O L K # L #
```

### Step 2

Start: (3, 1), End: (5, 1), Sacrifice: (2, 1)

```
K K O L L L K
K L O K O O K
J # K K K K L
# # L O K K O
# # O O J L K
# # O L J O K
L O L K # L #
```

### Step 3

Start: (0, 5), End: (2, 5), Sacrifice: (4, 4)

```
K K O L L # K
K L O K O # K
J # K K K # L
# # L O K K O
# # O O # L K
# # O L J O K
L O L K # L #
```

### Step 4

Start: (2, 6), End: (4, 6), Sacrifice: (5, 4)

```
K K O L L # K
K L O K O # K
J # K K K # #
# # L O K K #
# # O O # L #
# # O L # O K
L O L K # L #
```

### Step 5

Start: (0, 4), End: (2, 4), Sacrifice: (0, 6)

```
K K O L # # #
K L O K # # K
J # K K # # #
# # L O K K #
# # O O # L #
# # O L # O K
L O L K # L #
```

### Step 6

Start: (3, 2), End: (3, 4), Sacrifice: (5, 2)

```
K K O L # # #
K L O K # # K
J # K K # # #
# # # # # K #
# # O O # L #
# # # L # O K
L O L K # L #
```

### Step 7

Start: (2, 3), End: (5, 3), Sacrifice: (0, 0)

```
# K O L # # #
K L O K # # K
J # K # # # #
# # # # # K #
# # O # # L #
# # # # # O K
L O L K # L #
```

### Step 8

Start: (0, 1), End: (0, 3), Sacrifice: (2, 0)

```
# # # # # # #
K L O K # # K
# # K # # # #
# # # # # K #
# # O # # L #
# # # # # O K
L O L K # L #
```

### Step 9

Start: (2, 2), End: (6, 2), Sacrifice: (5, 6)

```
# # # # # # #
K L O K # # K
# # # # # # #
# # # # # K #
# # # # # L #
# # # # # O #
L O # K # L #
```

### Step 10

Start: (1, 1), End: (1, 3), Sacrifice: (4, 5)

```
# # # # # # #
K # # # # # K
# # # # # # #
# # # # # K #
# # # # # # #
# # # # # O #
L O # K # L #
```

### Step 11

Start: (3, 5), End: (6, 5), Sacrifice: (1, 6)

```
# # # # # # #
K # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
L O # K # # #
```

### Step 12

Start: (6, 0), End: (6, 3), Sacrifice: (1, 0)

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
L O K L K
L O K J J
O L O L O
K O L O L
O K O K #
```

## Solution

```
L O K L K
L O K J J
O L O L O
K O L O L
O K O K #
```

### Step 1

Start: (0, 0), End: (0, 2), Sacrifice: (1, 3)

```
# # # L K
L O K # J
O L O L O
K O L O L
O K O K #
```

### Step 2

Start: (2, 1), End: (4, 1), Sacrifice: (4, 2)

```
# # # L K
L O K # J
O # O L O
K # L O L
O # # K #
```

### Step 3

Start: (1, 0), End: (3, 0), Sacrifice: (1, 4)

```
# # # L K
# O K # #
# # O L O
# # L O L
O # # K #
```

### Step 4

Start: (0, 4), End: (3, 4), Sacrifice: (1, 1)

```
# # # L #
# # K # #
# # O L #
# # L O #
O # # K #
```

### Step 5

Start: (2, 3), End: (4, 3), Sacrifice: (4, 0)

```
# # # L #
# # K # #
# # O # #
# # L # #
# # # # #
```

### Step 6

Start: (1, 2), End: (3, 2), Sacrifice: (0, 3)

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
J J K O L
L K L L L
O O O K O
K L K O K
# L O K K
```

## Solution

```
J J K O L
L K L L L
O O O K O
K L K O K
# L O K K
```

### Step 1

Start: (1, 0), End: (3, 0), Sacrifice: (0, 1)

```
J # K O L
# K L L L
# O O K O
# L K O K
# L O K K
```

### Step 2

Start: (1, 2), End: (3, 2), Sacrifice: (0, 0)

```
# # K O L
# K # L L
# O # K O
# L # O K
# L O K K
```

### Step 3

Start: (0, 2), End: (0, 4), Sacrifice: (1, 3)

```
# # # # #
# K # # L
# O # K O
# L # O K
# L O K K
```

### Step 4

Start: (3, 1), End: (3, 4), Sacrifice: (4, 3)

```
# # # # #
# K # # L
# O # K O
# # # # #
# L O # K
```

### Step 5

Start: (1, 4), End: (4, 4), Sacrifice: (4, 2)

```
# # # # #
# K # # #
# O # K #
# # # # #
# L # # #
```

### Step 6

Start: (1, 1), End: (4, 1), Sacrifice: (2, 3)

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
O O L K O
J L O K O
L K L O K
# K O L L
```

## Solution

```
K L K L K
O O L K O
J L O K O
L K L O K
# K O L L
```

### Step 1

Start: (2, 1), End: (2, 3), Sacrifice: (1, 2)

```
K L K L K
O O # K O
J # # # O
L K L O K
# K O L L
```

### Step 2

Start: (0, 1), End: (3, 1), Sacrifice: (1, 4)

```
K # K L K
O # # K #
J # # # O
L # L O K
# K O L L
```

### Step 3

Start: (3, 2), End: (3, 4), Sacrifice: (0, 2)

```
K # # L K
O # # K #
J # # # O
L # # # #
# K O L L
```

### Step 4

Start: (0, 4), End: (4, 4), Sacrifice: (0, 3)

```
K # # # #
O # # K #
J # # # #
L # # # #
# K O L #
```

### Step 5

Start: (4, 1), End: (4, 3), Sacrifice: (2, 0)

```
K # # # #
O # # K #
# # # # #
L # # # #
# # # # #
```

### Step 6

Start: (0, 0), End: (3, 0), Sacrifice: (1, 3)

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
L O L K K K
K O L O L O
J O O L K L
L O K K O O
O O K O L K
K O L L L K
```

## Solution

```
L O L K K K
K O L O L O
J O O L K L
L O K K O O
O O K O L K
K O L L L K
```

### Step 1

Start: (2, 5), End: (4, 5), Sacrifice: (0, 5)

```
L O L K K #
K O L O L O
J O O L K #
L O K K O #
O O K O L #
K O L L L K
```

### Step 2

Start: (2, 4), End: (4, 4), Sacrifice: (1, 2)

```
L O L K K #
K O # O L O
J O O L # #
L O K K # #
O O K O # #
K O L L L K
```

### Step 3

Start: (3, 0), End: (3, 2), Sacrifice: (5, 4)

```
L O L K K #
K O # O L O
J O O L # #
# # # K # #
O O K O # #
K O L L # K
```

### Step 4

Start: (5, 0), End: (5, 2), Sacrifice: (2, 1)

```
L O L K K #
K O # O L O
J # O L # #
# # # K # #
O O K O # #
# # # L # K
```

### Step 5

Start: (0, 2), End: (4, 2), Sacrifice: (2, 0)

```
L O # K K #
K O # O L O
# # # L # #
# # # K # #
O O # O # #
# # # L # K
```

### Step 6

Start: (3, 3), End: (5, 3), Sacrifice: (1, 5)

```
L O # K K #
K O # O L #
# # # L # #
# # # # # #
O O # # # #
# # # # # K
```

### Step 7

Start: (0, 3), End: (2, 3), Sacrifice: (5, 5)

```
L O # # K #
K O # # L #
# # # # # #
# # # # # #
O O # # # #
# # # # # #
```

### Step 8

Start: (0, 0), End: (0, 4), Sacrifice: (4, 1)

```
# # # # # #
K O # # L #
# # # # # #
# # # # # #
O # # # # #
# # # # # #
```

### Step 9

Start: (1, 0), End: (1, 4), Sacrifice: (4, 0)

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
L # K O L
O L O K L
K K L J O
K O L O K
K L L L K
```

## Solution

```
L # K O L
O L O K L
K K L J O
K O L O K
K L L L K
```

### Step 1

Start: (0, 0), End: (2, 0), Sacrifice: (4, 0)

```
# # K O L
# L O K L
# K L J O
K O L O K
# L L L K
```

### Step 2

Start: (3, 2), End: (3, 4), Sacrifice: (2, 2)

```
# # K O L
# L O K L
# K # J O
K O # # #
# L L L K
```

### Step 3

Start: (1, 4), End: (4, 4), Sacrifice: (4, 2)

```
# # K O L
# L O K #
# K # J #
K O # # #
# L # L #
```

### Step 4

Start: (2, 1), End: (4, 1), Sacrifice: (2, 3)

```
# # K O L
# L O K #
# # # # #
K # # # #
# # # L #
```

### Step 5

Start: (1, 1), End: (1, 3), Sacrifice: (4, 3)

```
# # K O L
# # # # #
# # # # #
K # # # #
# # # # #
```

### Step 6

Start: (0, 2), End: (0, 4), Sacrifice: (3, 0)

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
K O L K O L
L O L K J O
L K L K K K
O O O K O L
K L K J O K
J L L L O K
```

## Solution

```
K O L K O L
L O L K J O
L K L K K K
O O O K O L
K L K J O K
J L L L O K
```

### Step 1

Start: (0, 3), End: (0, 5), Sacrifice: (2, 3)

```
K O L # # #
L O L K J O
L K L # K K
O O O K O L
K L K J O K
J L L L O K
```

### Step 2

Start: (3, 3), End: (3, 5), Sacrifice: (1, 4)

```
K O L # # #
L O L K # O
L K L # K K
O O O # # #
K L K J O K
J L L L O K
```

### Step 3

Start: (0, 0), End: (0, 2), Sacrifice: (1, 2)

```
# # # # # #
L O # K # O
L K L # K K
O O O # # #
K L K J O K
J L L L O K
```

### Step 4

Start: (1, 0), End: (1, 3), Sacrifice: (5, 3)

```
# # # # # #
# # # # # O
L K L # K K
O O O # # #
K L K J O K
J L L # O K
```

### Step 5

Start: (2, 2), End: (4, 2), Sacrifice: (1, 5)

```
# # # # # #
# # # # # #
L K # # K K
O O # # # #
K L # J O K
J L L # O K
```

### Step 6

Start: (2, 0), End: (4, 0), Sacrifice: (2, 5)

```
# # # # # #
# # # # # #
# K # # K #
# O # # # #
# L # J O K
J L L # O K
```

### Step 7

Start: (5, 2), End: (5, 5), Sacrifice: (4, 3)

```
# # # # # #
# # # # # #
# K # # K #
# O # # # #
# L # # O K
J L # # # #
```

### Step 8

Start: (4, 1), End: (4, 5), Sacrifice: (2, 4)

```
# # # # # #
# # # # # #
# K # # # #
# O # # # #
# # # # # #
J L # # # #
```

### Step 9

Start: (2, 1), End: (5, 1), Sacrifice: (5, 0)

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
L K K L O L
O O K O O L
J L L K J L
K O O K O L
L L K O O K
O L K O K K
```

## Solution

```
L K K L O L
O O K O O L
J L L K J L
K O O K O L
L L K O O K
O L K O K K
```

### Step 1

Start: (0, 3), End: (2, 3), Sacrifice: (2, 5)

```
L K K # O L
O O K # O L
J L L # J #
K O O K O L
L L K O O K
O L K O K K
```

### Step 2

Start: (3, 3), End: (3, 5), Sacrifice: (5, 2)

```
L K K # O L
O O K # O L
J L L # J #
K O O # # #
L L K O O K
O L # O K K
```

### Step 3

Start: (2, 2), End: (4, 2), Sacrifice: (4, 0)

```
L K K # O L
O O K # O L
J L # # J #
K O # # # #
# L # O O K
O L # O K K
```

### Step 4

Start: (0, 2), End: (0, 5), Sacrifice: (5, 4)

```
L K # # # #
O O K # O L
J L # # J #
K O # # # #
# L # O O K
O L # O # K
```

### Step 5

Start: (5, 1), End: (5, 5), Sacrifice: (4, 3)

```
L K # # # #
O O K # O L
J L # # J #
K O # # # #
# L # # O K
O # # # # #
```

### Step 6

Start: (0, 1), End: (2, 1), Sacrifice: (2, 0)

```
L # # # # #
O # K # O L
# # # # J #
K O # # # #
# L # # O K
O # # # # #
```

### Step 7

Start: (4, 1), End: (4, 5), Sacrifice: (2, 4)

```
L # # # # #
O # K # O L
# # # # # #
K O # # # #
# # # # # #
O # # # # #
```

### Step 8

Start: (1, 2), End: (1, 5), Sacrifice: (5, 0)

```
L # # # # #
O # # # # #
# # # # # #
K O # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 0), End: (3, 0), Sacrifice: (3, 1)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

