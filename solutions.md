# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
L L K L K
L L O K O
K K O O L
O O K K L
L L L # L
```

## Solution

```
L L K L K
L L O K O
K K O O L
O O K K L
L L L # L
```

### Step 1

Start: (1, 1), End: (1, 3), Sacrifice: (3, 2)

```
L L K L K
L # # # O
K K O O L
O O # K L
L L L # L
```

### Step 2

Start: (0, 2), End: (4, 2), Sacrifice: (2, 4)

```
L L # L K
L # # # O
K K # O #
O O # K L
L L # # L
```

### Step 3

Start: (2, 0), End: (4, 0), Sacrifice: (0, 0)

```
# L # L K
L # # # O
# K # O #
# O # K L
# L # # L
```

### Step 4

Start: (2, 1), End: (4, 1), Sacrifice: (0, 1)

```
# # # L K
L # # # O
# # # O #
# # # K L
# # # # L
```

### Step 5

Start: (0, 3), End: (3, 3), Sacrifice: (3, 4)

```
# # # # K
L # # # O
# # # # #
# # # # #
# # # # L
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

# Puzzle 2

## Generated Puzzle

```
L L L O K
K K # K J
O O K O K
K O L L O
L L O K L
```

## Solution

```
L L L O K
K K # K J
O O K O K
K O L L O
L L O K L
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (1, 4)

```
L L L O K
K K # K #
O O K O K
# # # L O
L L O K L
```

### Step 2

Start: (2, 4), End: (4, 4), Sacrifice: (0, 1)

```
L # L O K
K K # K #
O O K O #
# # # L #
L L O K #
```

### Step 3

Start: (1, 0), End: (4, 0), Sacrifice: (0, 0)

```
# # L O K
# K # K #
# O K O #
# # # L #
# L O K #
```

### Step 4

Start: (1, 3), End: (3, 3), Sacrifice: (2, 2)

```
# # L O K
# K # # #
# O # # #
# # # # #
# L O K #
```

### Step 5

Start: (0, 2), End: (0, 4), Sacrifice: (2, 1)

```
# # # # #
# K # # #
# # # # #
# # # # #
# L O K #
```

### Step 6

Start: (4, 1), End: (4, 3), Sacrifice: (1, 1)

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
L L O L K
K O L O K
L K K K O
O O O O L
K # L L K
```

## Solution

```
L L O L K
K O L O K
L K K K O
O O O O L
K # L L K
```

### Step 1

Start: (1, 2), End: (1, 4), Sacrifice: (3, 1)

```
L L O L K
K O # # #
L K K K O
O # O O L
K # L L K
```

### Step 2

Start: (2, 0), End: (4, 0), Sacrifice: (0, 0)

```
# L O L K
K O # # #
# K K K O
# # O O L
# # L L K
```

### Step 3

Start: (2, 2), End: (4, 2), Sacrifice: (0, 2)

```
# L # L K
K O # # #
# K # K O
# # # O L
# # # L K
```

### Step 4

Start: (0, 4), End: (3, 4), Sacrifice: (4, 4)

```
# L # L #
K O # # #
# K # K #
# # # O #
# # # L #
```

### Step 5

Start: (0, 1), End: (2, 1), Sacrifice: (0, 3)

```
# # # # #
K # # # #
# # # K #
# # # O #
# # # L #
```

### Step 6

Start: (2, 3), End: (4, 3), Sacrifice: (1, 0)

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
L L L O K
O L O J #
L O L L L
L O O O K
K K K K K
```

## Solution

```
L L L O K
O L O J #
L O L L L
L O O O K
K K K K K
```

### Step 1

Start: (2, 2), End: (4, 2), Sacrifice: (2, 4)

```
L L L O K
O L O J #
L O # L #
L O # O K
K K # K K
```

### Step 2

Start: (0, 2), End: (0, 4), Sacrifice: (2, 0)

```
L L # # #
O L O J #
# O # L #
L O # O K
K K # K K
```

### Step 3

Start: (2, 3), End: (4, 3), Sacrifice: (0, 1)

```
L # # # #
O L O J #
# O # # #
L O # # K
K K # # K
```

### Step 4

Start: (3, 0), End: (3, 4), Sacrifice: (4, 4)

```
L # # # #
O L O J #
# O # # #
# # # # #
K K # # #
```

### Step 5

Start: (1, 1), End: (4, 1), Sacrifice: (1, 2)

```
L # # # #
O # # J #
# # # # #
# # # # #
K # # # #
```

### Step 6

Start: (0, 0), End: (4, 0), Sacrifice: (1, 3)

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
L O L K K
L K O L #
O K O K L
K K K L O
L O O K K
```

## Solution

```
L O L K K
L K O L #
O K O K L
K K K L O
L O O K K
```

### Step 1

