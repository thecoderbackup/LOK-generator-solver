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
K J L J K O L
K K O O L J L
L K K O O K L
O O K K O K L
L O K L O K K
L J K J # O O
L L O J K L L
```

# Solution

```
K J L J K O L
K K O O L J L
L K K O O K L
O O K K O K L
L O K L O K K
L J K J # O O
L L O J K L L
```

## Move

Start: (4, 3), End: (4, 5), Sacrifice: (0, 3)

```
K J L # K O L
K K O O L J L
L K K O O K L
O O K K O K L
L O K # # # K
L J K J # O O
L L O J K L L
```

## Move

Start: (4, 0), End: (4, 2), Sacrifice: (5, 1)

```
K J L # K O L
K K O O L J L
L K K O O K L
O O K K O K L
# # # # # # K
L # K J # O O
L L O J K L L
```

## Move

Start: (2, 1), End: (6, 1), Sacrifice: (1, 6)

```
K J L # K O L
K K O O L J #
L # K O O K L
O # K K O K L
# # # # # # K
L # K J # O O
L # O J K L L
```

## Move

Start: (0, 2), End: (2, 2), Sacrifice: (2, 3)

```
K J # # K O L
K K # O L J #
L # # # O K L
O # K K O K L
# # # # # # K
L # K J # O O
L # O J K L L
```

## Move

Start: (0, 4), End: (0, 6), Sacrifice: (3, 3)

```
K J # # # # #
K K # O L J #
L # # # O K L
O # K # O K L
# # # # # # K
L # K J # O O
L # O J K L L
```

## Move

Start: (4, 6), End: (6, 6), Sacrifice: (6, 3)

```
K J # # # # #
K K # O L J #
L # # # O K L
O # K # O K L
# # # # # # #
L # K J # O #
L # O # K L #
```

## Move

Start: (3, 5), End: (6, 5), Sacrifice: (5, 2)

```
K J # # # # #
K K # O L J #
L # # # O K L
O # K # O # L
# # # # # # #
L # # J # # #
L # O # K # #
```

## Move

Start: (2, 0), End: (2, 5), Sacrifice: (0, 0)

```
# J # # # # #
K K # O L J #
# # # # # # L
O # K # O # L
# # # # # # #
L # # J # # #
L # O # K # #
```

## Move

Start: (3, 2), End: (3, 6), Sacrifice: (1, 5)

```
# J # # # # #
K K # O L # #
# # # # # # L
O # # # # # #
# # # # # # #
L # # J # # #
L # O # K # #
```

## Move

Start: (6, 0), End: (6, 4), Sacrifice: (2, 6)

```
# J # # # # #
K K # O L # #
# # # # # # #
O # # # # # #
# # # # # # #
L # # J # # #
# # # # # # #
```

## Move

Start: (1, 1), End: (1, 4), Sacrifice: (5, 3)

```
# J # # # # #
K # # # # # #
# # # # # # #
O # # # # # #
# # # # # # #
L # # # # # #
# # # # # # #
```

## Move

Start: (1, 0), End: (5, 0), Sacrifice: (0, 1)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

