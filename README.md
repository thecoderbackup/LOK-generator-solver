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
L J K O O L L
O K K L O K O
K J O J K L K
K L K L O O K
O O O O K K O
K K L K L K L
L # L L K O K
```

# Solution

```
L J K O O L L
O K K L O K O
K J O J K L K
K L K L O O K
O O O O K K O
K K L K L K L
L # L L K O K
```

## Move

Start: (3, 6), End: (5, 6), Sacrifice: (0, 1)

```
L # K O O L L
O K K L O K O
K J O J K L K
K L K L O O #
O O O O K K #
K K L K L K #
L # L L K O K
```

## Move

Start: (3, 2), End: (5, 2), Sacrifice: (0, 3)

```
L # K # O L L
O K K L O K O
K J O J K L K
K L # L O O #
O O # O K K #
K K # K L K #
L # L L K O K
```

## Move

Start: (1, 3), End: (1, 5), Sacrifice: (4, 4)

```
L # K # O L L
O K K # # # O
K J O J K L K
K L # L O O #
O O # O # K #
K K # K L K #
L # L L K O K
```

## Move

Start: (1, 2), End: (6, 2), Sacrifice: (6, 5)

```
L # K # O L L
O K # # # # O
K J # J K L K
K L # L O O #
O O # O # K #
K K # K L K #
L # # L K # K
```

## Move

Start: (0, 2), End: (0, 5), Sacrifice: (5, 0)

```
L # # # # # L
O K # # # # O
K J # J K L K
K L # L O O #
O O # O # K #
# K # K L K #
L # # L K # K
```

## Move

Start: (3, 0), End: (6, 0), Sacrifice: (6, 6)

```
L # # # # # L
O K # # # # O
K J # J K L K
# L # L O O #
# O # O # K #
# K # K L K #
# # # L K # #
```

## Move

Start: (3, 1), End: (5, 1), Sacrifice: (5, 5)

```
L # # # # # L
O K # # # # O
K J # J K L K
# # # L O O #
# # # O # K #
# # # K L # #
# # # L K # #
```

## Move

Start: (2, 5), End: (4, 5), Sacrifice: (1, 1)

```
L # # # # # L
O # # # # # O
K J # J K # K
# # # L O # #
# # # O # # #
# # # K L # #
# # # L K # #
```

## Move

Start: (0, 0), End: (2, 0), Sacrifice: (6, 3)

```
# # # # # # L
# # # # # # O
# J # J K # K
# # # L O # #
# # # O # # #
# # # K L # #
# # # # K # #
```

## Move

Start: (2, 4), End: (5, 4), Sacrifice: (6, 4)

```
# # # # # # L
# # # # # # O
# J # J # # K
# # # L # # #
# # # O # # #
# # # K # # #
# # # # # # #
```

## Move

Start: (3, 3), End: (5, 3), Sacrifice: (2, 3)

```
# # # # # # L
# # # # # # O
# J # # # # K
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

## Move

Start: (0, 6), End: (2, 6), Sacrifice: (2, 1)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

