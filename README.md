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
L O K L O K K
L L K O O K K
L O O K K # L
L K K O J O L
L L O O K J O
O O L L O K O
K K L J L O K
```

# Solution

```
L O K L O K K
L L K O O K K
L O O K K # L
L K K O J O L
L L O O K J O
O O L L O K O
K K L J L O K
```

## Move

Start: (4, 1), End: (6, 1), Sacrifice: (1, 4)

```
L O K L O K K
L L K O # K K
L O O K K # L
L K K O J O L
L # O O K J O
O # L L O K O
K # L J L O K
```

## Move

Start: (3, 2), End: (5, 2), Sacrifice: (4, 3)

```
L O K L O K K
L L K O # K K
L O O K K # L
L K # O J O L
L # # # K J O
O # # L O K O
K # L J L O K
```

## Move

Start: (4, 4), End: (6, 4), Sacrifice: (6, 5)

```
L O K L O K K
L L K O # K K
L O O K K # L
L K # O J O L
L # # # # J O
O # # L # K O
K # L J # # K
```

## Move

Start: (1, 2), End: (6, 2), Sacrifice: (1, 1)

```
L O K L O K K
L # # O # K K
L O # K K # L
L K # O J O L
L # # # # J O
O # # L # K O
K # # J # # K
```

## Move

Start: (2, 3), End: (5, 3), Sacrifice: (1, 6)

```
L O K L O K K
L # # O # K #
L O # # K # L
L K # # J O L
L # # # # J O
O # # # # K O
K # # J # # K
```

## Move

Start: (2, 0), End: (2, 4), Sacrifice: (3, 4)

```
L O K L O K K
L # # O # K #
# # # # # # L
L K # # # O L
L # # # # J O
O # # # # K O
K # # J # # K
```

## Move

Start: (1, 0), End: (1, 5), Sacrifice: (4, 6)

```
L O K L O K K
# # # # # # #
# # # # # # L
L K # # # O L
L # # # # J #
O # # # # K O
K # # J # # K
```

## Move

Start: (4, 0), End: (6, 0), Sacrifice: (5, 5)

```
L O K L O K K
# # # # # # #
# # # # # # L
L K # # # O L
# # # # # J #
# # # # # # O
# # # J # # K
```

## Move

Start: (3, 1), End: (3, 6), Sacrifice: (3, 0)

```
L O K L O K K
# # # # # # #
# # # # # # L
# # # # # # #
# # # # # J #
# # # # # # O
# # # J # # K
```

## Move

Start: (0, 0), End: (0, 2), Sacrifice: (0, 6)

```
# # # L O K #
# # # # # # #
# # # # # # L
# # # # # # #
# # # # # J #
# # # # # # O
# # # J # # K
```

## Move

Start: (2, 6), End: (6, 6), Sacrifice: (4, 5)

```
# # # L O K #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # J # # #
```

## Move

Start: (0, 3), End: (0, 5), Sacrifice: (6, 3)

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

