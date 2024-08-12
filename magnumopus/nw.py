def needleman_wunsch(seq_a: str, seq_b: str, match: int, mismatch: int, gap: int) -> tuple[tuple[str, str], int]:
    len_a = len(seq_a) + 1
    len_b = len(seq_b) + 1
    
    score_matrix = []

    for i in range(len_a):
        row = []
        for j in range(len_b):
            cell = [0, '']
            row.append(cell)
        score_matrix.append(row)

    for i in range(1, len_a):
        score_matrix[i][0] = [i * gap, 'up']
    for j in range(1, len_b):
        score_matrix[0][j] = [j * gap, 'left']

    for i in range(1, len_a):
        for j in range(1, len_b):
            if seq_a[i-1] == seq_b[j-1]:
                diagonal_score = score_matrix[i-1][j-1][0] + match
            else:
                diagonal_score = score_matrix[i-1][j-1][0] + mismatch
            up_score = score_matrix[i-1][j][0] + gap
            left_score = score_matrix[i][j-1][0] + gap
            best_score = max(diagonal_score, up_score, left_score)

            if best_score == diagonal_score:
                score_matrix[i][j] = [diagonal_score, 'diagonal']
            elif best_score == up_score:
                score_matrix[i][j] = [up_score, 'up']
            else:
                score_matrix[i][j] = [left_score, 'left']

    aligned_1 = ''
    aligned_2 = ''
    i - len_a - 1
    j = len_b - 1

    for _ in range(len_a + len_b):
        if i == 0 and j == 0:
            break
        direction = score_matrix[i][j][1]
        if direction == 'diagonal':
            i -= 1
            j -= 1
            aligned_1 = seq_a[i] + aligned_1
            aligned_2 = seq_b[j] + aligned_2
        elif direction == 'up':
            i -= 1
            aligned_1 = seq_a[i] + aligned_1
            aligned_2 = '-' + aligned_2
        elif direction == 'left':
            j -= 1
            aligned_1 = '-' + aligned_1
            aligned_2 = seq_b[j] + aligned_2
        else:
            break

    score = score_matrix[-1][-1][0]

    return (aligned_1, aligned_2), score