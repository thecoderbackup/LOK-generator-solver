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
L K K O L K
K J O O L O
O L L K O O
L O L O K L
J K K L K J
K O L K O L
```

# Solution

```
L K K O L K
K J O O L O
O L L K O O
L O L O K L
J K K L K J
K O L K O L
```

## Move

Start: (2, 1), End: (4, 1), Sacrifice: (4, 5)

```
L K K O L K
K J O O L O
O # L K O O
L # L O K L
J # K L K #
K O L K O L
```

## Move

Start: (5, 0), End: (5, 2), Sacrifice: (3, 2)

```
L K K O L K
K J O O L O
O # L K O O
L # # O K L
J # K L K #
# # # K O L
```

## Move

Start: (1, 4), End: (3, 4), Sacrifice: (2, 5)

```
L K K O L K
K J O O # O
O # L K # #
L # # O # L
J # K L K #
# # # K O L
```

## Move

Start: (5, 3), End: (5, 5), Sacrifice: (0, 0)

```
# K K O L K
K J O O # O
O # L K # #
L # # O # L
J # K L K #
# # # # # #
```

## Move

Start: (2, 3), End: (4, 3), Sacrifice: (4, 2)

```
# K K O L K
K J O O # O
O # L # # #
L # # # # L
J # # # K #
# # # # # #
```

## Move

Start: (0, 5), End: (3, 5), Sacrifice: (4, 0)

```
# K K O L #
K J O O # #
O # L # # #
L # # # # #
# # # # K #
# # # # # #
```

## Move

Start: (0, 2), End: (2, 2), Sacrifice: (1, 1)

```
# K # O L #
K # # O # #
O # # # # #
L # # # # #
# # # # K #
# # # # # #
```

## Move

Start: (1, 0), End: (3, 0), Sacrifice: (1, 3)

```
# K # O L #
# # # # # #
# # # # # #
# # # # # #
# # # # K #
# # # # # #
```

## Move

Start: (0, 1), End: (0, 4), Sacrifice: (4, 4)

```
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
```

