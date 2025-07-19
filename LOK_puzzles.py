import random
import copy

class Movimento:
    def __init__(self, inicio, fim, sacrificio, grid):
        self.inicio = inicio
        self.fim = fim
        self.sacrificio = sacrificio
        self.grid = grid

def generate_puzzle():
    size = random.randint(5, 7)
    grid = []
    movimentos = []
    while not grid or sum(row.count('#') for row in grid) != size * size % 4:
        grid = [['#' for _ in range(size)] for _ in range(size)]
        movimentos = []
        for _ in range(size * size):
            pos = get_posicao_vazia_aleatoria(grid)
            if pos is not None:
                word = random.choice(["LOK", "KOL"])
                new_grid, movimento = add_word_skip_occupied_with_sacrifice(grid, word, pos[0], pos[1], random.choice([True, False]))
                if movimento is not None:
                    movimentos.append(movimento)
                    grid = new_grid
    return grid, movimentos

def add_word_skip_occupied_with_sacrifice(original_grid, word, row, col, horizontal):
    grid = copy.deepcopy(original_grid)
    letter_to_place = len(word)
    lpos = (0, 0)
    def swap(a, b):
        return (a, b) if horizontal else (b, a)
    r, c = swap(row, col)
    offset = 0
    for char in word:
        found = False
        for it in range(c + offset, len(grid)):
            check_r, check_c = swap(r, it)
            if grid[check_r][check_c] == "#":
                lpos = (check_r, check_c)
                grid[lpos[0]][lpos[1]] = char
                letter_to_place -= 1
                offset = (it - c) + 1
                found = True
                break
        if not found:
            pass
    if letter_to_place != 0:
        return original_grid, None
    else:
        pos_sacrificio = get_posicao_vazia_aleatoria(grid)
        if pos_sacrificio is not None:
            add_sacrifice(grid, pos_sacrificio)
            movimento = Movimento(
                inicio=(row, col),
                fim=lpos,
                sacrificio=pos_sacrificio,
                grid=copy.deepcopy(grid)
            )
            return grid, movimento
        else:
            return original_grid, None

def add_sacrifice(grid, pos):
    letters = ["L", "O", "K", "J"]
    random_letter = random.choice(letters)
    if pos is not None:
        grid[pos[0]][pos[1]] = random_letter
    return grid

def get_posicao_vazia_aleatoria(grid):
    empty_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                empty_positions.append((i, j))
    if empty_positions:
        return random.choice(empty_positions)
    return None

def mask(grid1, grid2):
    grid_masked = copy.deepcopy(grid1)
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid2[i][j] != "#":
                grid_masked[i][j] = "#"
    return grid_masked

def grid_to_str(grid):
    return '\n'.join(' '.join(cell for cell in row) for row in grid)

def write_readme(grid, movimentos):
    with open('README.md', 'w') as f:
        f.write('# LOK Based Puzzle Generator\n\n')
        f.write('This puzzle generator is inspired by the puzzle book "LOK" created by Blaž Urban Gracar under Letibus Design, and its digital adaptation "LOK Digital" developed by Icedrop Games in collaboration with Raindrinker and published by Draknek & Friends.\n\n')
        f.write('In the original LOK, players engage in mind-bending word-search puzzles where the goal is to find keywords with special effects to black out all cells in a grid. The digital version expands this with procedural puzzles and new mechanics.\n\n')
        f.write('References:\n')
        f.write('- Original LOK puzzle book: [Blaž Urban Gracar\'s site](https://www.blazgracar.com/lok) and [Itch.io](https://letibus.itch.io/lok)\n')
        f.write('- LOK Digital: [Official site](https://lok-digital.com/), [Steam](https://store.steampowered.com/app/2207440/LOK_Digital/), [Google Play](https://play.google.com/store/apps/details?id=com.IcedropGames.LOK), [App Store](https://apps.apple.com/us/app/lok-digital/id6476513210)\n\n')
        f.write('## Descrição do Jogo\n\n')
        f.write('Dado um tabuleiro, você deve transformar todos os símbolos em #. Para isso, encontre a palavra "LOK", que pode estar na horizontal ou vertical, e também de trás para frente (ou seja, "KOL" também é válido!). Toda vez que encontrar uma palavra, você deve sacrificar uma letra e transformá-la em # também.\n\n')
        f.write('Se houver um # no meio da palavra, você pode ignorá-lo, ou seja, L#OK também é uma palavra válida.\n\n')
        f.write('Seu objetivo é transformar todo o tabuleiro em #.\n\n')
        f.write('Vale lembrar que se você transformar todo o tabuleiro e tiver sacrifícios pendentes, significa que não é uma solução válida!\n\n')
        f.write('Retorne uma lista com todos os seus movimentos, com posição (x,y) do início e fim de cada palavra e (x,y) de cada sacrifício.\n\n')
        f.write('# Puzzle Gerado\n\n')
        f.write('```\n')
        f.write(grid_to_str(grid))
        f.write('\n```\n\n')
        f.write('# Resolução\n\n')
        f.write('```\n')
        f.write(grid_to_str(grid))
        f.write('\n```\n\n')
        for mov in movimentos:
            f.write(f'## Movimento\n\nInicio: {mov.inicio}, Fim: {mov.fim}, Sacrificio: {mov.sacrificio}\n\n')
            masked = mask(grid, mov.grid)
            f.write('```\n')
            f.write(grid_to_str(masked))
            f.write('\n```\n\n')

def write_solucoes(puzzle_num, grid, movimentos):
    with open('solucoes.md', 'a') as f:
        f.write(f'# Puzzle {puzzle_num}\n\n')
        f.write('## Puzzle Gerado\n\n')
        f.write('```\n' + grid_to_str(grid) + '\n```\n\n')
        f.write('## Resolução\n\n')
        f.write('```\n' + grid_to_str(grid) + '\n```\n\n')
        for idx, mov in enumerate(movimentos, 1):
            f.write(f'### Passo {idx}\n\nInicio: {mov.inicio}, Fim: {mov.fim}, Sacrificio: {mov.sacrificio}\n\n')
            masked = mask(grid, mov.grid)
            f.write('```\n' + grid_to_str(masked) + '\n```\n\n')
        f.write('---\n\n')

def main():
    grid, movimentos = generate_puzzle()
    write_readme(grid, movimentos)
    for i in range(10):
        grid, movimentos = generate_puzzle()
        write_solucoes(i + 1, grid, movimentos)

main()
