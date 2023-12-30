import os
import cv2
import shutil

def extract_stills(input_folder, output_folder, num_stills=3):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a video file (you may need to adjust the file extensions)
        if filename.endswith(('.mp4', '.mkv')):
            video_path = os.path.join(input_folder, filename)

            # Create a folder for each episode's stills
            episode_folder = os.path.join(output_folder, os.path.splitext(filename)[0])
            if not os.path.exists(episode_folder):
                os.makedirs(episode_folder)

            # Open the video file
            cap = cv2.VideoCapture(video_path)

            # Get the total number of frames
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            # Calculate frame indices for the stills
            frame_indices = [int(i * total_frames / (num_stills + 1)) for i in range(1, num_stills + 1)]

            # Extract stills
            for index in frame_indices:
                cap.set(cv2.CAP_PROP_POS_FRAMES, index)
                ret, frame = cap.read()
                if ret:
                    still_path = os.path.join(episode_folder, f"still_{index}.png")
                    cv2.imwrite(still_path, frame)

            # Release the video capture object
            cap.release()

if __name__ == "__main__":
    # Specify input and output folders
    input_folder = input("Input Folder: ")
    output_folder = input("Output Folder: ")

    # Set the number of stills to be taken from each episode
    num_stills_per_episode = 3

    # Call the function to extract stills
    extract_stills(input_folder, output_folder, num_stills_per_episode)
