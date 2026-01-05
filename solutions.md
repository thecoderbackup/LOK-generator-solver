# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
J # K K L O K
K K O O L O L
L O L L J K L
O K O L J O O
K O K O L L K
O L L O K L L
L L O K K K O
```

## Solution

```
J # K K L O K
K K O O L O L
L O L L J K L
O K O L J O O
K O K O L L K
O L L O K L L
L L O K K K O
```

### Step 1

Start: (2, 5), End: (4, 5), Sacrifice: (2, 1)

```
J # K K L O K
K K O O L O L
L # L L J # L
O K O L J # O
K O K O L # K
O L L O K L L
L L O K K K O
```

### Step 2

Start: (3, 1), End: (5, 1), Sacrifice: (0, 0)

```
# # K K L O K
K K O O L O L
L # L L J # L
O # O L J # O
K # K O L # K
O # L O K L L
L L O K K K O
```

### Step 3

Start: (0, 3), End: (2, 3), Sacrifice: (3, 2)

```
# # K # L O K
K K O # L O L
L # L # J # L
O # # L J # O
K # K O L # K
O # L O K L L
L L O K K K O
```

### Step 4

Start: (2, 6), End: (4, 6), Sacrifice: (3, 4)

```
# # K # L O K
K K O # L O L
L # L # J # #
O # # L # # #
K # K O L # #
O # L O K L L
L L O K K K O
```

### Step 5

Start: (2, 0), End: (4, 0), Sacrifice: (6, 5)

```
# # K # L O K
K K O # L O L
# # L # J # #
# # # L # # #
# # K O L # #
O # L O K L L
L L O K K # O
```

### Step 6

Start: (0, 4), End: (0, 6), Sacrifice: (6, 6)

```
# # K # # # #
K K O # L O L
# # L # J # #
# # # L # # #
# # K O L # #
O # L O K L L
L L O K K # #
```

### Step 7

Start: (0, 2), End: (2, 2), Sacrifice: (2, 4)

```
# # # # # # #
K K # # L O L
# # # # # # #
# # # L # # #
# # K O L # #
O # L O K L L
L L O K K # #
```

### Step 8

Start: (4, 2), End: (4, 4), Sacrifice: (5, 4)

```
# # # # # # #
K K # # L O L
# # # # # # #
# # # L # # #
# # # # # # #
O # L O # L L
L L O K K # #
```

### Step 9

Start: (3, 3), End: (6, 3), Sacrifice: (5, 2)

```
# # # # # # #
K K # # L O L
# # # # # # #
# # # # # # #
# # # # # # #
O # # # # L L
L L O # K # #
```

### Step 10

Start: (6, 1), End: (6, 4), Sacrifice: (1, 4)

```
# # # # # # #
K K # # # O L
# # # # # # #
# # # # # # #
# # # # # # #
O # # # # L L
L # # # # # #
```

### Step 11

Start: (1, 1), End: (1, 6), Sacrifice: (5, 6)

```
# # # # # # #
K # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
O # # # # L #
L # # # # # #
```

### Step 12

Start: (1, 0), End: (6, 0), Sacrifice: (5, 5)

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
L L L O L J K
O L J # J L L
K O O L O L O
K K O J K L K
J L K O L J O
K O K L O K L
J K K O L K K
```

## Solution

```
L L L O L J K
O L J # J L L
K O O L O L O
K K O J K L K
J L K O L J O
K O K L O K L
J K K O L K K
```

### Step 1

Start: (1, 1), End: (3, 1), Sacrifice: (6, 5)

```
L L L O L J K
O # J # J L L
K # O L O L O
K # O J K L K
J L K O L J O
K O K L O K L
J K K O L # K
```

### Step 2

Start: (5, 3), End: (5, 5), Sacrifice: (6, 0)

```
L L L O L J K
O # J # J L L
K # O L O L O
K # O J K L K
J L K O L J O
K O K # # # L
# K K O L # K
```

### Step 3

Start: (4, 2), End: (4, 4), Sacrifice: (1, 4)

```
L L L O L J K
O # J # # L L
K # O L O L O
K # O J K L K
J L # # # J O
K O K # # # L
# K K O L # K
```

### Step 4

Start: (2, 0), End: (2, 3), Sacrifice: (0, 5)

```
L L L O L # K
O # J # # L L
# # # # O L O
K # O J K L K
J L # # # J O
K O K # # # L
# K K O L # K
```

### Step 5

Start: (3, 6), End: (5, 6), Sacrifice: (1, 2)

```
L L L O L # K
O # # # # L L
# # # # O L O
K # O J K L #
J L # # # J #
K O K # # # #
# K K O L # K
```

### Step 6

Start: (0, 0), End: (3, 0), Sacrifice: (3, 5)

