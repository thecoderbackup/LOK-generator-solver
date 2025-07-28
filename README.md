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
L O L K K O L
L L O L O K L
K O K L L O O
O O L K O L K
K L O K L K L
# O K O O O J
O K L L O L K
```

# Solution

```
L O L K K O L
L L O L O K L
K O K L L O O
O O L K O L K
K L O K L K L
# O K O O O J
O K L L O L K
```

## Move

Start: (0, 2), End: (2, 2), Sacrifice: (2, 3)

```
L O # K K O L
L L # L O K L
K O # # L O O
O O L K O L K
K L O K L K L
# O K O O O J
O K L L O L K
```

## Move

Start: (2, 0), End: (2, 4), Sacrifice: (4, 6)

```
L O # K K O L
L L # L O K L
# # # # # O O
O O L K O L K
K L O K L K #
# O K O O O J
O K L L O L K
```

## Move

Start: (0, 0), End: (0, 3), Sacrifice: (3, 2)

```
# # # # K O L
L L # L O K L
# # # # # O O
O O # K O L K
K L O K L K #
# O K O O O J
O K L L O L K
```

## Move

Start: (4, 5), End: (6, 5), Sacrifice: (1, 4)

```
# # # # K O L
L L # L # K L
# # # # # O O
O O # K O L K
K L O K L # #
# O K O O # J
O K L L O # K
```

## Move

Start: (4, 1), End: (4, 3), Sacrifice: (0, 5)

```
# # # # K # L
L L # L # K L
# # # # # O O
O O # K O L K
K # # # L # #
# O K O O # J
O K L L O # K
```

## Move

Start: (1, 0), End: (4, 0), Sacrifice: (3, 1)

```
# # # # K # L
# L # L # K L
# # # # # O O
# # # K O L K
# # # # L # #
# O K O O # J
O K L L O # K
```

## Move

Start: (1, 5), End: (3, 5), Sacrifice: (5, 2)

```
# # # # K # L
# L # L # # L
# # # # # # O
# # # K O # K
# # # # L # #
# O # O O # J
O K L L O # K
```

## Move

Start: (1, 1), End: (6, 1), Sacrifice: (5, 4)

```
# # # # K # L
# # # L # # L
# # # # # # O
# # # K O # K
# # # # L # #
# # # O # # J
O # L L O # K
```

## Move

Start: (3, 3), End: (6, 3), Sacrifice: (5, 6)

```
# # # # K # L
# # # L # # L
# # # # # # O
# # # # O # K
# # # # L # #
# # # # # # #
O # L # O # K
```

## Move

Start: (1, 6), End: (3, 6), Sacrifice: (0, 6)

```
# # # # K # #
# # # L # # #
# # # # # # #
# # # # O # #
# # # # L # #
# # # # # # #
O # L # O # K
```

## Move

Start: (0, 4), End: (4, 4), Sacrifice: (6, 0)

```
# # # # # # #
# # # L # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # L # O # K
```

## Move

Start: (6, 2), End: (6, 6), Sacrifice: (1, 3)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

