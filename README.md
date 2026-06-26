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
J L K L O K K
J O O K L K L
K K L O J K O
O O L K O O K
L # O L K O J
K K K L O L L
K K O L O L L
```

# Solution

```
J L K L O K K
J O O K L K L
K K L O J K O
O O L K O O K
L # O L K O J
K K K L O L L
K K O L O L L
```

## Move

Start: (1, 6), End: (3, 6), Sacrifice: (3, 3)

```
J L K L O K K
J O O K L K #
K K L O J K #
O O L # O O #
L # O L K O J
K K K L O L L
K K O L O L L
```

## Move

Start: (0, 2), End: (2, 2), Sacrifice: (2, 4)

```
J L # L O K K
J O # K L K #
K K # O # K #
O O L # O O #
L # O L K O J
K K K L O L L
K K O L O L L
```

## Move

Start: (0, 1), End: (2, 1), Sacrifice: (1, 5)

```
J # # L O K K
J # # K L # #
K # # O # K #
O O L # O O #
L # O L K O J
K K K L O L L
K K O L O L L
```

## Move

Start: (2, 0), End: (4, 0), Sacrifice: (5, 0)

```
J # # L O K K
J # # K L # #
# # # O # K #
# O L # O O #
# # O L K O J
# K K L O L L
K K O L O L L
```

## Move

Start: (6, 1), End: (6, 3), Sacrifice: (0, 0)

```
# # # L O K K
J # # K L # #
# # # O # K #
# O L # O O #
# # O L K O J
# K K L O L L
K # # # O L L
```

## Move

Start: (1, 4), End: (4, 4), Sacrifice: (6, 5)

```
# # # L O K K
J # # K # # #
# # # O # K #
# O L # # O #
# # O L # O J
# K K L O L L
K # # # O # L
```

## Move

Start: (3, 2), End: (5, 2), Sacrifice: (4, 6)

```
# # # L O K K
J # # K # # #
# # # O # K #
# O # # # O #
# # # L # O #
# K # L O L L
K # # # O # L
```

## Move

Start: (0, 3), End: (0, 5), Sacrifice: (4, 5)

```
# # # # # # K
J # # K # # #
# # # O # K #
# O # # # O #
# # # L # # #
# K # L O L L
K # # # O # L
```

## Move

Start: (6, 0), End: (6, 6), Sacrifice: (5, 3)

```
# # # # # # K
J # # K # # #
# # # O # K #
# O # # # O #
# # # L # # #
# K # # O L L
# # # # # # #
```

## Move

Start: (1, 3), End: (4, 3), Sacrifice: (3, 1)

```
# # # # # # K
J # # # # # #
# # # # # K #
# # # # # O #
# # # # # # #
# K # # O L L
# # # # # # #
```

## Move

Start: (2, 5), End: (5, 5), Sacrifice: (1, 0)

```
# # # # # # K
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# K # # O # L
# # # # # # #
```

## Move

Start: (5, 1), End: (5, 6), Sacrifice: (0, 6)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

