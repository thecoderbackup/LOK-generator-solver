# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
L O J K L L K
K K L O O L O
K O L K K O L
K K O O K L K
O O O L L J L
L L O K O J #
K L K L K L K
```

## Solution

```
L O J K L L K
K K L O O L O
K O L K K O L
K K O O K L K
O O O L L J L
L L O K O J #
K L K L K L K
```

### Step 1

Start: (5, 1), End: (5, 3), Sacrifice: (6, 2)

```
L O J K L L K
K K L O O L O
K O L K K O L
K K O O K L K
O O O L L J L
L # # # O J #
K L # L K L K
```

### Step 2

Start: (2, 4), End: (2, 6), Sacrifice: (0, 2)

```
L O # K L L K
K K L O O L O
K O L K # # #
K K O O K L K
O O O L L J L
L # # # O J #
K L # L K L K
```

### Step 3

Start: (4, 4), End: (6, 4), Sacrifice: (3, 6)

```
L O # K L L K
K K L O O L O
K O L K # # #
K K O O K L #
O O O L # J L
L # # # # J #
K L # L # L K
```

### Step 4

Start: (0, 6), End: (4, 6), Sacrifice: (0, 5)

```
L O # K L # #
K K L O O L #
K O L K # # #
K K O O K L #
O O O L # J #
L # # # # J #
K L # L # L K
```

### Step 5

Start: (3, 1), End: (6, 1), Sacrifice: (6, 3)

```
L O # K L # #
K K L O O L #
K O L K # # #
K # O O K L #
O # O L # J #
L # # # # J #
K # # # # L K
```

### Step 6

Start: (0, 0), End: (0, 3), Sacrifice: (6, 6)

```
# # # # L # #
K K L O O L #
K O L K # # #
K # O O K L #
O # O L # J #
L # # # # J #
K # # # # L #
```

### Step 7

Start: (2, 3), End: (4, 3), Sacrifice: (6, 5)

```
# # # # L # #
K K L O O L #
K O L # # # #
K # O # K L #
O # O # # J #
L # # # # J #
K # # # # # #
```

### Step 8

Start: (2, 0), End: (2, 2), Sacrifice: (4, 2)

```
# # # # L # #
K K L O O L #
# # # # # # #
K # O # K L #
O # # # # J #
L # # # # J #
K # # # # # #
```

### Step 9

Start: (0, 4), End: (3, 4), Sacrifice: (6, 0)

```
# # # # # # #
K K L O # L #
# # # # # # #
K # O # # L #
O # # # # J #
L # # # # J #
# # # # # # #
```

### Step 10

Start: (3, 0), End: (3, 5), Sacrifice: (1, 2)

```
# # # # # # #
K K # O # L #
# # # # # # #
# # # # # # #
O # # # # J #
L # # # # J #
# # # # # # #
```

### Step 11

Start: (1, 1), End: (1, 5), Sacrifice: (5, 5)

```
# # # # # # #
K # # # # # #
# # # # # # #
# # # # # # #
O # # # # J #
L # # # # # #
# # # # # # #
```

### Step 12

Start: (1, 0), End: (5, 0), Sacrifice: (4, 5)

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
J L O O K
K O L K L
K K O L L
L O K O O
# O K L K
```

## Solution

```
J L O O K
K O L K L
K K O L L
L O K O O
# O K L K
```

### Step 1

Start: (3, 0), End: (3, 2), Sacrifice: (4, 1)

```
J L O O K
K O L K L
K K O L L
# # # O O
# # K L K
```

### Step 2

Start: (2, 1), End: (2, 3), Sacrifice: (0, 3)

```
J L O # K
K O L K L
K # # # L
# # # O O
# # K L K
```

### Step 3

Start: (1, 3), End: (4, 3), Sacrifice: (2, 0)

```
J L O # K
K O L # L
# # # # L
# # # # O
# # K # K
```

### Step 4

Start: (0, 1), End: (0, 4), Sacrifice: (1, 2)

```
J # # # #
K O # # L
# # # # L
# # # # O
# # K # K
```

### Step 5

Start: (1, 0), End: (1, 4), Sacrifice: (4, 2)

```
J # # # #
# # # # #
# # # # L
# # # # O
# # # # K
```

### Step 6

