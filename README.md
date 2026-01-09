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
K L O J K K J
O # O L L O K
L L K J O L L
L O L K O O L
O K O O L K O
K K O O L L K
L K L L L O K
```

# Solution

```
K L O J K K J
O # O L L O K
L L K J O L L
L O L K O O L
O K O O L K O
K K O O L L K
L K L L L O K
```

## Move

Start: (6, 4), End: (6, 6), Sacrifice: (2, 4)

```
K L O J K K J
O # O L L O K
L L K J # L L
L O L K O O L
O K O O L K O
K K O O L L K
L K L L # # #
```

## Move

Start: (2, 1), End: (4, 1), Sacrifice: (5, 3)

```
K L O J K K J
O # O L L O K
L # K J # L L
L # L K O O L
O # O O L K O
K K O # L L K
L K L L # # #
```

## Move

Start: (0, 0), End: (2, 0), Sacrifice: (1, 4)

```
# L O J K K J
# # O L # O K
# # K J # L L
L # L K O O L
O # O O L K O
K K O # L L K
L K L L # # #
```

## Move

Start: (3, 6), End: (5, 6), Sacrifice: (5, 4)

```
# L O J K K J
# # O L # O K
# # K J # L L
L # L K O O #
O # O O L K #
K K O # # L #
L K L L # # #
```

## Move

Start: (2, 5), End: (4, 5), Sacrifice: (3, 2)

```
# L O J K K J
# # O L # O K
# # K J # # L
L # # K O # #
O # O O L # #
K K O # # L #
L K L L # # #
```

## Move

Start: (3, 3), End: (6, 3), Sacrifice: (6, 0)

```
# L O J K K J
# # O L # O K
# # K J # # L
L # # # O # #
O # O # L # #
K K O # # L #
# K L # # # #
```

## Move

Start: (3, 0), End: (5, 0), Sacrifice: (0, 3)

```
# L O # K K J
# # O L # O K
# # K J # # L
# # # # O # #
# # O # L # #
# K O # # L #
# K L # # # #
```

## Move

Start: (5, 1), End: (5, 5), Sacrifice: (2, 6)

```
# L O # K K J
# # O L # O K
# # K J # # #
# # # # O # #
# # O # L # #
# # # # # # #
# K L # # # #
```

## Move

Start: (1, 3), End: (1, 6), Sacrifice: (6, 1)

```
# L O # K K J
# # O # # # #
# # K J # # #
# # # # O # #
# # O # L # #
# # # # # # #
# # L # # # #
```

## Move

Start: (0, 4), End: (4, 4), Sacrifice: (0, 6)

```
# L O # # K #
# # O # # # #
# # K J # # #
# # # # # # #
# # O # # # #
# # # # # # #
# # L # # # #
```

## Move

Start: (2, 2), End: (6, 2), Sacrifice: (1, 2)

```
# L O # # K #
# # # # # # #
# # # J # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

## Move

Start: (0, 1), End: (0, 5), Sacrifice: (2, 3)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