```
# L L O L # K
# # # # # L L
# # # # O L O
# # O J K # #
J L # # # J #
K O K # # # #
# K K O L # K
```

### Step 7

Start: (1, 6), End: (6, 6), Sacrifice: (4, 5)

```
# L L O L # K
# # # # # L #
# # # # O L #
# # O J K # #
J L # # # # #
K O K # # # #
# K K O L # #
```

### Step 8

Start: (4, 1), End: (6, 1), Sacrifice: (4, 0)

```
# L L O L # K
# # # # # L #
# # # # O L #
# # O J K # #
# # # # # # #
K # K # # # #
# # K O L # #
```

### Step 9

Start: (0, 4), End: (3, 4), Sacrifice: (3, 3)

```
# L L O # # K
# # # # # L #
# # # # # L #
# # O # # # #
# # # # # # #
K # K # # # #
# # K O L # #
```

### Step 10

Start: (6, 2), End: (6, 4), Sacrifice: (1, 5)

```
# L L O # # K
# # # # # # #
# # # # # L #
# # O # # # #
# # # # # # #
K # K # # # #
# # # # # # #
```

### Step 11

Start: (0, 2), End: (5, 2), Sacrifice: (2, 5)

```
# L # O # # K
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
K # # # # # #
# # # # # # #
```

### Step 12

Start: (0, 1), End: (0, 6), Sacrifice: (5, 0)

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
J J K O L
L K O L J
L O K K K
O # L O K
K J K O L
```

## Solution

```
J J K O L
L K O L J
L O K K K
O # L O K
K J K O L
```

### Step 1

Start: (2, 0), End: (2, 2), Sacrifice: (0, 1)

```
J # K O L
L K O L J
# # # K K
O # L O K
K J K O L
```

### Step 2

Start: (0, 2), End: (0, 4), Sacrifice: (1, 4)

```
J # # # #
L K O L #
# # # K K
O # L O K
K J K O L
```

### Step 3

Start: (1, 0), End: (4, 0), Sacrifice: (4, 1)

```
J # # # #
# K O L #
# # # K K
# # L O K
# # K O L
```

### Step 4

Start: (1, 1), End: (1, 3), Sacrifice: (2, 4)

```
J # # # #
# # # # #
# # # K #
# # L O K
# # K O L
```

### Step 5

Start: (4, 2), End: (4, 4), Sacrifice: (0, 0)

```
# # # # #
# # # # #
# # # K #
# # L O K
# # # # #
```

### Step 6

Start: (3, 2), End: (3, 4), Sacrifice: (2, 3)

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
K O L # L
L O J K O
L O K K K
L O J O K
K J L L O
```

## Solution

```
K O L # L
L O J K O
L O K K K
L O J O K
K J L L O
```

### Step 1

Start: (0, 4), End: (2, 4), Sacrifice: (4, 4)

```
K O L # #
L O J K #
L O K K #
L O J O K
K J L L #
```

### Step 2

Start: (2, 3), End: (4, 3), Sacrifice: (4, 1)

```
K O L # #
L O J K #
L O K # #
L O J # K
K # L # #
```

### Step 3

Start: (2, 0), End: (2, 2), Sacrifice: (1, 2)

```
K O L # #
L O # K #
# # # # #
L O J # K
K # L # #
```

### Step 4

Start: (1, 0), End: (1, 3), Sacrifice: (3, 2)

```
K O L # #
# # # # #
# # # # #
L O # # K
K # L # #
```

### Step 5

Start: (0, 0), End: (0, 2), Sacrifice: (4, 2)

```
# # # # #
# # # # #
# # # # #
L O # # K
K # # # #
```

### Step 6

Start: (3, 0), End: (3, 4), Sacrifice: (4, 0)

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
L O K O L
K O J L K
O L O K O
K J L O L
L O K # O
```

## Solution

```
L O K O L
K O J L K
O L O K O
K J L O L
L O K # O
```

### Step 1

Start: (4, 0), End: (4, 2), Sacrifice: (3, 1)

```
L O K O L
K O J L K
O L O K O
K # L O L
# # # # O
```

### Step 2

Start: (1, 4), End: (3, 4), Sacrifice: (1, 2)

```
L O K O L
K O # L #
O L O K #
K # L O #
# # # # O
```

### Step 3

Start: (1, 0), End: (1, 3), Sacrifice: (3, 3)

```
L O K O L
# # # # #
O L O K #
K # L # #
# # # # O
```

### Step 4

Start: (2, 1), End: (2, 3), Sacrifice: (3, 2)

```
L O K O L
# # # # #
O # # # #
K # # # #
# # # # O
```

### Step 5

Start: (0, 0), End: (3, 0), Sacrifice: (4, 4)

```
# O K O L
# # # # #
# # # # #
# # # # #
# # # # #
```

### Step 6

Start: (0, 2), End: (0, 4), Sacrifice: (0, 1)

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
L L O K J J
L K L L O K
K J O L K K
K K O L L O
L O O O K L
L L O K K K
```

