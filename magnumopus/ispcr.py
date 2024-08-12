import subprocess
import tempfile

def ispcr(primer_file: str, assembly_file: str, max_amplicon_size: int) -> str:
    blastn_command = [
        "blastn",
        "-task", "blastn-short",
        "-query", primer_file,
        "-subject", assembly_file,
        "-outfmt", '6 std qlen'
    ]
    blast_output = subprocess.check_output(blastn_command).decode('utf-8').splitlines()
    blast_hits = []
    for line in blast_output:
        rows = line.split('\t')
        align_len = int(rows[3])
        identity = float(rows[2])
        qlen = int(rows[12])
        if identity >= 80 and align_len == qlen:
            blast_hits.append(rows)
    blast_hits.sort(key=lambda x: int(x[8]))
    formatted_hits = [[str(hit) for hit in hits] for hits in blast_hits]
    amplicons = []
    for i in range(len(formatted_hits)):
        for j in range(len(formatted_hits)):
            primer1 = formatted_hits[i]
            primer2 = formatted_hits[j]
            if int(primer1[8]) < int(primer1[9]):
                primer1_direction = 'right'
            else:
                primer1_direction = 'left'
            if int(primer2[8]) < int(primer2[9]):
                primer2_direction = 'right'
            else:
                primer2_direction = 'left'
            if primer1_direction == 'right' and primer2_direction == 'left':
                distance = int(primer2[8]) - int(primer1[9])
            elif primer1_direction == 'left' and primer2_direction == 'right':
                distance = int(primer1[8]) - int(primer2[9])
            else:
                continue
            if 0 < distance < max_amplicon_size:
                amplicons.append((primer1, primer2))

    uniques = []
    for sequence_pair in amplicons:
        sorted_pair = tuple(sorted(sequence_pair, key=lambda x: x[8]))
        if sorted_pair not in uniques:
            uniques.append(sorted_pair)
    bed = "\n".join([
        "\t".join([
            pair[0][1],
            str(int(pair[0][9])),
            str(int(pair[1][9])-1)
        ])
        for pair in uniques
    ])
    with tempfile.NamedTemporaryFile(mode='w+t', suffix='.bed', delete=True) as temp_file:
        temp_file.write(bed)
        temp_file.flush()
        command = f"seqtk subseq {assembly_file} {temp_file.name}"
        output = subprocess.run(command, stdout=subprocess.PIPE, shell=True)

    return output.stdout.decode()