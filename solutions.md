# Puzzle Solutions

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Puzzle 1

## Generated Puzzle

```
L L K L L O K
L L O K L J L
L O K O O O O
O O K # K L K
K O O L O O K
J K L K O L O
K K O K J K L
```

## Solution

```
L L K L L O K
L L O K L J L
L O K O O O O
O O K # K L K
K O O L O O K
J K L K O L O
K K O K J K L
```

### Step 1

Start: (2, 0), End: (2, 2), Sacrifice: (6, 3)

```
L L K L L O K
L L O K L J L
# # # O O O O
O O K # K L K
K O O L O O K
J K L K O L O
K K O # J K L
```

### Step 2

Start: (3, 2), End: (5, 2), Sacrifice: (4, 1)

```
L L K L L O K
L L O K L J L
# # # O O O O
O O # # K L K
K # # L O O K
J K # K O L O
K K O # J K L
```

### Step 3

Start: (5, 3), End: (5, 5), Sacrifice: (1, 0)

```
L L K L L O K
# L O K L J L
# # # O O O O
O O # # K L K
K # # L O O K
J K # # # # O
K K O # J K L
```

### Step 4

Start: (3, 5), End: (6, 5), Sacrifice: (2, 3)

```
L L K L L O K
# L O K L J L
# # # # O O O
O O # # K # K
K # # L O # K
J K # # # # O
K K O # J # L
```

### Step 5

Start: (1, 6), End: (3, 6), Sacrifice: (5, 0)

```
L L K L L O K
# L O K L J #
# # # # O O #
O O # # K # #
K # # L O # K
# K # # # # O
K K O # J # L
```

### Step 6

Start: (0, 4), End: (0, 6), Sacrifice: (2, 5)

```
L L K L # # #
# L O K L J #
# # # # O # #
O O # # K # #
K # # L O # K
# K # # # # O
K K O # J # L
```

### Step 7

Start: (1, 1), End: (1, 3), Sacrifice: (0, 2)

```
L L # L # # #
# # # # L J #
# # # # O # #
O O # # K # #
K # # L O # K
# K # # # # O
K K O # J # L
```

### Step 8

Start: (0, 0), End: (4, 0), Sacrifice: (6, 4)

```
# L # L # # #
# # # # L J #
# # # # O # #
# O # # K # #
# # # L O # K
# K # # # # O
K K O # # # L
```

### Step 9

Start: (0, 1), End: (5, 1), Sacrifice: (6, 0)

```
# # # L # # #
# # # # L J #
# # # # O # #
# # # # K # #
# # # L O # K
# # # # # # O
# K O # # # L
```

### Step 10

Start: (4, 3), End: (4, 6), Sacrifice: (1, 5)

```
# # # L # # #
# # # # L # #
# # # # O # #
# # # # K # #
# # # # # # #
# # # # # # O
# K O # # # L
```

### Step 11

Start: (6, 1), End: (6, 6), Sacrifice: (0, 3)

```
# # # # # # #
# # # # L # #
# # # # O # #
# # # # K # #
# # # # # # #
# # # # # # O
# # # # # # #
```

### Step 12

Start: (1, 4), End: (3, 4), Sacrifice: (5, 6)

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
L L O K L
L O K O K
K O O L O
K O L J L
# K K O L
```

## Solution

```
L L O K L
L O K O K
K O O L O
K O L J L
# K K O L
```

### Step 1

Start: (4, 2), End: (4, 4), Sacrifice: (3, 3)

```
L L O K L
L O K O K
K O O L O
K O L # L
# K # # #
```

### Step 2

Start: (1, 0), End: (1, 2), Sacrifice: (2, 0)

```
L L O K L
# # # O K
# O O L O
K O L # L
# K # # #
```

### Step 3

Start: (3, 0), End: (3, 2), Sacrifice: (0, 2)

```
L L # K L
# # # O K
# O O L O
# # # # L
# K # # #
```

### Step 4

Start: (0, 1), End: (4, 1), Sacrifice: (2, 2)

```
L # # K L
# # # O K
# # # L O
# # # # L
# # # # #
```

### Step 5

Start: (1, 4), End: (3, 4), Sacrifice: (0, 4)

```
L # # K #
# # # O #
# # # L #
# # # # #
# # # # #
```

### Step 6

Start: (0, 3), End: (2, 3), Sacrifice: (0, 0)

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
K L O O O L
K O O L L K
L K K K O K
L K J O K O
O K O L L L
L O K K O L
```

## Solution

```
K L O O O L
K O O L L K
L K K K O K
L K J O K O
O K O L L L
L O K K O L
```

### Step 1

Start: (5, 0), End: (5, 2), Sacrifice: (3, 2)

