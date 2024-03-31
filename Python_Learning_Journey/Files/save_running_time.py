# this program saves a sequence of Video running times to the video_times.txt file

def main():
    # Get the number of Videos in the Project

    num_videos = int(input('How many videos are in the project? : '))

    # Open the file to hold the running times

    video_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\video_times.txt', 'w')

    # get each video's running time and write it to the file

    print('Enter the Running Times for Each Video')

    for count in range(1, num_videos + 1):

        run_time = float(input('Video # ' + str(count) + ':'))

        video_file.write(str(run_time) + '\n')

    #close file

    video_file.close

    print('The times have been Written to the file video_times.txt')

main()