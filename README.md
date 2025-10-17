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
K J K O K L
O K K L O K
L K O J L L
K K L K O L
O O J L O K
L L J L O K
```

# Solution

```
K J K O K L
O K K L O K
L K O J L L
K K L K O L
O O J L O K
L L J L O K
```

## Move

Start: (0, 4), End: (2, 4), Sacrifice: (2, 3)

```
K J K O # L
O K K L # K
L K O # # L
K K L K O L
O O J L O K
L L J L O K
```

## Move

Start: (5, 3), End: (5, 5), Sacrifice: (3, 2)

```
K J K O # L
O K K L # K
L K O # # L
K K # K O L
O O J L O K
L L J # # #
```

## Move

Start: (2, 1), End: (2, 5), Sacrifice: (3, 3)

```
K J K O # L
O K K L # K
L # # # # #
K K # # O L
O O J L O K
L L J # # #
```

## Move

Start: (3, 1), End: (3, 5), Sacrifice: (1, 3)

```
K J K O # L
O K K # # K
L # # # # #
K # # # # #
O O J L O K
L L J # # #
```

## Move

Start: (4, 3), End: (4, 5), Sacrifice: (1, 5)

```
K J K O # L
O K K # # #
L # # # # #
K # # # # #
O O J # # #
L L J # # #
```

## Move

Start: (3, 0), End: (5, 0), Sacrifice: (0, 1)

```
K # K O # L
O K K # # #
L # # # # #
# # # # # #
# O J # # #
# L J # # #
```

## Move

Start: (1, 1), End: (5, 1), Sacrifice: (1, 2)

```
K # K O # L
O # # # # #
L # # # # #
# # # # # #
# # J # # #
# # J # # #
```

## Move

Start: (0, 2), End: (0, 5), Sacrifice: (4, 2)

```
K # # # # #
O # # # # #
L # # # # #
# # # # # #
# # # # # #
# # J # # #
```

## Move

Start: (0, 0), End: (2, 0), Sacrifice: (5, 2)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