Start: (2, 4), End: (4, 4), Sacrifice: (0, 0)

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
L # L L L
O L O O O
K O K K L
K K O L O
K L O K K
```

## Solution

```
L # L L L
O L O O O
K O K K L
K K O L O
K L O K K
```

### Step 1

Start: (1, 1), End: (3, 1), Sacrifice: (1, 4)

```
L # L L L
O # O O #
K # K K L
K # O L O
K L O K K
```

### Step 2

Start: (0, 2), End: (2, 2), Sacrifice: (2, 3)

```
L # # L L
O # # O #
K # # # L
K # O L O
K L O K K
```

### Step 3

Start: (0, 0), End: (2, 0), Sacrifice: (4, 0)

```
# # # L L
# # # O #
# # # # L
K # O L O
# L O K K
```

### Step 4

Start: (3, 0), End: (3, 3), Sacrifice: (4, 2)

```
# # # L L
# # # O #
# # # # L
# # # # O
# L # K K
```

### Step 5

Start: (0, 3), End: (4, 3), Sacrifice: (2, 4)

```
# # # # L
# # # # #
# # # # #
# # # # O
# L # # K
```

### Step 6

Start: (0, 4), End: (4, 4), Sacrifice: (4, 1)

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
J L O K K
K K K J O
O O K J L
L O O K K
L L L J #
```

## Solution

```
J L O K K
K K K J O
O O K J L
L O O K K
L L L J #
```

### Step 1

Start: (0, 4), End: (2, 4), Sacrifice: (1, 3)

```
J L O K #
K K K # #
O O K J #
L O O K K
L L L J #
```

### Step 2

Start: (2, 2), End: (4, 2), Sacrifice: (3, 4)

```
J L O K #
K K K # #
O O # J #
L O # K #
L L # J #
```

### Step 3

Start: (0, 1), End: (0, 3), Sacrifice: (1, 2)

```
J # # # #
K K # # #
O O # J #
L O # K #
L L # J #
```

### Step 4

Start: (3, 0), End: (3, 3), Sacrifice: (4, 3)

```
J # # # #
K K # # #
O O # J #
# # # # #
L L # # #
```

### Step 5

Start: (1, 1), End: (4, 1), Sacrifice: (0, 0)

```
# # # # #
K # # # #
O # # J #
# # # # #
L # # # #
```

### Step 6

Start: (1, 0), End: (4, 0), Sacrifice: (2, 3)

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
J L O K K K K
# L O K L O O
O K O J L L L
L L O K O K J
O L O J O O K
K J L O L L K
K O K O L L L
```

## Solution

```
J L O K K K K
# L O K L O O
O K O J L L L
L L O K O K J
O L O J O O K
K J L O L L K
K O K O L L L
```

### Step 1

Start: (1, 1), End: (1, 3), Sacrifice: (2, 3)

```
J L O K K K K
# # # # L O O
O K O # L L L
L L O K O K J
O L O J O O K
K J L O L L K
K O K O L L L
```

### Step 2

Start: (0, 1), End: (0, 3), Sacrifice: (1, 4)

```
J # # # K K K
# # # # # O O
O K O # L L L
L L O K O K J
O L O J O O K
K J L O L L K
K O K O L L L
```

### Step 3

Start: (0, 6), End: (2, 6), Sacrifice: (4, 3)

```
J # # # K K #
# # # # # O #
O K O # L L #
L L O K O K J
O L O # O O K
K J L O L L K
K O K O L L L
```

### Step 4

Start: (2, 1), End: (2, 4), Sacrifice: (3, 6)

```
J # # # K K #
# # # # # O #
O # # # # L #
L L O K O K #
O L O # O O K
K J L O L L K
K O K O L L L
```

### Step 5

Start: (0, 5), End: (2, 5), Sacrifice: (4, 4)

```
J # # # K # #
# # # # # # #
O # # # # # #
L L O K O K #
O L O # # O K
K J L O L L K
K O K O L L L
```

### Step 6

Start: (3, 0), End: (5, 0), Sacrifice: (6, 4)

```
J # # # K # #
# # # # # # #
O # # # # # #
# L O K O K #
# L O # # O K
# J L O L L K
K O K O # L L
```

### Step 7

Start: (6, 2), End: (6, 5), Sacrifice: (0, 4)

```
J # # # # # #
# # # # # # #
O # # # # # #
# L O K O K #
# L O # # O K
# J L O L L K
K O # # # # L
```

### Step 8

Start: (3, 1), End: (3, 3), Sacrifice: (5, 1)

```
J # # # # # #
# # # # # # #
O # # # # # #
# # # # O K #
# L O # # O K
# # L O L L K
K O # # # # L
```

### Step 9

Start: (3, 5), End: (5, 5), Sacrifice: (5, 4)

```
J # # # # # #
# # # # # # #
O # # # # # #
# # # # O # #
# L O # # # K
# # L O # # K
K O # # # # L
```

### Step 10

Start: (4, 1), End: (4, 6), Sacrifice: (0, 0)

```
# # # # # # #
# # # # # # #
O # # # # # #
# # # # O # #
# # # # # # #
# # L O # # K
K O # # # # L
```

### Step 11

Start: (6, 0), End: (6, 6), Sacrifice: (2, 0)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # O # #
# # # # # # #
# # L O # # K
# # # # # # #
```

