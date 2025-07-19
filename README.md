# LOK Based Puzzle Generator

This puzzle generator is inspired by the puzzle book "LOK" created by Blaž Urban Gracar under Letibus Design, and its digital adaptation "LOK Digital" developed by Icedrop Games in collaboration with Raindrinker and published by Draknek & Friends.

In the original LOK, players engage in mind-bending word-search puzzles where the goal is to find keywords with special effects to black out all cells in a grid. The digital version expands this with procedural puzzles and new mechanics.

References:
- Original LOK puzzle book: [Blaž Urban Gracar's site](https://www.blazgracar.com/lok) and [Itch.io](https://letibus.itch.io/lok)
- LOK Digital: [Official site](https://lok-digital.com/), [Steam](https://store.steampowered.com/app/2207440/LOK_Digital/), [Google Play](https://play.google.com/store/apps/details?id=com.IcedropGames.LOK), [App Store](https://apps.apple.com/us/app/lok-digital/id6476513210)

## Descrição do Jogo

Dado um tabuleiro, você deve transformar todos os símbolos em #. Para isso, encontre a palavra "LOK", que pode estar na horizontal ou vertical, e também de trás para frente (ou seja, "KOL" também é válido!). Toda vez que encontrar uma palavra, você deve sacrificar uma letra e transformá-la em # também.

Se houver um # no meio da palavra, você pode ignorá-lo, ou seja, L#OK também é uma palavra válida.

Seu objetivo é transformar todo o tabuleiro em #.

Vale lembrar que se você transformar todo o tabuleiro e tiver sacrifícios pendentes, significa que não é uma solução válida!

Retorne uma lista com todos os seus movimentos, com posição (x,y) do início e fim de cada palavra e (x,y) de cada sacrifício.

# Puzzle Gerado

```
L L O K L
# O O K K
L O K J O
K O L K K
K K O L L
```

# Resolução

```
L L O K L
# O O K K
L O K J O
K O L K K
K K O L L
```

## Movimento

Inicio: (2, 0), Fim: (2, 2), Sacrificio: (3, 3)

```
L L O K L
# O O K K
# # # J O
K O L # K
K K O L L
```

## Movimento

Inicio: (3, 0), Fim: (3, 2), Sacrificio: (3, 4)

```
L L O K L
# O O K K
# # # J O
# # # # #
K K O L L
```

## Movimento

Inicio: (0, 1), Fim: (4, 1), Sacrificio: (1, 3)

```
L # O K L
# # O # K
# # # J O
# # # # #
K # O L L
```

## Movimento

Inicio: (1, 4), Fim: (4, 4), Sacrificio: (2, 3)

```
L # O K L
# # O # #
# # # # #
# # # # #
K # O L #
```

## Movimento

Inicio: (0, 0), Fim: (0, 3), Sacrificio: (1, 2)

```
# # # # L
# # # # #
# # # # #
# # # # #
K # O L #
```

## Movimento

Inicio: (4, 0), Fim: (4, 3), Sacrificio: (0, 4)

```
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
```