```
K L O O O L
K O O L L K
L K K K O K
L K # O K O
O K O L L L
# # # K O L
```

### Step 2

Start: (0, 1), End: (2, 1), Sacrifice: (4, 0)

```
K # O O O L
K # O L L K
L # K K O K
L K # O K O
# K O L L L
# # # K O L
```

### Step 3

Start: (2, 3), End: (4, 3), Sacrifice: (2, 5)

```
K # O O O L
K # O L L K
L # K # O #
L K # # K O
# K O # L L
# # # K O L
```

### Step 4

Start: (1, 4), End: (3, 4), Sacrifice: (3, 1)

```
K # O O O L
K # O L # K
L # K # # #
L # # # # O
# K O # L L
# # # K O L
```

### Step 5

Start: (1, 5), End: (4, 5), Sacrifice: (3, 0)

```
K # O O O L
K # O L # #
L # K # # #
# # # # # #
# K O # L #
# # # K O L
```

### Step 6

Start: (5, 3), End: (5, 5), Sacrifice: (0, 4)

```
K # O O # L
K # O L # #
L # K # # #
# # # # # #
# K O # L #
# # # # # #
```

### Step 7

Start: (1, 0), End: (1, 3), Sacrifice: (0, 3)

```
K # O # # L
# # # # # #
L # K # # #
# # # # # #
# K O # L #
# # # # # #
```

### Step 8

Start: (0, 0), End: (0, 5), Sacrifice: (2, 2)

```
# # # # # #
# # # # # #
L # # # # #
# # # # # #
# K O # L #
# # # # # #
```

### Step 9

Start: (4, 1), End: (4, 4), Sacrifice: (2, 0)

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
L O K J L L
K O J L O K
O L L O K O
L O J L O K
O K O K O L
L L J O K K
```

## Solution

```
L O K J L L
K O J L O K
O L L O K O
L O J L O K
O K O K O L
L L J O K K
```

### Step 1

Start: (1, 3), End: (1, 5), Sacrifice: (4, 2)

```
L O K J L L
K O J # # #
O L L O K O
L O J L O K
O K # K O L
L L J O K K
```

### Step 2

Start: (4, 3), End: (4, 5), Sacrifice: (5, 2)

```
L O K J L L
K O J # # #
O L L O K O
L O J L O K
O K # # # #
L L # O K K
```

### Step 3

Start: (0, 0), End: (0, 2), Sacrifice: (3, 2)

```
# # # J L L
K O J # # #
O L L O K O
L O # L O K
O K # # # #
L L # O K K
```

### Step 4

Start: (2, 1), End: (4, 1), Sacrifice: (4, 0)

```
# # # J L L
K O J # # #
O # L O K O
L # # L O K
# # # # # #
L L # O K K
```

### Step 5

Start: (0, 5), End: (3, 5), Sacrifice: (1, 2)

```
# # # J L #
K O # # # #
O # L O K #
L # # L O #
# # # # # #
L L # O K K
```

### Step 6

Start: (2, 2), End: (2, 4), Sacrifice: (0, 3)

```
# # # # L #
K O # # # #
O # # # # #
L # # L O #
# # # # # #
L L # O K K
```

### Step 7

Start: (0, 4), End: (5, 4), Sacrifice: (3, 3)

```
# # # # # #
K O # # # #
O # # # # #
L # # # # #
# # # # # #
L L # O # K
```

### Step 8

Start: (5, 1), End: (5, 5), Sacrifice: (3, 0)

```
# # # # # #
K O # # # #
O # # # # #
# # # # # #
# # # # # #
L # # # # #
```

### Step 9

Start: (1, 0), End: (5, 0), Sacrifice: (1, 1)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

# Puzzle 5

## Generated Puzzle

```
L L O K L L L
L O O O O O K
L # K O L O K
L O K J K K O
O K O J O L L
K J L O K K O
J K L O K O L
```

## Solution

```
L L O K L L L
L O O O O O K
L # K O L O K
L O K J K K O
O K O J O L L
K J L O K K O
J K L O K O L
```

### Step 1

Start: (2, 2), End: (2, 4), Sacrifice: (4, 3)

```
L L O K L L L
L O O O O O K
L # # # # O K
L O K J K K O
O K O # O L L
K J L O K K O
J K L O K O L
```

### Step 2

Start: (3, 0), End: (3, 2), Sacrifice: (5, 1)

```
L L O K L L L
L O O O O O K
L # # # # O K
# # # J K K O
O K O # O L L
K # L O K K O
J K L O K O L
```

### Step 3

Start: (2, 6), End: (4, 6), Sacrifice: (1, 5)

```
L L O K L L L
L O O O O # K
L # # # # O #
# # # J K K #
O K O # O L #
K # L O K K O
J K L O K O L
```

### Step 4

Start: (0, 5), End: (3, 5), Sacrifice: (0, 1)

```
L # O K L # L
L O O O O # K
L # # # # # #
# # # J K # #
O K O # O L #
K # L O K K O
J K L O K O L
```

### Step 5

Start: (6, 2), End: (6, 4), Sacrifice: (4, 2)

```
L # O K L # L
L O O O O # K
L # # # # # #
# # # J K # #
O K # # O L #
K # L O K K O
J K # # # O L
```

### Step 6

Start: (0, 4), End: (3, 4), Sacrifice: (5, 6)

```
L # O K # # L
L O O O # # K
L # # # # # #
# # # J # # #
O K # # O L #
K # L O K K #
J K # # # O L
```

### Step 7

Start: (5, 2), End: (5, 4), Sacrifice: (3, 3)

```
L # O K # # L
L O O O # # K
L # # # # # #
# # # # # # #
O K # # O L #
K # # # # K #
J K # # # O L
```

### Step 8

Start: (6, 1), End: (6, 6), Sacrifice: (1, 1)

```
L # O K # # L
L # O O # # K
L # # # # # #
# # # # # # #
O K # # O L #
K # # # # K #
J # # # # # #
```

### Step 9

Start: (4, 1), End: (4, 5), Sacrifice: (1, 2)

```
L # O K # # L
L # # O # # K
L # # # # # #
# # # # # # #
O # # # # # #
K # # # # K #
J # # # # # #
```

### Step 10

Start: (0, 0), End: (0, 3), Sacrifice: (6, 0)

```
# # # # # # L
L # # O # # K
L # # # # # #
# # # # # # #
O # # # # # #
K # # # # K #
# # # # # # #
```

### Step 11

Start: (2, 0), End: (5, 0), Sacrifice: (0, 6)

```
# # # # # # #
L # # O # # K
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # K #
# # # # # # #
```

### Step 12

Start: (1, 0), End: (1, 6), Sacrifice: (5, 5)

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
L # K O L
L L O K L
O L J O O
J O L O K
K K J O K
```