### Step 12

Start: (5, 2), End: (5, 6), Sacrifice: (3, 4)

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
L O K K L L
K O L O O L
L O K L O O
O L K L O K
O O O K O L
L K L L K K
```

## Solution

```
L O K K L L
K O L O O L
L O K L O O
O L K L O K
O O O K O L
L K L L K K
```

### Step 1

Start: (3, 3), End: (3, 5), Sacrifice: (2, 1)

```
L O K K L L
K O L O O L
L # K L O O
O L K # # #
O O O K O L
L K L L K K
```

### Step 2

Start: (0, 0), End: (0, 2), Sacrifice: (1, 1)

```
# # # K L L
K # L O O L
L # K L O O
O L K # # #
O O O K O L
L K L L K K
```

### Step 3

Start: (0, 3), End: (2, 3), Sacrifice: (5, 0)

```
# # # # L L
K # L # O L
L # K # O O
O L K # # #
O O O K O L
# K L L K K
```

### Step 4

Start: (3, 1), End: (5, 1), Sacrifice: (5, 3)

```
# # # # L L
K # L # O L
L # K # O O
O # K # # #
O # O K O L
# # L # K K
```

### Step 5

Start: (4, 3), End: (4, 5), Sacrifice: (1, 2)

```
# # # # L L
K # # # O L
L # K # O O
O # K # # #
O # O # # #
# # L # K K
```

### Step 6

Start: (1, 0), End: (1, 5), Sacrifice: (3, 0)

```
# # # # L L
# # # # # #
L # K # O O
# # K # # #
O # O # # #
# # L # K K
```

### Step 7

Start: (0, 5), End: (5, 5), Sacrifice: (4, 0)

```
# # # # L #
# # # # # #
L # K # O #
# # K # # #
# # O # # #
# # L # K #
```

### Step 8

Start: (0, 4), End: (5, 4), Sacrifice: (2, 2)

```
# # # # # #
# # # # # #
L # # # # #
# # K # # #
# # O # # #
# # L # # #
```

### Step 9

Start: (3, 2), End: (5, 2), Sacrifice: (2, 0)

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
L J L O K
O # J L O
K O L O L
K K O K L
K O K O L
```

## Solution

```
L J L O K
O # J L O
K O L O L
K K O K L
K O K O L
```

### Step 1

Start: (1, 3), End: (3, 3), Sacrifice: (4, 0)

```
L J L O K
O # J # O
K O L # L
K K O # L
# O K O L
```

### Step 2

Start: (2, 0), End: (2, 2), Sacrifice: (1, 2)

```
L J L O K
O # # # O
# # # # L
K K O # L
# O K O L
```

### Step 3

Start: (3, 1), End: (3, 4), Sacrifice: (0, 3)

```
L J L # K
O # # # O
# # # # L
K # # # #
# O K O L
```

### Step 4

Start: (0, 4), End: (2, 4), Sacrifice: (0, 1)

```
L # L # #
O # # # #
# # # # #
K # # # #
# O K O L
```

### Step 5

Start: (0, 0), End: (3, 0), Sacrifice: (4, 1)

```
# # L # #
# # # # #
# # # # #
# # # # #
# # K O L
```

### Step 6

