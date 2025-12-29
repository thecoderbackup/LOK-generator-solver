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
K O K L K K K
J K K J L O K
K O L K O O O
K O O L L O L
L L O K L O K
L O O J K O L
# K L J J L J
```

# Solution

```
K O K L K K K
J K K J L O K
K O L K O O O
K O O L L O L
L L O K L O K
L O O J K O L
# K L J J L J
```

## Move

Start: (1, 4), End: (1, 6), Sacrifice: (5, 2)

```
K O K L K K K
J K K J # # #
K O L K O O O
K O O L L O L
L L O K L O K
L O # J K O L
# K L J J L J
```

## Move

Start: (4, 1), End: (6, 1), Sacrifice: (5, 3)

```
K O K L K K K
J K K J # # #
K O L K O O O
K O O L L O L
L # O K L O K
L # # # K O L
# # L J J L J
```

## Move

Start: (2, 0), End: (2, 2), Sacrifice: (1, 2)

```
K O K L K K K
J K # J # # #
# # # K O O O
K O O L L O L
L # O K L O K
L # # # K O L
# # L J J L J
```

## Move

Start: (4, 0), End: (4, 3), Sacrifice: (1, 1)

```
K O K L K K K
J # # J # # #
# # # K O O O
K O O L L O L
# # # # L O K
L # # # K O L
# # L J J L J
```

## Move

Start: (4, 4), End: (4, 6), Sacrifice: (6, 3)

```
K O K L K K K
J # # J # # #
# # # K O O O
K O O L L O L
# # # # # # #
L # # # K O L
# # L # J L J
```

## Move

Start: (0, 4), End: (3, 4), Sacrifice: (1, 0)

```
K O K L # K K
# # # J # # #
# # # K # O O
K O O L # O L
# # # # # # #
L # # # K O L
# # L # J L J
```

## Move

Start: (0, 2), End: (6, 2), Sacrifice: (2, 5)

```
K O # L # K K
# # # J # # #
# # # K # # O
K O # L # O L
# # # # # # #
L # # # K O L
# # # # J L J
```

## Move

Start: (3, 0), End: (3, 3), Sacrifice: (1, 3)

```
K O # L # K K
# # # # # # #
# # # K # # O
# # # # # O L
# # # # # # #
L # # # K O L
# # # # J L J
```

## Move

Start: (5, 4), End: (5, 6), Sacrifice: (5, 0)

```
K O # L # K K
# # # # # # #
# # # K # # O
# # # # # O L
# # # # # # #
# # # # # # #
# # # # J L J
```

## Move

Start: (0, 5), End: (6, 5), Sacrifice: (2, 3)

```
K O # L # # K
# # # # # # #
# # # # # # O
# # # # # # L
# # # # # # #
# # # # # # #
# # # # J # J
```

## Move

Start: (0, 6), End: (3, 6), Sacrifice: (6, 4)

```
K O # L # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # J
```

## Move

Start: (0, 0), End: (0, 3), Sacrifice: (6, 6)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

