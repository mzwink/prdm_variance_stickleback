population_variance = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/variance/population_snp_variance.txt'
sample_info = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/fq_file_id.txt'

output = population_variance.replace('.txt', '_final.txt')
output = open(output, 'w')

sample_info = open(sample_info).readlines()
variance_info = open(population_variance).readlines()
sample_dict = {}

for sample in sample_info:

    sample = sample.rstrip()
    sample = sample.split("    ")
    #print(sample)

    sample_name = sample[0]
    sample_id = sample[1]
    sex = sample[2]
    population = sample[3]

    sample_dict[sample_name] = [sample_id, sex, population]

for variance in variance_info:

    if variance.startswith('PRDM_GENE'):
        variance = variance.rstrip().split('\t')

        print(variance[0])
        header = variance

        for value in header:

            if value == ('PRDM_GENE'):
                output.write(value + "\tID\tSEX\tPOPULATION\t")

            elif value == ('prdm14'):
                output.write(value + "\n")

            else:
                output.write(value + "\t")

        output.write("\n")

    else:
        variance = variance.rstrip()
        variance = variance.split(" ")
        #print(variance[0])
        sample_name = variance[0]

        population_info = sample_dict[sample_name]

        #print(population_info[0])
        #print(population_info[1])
        #print(population_info[2])

        sample_id = population_info[0]
        sex = population_info[1]
        population = population_info[2]

        for v in variance:
            if v == sample_name:
                output.write(variance[0] + "\t" + sample_id + "\t" + sex + "\t" + population + "\t")
            else:
                output.write(v + "\t")

        output.write("\n")
