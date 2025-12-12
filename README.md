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
K L O K L
O K K L J
O O # O L
J L O K K
L L L O K
```

# Solution

```
K L O K L
O K K L J
O O # O L
J L O K K
L L L O K
```

## Move

Start: (0, 1), End: (0, 3), Sacrifice: (1, 2)

```
K # # # L
O K # L J
O O # O L
J L O K K
L L L O K
```

## Move

Start: (1, 3), End: (3, 3), Sacrifice: (2, 4)

```
K # # # L
O K # # J
O O # # #
J L O # K
L L L O K
```

## Move

Start: (4, 2), End: (4, 4), Sacrifice: (2, 0)

```
K # # # L
O K # # J
# O # # #
J L O # K
L L # # #
```

## Move

Start: (3, 1), End: (3, 4), Sacrifice: (3, 0)

```
K # # # L
O K # # J
# O # # #
# # # # #
L L # # #
```

## Move

Start: (0, 0), End: (4, 0), Sacrifice: (0, 4)

```
# # # # #
# K # # J
# O # # #
# # # # #
# L # # #
```

## Move

Start: (1, 1), End: (4, 1), Sacrifice: (1, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

