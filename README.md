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
L O K L J L L
L L K O L O O
O L O K K K K
K O O K O O O
# O L L L L O
O K K O O K L
L K O K K K J
```

# Solution

```
L O K L J L L
L L K O L O O
O L O K K K K
K O O K O O O
# O L L L L O
O K K O O K L
L K O K K K J
```

## Move

Start: (0, 0), End: (0, 2), Sacrifice: (3, 2)

```
# # # L J L L
L L K O L O O
O L O K K K K
K O # K O O O
# O L L L L O
O K K O O K L
L K O K K K J
```

## Move

Start: (2, 5), End: (4, 5), Sacrifice: (0, 4)

```
# # # L # L L
L L K O L O O
O L O K K # K
K O # K O # O
# O L L L # O
O K K O O K L
L K O K K K J
```

## Move

Start: (0, 5), End: (5, 5), Sacrifice: (6, 6)

```
# # # L # # L
L L K O L # O
O L O K K # K
K O # K O # O
# O L L L # O
O K K O O # L
L K O K K K #
```

## Move

Start: (2, 4), End: (4, 4), Sacrifice: (6, 1)

```
# # # L # # L
L L K O L # O
O L O K # # K
K O # K # # O
# O L L # # O
O K K O O # L
L # O K K K #
```

## Move

Start: (1, 4), End: (6, 4), Sacrifice: (2, 3)

```
# # # L # # L
L L K O # # O
O L O # # # K
K O # K # # O
# O L L # # O
O K K O # # L
L # O K # K #
```

## Move

Start: (1, 2), End: (4, 2), Sacrifice: (4, 1)

```
# # # L # # L
L L # O # # O
O L # # # # K
K O # K # # O
# # # L # # O
O K K O # # L
L # O K # K #
```

## Move

Start: (6, 0), End: (6, 3), Sacrifice: (6, 5)

```
# # # L # # L
L L # O # # O
O L # # # # K
K O # K # # O
# # # L # # O
O K K O # # L
# # # # # # #
```

## Move

Start: (0, 6), End: (2, 6), Sacrifice: (1, 1)

```
# # # L # # #
L # # O # # #
O L # # # # #
K O # K # # O
# # # L # # O
O K K O # # L
# # # # # # #
```

## Move

Start: (1, 0), End: (3, 0), Sacrifice: (5, 0)

```
# # # L # # #
# # # O # # #
# L # # # # #
# O # K # # O
# # # L # # O
# K K O # # L
# # # # # # #
```

## Move

Start: (5, 2), End: (5, 6), Sacrifice: (4, 3)

```
# # # L # # #
# # # O # # #
# L # # # # #
# O # K # # O
# # # # # # O
# K # # # # #
# # # # # # #
```

## Move

Start: (2, 1), End: (5, 1), Sacrifice: (3, 6)

```
# # # L # # #
# # # O # # #
# # # # # # #
# # # K # # #
# # # # # # O
# # # # # # #
# # # # # # #
```

## Move

Start: (0, 3), End: (3, 3), Sacrifice: (4, 6)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

