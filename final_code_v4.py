

dat_file = 'final_data - Copy.dat'

output_dat_file = f'Output_{dat_file}'


# #data save interval for final file # milisecond
data_interval = 1000  # 1000 milisecond
# data_interval = 500   # 500 milisecond


# keep every 1000th line
# keep every (data_interval)th line

try:
    with open(dat_file, 'r') as fr:
        # reading line by line
        lines = fr.readlines()

        # opening in writing mode
        with open(output_dat_file, 'w') as fw:
            for x in range(9,len(lines),data_interval):
                #print(lines[x])
                fw.write(lines[x])
            
        print(f"Sucessfully done  {dat_file}")
        print(f"Flie saved as  {output_dat_file}")


except:
    print("Oops! something error in writing files")
    

def cutFile(fname, lastWantedColumn):
    """Keep wanted lines and colums: detect lines beginning with number and keep input columns"""
    f=open(fname, "r")
    lf = f.readlines()
    f.close()

    txtOut = ""
    for l in lf:
        if l[0].isdigit(): #detect if first char is a number
            txtOut += "\t".join(l.split()[:lastWantedColumn]) + "\n"
            #print(txtOut)
    g = open(".".join(fname.split(".")[:-1]) + "_cutted_column." + fname.split(".")[-1], "w")
    g.write(txtOut)
    g.close()
    print(f'Cutted & saved as {".".join(fname.split(".")[:-1]) + "_cutted_column." + fname.split(".")[-1]}')

cutFile(output_dat_file, -12)

