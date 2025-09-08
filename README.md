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
L K L K #
O L O O L
K L K K O
K O L O K
K J O L L
```

# Solution

```
L K L K #
O L O O L
K L K K O
K O L O K
K J O L L
```

## Move

Start: (0, 2), End: (2, 2), Sacrifice: (1, 3)

```
L K # K #
O L # # L
K L # K O
K O L O K
K J O L L
```

## Move

Start: (0, 0), End: (2, 0), Sacrifice: (4, 1)

```
# K # K #
# L # # L
# L # K O
K O L O K
K # O L L
```

## Move

Start: (2, 3), End: (4, 3), Sacrifice: (0, 3)

```
# K # # #
# L # # L
# L # # O
K O L # K
K # O # L
```

## Move

Start: (4, 0), End: (4, 4), Sacrifice: (2, 1)

```
# K # # #
# L # # L
# # # # O
K O L # K
# # # # #
```

## Move

Start: (1, 4), End: (3, 4), Sacrifice: (1, 1)

```
# K # # #
# # # # #
# # # # #
K O L # #
# # # # #
```

## Move

Start: (3, 0), End: (3, 2), Sacrifice: (0, 1)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

