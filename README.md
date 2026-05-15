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
L L O K # K L
L K O K L O O
K O L K O K K
K L L O O O K
L O O L K L K
J K O K O L O
O L K K O L L
```

# Solution

```
L L O K # K L
L K O K L O O
K O L K O K K
K L L O O O K
L O O L K L K
J K O K O L O
O L K K O L L
```

## Move

Start: (3, 1), End: (5, 1), Sacrifice: (6, 3)

```
L L O K # K L
L K O K L O O
K O L K O K K
K # L O O O K
L # O L K L K
J # O K O L O
O L K # O L L
```

## Move

Start: (6, 2), End: (6, 5), Sacrifice: (5, 2)

```
L L O K # K L
L K O K L O O
K O L K O K K
K # L O O O K
L # O L K L K
J # # K O L O
O L # # # # L
```

## Move

Start: (4, 6), End: (6, 6), Sacrifice: (3, 5)

```
L L O K # K L
L K O K L O O
K O L K O K K
K # L O O # K
L # O L K L #
J # # K O L #
O L # # # # #
```

## Move

Start: (0, 1), End: (0, 3), Sacrifice: (3, 0)

```
L # # # # K L
L K O K L O O
K O L K O K K
# # L O O # K
L # O L K L #
J # # K O L #
O L # # # # #
```

## Move

Start: (2, 0), End: (2, 2), Sacrifice: (1, 3)

```
L # # # # K L
L K O # L O O
# # # K O K K
# # L O O # K
L # O L K L #
J # # K O L #
O L # # # # #
```

## Move

Start: (2, 3), End: (4, 3), Sacrifice: (2, 5)

```
L # # # # K L
L K O # L O O
# # # # O # K
# # L # O # K
L # O # K L #
J # # K O L #
O L # # # # #
```

## Move

Start: (5, 3), End: (5, 5), Sacrifice: (0, 0)

```
# # # # # K L
L K O # L O O
# # # # O # K
# # L # O # K
L # O # K L #
J # # # # # #
O L # # # # #
```

## Move

Start: (4, 0), End: (4, 4), Sacrifice: (2, 4)

```
# # # # # K L
L K O # L O O
# # # # # # K
# # L # O # K
# # # # # L #
J # # # # # #
O L # # # # #
```

## Move

Start: (0, 6), End: (2, 6), Sacrifice: (1, 0)

```
# # # # # K #
# K O # L O #
# # # # # # #
# # L # O # K
# # # # # L #
J # # # # # #
O L # # # # #
```

## Move

Start: (1, 1), End: (1, 4), Sacrifice: (6, 0)

```
# # # # # K #
# # # # # O #
# # # # # # #
# # L # O # K
# # # # # L #
J # # # # # #
# L # # # # #
```

## Move

Start: (0, 5), End: (4, 5), Sacrifice: (5, 0)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # L # O # K
# # # # # # #
# # # # # # #
# L # # # # #
```

## Move

Start: (3, 2), End: (3, 6), Sacrifice: (6, 1)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

