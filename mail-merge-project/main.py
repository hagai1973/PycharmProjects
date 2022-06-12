with open('./input/Names/invited_names.txt', 'r') as f:
    Names = [line.strip() for line in f]

for name in Names:
    # print(name)
    # input file
    fin = open("base_letter.txt", "rt")
    # output file to write the result to
    fout = open(f"./output/ReadyToSend/letter_for_{name}.txt", "wt")
    # for each line in the input file
    for line in fin:
        # read replace the string and write to output file
        fout.write(line.replace('[name]', name))
    # close input and output files
    fout.close()
fin.close()










# with open("base_letter.txt") as file1:
#     lines = file1.readlines()
#     lines.replace('[name]', 'the_new_name')
#     copied_lines = [line for line in lines]
#
# with open("sample2.txt", "w") as file2:
# 	file2.writelines(copied_lines)


# with open('base_letter.txt') as f:
#     lines = f.readlines()
#
#
# n = open("myfile.txt", "w")
# n.write(str(lines))
# n.close()
# print(lines)
