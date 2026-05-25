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
L K O L K L K
L O # O K O L
K L O L K J O
J J L L J K L
O J O J O O O
L O K J L L K
K K K K O L L
```

# Solution

```
L K O L K L K
L O # O K O L
K L O L K J O
J J L L J K L
O J O J O O O
L O K J L L K
K K K K O L L
```

## Move

Start: (0, 1), End: (2, 1), Sacrifice: (1, 3)

```
L # O L K L K
L # # # K O L
K # O L K J O
J J L L J K L
O J O J O O O
L O K J L L K
K K K K O L L
```

## Move

Start: (5, 0), End: (5, 2), Sacrifice: (4, 3)

```
L # O L K L K
L # # # K O L
K # O L K J O
J J L L J K L
O J O # O O O
# # # J L L K
K K K K O L L
```

## Move

Start: (3, 2), End: (6, 2), Sacrifice: (3, 4)

```
L # O L K L K
L # # # K O L
K # O L K J O
J J # L # K L
O J # # O O O
# # # J L L K
K K # K O L L
```

## Move

Start: (3, 5), End: (5, 5), Sacrifice: (5, 3)

```
L # O L K L K
L # # # K O L
K # O L K J O
J J # L # # L
O J # # O # O
# # # # L # K
K K # K O L L
```

## Move

Start: (3, 6), End: (5, 6), Sacrifice: (0, 3)

```
L # O # K L K
L # # # K O L
K # O L K J O
J J # L # # #
O J # # O # #
# # # # L # #
K K # K O L L
```

## Move

Start: (1, 4), End: (1, 6), Sacrifice: (3, 1)

```
L # O # K L K
L # # # # # #
K # O L K J O
J # # L # # #
O J # # O # #
# # # # L # #
K K # K O L L
```

## Move

Start: (0, 0), End: (0, 4), Sacrifice: (2, 5)

```
# # # # # L K
L # # # # # #
K # O L K # O
J # # L # # #
O J # # O # #
# # # # L # #
K K # K O L L
```

## Move

Start: (2, 4), End: (5, 4), Sacrifice: (3, 3)

```
# # # # # L K
L # # # # # #
K # O L # # O
J # # # # # #
O J # # # # #
# # # # # # #
K K # K O L L
```

## Move

Start: (0, 6), End: (6, 6), Sacrifice: (0, 5)

```
# # # # # # #
L # # # # # #
K # O L # # #
J # # # # # #
O J # # # # #
# # # # # # #
K K # K O L #
```

## Move

Start: (2, 0), End: (2, 3), Sacrifice: (3, 0)

```
# # # # # # #
L # # # # # #
# # # # # # #
# # # # # # #
O J # # # # #
# # # # # # #
K K # K O L #
```

## Move

Start: (6, 3), End: (6, 5), Sacrifice: (4, 1)

```
# # # # # # #
L # # # # # #
# # # # # # #
# # # # # # #
O # # # # # #
# # # # # # #
K K # # # # #
```

## Move

Start: (1, 0), End: (6, 0), Sacrifice: (6, 1)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

