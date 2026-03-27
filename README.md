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
# J L O K K K
L L O L K O O
J L J L O K L
K O K O O O L
K K O K L L L
K O O K O L O
J L L K L L K
```

# Solution

```
# J L O K K K
L L O L K O O
J L J L O K L
K O K O O O L
K K O K L L L
K O O K O L O
J L L K L L K
```

## Move

Start: (0, 2), End: (0, 4), Sacrifice: (2, 0)

```
# J # # # K K
L L O L K O O
# L J L O K L
K O K O O O L
K K O K L L L
K O O K O L O
J L L K L L K
```

## Move

Start: (2, 3), End: (2, 5), Sacrifice: (0, 1)

```
# # # # # K K
L L O L K O O
# L J # # # L
K O K O O O L
K K O K L L L
K O O K O L O
J L L K L L K
```

## Move

Start: (1, 3), End: (4, 3), Sacrifice: (1, 2)

```
# # # # # K K
L L # # K O O
# L J # # # L
K O K # O O L
K K O # L L L
K O O K O L O
J L L K L L K
```

## Move

Start: (5, 3), End: (5, 5), Sacrifice: (3, 5)

```
# # # # # K K
L L # # K O O
# L J # # # L
K O K # O # L
K K O # L L L
K O O # # # O
J L L K L L K
```

## Move

Start: (4, 1), End: (6, 1), Sacrifice: (2, 1)

```
# # # # # K K
L L # # K O O
# # J # # # L
K O K # O # L
K # O # L L L
K # O # # # O
J # L K L L K
```

## Move

Start: (1, 4), End: (4, 4), Sacrifice: (5, 0)

```
# # # # # K K
L L # # # O O
# # J # # # L
K O K # # # L
K # O # # L L
# # O # # # O
J # L K L L K
```

## Move

Start: (0, 6), End: (2, 6), Sacrifice: (6, 4)

```
# # # # # K #
L L # # # O #
# # J # # # #
K O K # # # L
K # O # # L L
# # O # # # O
J # L K # L K
```

## Move

Start: (4, 0), End: (4, 5), Sacrifice: (2, 2)

```
# # # # # K #
L L # # # O #
# # # # # # #
K O K # # # L
# # # # # # L
# # O # # # O
J # L K # L K
```

## Move

Start: (0, 5), End: (6, 5), Sacrifice: (6, 3)

```
# # # # # # #
L L # # # # #
# # # # # # #
K O K # # # L
# # # # # # L
# # O # # # O
J # L # # # K
```

## Move

Start: (3, 2), End: (6, 2), Sacrifice: (1, 0)

```
# # # # # # #
# L # # # # #
# # # # # # #
K O # # # # L
# # # # # # L
# # # # # # O
J # # # # # K
```

## Move

Start: (4, 6), End: (6, 6), Sacrifice: (1, 1)

```
# # # # # # #
# # # # # # #
# # # # # # #
K O # # # # L
# # # # # # #
# # # # # # #
J # # # # # #
```

## Move

Start: (3, 0), End: (3, 6), Sacrifice: (6, 0)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