## Solution

```
L L O K J J
L K L L O K
K J O L K K
K K O L L O
L O O O K L
L L O K K K
```

### Step 1

Start: (3, 1), End: (5, 1), Sacrifice: (0, 5)

```
L L O K J #
L K L L O K
K J O L K K
K # O L L O
L # O O K L
L # O K K K
```

### Step 2

Start: (3, 3), End: (5, 3), Sacrifice: (2, 1)

```
L L O K J #
L K L L O K
K # O L K K
K # O # L O
L # O # K L
L # O # K K
```

### Step 3

Start: (5, 0), End: (5, 4), Sacrifice: (1, 2)

```
L L O K J #
L K # L O K
K # O L K K
K # O # L O
L # O # K L
# # # # # K
```

### Step 4

Start: (2, 5), End: (4, 5), Sacrifice: (1, 0)

```
L L O K J #
# K # L O K
K # O L K #
K # O # L #
L # O # K #
# # # # # K
```

### Step 5

Start: (0, 1), End: (0, 3), Sacrifice: (1, 1)

```
L # # # J #
# # # L O K
K # O L K #
K # O # L #
L # O # K #
# # # # # K
```

### Step 6

Start: (2, 0), End: (2, 3), Sacrifice: (2, 4)

```
L # # # J #
# # # L O K
# # # # # #
K # O # L #
L # O # K #
# # # # # K
```

### Step 7

Start: (4, 0), End: (4, 4), Sacrifice: (0, 0)

```
# # # # J #
# # # L O K
# # # # # #
K # O # L #
# # # # # #
# # # # # K
```

### Step 8

Start: (3, 0), End: (3, 4), Sacrifice: (5, 5)

```
# # # # J #
# # # L O K
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

### Step 9

Start: (1, 3), End: (1, 5), Sacrifice: (0, 4)

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
# O L L K
J L O K O
K L O K K
L O K O L
K O L L L
```

## Solution

```
# O L L K
J L O K O
K L O K K
L O K O L
K O L L L
```

### Step 1

Start: (4, 0), End: (4, 2), Sacrifice: (2, 0)

```
# O L L K
J L O K O
# L O K K
L O K O L
# # # L L
```

### Step 2

Start: (1, 1), End: (1, 3), Sacrifice: (0, 3)

```
# O L # K
J # # # O
# L O K K
L O K O L
# # # L L
```

### Step 3

Start: (2, 3), End: (4, 3), Sacrifice: (1, 0)

```
# O L # K
# # # # O
# L O # K
L O K # L
# # # # L
```

### Step 4

Start: (2, 1), End: (2, 4), Sacrifice: (0, 1)

```
# # L # K
# # # # O
# # # # #
L O K # L
# # # # L
```

### Step 5

Start: (0, 4), End: (3, 4), Sacrifice: (0, 2)

```
# # # # #
# # # # #
# # # # #
L O K # #
# # # # L
```

### Step 6