Start: (1, 1), End: (1, 3), Sacrifice: (3, 3)

```
L O L K K
L # # # #
O K O K L
K K K # O
L O O K K
```

### Step 2

Start: (2, 4), End: (4, 4), Sacrifice: (0, 4)

```
L O L K #
L # # # #
O K O K #
K K K # #
L O O K #
```

### Step 3

Start: (1, 0), End: (3, 0), Sacrifice: (3, 1)

```
L O L K #
# # # # #
# K O K #
# # K # #
L O O K #
```

### Step 4

Start: (0, 2), End: (3, 2), Sacrifice: (4, 1)

```
L O # K #
# # # # #
# K # K #
# # # # #
L # O K #
```

### Step 5

Start: (0, 0), End: (0, 3), Sacrifice: (2, 3)

```
# # # # #
# # # # #
# K # # #
# # # # #
L # O K #
```

### Step 6

Start: (4, 0), End: (4, 3), Sacrifice: (2, 1)

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
L L K O L L
O O K O L K
L K L O O J
O L O K K L
K K K O L O
K L O K J L
```

## Solution

```
L L K O L L
O O K O L K
L K L O O J
O L O K K L
K K K O L O
K L O K J L
```

### Step 1

Start: (5, 1), End: (5, 3), Sacrifice: (3, 5)

```
L L K O L L
O O K O L K
L K L O O J
O L O K K #
K K K O L O
K # # # J L
```

### Step 2

Start: (2, 0), End: (4, 0), Sacrifice: (2, 5)

```
L L K O L L
O O K O L K
# K L O O #
# L O K K #
# K K O L O
K # # # J L
```

### Step 3

Start: (0, 0), End: (5, 0), Sacrifice: (1, 4)

```
# L K O L L
# O K O # K
# K L O O #
# L O K K #
# K K O L O
# # # # J L
```

### Step 4

Start: (1, 5), End: (5, 5), Sacrifice: (1, 3)

```
# L K O L L
# O K # # #
# K L O O #
# L O K K #
# K K O L #
# # # # J #
```

### Step 5

Start: (0, 4), End: (3, 4), Sacrifice: (5, 4)

```
# L K O # L
# O K # # #
# K L O # #
# L O K # #
# K K O L #
# # # # # #
```

### Step 6

Start: (4, 2), End: (4, 4), Sacrifice: (2, 1)

```
# L K O # L
# O K # # #
# # L O # #
# L O K # #
# K # # # #
# # # # # #
```

### Step 7

Start: (3, 1), End: (3, 3), Sacrifice: (1, 2)

```
# L K O # L
# O # # # #
# # L O # #
# # # # # #
# K # # # #
# # # # # #
```

### Step 8

Start: (0, 2), End: (0, 5), Sacrifice: (2, 2)

```
# L # # # #
# O # # # #
# # # O # #
# # # # # #
# K # # # #
# # # # # #
```

### Step 9

Start: (0, 1), End: (4, 1), Sacrifice: (2, 3)

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
K L L K L
O O K L J
J K O # L
K O L L O
L K O L K
```

## Solution

```
K L L K L
O O K L J
J K O # L
K O L L O
L K O L K
```

### Step 1

Start: (0, 1), End: (2, 1), Sacrifice: (0, 3)

```
K # L # L
O # K L J
J # O # L
K O L L O
L K O L K
```

### Step 2

Start: (1, 2), End: (3, 2), Sacrifice: (1, 3)

```
K # L # L
O # # # J
J # # # L
K O # L O
L K O L K
```

### Step 3

Start: (4, 1), End: (4, 3), Sacrifice: (2, 0)

```
K # L # L
O # # # J
# # # # L
K O # L O
L # # # K
```

### Step 4

Start: (3, 0), End: (3, 3), Sacrifice: (1, 4)

```
K # L # L
O # # # #
# # # # L
# # # # O
L # # # K
```

### Step 5

Start: (0, 0), End: (4, 0), Sacrifice: (2, 4)

```
# # L # L
# # # # #
# # # # #
# # # # O
# # # # K
```

### Step 6

Start: (0, 4), End: (4, 4), Sacrifice: (0, 2)

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
L L O K K
L O L K K
O L O K O
K O K # L
O K O L L
```

## Solution

```
L L O K K
L O L K K
O L O K O
K O K # L
O K O L L
```

### Step 1

Start: (1, 2), End: (3, 2), Sacrifice: (2, 3)

```
L L O K K
L O # K K
O L # # O
K O # # L
O K O L L
```

### Step 2

Start: (4, 1), End: (4, 3), Sacrifice: (0, 4)

```
L L O K #
L O # K K
O L # # O
K O # # L
O # # # L
```

### Step 3

Start: (1, 0), End: (1, 3), Sacrifice: (3, 4)

```
L L O K #
# # # # K
O L # # O
K O # # #
O # # # L
```

### Step 4

Start: (0, 0), End: (3, 0), Sacrifice: (3, 1)

```
# L O K #
# # # # K
# L # # O
# # # # #
O # # # L
```

### Step 5

Start: (1, 4), End: (4, 4), Sacrifice: (2, 1)

```
# L O K #
# # # # #
# # # # #
# # # # #
O # # # #
```

### Step 6

Start: (0, 1), End: (0, 3), Sacrifice: (4, 0)

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
O L K L O L L
O O L O J K O
O K O O O O K
J K L K L O K
K L O J O K O
O O K # O L L
L L K L K J K
```

