# This programs read the values in the file and calculate their total

def main():
    # open the file video_times.txt for readoing

    video_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\video_times.txt', 'r')

    # initialize the total

    total = 0.0

    #Count for the videos

    count = 0.0

    print('Here are the running times for each video')

    #Get the values from the file and total them

    for line in video_file:

        #Convert a line to a float

        run_time = float(line)

        #add 1 to counter

        count = count + 1

        #Display the time

        print('Video #', count, ':', run_time, sep='')

        #Add the time to total

        total = total + run_time

    #Close file

    video_file.close()

    #Display the total and Running times

    print('The total running time is: ', total, "minutes")

main()