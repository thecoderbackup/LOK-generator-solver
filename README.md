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
K O K K K K L
L L O L O J L
O K L O L O O
K O O K O L O
J L L # K K K
K O L L K O L
K J O L O K L
```

# Solution

```
K O K K K K L
L L O L O J L
O K L O L O O
K O O K O L O
J L L # K K K
K O L L K O L
K J O L O K L
```

## Move

Start: (2, 4), End: (4, 4), Sacrifice: (3, 6)

```
K O K K K K L
L L O L O J L
O K L O # O O
K O O K # L #
J L L # # K K
K O L L K O L
K J O L O K L
```

## Move

Start: (1, 0), End: (3, 0), Sacrifice: (6, 1)

```
K O K K K K L
# L O L O J L
# K L O # O O
# O O K # L #
J L L # # K K
K O L L K O L
K # O L O K L
```

## Move

Start: (1, 6), End: (4, 6), Sacrifice: (1, 1)

```
K O K K K K L
# # O L O J #
# K L O # O #
# O O K # L #
J L L # # K #
K O L L K O L
K # O L O K L
```

## Move

Start: (6, 3), End: (6, 5), Sacrifice: (3, 2)

```
K O K K K K L
# # O L O J #
# K L O # O #
# O # K # L #
J L L # # K #
K O L L K O L
K # O # # # L
```

## Move

Start: (0, 2), End: (2, 2), Sacrifice: (1, 5)

```
K O # K K K L
# # # L O # #
# K # O # O #
# O # K # L #
J L L # # K #
K O L L K O L
K # O # # # L
```

## Move

Start: (1, 3), End: (3, 3), Sacrifice: (1, 4)

```
K O # K K K L
# # # # # # #
# K # # # O #
# O # # # L #
J L L # # K #
K O L L K O L
K # O # # # L
```

## Move

Start: (6, 0), End: (6, 6), Sacrifice: (4, 5)

```
K O # K K K L
# # # # # # #
# K # # # O #
# O # # # L #
J L L # # # #
K O L L K O L
# # # # # # #
```

## Move

Start: (0, 5), End: (3, 5), Sacrifice: (0, 3)

```
K O # # K # L
# # # # # # #
# K # # # # #
# O # # # # #
J L L # # # #
K O L L K O L
# # # # # # #
```

## Move

Start: (2, 1), End: (4, 1), Sacrifice: (5, 2)

```
K O # # K # L
# # # # # # #
# # # # # # #
# # # # # # #
J # L # # # #
K O # L K O L
# # # # # # #
```

## Move

Start: (5, 0), End: (5, 3), Sacrifice: (0, 4)

```
K O # # # # L
# # # # # # #
# # # # # # #
# # # # # # #
J # L # # # #
# # # # K O L
# # # # # # #
```

## Move

Start: (5, 4), End: (5, 6), Sacrifice: (4, 2)

```
K O # # # # L
# # # # # # #
# # # # # # #
# # # # # # #
J # # # # # #
# # # # # # #
# # # # # # #
```

## Move

Start: (0, 0), End: (0, 6), Sacrifice: (4, 0)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