## Solution

```
O L K L O L L
O O L O J K O
O K O O O O K
J K L K L O K
K L O J O K O
O O K # O L L
L L K L K J K
```

### Step 1

Start: (3, 4), End: (3, 6), Sacrifice: (0, 0)

```
# L K L O L L
O O L O J K O
O K O O O O K
J K L K # # #
K L O J O K O
O O K # O L L
L L K L K J K
```

### Step 2

Start: (3, 2), End: (5, 2), Sacrifice: (4, 3)

```
# L K L O L L
O O L O J K O
O K O O O O K
J K # K # # #
K L # # O K O
O O # # O L L
L L K L K J K
```

### Step 3

Start: (4, 1), End: (4, 5), Sacrifice: (2, 4)

```
# L K L O L L
O O L O J K O
O K O O # O K
J K # K # # #
K # # # # # O
O O # # O L L
L L K L K J K
```

### Step 4

Start: (2, 6), End: (5, 6), Sacrifice: (6, 4)

```
# L K L O L L
O O L O J K O
O K O O # O #
J K # K # # #
K # # # # # #
O O # # O L #
L L K L # J K
```

### Step 5

Start: (4, 0), End: (6, 0), Sacrifice: (6, 5)

```
# L K L O L L
O O L O J K O
O K O O # O #
J K # K # # #
# # # # # # #
# O # # O L #
# L K L # # K
```

### Step 6

Start: (3, 1), End: (6, 1), Sacrifice: (2, 0)

```
# L K L O L L
O O L O J K O
# K O O # O #
J # # K # # #
# # # # # # #
# # # # O L #
# # K L # # K
```

### Step 7

Start: (0, 1), End: (2, 1), Sacrifice: (2, 3)

```
# # K L O L L
O # L O J K O
# # O # # O #
J # # K # # #
# # # # # # #
# # # # O L #
# # K L # # K
```

### Step 8

Start: (0, 3), End: (3, 3), Sacrifice: (5, 4)

```
# # K # O L L
O # L # J K O
# # O # # O #
J # # # # # #
# # # # # # #
# # # # # L #
# # K L # # K
```

### Step 9

Start: (1, 2), End: (6, 2), Sacrifice: (1, 4)

```
# # K # O L L
O # # # # K O
# # # # # O #
J # # # # # #
# # # # # # #
# # # # # L #
# # # L # # K
```

### Step 10

Start: (0, 2), End: (0, 5), Sacrifice: (6, 3)

```
# # # # # # L
O # # # # K O
# # # # # O #
J # # # # # #
# # # # # # #
# # # # # L #
# # # # # # K
```

### Step 11

Start: (0, 6), End: (6, 6), Sacrifice: (3, 0)

```
# # # # # # #
O # # # # K #
# # # # # O #
# # # # # # #
# # # # # # #
# # # # # L #
# # # # # # #
```

### Step 12

Start: (1, 5), End: (5, 5), Sacrifice: (1, 0)

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
L K O L O
K O O L L
O L K L L
L O O L O
K K L # K
```

## Solution

```
L K O L O
K O O L L
O L K L L
L O O L O
K K L # K
```

### Step 1

Start: (2, 2), End: (4, 2), Sacrifice: (3, 3)

```
L K O L O
K O O L L
O L # L L
L O # # O
K K # # K
```

### Step 2

Start: (2, 4), End: (4, 4), Sacrifice: (2, 3)

```
L K O L O
K O O L L
O L # # #
L O # # #
K K # # #
```

### Step 3

Start: (0, 1), End: (0, 3), Sacrifice: (1, 1)

```
L # # # O
K # O L L
O L # # #
L O # # #
K K # # #
```

### Step 4

Start: (1, 0), End: (1, 3), Sacrifice: (0, 4)

```
L # # # #
# # # # L
O L # # #
L O # # #
K K # # #
```

### Step 5

Start: (2, 1), End: (4, 1), Sacrifice: (3, 0)

```
L # # # #
# # # # L
O # # # #
# # # # #
K # # # #
```

### Step 6

Start: (0, 0), End: (4, 0), Sacrifice: (1, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

