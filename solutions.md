# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
K O O J K L
O L O K O L
J L O K J O
L L L O K K
K J O L L L
K O L K O L
```

## Solution

```
K O O J K L
O L O K O L
J L O K J O
L L L O K K
K J O L L L
K O L K O L
```

### Step 1

Start: (1, 5), End: (3, 5), Sacrifice: (0, 1)

```
K # O J K L
O L O K O #
J L O K J #
L L L O K #
K J O L L L
K O L K O L
```

### Step 2

Start: (2, 1), End: (2, 3), Sacrifice: (0, 2)

```
K # # J K L
O L O K O #
J # # # J #
L L L O K #
K J O L L L
K O L K O L
```

### Step 3

Start: (3, 2), End: (3, 4), Sacrifice: (2, 4)

```
K # # J K L
O L O K O #
J # # # # #
L L # # # #
K J O L L L
K O L K O L
```

### Step 4

Start: (1, 1), End: (1, 3), Sacrifice: (2, 0)

```
K # # J K L
O # # # O #
# # # # # #
L L # # # #
K J O L L L
K O L K O L
```

### Step 5

Start: (0, 4), End: (4, 4), Sacrifice: (4, 1)

```
K # # J # L
O # # # # #
# # # # # #
L L # # # #
K # O L # L
K O L K O L
```

### Step 6

Start: (5, 0), End: (5, 2), Sacrifice: (4, 3)

```
K # # J # L
O # # # # #
# # # # # #
L L # # # #
K # O # # L
# # # K O L
```

### Step 7

Start: (4, 0), End: (4, 5), Sacrifice: (3, 1)

```
K # # J # L
O # # # # #
# # # # # #
L # # # # #
# # # # # #
# # # K O L
```

### Step 8

Start: (0, 0), End: (3, 0), Sacrifice: (0, 5)

```
# # # J # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # K O L
```

### Step 9

Start: (5, 3), End: (5, 5), Sacrifice: (0, 3)

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
L K L O J K K
O L L O K O K
K L O K K L L
L L L O O J O
O O J O L # J
O L K O L O K
K K K O L O L
```

## Solution

```
L K L O J K K
O L L O K O K
K L O K K L L
L L L O O J O
O O J O L # J
O L K O L O K
K K K O L O L
```

### Step 1

Start: (0, 5), End: (2, 5), Sacrifice: (5, 0)

```
L K L O J # K
O L L O K # K
K L O K K # L
L L L O O J O
O O J O L # J
# L K O L O K
K K K O L O L
```

### Step 2

Start: (6, 2), End: (6, 4), Sacrifice: (1, 1)

```
L K L O J # K
O # L O K # K
K L O K K # L
L L L O O J O
O O J O L # J
# L K O L O K
K K # # # O L
```

### Step 3

Start: (2, 1), End: (2, 3), Sacrifice: (1, 6)

```
L K L O J # K
O # L O K # #
K # # # K # L
L L L O O J O
O O J O L # J
# L K O L O K
K K # # # O L
```

### Step 4

Start: (2, 4), End: (4, 4), Sacrifice: (5, 5)

```
L K L O J # K
O # L O K # #
K # # # # # L
L L L O # J O
O O J O # # J
# L K O L # K
K K # # # O L
```

### Step 5

Start: (6, 1), End: (6, 6), Sacrifice: (4, 2)

```
L K L O J # K
O # L O K # #
K # # # # # L
L L L O # J O
O O # O # # J
# L K O L # K
K # # # # # #
```

### Step 6

Start: (3, 0), End: (6, 0), Sacrifice: (0, 4)

```
L K L O # # K
O # L O K # #
K # # # # # L
# L L O # J O
# O # O # # J
# L K O L # K
# # # # # # #
```

### Step 7

Start: (1, 2), End: (1, 4), Sacrifice: (3, 3)

```
L K L O # # K
O # # # # # #
K # # # # # L
# L L # # J O
# O # O # # J
# L K O L # K
# # # # # # #
```

### Step 8

Start: (5, 2), End: (5, 4), Sacrifice: (3, 2)

```
L K L O # # K
O # # # # # #
K # # # # # L
# L # # # J O
# O # O # # J
# L # # # # K
# # # # # # #
```

### Step 9

Start: (0, 2), End: (0, 6), Sacrifice: (4, 6)

```
L K # # # # #
O # # # # # #
K # # # # # L
# L # # # J O
# O # O # # #
# L # # # # K
# # # # # # #
```