Start: (3, 0), End: (3, 2), Sacrifice: (4, 4)

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
L O J L J L K
O O K O L O L
K L L O L K O
L K O O L J L
J L L O K # K
O O K L O K O
K K J L O K L
```

## Solution

```
L O J L J L K
O O K O L O L
K L L O L K O
L K O O L J L
J L L O K # K
O O K L O K O
K K J L O K L
```

### Step 1

Start: (6, 3), End: (6, 5), Sacrifice: (4, 0)

```
L O J L J L K
O O K O L O L
K L L O L K O
L K O O L J L
# L L O K # K
O O K L O K O
K K J # # # L
```

### Step 2

Start: (4, 2), End: (4, 4), Sacrifice: (0, 3)

```
L O J # J L K
O O K O L O L
K L L O L K O
L K O O L J L
# L # # # # K
O O K L O K O
K K J # # # L
```

### Step 3

Start: (5, 3), End: (5, 5), Sacrifice: (1, 6)

```
L O J # J L K
O O K O L O #
K L L O L K O
L K O O L J L
# L # # # # K
O O K # # # O
K K J # # # L
```

### Step 4

Start: (4, 1), End: (6, 1), Sacrifice: (2, 3)

```
L O J # J L K
O O K O L O #
K L L # L K O
L K O O L J L
# # # # # # K
O # K # # # O
K # J # # # L
```

### Step 5

Start: (1, 2), End: (1, 4), Sacrifice: (2, 4)

```
L O J # J L K
O O # # # O #
K L L # # K O
L K O O L J L
# # # # # # K
O # K # # # O
K # J # # # L
```

### Step 6

Start: (0, 0), End: (2, 0), Sacrifice: (0, 4)

```
# O J # # L K
# O # # # O #
# L L # # K O
L K O O L J L
# # # # # # K
O # K # # # O
K # J # # # L
```

### Step 7

Start: (0, 5), End: (2, 5), Sacrifice: (0, 1)

```
# # J # # # K
# O # # # # #
# L L # # # O
L K O O L J L
# # # # # # K
O # K # # # O
K # J # # # L
```

### Step 8

Start: (4, 6), End: (6, 6), Sacrifice: (3, 5)

```
# # J # # # K
# O # # # # #
# L L # # # O
L K O O L # L
# # # # # # #
O # K # # # #
K # J # # # #
```

### Step 9

Start: (2, 2), End: (5, 2), Sacrifice: (1, 1)

```
# # J # # # K
# # # # # # #
# L # # # # O
L K # O L # L
# # # # # # #
O # # # # # #
K # J # # # #
```

### Step 10

Start: (0, 6), End: (3, 6), Sacrifice: (0, 2)

```
# # # # # # #
# # # # # # #
# L # # # # #
L K # O L # #
# # # # # # #
O # # # # # #
K # J # # # #
```

### Step 11

Start: (3, 1), End: (3, 4), Sacrifice: (2, 1)

```
# # # # # # #
# # # # # # #
# # # # # # #
L # # # # # #
# # # # # # #
O # # # # # #
K # J # # # #
```

### Step 12

Start: (3, 0), End: (6, 0), Sacrifice: (6, 2)

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
L O L K K L
K L O J O K
L L K O K O
K O O L K O
K K O J L O
L O K L O K
```

## Solution

```
L O L K K L
K L O J O K
L L K O K O
K O O L K O
K K O J L O
L O K L O K
```

### Step 1

Start: (5, 3), End: (5, 5), Sacrifice: (4, 5)

```
L O L K K L
K L O J O K
L L K O K O
K O O L K O
K K O J L #
L O K # # #
```

### Step 2

Start: (2, 1), End: (4, 1), Sacrifice: (1, 3)

```
L O L K K L
K L O # O K
L # K O K O
K # O L K O
K # O J L #
L O K # # #
```

### Step 3

Start: (0, 2), End: (2, 2), Sacrifice: (0, 5)

```
L O # K K #
K L # # O K
L # # O K O
K # O L K O
K # O J L #
L O K # # #
```

### Step 4

Start: (3, 0), End: (3, 3), Sacrifice: (2, 5)

```
L O # K K #
K L # # O K
L # # O K #
# # # # K O
K # O J L #
L O K # # #
```

### Step 5

Start: (1, 1), End: (1, 5), Sacrifice: (4, 3)

```
L O # K K #
K # # # # #
L # # O K #
# # # # K O
K # O # L #
L O K # # #
```

### Step 6

Start: (2, 0), End: (2, 4), Sacrifice: (0, 3)

```
L O # # K #
K # # # # #
# # # # # #
# # # # K O
K # O # L #
L O K # # #
```

### Step 7

Start: (5, 0), End: (5, 2), Sacrifice: (3, 4)

```
L O # # K #
K # # # # #
# # # # # #
# # # # # O
K # O # L #
# # # # # #
```

### Step 8

Start: (4, 0), End: (4, 4), Sacrifice: (1, 0)

```
L O # # K #
# # # # # #
# # # # # #
# # # # # O
# # # # # #
# # # # # #
```

### Step 9

Start: (0, 0), End: (0, 4), Sacrifice: (3, 5)

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
J K K L K
O L O O O
K L O K L
O O L K L
L L O # O
```

## Solution

```
J K K L K
O L O O O
K L O K L
O O L K L
L L O # O
```

### Step 1

Start: (2, 0), End: (4, 0), Sacrifice: (1, 1)

```
J K K L K
O # O O O
# L O K L
# O L K L
# L O # O
```

### Step 2

Start: (0, 4), End: (2, 4), Sacrifice: (4, 4)

```
J K K L #
O # O O #
# L O K #
# O L K L
# L O # #
```

### Step 3

Start: (2, 1), End: (2, 3), Sacrifice: (3, 4)

```
J K K L #
O # O O #
# # # # #
# O L K #
# L O # #
```

### Step 4

Start: (0, 2), End: (3, 2), Sacrifice: (4, 2)

```
J K # L #
O # # O #
# # # # #
# O # K #
# L # # #
```

### Step 5

Start: (0, 3), End: (3, 3), Sacrifice: (0, 0)

```
# K # # #
O # # # #
# # # # #
# O # # #
# L # # #
```

### Step 6

Start: (0, 1), End: (4, 1), Sacrifice: (1, 0)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

---

