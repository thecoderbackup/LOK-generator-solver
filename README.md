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
L O L K J K L
K K O L # L O
L L K O K O K
O O O J L O K
O L L L J O K
L O K K K K O
K O L O K K L
```

# Solution

```
L O L K J K L
K K O L # L O
L L K O K O K
O O O J L O K
O L L L J O K
L O K K K K O
K O L O K K L
```

## Move

Start: (2, 2), End: (4, 2), Sacrifice: (4, 3)

```
L O L K J K L
K K O L # L O
L L # O K O K
O O # J L O K
O L # # J O K
L O K K K K O
K O L O K K L
```

## Move

Start: (0, 2), End: (5, 2), Sacrifice: (3, 3)

```
L O # K J K L
K K # L # L O
L L # O K O K
O O # # L O K
O L # # J O K
L O # K K K O
K O L O K K L
```

## Move

Start: (4, 6), End: (6, 6), Sacrifice: (1, 0)

```
L O # K J K L
# K # L # L O
L L # O K O K
O O # # L O K
O L # # J O #
L O # K K K #
K O L O K K #
```

## Move

Start: (6, 2), End: (6, 4), Sacrifice: (5, 5)

```
L O # K J K L
# K # L # L O
L L # O K O K
O O # # L O K
O L # # J O #
L O # K K # #
K O # # # K #
```

## Move

Start: (3, 4), End: (3, 6), Sacrifice: (4, 0)

```
L O # K J K L
# K # L # L O
L L # O K O K
O O # # # # #
# L # # J O #
L O # K K # #
K O # # # K #
```

## Move

Start: (0, 0), End: (0, 3), Sacrifice: (2, 5)

```
# # # # J K L
# K # L # L O
L L # O K # K
O O # # # # #
# L # # J O #
L O # K K # #
K O # # # K #
```

## Move

Start: (2, 1), End: (2, 4), Sacrifice: (1, 3)

```
# # # # J K L
# K # # # L O
L # # # # # K
O O # # # # #
# L # # J O #
L O # K K # #
K O # # # K #
```

## Move

Start: (1, 5), End: (6, 5), Sacrifice: (5, 4)

```
# # # # J K L
# K # # # # O
L # # # # # K
O O # # # # #
# L # # J # #
L O # K # # #
K O # # # # #
```

## Move

Start: (1, 1), End: (4, 1), Sacrifice: (0, 4)

```
# # # # # K L
# # # # # # O
L # # # # # K
O # # # # # #
# # # # J # #
L O # K # # #
K O # # # # #
```

## Move

Start: (5, 0), End: (5, 3), Sacrifice: (4, 4)

```
# # # # # K L
# # # # # # O
L # # # # # K
O # # # # # #
# # # # # # #
# # # # # # #
K O # # # # #
```

## Move

Start: (2, 0), End: (6, 0), Sacrifice: (0, 5)

```
# # # # # # L
# # # # # # O
# # # # # # K
# # # # # # #
# # # # # # #
# # # # # # #
# O # # # # #
```

## Move

Start: (0, 6), End: (2, 6), Sacrifice: (6, 1)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

