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
K K L L O K K
K K O L K O L
K O L O K J J
O L K K L O K
K O L J L O K
L # K O L O K
L O K L O L K
```

# Solution

```
K K L L O K K
K K O L K O L
K O L O K J J
O L K K L O K
K O L J L O K
L # K O L O K
L O K L O L K
```

## Move

Start: (5, 4), End: (5, 6), Sacrifice: (0, 6)

```
K K L L O K #
K K O L K O L
K O L O K J J
O L K K L O K
K O L J L O K
L # K O # # #
L O K L O L K
```

## Move

Start: (1, 3), End: (3, 3), Sacrifice: (6, 3)

```
K K L L O K #
K K O # K O L
K O L # K J J
O L K # L O K
K O L J L O K
L # K O # # #
L O K # O L K
```

## Move

Start: (1, 4), End: (1, 6), Sacrifice: (2, 5)

```
K K L L O K #
K K O # # # #
K O L # K # J
O L K # L O K
K O L J L O K
L # K O # # #
L O K # O L K
```

## Move

Start: (6, 2), End: (6, 5), Sacrifice: (4, 3)

```
K K L L O K #
K K O # # # #
K O L # K # J
O L K # L O K
K O L # L O K
L # K O # # #
L O # # # # K
```

## Move

Start: (6, 0), End: (6, 6), Sacrifice: (1, 0)

```
K K L L O K #
# K O # # # #
K O L # K # J
O L K # L O K
K O L # L O K
L # K O # # #
# # # # # # #
```

## Move

Start: (3, 4), End: (3, 6), Sacrifice: (1, 1)

```
K K L L O K #
# # O # # # #
K O L # K # J
O L K # # # #
K O L # L O K
L # K O # # #
# # # # # # #
```

## Move

Start: (4, 4), End: (4, 6), Sacrifice: (3, 2)

```
K K L L O K #
# # O # # # #
K O L # K # J
O L # # # # #
K O L # # # #
L # K O # # #
# # # # # # #
```

## Move

Start: (4, 0), End: (4, 2), Sacrifice: (2, 0)

```
K K L L O K #
# # O # # # #
# O L # K # J
O L # # # # #
# # # # # # #
L # K O # # #
# # # # # # #
```

## Move

Start: (0, 1), End: (3, 1), Sacrifice: (2, 2)

```
K # L L O K #
# # O # # # #
# # # # K # J
O # # # # # #
# # # # # # #
L # K O # # #
# # # # # # #
```

## Move

Start: (0, 2), End: (5, 2), Sacrifice: (5, 3)

```
K # # L O K #
# # # # # # #
# # # # K # J
O # # # # # #
# # # # # # #
L # # # # # #
# # # # # # #
```

## Move

Start: (0, 0), End: (5, 0), Sacrifice: (2, 4)

```
# # # L O K #
# # # # # # #
# # # # # # J
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

## Move

Start: (0, 3), End: (0, 5), Sacrifice: (2, 6)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

