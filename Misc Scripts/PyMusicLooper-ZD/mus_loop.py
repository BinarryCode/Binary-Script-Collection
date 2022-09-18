import os
import sys
curr_dir = os.getcwd();
loop_dir = curr_dir + "\\Loops\\Loop.txt";

# opening the text file
loop_start = 0;
loop_end = 0;
loop_tracker = 0;
mus_name = "";
with open(loop_dir,'r') as file:
	# reading each line    
	for line in file:
		# array thingy
		for word in line.split():
			# displaying the word
			if (loop_tracker == 0):
				#print("loop start is");
				loop_start = word;
			elif (loop_tracker == 1):
				#print("loop end is");
				loop_end = word;
			elif (loop_tracker == 2):
				mus_name = word;
				#print("looking for " + str(sys.argv[1]));
				if(word == sys.argv[1]):
					# loop properly
					#print("loopin' time!")
					os.system("ffmpeg -i {} -af atrim=start_sample=0:end_sample={} -metadata LOOP_START={} -c:a libvorbis {}".format(mus_name, loop_end, loop_start, mus_name[:-4] + "_LOOP.ogg"));
			loop_tracker = (loop_tracker + 1) % 3;
			print(word);