### Step 10

Start: (2, 6), End: (5, 6), Sacrifice: (3, 1)

```
L K # # # # #
O # # # # # #
K # # # # # #
# # # # # J #
# O # O # # #
# L # # # # #
# # # # # # #
```

### Step 11

Start: (0, 1), End: (5, 1), Sacrifice: (4, 3)

```
L # # # # # #
O # # # # # #
K # # # # # #
# # # # # J #
# # # # # # #
# # # # # # #
# # # # # # #
```

### Step 12

Start: (0, 0), End: (2, 0), Sacrifice: (3, 5)

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
L J J L L L
O J K O L L
K K K O L O
K L K O L K
L O O O K K
K K L O L O
```

## Solution

```
L J J L L L
O J K O L L
K K K O L O
K L K O L K
L O O O K K
K K L O L O
```

### Step 1

Start: (1, 2), End: (1, 4), Sacrifice: (0, 5)

```
L J J L L #
O J # # # L
K K K O L O
K L K O L K
L O O O K K
K K L O L O
```

### Step 2

Start: (3, 1), End: (5, 1), Sacrifice: (1, 1)

```
L J J L L #
O # # # # L
K K K O L O
K # K O L K
L # O O K K
K # L O L O
```

### Step 3

Start: (3, 2), End: (5, 2), Sacrifice: (0, 4)

```
L J J L # #
O # # # # L
K K K O L O
K # # O L K
L # # O K K
K # # O L O
```

### Step 4

Start: (5, 0), End: (5, 4), Sacrifice: (5, 5)

```
L J J L # #
O # # # # L
K K K O L O
K # # O L K
L # # O K K
# # # # # #
```

### Step 5

Start: (3, 0), End: (3, 4), Sacrifice: (0, 2)

```
L J # L # #
O # # # # L
K K K O L O
# # # # # K
L # # O K K
# # # # # #
```

### Step 6

Start: (0, 0), End: (2, 0), Sacrifice: (4, 4)

```
# J # L # #
# # # # # L
# K K O L O
# # # # # K
L # # O # K
# # # # # #
```

### Step 7

Start: (4, 0), End: (4, 5), Sacrifice: (0, 1)

```
# # # L # #
# # # # # L
# K K O L O
# # # # # K
# # # # # #
# # # # # #
```

### Step 8

Start: (1, 5), End: (3, 5), Sacrifice: (2, 1)

```
# # # L # #
# # # # # #
# # K O L #
# # # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (2, 2), End: (2, 4), Sacrifice: (0, 3)

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
L K O O L
O L O K L
K K O L O
K K O L K
# L L O O
```

## Solution

```
L K O O L
O L O K L
K K O L O
K K O L K
# L L O O
```

### Step 1

Start: (1, 4), End: (3, 4), Sacrifice: (0, 2)

```
L K # O L
O L O K #
K K O L #
K K O L #
# L L O O
```

### Step 2

Start: (0, 0), End: (2, 0), Sacrifice: (3, 1)

```
# K # O L
# L O K #
# K O L #
K # O L #
# L L O O
```

### Step 3

Start: (2, 1), End: (2, 3), Sacrifice: (4, 4)

```
# K # O L
# L O K #
# # # # #
K # O L #
# L L O #
```

### Step 4

Start: (3, 0), End: (3, 3), Sacrifice: (4, 3)

```
# K # O L
# L O K #
# # # # #
# # # # #
# L L # #
```

### Step 5

Start: (1, 1), End: (1, 3), Sacrifice: (4, 1)

```
# K # O L
# # # # #
# # # # #
# # # # #
# # L # #
```

### Step 6

Start: (0, 1), End: (0, 4), Sacrifice: (4, 2)

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
# O K O L
L O K L O
K O L L L
K L O K O
L O J K K
```

## Solution

```
# O K O L
L O K L O
K O L L L
K L O K O
L O J K K
```

### Step 1

Start: (3, 1), End: (3, 3), Sacrifice: (1, 3)

```
# O K O L
L O K # O
K O L L L
K # # # O
L O J K K
```

### Step 2

Start: (0, 2), End: (0, 4), Sacrifice: (3, 0)

```
# O # # #
L O K # O
K O L L L
# # # # O
L O J K K
```

### Step 3

Start: (2, 4), End: (4, 4), Sacrifice: (0, 1)

