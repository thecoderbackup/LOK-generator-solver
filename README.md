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
L O K K K O L
L K K L O K O
K O O L O L K
O K K O O L K
L L L K K O O
L O K O L O L
K J K L J K #
```

# Solution

```
L O K K K O L
L K K L O K O
K O O L O L K
O K K O O L K
L L L K K O O
L O K O L O L
K J K L J K #
```

## Move

Start: (5, 0), End: (5, 2), Sacrifice: (6, 1)

```
L O K K K O L
L K K L O K O
K O O L O L K
O K K O O L K
L L L K K O O
# # # O L O L
K # K L J K #
```

## Move

Start: (2, 3), End: (4, 3), Sacrifice: (6, 4)

```
L O K K K O L
L K K L O K O
K O O # O L K
O K K # O L K
L L L # K O O
# # # O L O L
K # K L # K #
```

## Move

Start: (0, 4), End: (0, 6), Sacrifice: (2, 4)

```
L O K K # # #
L K K L O K O
K O O # # L K
O K K # O L K
L L L # K O O
# # # O L O L
K # K L # K #
```

## Move

Start: (1, 3), End: (1, 5), Sacrifice: (1, 6)

```
L O K K # # #
L K K # # # #
K O O # # L K
O K K # O L K
L L L # K O O
# # # O L O L
K # K L # K #
```

## Move

Start: (3, 2), End: (3, 5), Sacrifice: (2, 6)

```
L O K K # # #
L K K # # # #
K O O # # L #
O K # # # # K
L L L # K O O
# # # O L O L
K # K L # K #
```

## Move

Start: (2, 0), End: (4, 0), Sacrifice: (6, 0)

```
L O K K # # #
L K K # # # #
# O O # # L #
# K # # # # K
# L L # K O O
# # # O L O L
# # K L # K #
```

## Move

Start: (1, 2), End: (4, 2), Sacrifice: (4, 5)

```
L O K K # # #
L K # # # # #
# O # # # L #
# K # # # # K
# L # # K # O
# # # O L O L
# # K L # K #
```

## Move

Start: (3, 6), End: (5, 6), Sacrifice: (6, 2)

```
L O K K # # #
L K # # # # #
# O # # # L #
# K # # # # #
# L # # K # #
# # # O L O #
# # # L # K #
```

## Move

Start: (0, 0), End: (0, 2), Sacrifice: (4, 4)

```
# # # K # # #
L K # # # # #
# O # # # L #
# K # # # # #
# L # # # # #
# # # O L O #
# # # L # K #
```

## Move

Start: (0, 3), End: (6, 3), Sacrifice: (3, 1)

```
# # # # # # #
L K # # # # #
# O # # # L #
# # # # # # #
# L # # # # #
# # # # L O #
# # # # # K #
```

## Move

Start: (2, 5), End: (6, 5), Sacrifice: (5, 4)

```
# # # # # # #
L K # # # # #
# O # # # # #
# # # # # # #
# L # # # # #
# # # # # # #
# # # # # # #
```

## Move

Start: (1, 1), End: (4, 1), Sacrifice: (1, 0)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