## Solution

```
L # K O L
L L O K L
O L J O O
J O L O K
K K J O K
```

### Step 1

Start: (2, 1), End: (4, 1), Sacrifice: (4, 2)

```
L # K O L
L L O K L
O # J O O
J # L O K
K # # O K
```

### Step 2

Start: (3, 2), End: (3, 4), Sacrifice: (1, 0)

```
L # K O L
# L O K L
O # J O O
J # # # #
K # # O K
```

### Step 3

Start: (1, 4), End: (4, 4), Sacrifice: (4, 3)

```
L # K O L
# L O K #
O # J O #
J # # # #
K # # # #
```

### Step 4

Start: (1, 1), End: (1, 3), Sacrifice: (2, 3)

```
L # K O L
# # # # #
O # J # #
J # # # #
K # # # #
```

### Step 5

Start: (0, 2), End: (0, 4), Sacrifice: (3, 0)

```
L # # # #
# # # # #
O # J # #
# # # # #
K # # # #
```

### Step 6

Start: (0, 0), End: (4, 0), Sacrifice: (2, 2)

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
J L K K L J
J O L O O L
K K O L L O
O O K J O L
L L O K K O
L O K J K K
```

## Solution

```
J L K K L J
J O L O O L
K K O L L O
O O K J O L
L L O K K O
L O K J K K
```

### Step 1

Start: (2, 4), End: (4, 4), Sacrifice: (3, 1)

```
J L K K L J
J O L O O L
K K O L # O
O # K J # L
L L O K # O
L O K J K K
```

### Step 2

Start: (1, 2), End: (3, 2), Sacrifice: (0, 2)

```
J L # K L J
J O # O O L
K K # L # O
O # # J # L
L L O K # O
L O K J K K
```

### Step 3

Start: (4, 1), End: (4, 3), Sacrifice: (5, 3)

```
J L # K L J
J O # O O L
K K # L # O
O # # J # L
L # # # # O
L O K # K K
```

### Step 4

Start: (5, 0), End: (5, 2), Sacrifice: (2, 5)

```
J L # K L J
J O # O O L
K K # L # #
O # # J # L
L # # # # O
# # # # K K
```

### Step 5

Start: (3, 5), End: (5, 5), Sacrifice: (3, 3)

```
J L # K L J
J O # O O L
K K # L # #
O # # # # #
L # # # # #
# # # # K #
```

### Step 6

Start: (0, 1), End: (2, 1), Sacrifice: (1, 5)

```
J # # K L J
J # # O O #
K # # L # #
O # # # # #
L # # # # #
# # # # K #
```

### Step 7

Start: (0, 4), End: (5, 4), Sacrifice: (1, 0)

```
J # # K # J
# # # O # #
K # # L # #
O # # # # #
L # # # # #
# # # # # #
```

### Step 8

Start: (0, 3), End: (2, 3), Sacrifice: (0, 0)

```
# # # # # J
# # # # # #
K # # # # #
O # # # # #
L # # # # #
# # # # # #
```

### Step 9

Start: (2, 0), End: (4, 0), Sacrifice: (0, 5)

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
L L O K L
O L K O K
J L O J O
K O L L #
K K L O K
```