```
# # # # #
L O K # O
K O L L #
# # # # #
L O J K #
```

### Step 4

Start: (2, 0), End: (2, 2), Sacrifice: (2, 3)

```
# # # # #
L O K # O
# # # # #
# # # # #
L O J K #
```

### Step 5

Start: (1, 0), End: (1, 2), Sacrifice: (4, 2)

```
# # # # #
# # # # O
# # # # #
# # # # #
L O # K #
```

### Step 6

Start: (4, 0), End: (4, 3), Sacrifice: (1, 4)

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
L L J L O L
L O K O L O
O L K K O K
O O O O K J
K K L O K L
J K L O L O
```

## Solution

```
L L J L O L
L O K O L O
O L K K O K
O O O O K J
K K L O K L
J K L O L O
```

### Step 1

Start: (0, 3), End: (2, 3), Sacrifice: (0, 4)

```
L L J # # L
L O K # L O
O L K # O K
O O O O K J
K K L O K L
J K L O L O
```

### Step 2

Start: (1, 0), End: (1, 2), Sacrifice: (0, 2)

```
L L # # # L
# # # # L O
O L K # O K
O O O O K J
K K L O K L
J K L O L O
```

### Step 3

Start: (4, 2), End: (4, 4), Sacrifice: (3, 0)

```
L L # # # L
# # # # L O
O L K # O K
# O O O K J
K K # # # L
J K L O L O
```

### Step 4

Start: (2, 2), End: (5, 2), Sacrifice: (2, 1)

```
L L # # # L
# # # # L O
O # # # O K
# O # O K J
K K # # # L
J K # O L O
```

### Step 5

Start: (1, 4), End: (3, 4), Sacrifice: (3, 5)

```
L L # # # L
# # # # # O
O # # # # K
# O # O # #
K K # # # L
J K # O L O
```

### Step 6

Start: (5, 1), End: (5, 4), Sacrifice: (4, 5)

```
L L # # # L
# # # # # O
O # # # # K
# O # O # #
K K # # # #
J # # # # O
```

### Step 7

Start: (0, 0), End: (4, 0), Sacrifice: (5, 5)

```
# L # # # L
# # # # # O
# # # # # K
# O # O # #
# K # # # #
J # # # # #
```

### Step 8

Start: (0, 1), End: (4, 1), Sacrifice: (3, 3)

```
# # # # # L
# # # # # O
# # # # # K
# # # # # #
# # # # # #
J # # # # #
```

### Step 9

Start: (0, 5), End: (2, 5), Sacrifice: (5, 0)

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
L O K O L
L O O K O
O K J # K
L O O K K
K L K O L
```

## Solution

```
L O K O L
L O O K O
O K J # K
L O O K K
K L K O L
```

### Step 1

Start: (2, 1), End: (4, 1), Sacrifice: (1, 1)

```
L O K O L
L # O K O
O # J # K
L # O K K
K # K O L
```

### Step 2

Start: (4, 2), End: (4, 4), Sacrifice: (3, 4)

```
L O K O L
L # O K O
O # J # K
L # O K #
K # # # #
```

### Step 3

Start: (0, 4), End: (2, 4), Sacrifice: (0, 1)

```
L # K O #
L # O K #
O # J # #
L # O K #
K # # # #
```

### Step 4

Start: (3, 0), End: (3, 3), Sacrifice: (0, 2)

```
L # # O #
L # O K #
O # J # #
# # # # #
K # # # #
```

### Step 5

Start: (1, 0), End: (1, 3), Sacrifice: (2, 2)

