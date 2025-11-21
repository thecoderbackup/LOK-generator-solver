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
L L O L L L J
O O O O O K L
K K O L J O K
K L # K K L O
O K K O K O O
L O K O O L O
L O K L L K L
```

# Solution

```
L L O L L L J
O O O O O K L
K K O L J O K
K L # K K L O
O K K O K O O
L O K O O L O
L O K L L K L
```

## Move

Start: (3, 0), End: (5, 0), Sacrifice: (3, 1)

```
L L O L L L J
O O O O O K L
K K O L J O K
# # # K K L O
# K K O K O O
# O K O O L O
L O K L L K L
```

## Move

Start: (1, 5), End: (3, 5), Sacrifice: (2, 4)

```
L L O L L L J
O O O O O # L
K K O L # # K
# # # K K # O
# K K O K O O
# O K O O L O
L O K L L K L
```

## Move

Start: (6, 0), End: (6, 2), Sacrifice: (3, 6)

```
L L O L L L J
O O O O O # L
K K O L # # K
# # # K K # #
# K K O K O O
# O K O O L O
# # # L L K L
```

## Move

Start: (4, 4), End: (6, 4), Sacrifice: (5, 6)

```
L L O L L L J
O O O O O # L
K K O L # # K
# # # K K # #
# K K O # O O
# O K O # L #
# # # L # K L
```

## Move

Start: (2, 6), End: (6, 6), Sacrifice: (4, 3)

```
L L O L L L J
O O O O O # L
K K O L # # #
# # # K K # #
# K K # # O #
# O K O # L #
# # # L # K #
```

## Move

Start: (5, 2), End: (5, 5), Sacrifice: (0, 2)

```
L L # L L L J
O O O O O # L
K K O L # # #
# # # K K # #
# K K # # O #
# O # # # # #
# # # L # K #
```

## Move

Start: (2, 1), End: (2, 3), Sacrifice: (1, 6)

```
L L # L L L J
O O O O O # #
K # # # # # #
# # # K K # #
# K K # # O #
# O # # # # #
# # # L # K #
```

## Move

Start: (0, 4), End: (3, 4), Sacrifice: (1, 2)

```
L L # L # L J
O O # O # # #
K # # # # # #
# # # K # # #
# K K # # O #
# O # # # # #
# # # L # K #
```

## Move

Start: (0, 3), End: (3, 3), Sacrifice: (6, 3)

```
L L # # # L J
O O # # # # #
K # # # # # #
# # # # # # #
# K K # # O #
# O # # # # #
# # # # # K #
```

## Move

Start: (0, 0), End: (2, 0), Sacrifice: (5, 1)

```
# L # # # L J
# O # # # # #
# # # # # # #
# # # # # # #
# K K # # O #
# # # # # # #
# # # # # K #
```

## Move

Start: (0, 5), End: (6, 5), Sacrifice: (0, 6)

```
# L # # # # #
# O # # # # #
# # # # # # #
# # # # # # #
# K K # # # #
# # # # # # #
# # # # # # #
```

## Move

Start: (0, 1), End: (4, 1), Sacrifice: (4, 2)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