## Solution

```
L L O K L
O L K O K
J L O J O
K O L L #
K K L O K
```

### Step 1

Start: (1, 2), End: (3, 2), Sacrifice: (2, 4)

```
L L O K L
O L # O K
J L # J #
K O # L #
K K L O K
```

### Step 2

Start: (0, 1), End: (0, 3), Sacrifice: (2, 0)

```
L # # # L
O L # O K
# L # J #
K O # L #
K K L O K
```

### Step 3

Start: (4, 2), End: (4, 4), Sacrifice: (3, 3)

```
L # # # L
O L # O K
# L # J #
K O # # #
K K # # #
```

### Step 4

Start: (0, 0), End: (3, 0), Sacrifice: (4, 0)

```
# # # # L
# L # O K
# L # J #
# O # # #
# K # # #
```

### Step 5

Start: (2, 1), End: (4, 1), Sacrifice: (2, 3)

```
# # # # L
# L # O K
# # # # #
# # # # #
# # # # #
```

### Step 6

Start: (1, 1), End: (1, 4), Sacrifice: (0, 4)

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
L O L L K
J O J O K
L K O L O
O L O K L
K # L O K
```

## Solution

```
L O L L K
J O J O K
L K O L O
O L O K L
K # L O K
```

### Step 1

Start: (4, 2), End: (4, 4), Sacrifice: (0, 2)

```
L O # L K
J O J O K
L K O L O
O L O K L
K # # # #
```

### Step 2

Start: (2, 1), End: (2, 3), Sacrifice: (1, 3)

```
L O # L K
J O J # K
L # # # O
O L O K L
K # # # #
```

### Step 3

Start: (1, 4), End: (3, 4), Sacrifice: (1, 0)

```
L O # L K
# O J # #
L # # # #
O L O K #
K # # # #
```

### Step 4

Start: (2, 0), End: (4, 0), Sacrifice: (0, 3)

```
L O # # K
# O J # #
# # # # #
# L O K #
# # # # #
```

### Step 5

Start: (0, 0), End: (0, 4), Sacrifice: (1, 2)

```
# # # # #
# O # # #
# # # # #
# L O K #
# # # # #
```

### Step 6

Start: (3, 1), End: (3, 3), Sacrifice: (1, 1)

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
K K K O L L
L O L L K K
O J O O O O
K L K K L L
K K L O O K
K L L O K J
```

## Solution

```
K K K O L L
L O L L K K
O J O O O O
K L K K L L
K K L O O K
K L L O K J
```

### Step 1

Start: (1, 3), End: (3, 3), Sacrifice: (3, 1)

```
K K K O L L
L O L # K K
O J O # O O
K # K # L L
K K L O O K
K L L O K J
```

### Step 2

Start: (1, 4), End: (3, 4), Sacrifice: (5, 3)

```
K K K O L L
L O L # # K
O J O # # O
K # K # # L
K K L O O K
K L L # K J
```

### Step 3

Start: (1, 5), End: (3, 5), Sacrifice: (0, 0)

```
# K K O L L
L O L # # #
O J O # # #
K # K # # #
K K L O O K
K L L # K J
```

### Step 4

Start: (0, 4), End: (5, 4), Sacrifice: (4, 0)

```
# K K O # L
L O L # # #
O J O # # #
K # K # # #
# K L O # K
K L L # # J
```

### Step 5

Start: (4, 2), End: (4, 5), Sacrifice: (4, 1)

```
# K K O # L
L O L # # #
O J O # # #
K # K # # #
# # # # # #
K L L # # J
```

### Step 6

Start: (0, 2), End: (0, 5), Sacrifice: (5, 2)

```
# K # # # #
L O L # # #
O J O # # #
K # K # # #
# # # # # #
K L # # # J
```

### Step 7

Start: (1, 2), End: (3, 2), Sacrifice: (2, 1)

```
# K # # # #
L O # # # #
O # # # # #
K # # # # #
# # # # # #
K L # # # J
```

### Step 8

Start: (1, 0), End: (3, 0), Sacrifice: (5, 0)

```
# K # # # #
# O # # # #
# # # # # #
# # # # # #
# # # # # #
# L # # # J
```

### Step 9

Start: (0, 1), End: (5, 1), Sacrifice: (5, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

---

