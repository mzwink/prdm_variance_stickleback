from xlrd import open_workbook

excel_workbook = open_workbook('/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/consensus_variance.xlsx')
prdm_genes = ['mecom', 'prdm1a', 'prdm1c', 'prdm2b', 'prdm4', 'prdm8', 'prdm9', 'prdm10', 'prdm12' ,'prdm13', 'prdm14']

def create_text_files(excel_workbook, prdm_genes):

    counter = 0

    for gene in prdm_genes:

        sh = excel_workbook.sheets()[counter]
        counter +=1

        num_rows = sh.nrows
        num_columns = sh.ncols

        output = str(gene) + '_consensus_variance.txt'
        output = open(output, 'w')

        for i in range(0, num_rows):
            for j in range(0, num_columns):
                if j == num_columns -1:
                    output.write(str(sh.cell_value(rowx=i, colx=j)) + "\n")
                else:
                    output.write(str(sh.cell_value(rowx=i, colx=j)) + "\t")


def find_variance(file_list):

    #output.write('\tmecom\tprdm1a\tprdm1c\tprdm2b\tprdm4\tprdm8\tprdm9\tprdm10\tprdm12\tprdm13\tprdm14\n')

    for prdm in file_list:

        output = prdm + "_snp_variance.txt"
        output = open(output, 'w')
        output.write('A' + "\t" + prdm + "\n")

        prdm_file = prdm + "_consensus_variance.txt"
        prdm_file = open(prdm_file).readlines()

        ref_allele_list = []
        for row in prdm_file:

            sample_name = ''
            alt_allele_list = []

            if row.startswith('REFERENCE'):
                ref_allele = row.rstrip().split("\t")

                for allele in ref_allele:
                    if len(allele) == 1:
                        ref_allele_list.append(allele)

            elif row.startswith('ERR407'):

                consensus_values = row.rstrip().split("\t")
                sample_name = consensus_values[0]

                for alt_allele in consensus_values:
                    if len(alt_allele) < 3:
                        #print(alt_allele)
                        alt_allele_list.append(alt_allele)



                non_match_counter = 0
                total_alleles = len(ref_allele_list)
                snp_variance = 0

                for i in range(len(ref_allele_list)):

                    if alt_allele_list[i] != ref_allele_list[i] and alt_allele_list[i] != 'NA':
                        non_match_counter += 1


                if non_match_counter > 0:

                    snp_variance = float(non_match_counter/total_alleles)*100

                output.write(str(sample_name) + "\t" + str(snp_variance) + "%" + "\n")






######################### Main ###############################

create_text_files(excel_workbook, prdm_genes)
find_variance(prdm_genes)



####################################################################
#mecom=excel_workbook.sheets()[0]
#prdm1a=excel_workbook.sheets()[1]
#prdm1c=excel_workbook.sheets()[2]
#prdm2b=excel_workbook.sheets()[3]
#prdm4=excel_workbook.sheets()[4]
#prdm8=excel_workbook.sheets()[5]
#prdm9=excel_workbook.sheets()[6]
#prdm10=excel_workbook.sheets()[7]
#prdm12=excel_workbook.sheets()[8]
#prdm13=excel_workbook.sheets()[9]
#prdm14=excel_workbook.sheets()[10]
