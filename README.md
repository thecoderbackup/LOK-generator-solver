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
L L O K L J #
L K K L O L K
K O O O L O L
O L L L O K J
O O K K J K O
O K O O J O J
K J L L K L K
```

# Solution

```
L L O K L J #
L K K L O L K
K O O O L O L
O L L L O K J
O O K K J K O
O K O O J O J
K J L L K L K
```

## Move

Start: (4, 2), End: (6, 2), Sacrifice: (2, 3)

```
L L O K L J #
L K K L O L K
K O O # L O L
O L L L O K J
O O # K J K O
O K # O J O J
K J # L K L K
```

## Move

Start: (1, 1), End: (3, 1), Sacrifice: (5, 4)

```
L L O K L J #
L # K L O L K
K # O # L O L
O # L L O K J
O O # K J K O
O K # O # O J
K J # L K L K
```

## Move

Start: (4, 5), End: (6, 5), Sacrifice: (0, 5)

```
L L O K L # #
L # K L O L K
K # O # L O L
O # L L O K J
O O # K J # O
O K # O # # J
K J # L K # K
```

## Move

Start: (0, 1), End: (5, 1), Sacrifice: (3, 0)

```
L # O K L # #
L # K L O L K
K # O # L O L
# # L L O K J
O # # K J # O
O # # O # # J
K J # L K # K
```

## Move

Start: (4, 3), End: (6, 3), Sacrifice: (5, 0)

```
L # O K L # #
L # K L O L K
K # O # L O L
# # L L O K J
O # # # J # O
# # # # # # J
K J # # K # K
```

## Move

Start: (1, 5), End: (3, 5), Sacrifice: (2, 0)

```
L # O K L # #
L # K L O # K
# # O # L # L
# # L L O # J
O # # # J # O
# # # # # # J
K J # # K # K
```

## Move

Start: (1, 2), End: (3, 2), Sacrifice: (4, 4)

```
L # O K L # #
L # # L O # K
# # # # L # L
# # # L O # J
O # # # # # O
# # # # # # J
K J # # K # K
```

## Move

Start: (1, 0), End: (6, 0), Sacrifice: (0, 4)

```
L # O K # # #
# # # L O # K
# # # # L # L
# # # L O # J
# # # # # # O
# # # # # # J
# J # # K # K
```

## Move

Start: (0, 0), End: (0, 3), Sacrifice: (3, 6)

```
# # # # # # #
# # # L O # K
# # # # L # L
# # # L O # #
# # # # # # O
# # # # # # J
# J # # K # K
```

## Move

Start: (1, 3), End: (1, 6), Sacrifice: (5, 6)

```
# # # # # # #
# # # # # # #
# # # # L # L
# # # L O # #
# # # # # # O
# # # # # # #
# J # # K # K
```

## Move

Start: (2, 4), End: (6, 4), Sacrifice: (3, 3)

```
# # # # # # #
# # # # # # #
# # # # # # L
# # # # # # #
# # # # # # O
# # # # # # #
# J # # # # K
```

## Move

Start: (2, 6), End: (6, 6), Sacrifice: (6, 1)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