```
L # # O #
# # # # #
O # # # #
# # # # #
K # # # #
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

# Puzzle 8

## Generated Puzzle

```
K K L K K K
K O O O L K
O O K L J O
O L L O K L
K O L O O K
L L L O K O
```

## Solution

```
K K L K K K
K O O O L K
O O K L J O
O L L O K L
K O L O O K
L L L O K O
```

### Step 1

Start: (3, 2), End: (3, 4), Sacrifice: (1, 5)

```
K K L K K K
K O O O L #
O O K L J O
O L # # # L
K O L O O K
L L L O K O
```

### Step 2

Start: (0, 3), End: (2, 3), Sacrifice: (5, 1)

```
K K L # K K
K O O # L #
O O K # J O
O L # # # L
K O L O O K
L # L O K O
```

### Step 3

Start: (0, 2), End: (2, 2), Sacrifice: (4, 0)

```
K K # # K K
K O # # L #
O O # # J O
O L # # # L
# O L O O K
L # L O K O
```

### Step 4

Start: (1, 0), End: (1, 4), Sacrifice: (4, 3)

```
K K # # K K
# # # # # #
O O # # J O
O L # # # L
# O L # O K
L # L O K O
```

### Step 5

Start: (5, 2), End: (5, 4), Sacrifice: (2, 4)

```
K K # # K K
# # # # # #
O O # # # O
O L # # # L
# O L # O K
L # # # # O
```

### Step 6

Start: (0, 1), End: (3, 1), Sacrifice: (0, 4)

```
K # # # # K
# # # # # #
O # # # # O
O # # # # L
# O L # O K
L # # # # O
```

### Step 7

Start: (0, 5), End: (3, 5), Sacrifice: (4, 1)

```
K # # # # #
# # # # # #
O # # # # #
O # # # # #
# # L # O K
L # # # # O
```

### Step 8

Start: (4, 2), End: (4, 5), Sacrifice: (3, 0)

```
K # # # # #
# # # # # #
O # # # # #
# # # # # #
# # # # # #
L # # # # O
```

### Step 9

Start: (0, 0), End: (5, 0), Sacrifice: (5, 5)

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
K K O L J
O K O L L
K O L # L
L K L O K
K L O L L
```

## Solution

```
K K O L J
O K O L L
K O L # L
L K L O K
K L O L L
```

### Step 1

Start: (2, 0), End: (2, 2), Sacrifice: (4, 3)

```
K K O L J
O K O L L
# # # # L
L K L O K
K L O # L
```

### Step 2

Start: (1, 1), End: (1, 3), Sacrifice: (4, 1)

```
K K O L J
O # # # L
# # # # L
L K L O K
K # O # L
```

### Step 3

Start: (0, 1), End: (0, 3), Sacrifice: (1, 4)

```
K # # # J
O # # # #
# # # # L
L K L O K
K # O # L
```

### Step 4

Start: (3, 2), End: (3, 4), Sacrifice: (2, 4)

```
K # # # J
O # # # #
# # # # #
L K # # #
K # O # L
```

### Step 5

Start: (0, 0), End: (3, 0), Sacrifice: (0, 4)

```
# # # # #
# # # # #
# # # # #
# K # # #
K # O # L
```

### Step 6

Start: (4, 0), End: (4, 4), Sacrifice: (3, 1)

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
L O O K K L
K L L O O K
O O O L L K
O L O K K O
K O L O J K
L K L L K O
```

## Solution

```
L O O K K L
K L L O O K
O O O L L K
O L O K K O
K O L O J K
L K L L K O
```

### Step 1

Start: (0, 4), End: (2, 4), Sacrifice: (3, 0)

```
L O O K # L
K L L O # K
O O O L # K
# L O K K O
K O L O J K
L K L L K O
```

### Step 2

Start: (3, 3), End: (5, 3), Sacrifice: (0, 2)

```
L O # K # L
K L L O # K
O O O L # K
# L O # K O
K O L # J K
L K L # K O
```

### Step 3

Start: (3, 1), End: (3, 4), Sacrifice: (4, 4)

```
L O # K # L
K L L O # K
O O O L # K
# # # # # O
K O L # # K
L K L # K O
```

### Step 4

Start: (4, 0), End: (4, 2), Sacrifice: (2, 5)

```
L O # K # L
K L L O # K
O O O L # #
# # # # # O
# # # # # K
L K L # K O
```

### Step 5

Start: (1, 2), End: (1, 5), Sacrifice: (2, 3)

```
L O # K # L
K L # # # #
O O O # # #
# # # # # O
# # # # # K
L K L # K O
```

### Step 6

Start: (0, 5), End: (4, 5), Sacrifice: (2, 2)

```
L O # K # #
K L # # # #
O O # # # #
# # # # # #
# # # # # #
L K L # K O
```

### Step 7

Start: (1, 1), End: (5, 1), Sacrifice: (5, 4)

```
L O # K # #
K # # # # #
O # # # # #
# # # # # #
# # # # # #
L # L # # O
```

### Step 8

Start: (0, 0), End: (0, 3), Sacrifice: (5, 2)

```
# # # # # #
K # # # # #
O # # # # #
# # # # # #
# # # # # #
L # # # # O
```

### Step 9

Start: (1, 0), End: (5, 0), Sacrifice: (5, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

