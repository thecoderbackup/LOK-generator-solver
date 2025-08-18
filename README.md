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
K # L K L O K
J J K O K L L
K K O K L O O
J L K O O L O
O O O L K O K
L L O K L K J
K K L L O K J
```

# Solution

```
K # L K L O K
J J K O K L L
K K O K L O O
J L K O O L O
O O O L K O K
L L O K L K J
K K L L O K J
```

## Move

Start: (3, 5), End: (5, 5), Sacrifice: (1, 0)

```
K # L K L O K
# J K O K L L
K K O K L O O
J L K O O # O
O O O L K # K
L L O K L # J
K K L L O K J
```

## Move

Start: (2, 3), End: (4, 3), Sacrifice: (2, 6)

```
K # L K L O K
# J K O K L L
K K O # L O #
J L K # O # O
O O O # K # K
L L O K L # J
K K L L O K J
```

## Move

Start: (1, 6), End: (4, 6), Sacrifice: (3, 0)

```
K # L K L O K
# J K O K L #
K K O # L O #
# L K # O # #
O O O # K # #
L L O K L # J
K K L L O K J
```

## Move

Start: (2, 1), End: (2, 4), Sacrifice: (0, 4)

```
K # L K # O K
# J K O K L #
K # # # # O #
# L K # O # #
O O O # K # #
L L O K L # J
K K L L O K J
```

## Move

Start: (5, 1), End: (5, 3), Sacrifice: (6, 4)

```
K # L K # O K
# J K O K L #
K # # # # O #
# L K # O # #
O O O # K # #
L # # # L # J
K K L L # K J
```

## Move

Start: (0, 3), End: (6, 3), Sacrifice: (4, 4)

```
K # L # # O K
# J K # K L #
K # # # # O #
# L K # O # #
O O O # # # #
L # # # L # J
K K L # # K J
```

## Move

Start: (0, 2), End: (0, 6), Sacrifice: (2, 0)

```
K # # # # # #
# J K # K L #
# # # # # O #
# L K # O # #
O O O # # # #
L # # # L # J
K K L # # K J
```

## Move

Start: (0, 0), End: (5, 0), Sacrifice: (6, 6)

```
# # # # # # #
# J K # K L #
# # # # # O #
# L K # O # #
# O O # # # #
# # # # L # J
K K L # # K #
```

## Move

Start: (3, 1), End: (6, 1), Sacrifice: (1, 1)

```
# # # # # # #
# # K # K L #
# # # # # O #
# # K # O # #
# # O # # # #
# # # # L # J
K # L # # K #
```

## Move

Start: (3, 2), End: (6, 2), Sacrifice: (1, 2)

```
# # # # # # #
# # # # K L #
# # # # # O #
# # # # O # #
# # # # # # #
# # # # L # J
K # # # # K #
```

## Move

Start: (1, 4), End: (5, 4), Sacrifice: (6, 0)

```
# # # # # # #
# # # # # L #
# # # # # O #
# # # # # # #
# # # # # # #
# # # # # # J
# # # # # K #
```

## Move

Start: (1, 5), End: (6, 5), Sacrifice: (5, 6)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

