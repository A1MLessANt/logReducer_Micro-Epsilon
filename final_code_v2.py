# #dat_file = "C:\Users\HPO2KOR\Desktop\Work\data1.dat"
#dat_file = 'TestData\Final_pyro_and_2thermocouple data repeat.dat'

dat_file = 'final_data - Copy.dat'

# output_dat_file = 'output_data.dat'
output_dat_file = f'Output_{dat_file}'
# print(output_dat_file)

# #data save interval for final file # milisecond
data_interval = 1000  # 1000 milisecond
# data_interval = 500   # 500 milisecond


# Delete upto 9th line of dat file

try:
    for x in range(9):
        with open(dat_file, 'r') as fr:
            # reading line by line
            lines = fr.readlines()
            # pointer for position
            ptr = 1

            # opening in writing mode
            with open(dat_file, 'w') as fw:
                for line in lines:
                    # we want to remove 5th line
                    if ptr != 1:
                        fw.write(line)
                    ptr += 1
        print(f"Deleted line {x+1}")

except:
    print("Oops! something error in deleting files")


# keep every 1000th line
# keep every (data_interval)th line

try:
    with open(dat_file, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
#old Method
#         rangeOfLine = int(len(lines)/data_interval)

        # opening in writing mode
        with open(output_dat_file, 'w') as fw:
            for x in range(0,len(lines),data_interval):
                #print(lines[x])
                fw.write(lines[x])
            
## old Method for write in dat file           
#             for x in range(rangeOfLine):
#                 # print(lines[(x*data_interval)])
#                 fw.write(lines[(x*data_interval)])


        print(f"Sucessfully done  {dat_file}")
        print(f"Flie saved as  {output_dat_file}")


except:
    print("Oops! something error in writing files")
