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
K K O L J L
K O L K O L
K O O O L K
K O L J L O
L J O K O L
L K O K K K
```

# Solution

```
K K O L J L
K O L K O L
K O O O L K
K O L J L O
L J O K O L
L K O K K K
```

## Move

Start: (0, 1), End: (0, 3), Sacrifice: (2, 1)

```
K # # # J L
K O L K O L
K # O O L K
K O L J L O
L J O K O L
L K O K K K
```

## Move

Start: (2, 5), End: (4, 5), Sacrifice: (0, 0)

```
# # # # J L
K O L K O L
K # O O L #
K O L J L #
L J O K O #
L K O K K K
```

## Move

Start: (1, 3), End: (1, 5), Sacrifice: (5, 1)

```
# # # # J L
K O L # # #
K # O O L #
K O L J L #
L J O K O #
L # O K K K
```

## Move

Start: (5, 0), End: (5, 3), Sacrifice: (2, 3)

```
# # # # J L
K O L # # #
K # O # L #
K O L J L #
L J O K O #
# # # # K K
```

## Move

Start: (3, 0), End: (3, 2), Sacrifice: (4, 1)

```
# # # # J L
K O L # # #
K # O # L #
# # # J L #
L # O K O #
# # # # K K
```

## Move

Start: (2, 0), End: (2, 4), Sacrifice: (0, 5)

```
# # # # J #
K O L # # #
# # # # # #
# # # J L #
L # O K O #
# # # # K K
```

## Move

Start: (1, 0), End: (1, 2), Sacrifice: (0, 4)

```
# # # # # #
# # # # # #
# # # # # #
# # # J L #
L # O K O #
# # # # K K
```

## Move

Start: (4, 0), End: (4, 3), Sacrifice: (3, 3)

```
# # # # # #
# # # # # #
# # # # # #
# # # # L #
# # # # O #
# # # # K K
```

## Move

Start: (3, 4), End: (5, 4), Sacrifice: (5, 5)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

