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
L L K O L L L
# O K J O K O
K K O K J K O
K O L O K L K
O K O L O O K
K O L L L L O
L O L O K O L
```

# Solution

```
L L K O L L L
# O K J O K O
K K O K J K O
K O L O K L K
O K O L O O K
K O L L L L O
L O L O K O L
```

## Move

Start: (3, 4), End: (5, 4), Sacrifice: (3, 5)

```
L L K O L L L
# O K J O K O
K K O K J K O
K O L O # # K
O K O L # O K
K O L L # L O
L O L O K O L
```

## Move

Start: (4, 1), End: (4, 3), Sacrifice: (6, 5)

```
L L K O L L L
# O K J O K O
K K O K J K O
K O L O # # K
O # # # # O K
K O L L # L O
L O L O K # L
```

## Move

Start: (0, 1), End: (2, 1), Sacrifice: (3, 2)

```
L # K O L L L
# # K J O K O
K # O K J K O
K O # O # # K
O # # # # O K
K O L L # L O
L O L O K # L
```

## Move

Start: (5, 0), End: (5, 2), Sacrifice: (0, 0)

```
# # K O L L L
# # K J O K O
K # O K J K O
K O # O # # K
O # # # # O K
# # # L # L O
L O L O K # L
```

## Move

Start: (2, 5), End: (5, 5), Sacrifice: (6, 1)

```
# # K O L L L
# # K J O K O
K # O K J # O
K O # O # # K
O # # # # # K
# # # L # # O
L # L O K # L
```

## Move

Start: (2, 3), End: (5, 3), Sacrifice: (3, 1)

```
# # K O L L L
# # K J O K O
K # O # J # O
K # # # # # K
O # # # # # K
# # # # # # O
L # L O K # L
```

## Move

Start: (1, 2), End: (6, 2), Sacrifice: (1, 5)

```
# # K O L L L
# # # J O # O
K # # # J # O
K # # # # # K
O # # # # # K
# # # # # # O
L # # O K # L
```

## Move

Start: (4, 6), End: (6, 6), Sacrifice: (1, 3)

```
# # K O L L L
# # # # O # O
K # # # J # O
K # # # # # K
O # # # # # #
# # # # # # #
L # # O K # #
```

## Move

Start: (3, 0), End: (6, 0), Sacrifice: (2, 4)

```
# # K O L L L
# # # # O # O
K # # # # # O
# # # # # # K
# # # # # # #
# # # # # # #
# # # O K # #
```

## Move

Start: (0, 4), End: (6, 4), Sacrifice: (1, 6)

```
# # K O # L L
# # # # # # #
K # # # # # O
# # # # # # K
# # # # # # #
# # # # # # #
# # # O # # #
```

## Move

Start: (0, 6), End: (3, 6), Sacrifice: (2, 0)

```
# # K O # L #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # O # # #
```

## Move

Start: (0, 2), End: (0, 5), Sacrifice: (6, 3)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