Start: (4, 2), End: (4, 4), Sacrifice: (0, 2)

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
J K K K O L
L O K O J O
O L O L K K
O L L O O O
K L O K L O
K O K L L L
```

## Solution

```
J K K K O L
L O K O J O
O L O L K K
O L L O O O
K L O K L O
K O K L L L
```

### Step 1

Start: (4, 1), End: (4, 3), Sacrifice: (5, 3)

```
J K K K O L
L O K O J O
O L O L K K
O L L O O O
K # # # L O
K O K # L L
```

### Step 2

Start: (0, 3), End: (2, 3), Sacrifice: (4, 5)

```
J K K # O L
L O K # J O
O L O # K K
O L L O O O
K # # # L #
K O K # L L
```

### Step 3

Start: (2, 5), End: (5, 5), Sacrifice: (3, 3)

```
J K K # O L
L O K # J O
O L O # K #
O L L # O #
K # # # L #
K O K # L #
```

### Step 4

Start: (2, 4), End: (4, 4), Sacrifice: (3, 0)

```
J K K # O L
L O K # J O
O L O # # #
# L L # # #
K # # # # #
K O K # L #
```

### Step 5

Start: (1, 2), End: (3, 2), Sacrifice: (1, 5)

```
J K K # O L
L O # # J #
O L # # # #
# L # # # #
K # # # # #
K O K # L #
```

### Step 6

Start: (1, 0), End: (4, 0), Sacrifice: (5, 2)

```
J K K # O L
# O # # J #
# L # # # #
# L # # # #
# # # # # #
K O # # L #
```

### Step 7

Start: (5, 0), End: (5, 4), Sacrifice: (1, 4)

```
J K K # O L
# O # # # #
# L # # # #
# L # # # #
# # # # # #
# # # # # #
```

### Step 8

Start: (0, 1), End: (2, 1), Sacrifice: (3, 1)

```
J # K # O L
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 2), End: (0, 5), Sacrifice: (0, 0)

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
O L O L J
K O K O K
L L O K L
O K O K O
L K L # K
```

## Solution

```
O L O L J
K O K O K
L L O K L
O K O K O
L K L # K
```

### Step 1

Start: (2, 4), End: (4, 4), Sacrifice: (2, 1)

```
O L O L J
K O K O K
L # O K #
O K O K #
L K L # #
```

### Step 2

Start: (2, 0), End: (2, 3), Sacrifice: (3, 1)

```
O L O L J
K O K O K
# # # # #
O # O K #
L K L # #
```

### Step 3

Start: (1, 0), End: (4, 0), Sacrifice: (0, 2)

```
O L # L J
# O K O K
# # # # #
# # O K #
# K L # #
```

### Step 4

Start: (0, 3), End: (3, 3), Sacrifice: (1, 4)

```
O L # # J
# O K # #
# # # # #
# # O # #
# K L # #
```

### Step 5

Start: (1, 2), End: (4, 2), Sacrifice: (0, 4)

```
O L # # #
# O # # #
# # # # #
# # # # #
# K # # #
```

### Step 6

Start: (0, 1), End: (4, 1), Sacrifice: (0, 0)

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
K O L L O
L J L O K
K K O K K
# O K O O
L L K L L
```

## Solution

```
K O L L O
L J L O K
K K O K K
# O K O O
L L K L L
```

### Step 1

Start: (2, 1), End: (4, 1), Sacrifice: (3, 2)

```
K O L L O
L J L O K
K # O K K
# # # O O
L # K L L
```

### Step 2

Start: (2, 3), End: (4, 3), Sacrifice: (1, 1)

```
K O L L O
L # L O K
K # O # K
# # # # O
L # K # L
```

### Step 3

Start: (0, 0), End: (0, 2), Sacrifice: (4, 0)

```
# # # L O
L # L O K
K # O # K
# # # # O
# # K # L
```

### Step 4

Start: (1, 2), End: (4, 2), Sacrifice: (2, 0)

```
# # # L O
L # # O K
# # # # K
# # # # O
# # # # L
```

### Step 5

Start: (1, 0), End: (1, 4), Sacrifice: (0, 4)

```
# # # L #
# # # # #
# # # # K
# # # # O
# # # # L
```

### Step 6

Start: (2, 4), End: (4, 4), Sacrifice: (0, 3)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

