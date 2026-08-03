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
K L O K O L J
L O K L O K J
J K O L K O L
J O L L L K L
K O O L J # O
J O K K O L J
K L O K O L K
```

# Solution

```
K L O K O L J
L O K L O K J
J K O L K O L
J O L L L K L
K O O L J # O
J O K K O L J
K L O K O L K
```

## Move

Start: (6, 1), End: (6, 3), Sacrifice: (0, 6)

```
K L O K O L #
L O K L O K J
J K O L K O L
J O L L L K L
K O O L J # O
J O K K O L J
K # # # O L K
```

## Move

Start: (6, 0), End: (6, 5), Sacrifice: (3, 4)

```
K L O K O L #
L O K L O K J
J K O L K O L
J O L L # K L
K O O L J # O
J O K K O L J
# # # # # # K
```

## Move

Start: (0, 1), End: (0, 3), Sacrifice: (1, 6)

```
K # # # O L #
L O K L O K #
J K O L K O L
J O L L # K L
K O O L J # O
J O K K O L J
# # # # # # K
```

## Move

Start: (1, 3), End: (1, 5), Sacrifice: (5, 6)

```
K # # # O L #
L O K # # # #
J K O L K O L
J O L L # K L
K O O L J # O
J O K K O L #
# # # # # # K
```

## Move

Start: (3, 2), End: (5, 2), Sacrifice: (3, 1)

```
K # # # O L #
L O K # # # #
J K O L K O L
J # # L # K L
K O # L J # O
J O # K O L #
# # # # # # K
```

## Move

Start: (4, 0), End: (4, 3), Sacrifice: (3, 0)

```
K # # # O L #
L O K # # # #
J K O L K O L
# # # L # K L
# # # # J # O
J O # K O L #
# # # # # # K
```

## Move

Start: (5, 3), End: (5, 5), Sacrifice: (4, 4)

```
K # # # O L #
L O K # # # #
J K O L K O L
# # # L # K L
# # # # # # O
J O # # # # #
# # # # # # K
```

## Move

Start: (2, 4), End: (2, 6), Sacrifice: (3, 5)

```
K # # # O L #
L O K # # # #
J K O L # # #
# # # L # # L
# # # # # # O
J O # # # # #
# # # # # # K
```

## Move

Start: (0, 0), End: (0, 5), Sacrifice: (3, 3)

```
# # # # # # #
L O K # # # #
J K O L # # #
# # # # # # L
# # # # # # O
J O # # # # #
# # # # # # K
```

## Move

Start: (2, 1), End: (2, 3), Sacrifice: (5, 1)

```
# # # # # # #
L O K # # # #
J # # # # # #
# # # # # # L
# # # # # # O
J # # # # # #
# # # # # # K
```

## Move

Start: (3, 6), End: (6, 6), Sacrifice: (5, 0)

```
# # # # # # #
L O K # # # #
J # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

## Move

Start: (1, 0), End: (1, 2), Sacrifice: (2, 0)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

