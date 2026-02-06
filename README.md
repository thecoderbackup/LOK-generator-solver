# LOK Based Puzzle Generator

This puzzle generator is inspired by the puzzle book "LOK" created by Blaž Urban Gracar under Letibus Design, and its digital adaptation "LOK Digital" developed by Icedrop Games in collaboration with Raindrinker and published by Draknek & Friends.

In the original LOK, players engage in mind-bending word-search puzzles where the goal is to find keywords with special effects to black out all cells in a grid. The digital version expands this with procedural puzzles and new mechanics.

References:
- Original LOK puzzle book: [Blaž Urban Gracar's site](https://www.blazgracar.com/lok) and [Itch.io](https://letibus.itch.io/lok)
- LOK Digital: [Official site](https://lok-digital.com/), [Steam](https://store.steampowered.com/app/2207440/LOK_Digital/), [Google Play](https://play.google.com/store/apps/details?id=com.IcedropGames.LOK), [App Store](https://apps.apple.com/us/app/lok-digital/id6476513210)

## Game Description

Given a board, you must transform all symbols into #. To do this, find the word "LOK", which can be horizontal or vertical, and also backwards (i.e., "KOL" is also valid!). Every time you find a word, you must sacrifice a letter and transform it into # as well.

If there is a # in the middle of the word, you can ignore it, i.e., L#OK is also a valid word.

Your goal is to transform the entire board into #.

Remember that if you transform the entire board and have pending sacrifices, it means it is not a valid solution!

# Generated Puzzle

```
K # K O L J L
K K L O O K L
O O K J J L J
L L O O K O K
K K L O L K O
O K O L L O K
L L O O O K L
```

# Solution

```
K # K O L J L
K K L O O K L
O O K J J L J
L L O O K O K
K K L O L K O
O K O L L O K
L L O O O K L
```

## Move

Start: (4, 0), End: (6, 0), Sacrifice: (0, 4)

```
K # K O # J L
K K L O O K L
O O K J J L J
L L O O K O K
# K L O L K O
# K O L L O K
# L O O O K L
```

## Move

Start: (5, 4), End: (5, 6), Sacrifice: (1, 4)

```
K # K O # J L
K K L O # K L
O O K J J L J
L L O O K O K
# K L O L K O
# K O L # # #
# L O O O K L
```

## Move

Start: (2, 2), End: (4, 2), Sacrifice: (0, 5)

```
K # K O # # L
K K L O # K L
O O # J J L J
L L # O K O K
# K # O L K O
# K O L # # #
# L O O O K L
```

## Move

Start: (3, 6), End: (6, 6), Sacrifice: (6, 4)

```
K # K O # # L
K K L O # K L
O O # J J L J
L L # O K O #
# K # O L K #
# K O L # # #
# L O O # K #
```

## Move

Start: (0, 2), End: (0, 6), Sacrifice: (0, 0)

```
# # # # # # #
K K L O # K L
O O # J J L J
L L # O K O #
# K # O L K #
# K O L # # #
# L O O # K #
```

## Move

Start: (3, 1), End: (3, 4), Sacrifice: (2, 3)

```
# # # # # # #
K K L O # K L
O O # # J L J
L # # # # O #
# K # O L K #
# K O L # # #
# L O O # K #
```

## Move

Start: (4, 1), End: (4, 4), Sacrifice: (2, 4)

```
# # # # # # #
K K L O # K L
O O # # # L J
L # # # # O #
# # # # # K #
# K O L # # #
# L O O # K #
```

## Move

Start: (5, 1), End: (5, 3), Sacrifice: (1, 2)

```
# # # # # # #
K K # O # K L
O O # # # L J
L # # # # O #
# # # # # K #
# # # # # # #
# L O O # K #
```

## Move

Start: (1, 0), End: (3, 0), Sacrifice: (2, 1)

```
# # # # # # #
# K # O # K L
# # # # # L J
# # # # # O #
# # # # # K #
# # # # # # #
# L O O # K #
```

## Move

Start: (2, 5), End: (4, 5), Sacrifice: (1, 5)

```
# # # # # # #
# K # O # # L
# # # # # # J
# # # # # # #
# # # # # # #
# # # # # # #
# L O O # K #
```

## Move

Start: (1, 1), End: (1, 6), Sacrifice: (6, 2)

```
# # # # # # #
# # # # # # #
# # # # # # J
# # # # # # #
# # # # # # #
# # # # # # #
# L # O # K #
```

## Move

Start: (6, 1), End: (6, 5), Sacrifice: (2, 6)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

