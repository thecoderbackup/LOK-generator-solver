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
L K O K L L #
O K O L L O K
K J L K K O L
L K O K O K J
L L K O K O K
O O J K J O L
L L K O L K J
```

# Solution

```
L K O K L L #
O K O L L O K
K J L K K O L
L K O K O K J
L L K O K O K
O O J K J O L
L L K O L K J
```

## Move

Start: (2, 2), End: (4, 2), Sacrifice: (0, 3)

```
L K O # L L #
O K O L L O K
K J # K K O L
L K # K O K J
L L # O K O K
O O J K J O L
L L K O L K J
```

## Move

Start: (6, 2), End: (6, 4), Sacrifice: (1, 0)

```
L K O # L L #
# K O L L O K
K J # K K O L
L K # K O K J
L L # O K O K
O O J K J O L
L L # # # K J
```

## Move

Start: (4, 1), End: (4, 4), Sacrifice: (6, 6)

```
L K O # L L #
# K O L L O K
K J # K K O L
L K # K O K J
L # # # # O K
O O J K J O L
L L # # # K #
```

## Move

Start: (1, 4), End: (1, 6), Sacrifice: (5, 3)

```
L K O # L L #
# K O L # # #
K J # K K O L
L K # K O K J
L # # # # O K
O O J # J O L
L L # # # K #
```

## Move

Start: (0, 1), End: (0, 4), Sacrifice: (5, 4)

```
L # # # # L #
# K O L # # #
K J # K K O L
L K # K O K J
L # # # # O K
O O J # # O L
L L # # # K #
```

## Move

Start: (2, 4), End: (2, 6), Sacrifice: (2, 1)

```
L # # # # L #
# K O L # # #
K # # K # # #
L K # K O K J
L # # # # O K
O O J # # O L
L L # # # K #
```

## Move

Start: (4, 0), End: (4, 6), Sacrifice: (0, 0)

```
# # # # # L #
# K O L # # #
K # # K # # #
L K # K O K J
# # # # # # #
O O J # # O L
L L # # # K #
```

## Move

Start: (3, 1), End: (6, 1), Sacrifice: (3, 3)

```
# # # # # L #
# K O L # # #
K # # K # # #
L # # # O K J
# # # # # # #
O # J # # O L
L # # # # K #
```

## Move

Start: (3, 0), End: (3, 5), Sacrifice: (2, 3)

```
# # # # # L #
# K O L # # #
K # # # # # #
# # # # # # J
# # # # # # #
O # J # # O L
L # # # # K #
```

## Move

Start: (1, 1), End: (1, 3), Sacrifice: (5, 6)

```
# # # # # L #
# # # # # # #
K # # # # # #
# # # # # # J
# # # # # # #
O # J # # O #
L # # # # K #
```

## Move

Start: (0, 5), End: (6, 5), Sacrifice: (5, 2)

```
# # # # # # #
# # # # # # #
K # # # # # #
# # # # # # J
# # # # # # #
O # # # # # #
L # # # # # #
```

## Move

Start: (2, 0), End: (6, 0), Sacrifice: (3, 6)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

